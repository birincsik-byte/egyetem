<?php
// Online marketing, Pannon Egyetem, 2026 ősz. Csapatregiszter, beadandók, szavazás.
// Egy fájl, JSON-tár. Tedd a deck mellé, és hozz létre mellé egy írható "data" mappát.
// Oktatói kulcs: ezt írd át, ezzel lehet törölni és exportálni.
$KEY = 'valtoztasd-meg';
// Ha van key.php a mappában (nincs a gitben), az felülírja: <?php $KEY = 'sajat-kulcs';
if (file_exists(__DIR__ . '/key.php')) { include __DIR__ . '/key.php'; }
// Hallgatói Neptun-kódok listája (neptun.php, nincs a gitben): <?php $NEPTUN = array('ABC123', ...);
$NEPTUN = array();
if (file_exists(__DIR__ . '/neptun.php')) { include __DIR__ . '/neptun.php'; }

$DIR = __DIR__ . '/data';
$FILE = $DIR . '/store.json';
if (!is_dir($DIR)) { @mkdir($DIR, 0755, true); }
if (!file_exists($DIR . '/.htaccess')) { @file_put_contents($DIR . '/.htaccess', "Require all denied\n"); }

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function load() {
  global $FILE;
  if (!file_exists($FILE)) return array('teams' => array(), 'subs' => array(), 'votes' => array(), 'locks' => array());
  $d = json_decode(file_get_contents($FILE), true);
  if (!is_array($d)) $d = array();
  foreach (array('teams', 'subs', 'votes', 'locks') as $k) if (!isset($d[$k])) $d[$k] = array();
  return $d;
}
function save($d) {
  global $FILE;
  $fp = fopen($FILE, 'c+');
  if (!$fp) fail('nem tudok írni a data mappába');
  flock($fp, LOCK_EX);
  ftruncate($fp, 0);
  fwrite($fp, json_encode($d, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));
  fflush($fp);
  flock($fp, LOCK_UN);
  fclose($fp);
}
function fail($msg, $code = 400) { http_response_code($code); echo json_encode(array('ok' => false, 'error' => $msg), JSON_UNESCAPED_UNICODE); exit; }
function clean($s, $max = 4000) { $s = trim((string)$s); $s = mb_substr($s, 0, $max); return $s; }
function tally($d, $ep) {
  $t = array();
  foreach ($d['teams'] as $tm) $t[$tm['id']] = array('n' => 0, 'sum' => 0, 'avg' => 0, 'reasons' => array());
  if (isset($d['votes'][$ep])) foreach ($d['votes'][$ep] as $v) {
    $ratings = isset($v['ratings']) ? $v['ratings'] : (isset($v['team']) ? array(array('team' => $v['team'], 'stars' => $v['stars'], 'reason' => $v['reason'])) : array());
    foreach ($ratings as $r) {
      $c = isset($r['team']) ? $r['team'] : '';
      if (!isset($t[$c])) continue;
      $t[$c]['n']++; $t[$c]['sum'] += (int)$r['stars'];
      $t[$c]['reasons'][] = array('stars' => (int)$r['stars'], 'reason' => $r['reason']);
    }
  }
  foreach ($t as $k => $r) $t[$k]['avg'] = $r['n'] ? round($r['sum'] / $r['n'], 2) : 0;
  return $t;
}
function state($d, $ep) {
  $subs = isset($d['subs'][$ep]) ? $d['subs'][$ep] : array();
  $public = array();
  foreach ($subs as $tid => $s) {
    $row = array('team_id' => $tid, 'sentence' => isset($s['f3']) ? $s['f3'] : '', 'ts' => $s['ts']);
    foreach (array('f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8') as $f) $row[$f] = isset($s[$f]) ? $s[$f] : '';
    $public[$tid] = $row;
  }
  return array(
    'ok' => true,
    'teams' => array_values($d['teams']),
    'subs' => $public,
    'tally' => tally($d, $ep),
    'votes' => isset($d['votes'][$ep]) ? count($d['votes'][$ep]) : 0,
    'locked' => !empty($d['locks'][$ep])
  );
}

// belépés a nyitólaphoz: Neptun-kód (hallgató) vagy oktatói kulcs (oktató); aláírt süti
function auth_token($role, $code) { global $KEY; return $role . '.' . $code . '.' . hash_hmac('sha256', $role . '.' . $code, $KEY); }
function auth_read() {
  global $KEY;
  if (empty($_COOKIE['omauth'])) return null;
  $p = explode('.', $_COOKIE['omauth']);
  if (count($p) !== 3) return null;
  if (!hash_equals(hash_hmac('sha256', $p[0] . '.' . $p[1], $KEY), $p[2])) return null;
  return array('role' => $p[0], 'code' => $p[1]);
}

$a = isset($_REQUEST['a']) ? $_REQUEST['a'] : 'state';
$ep = isset($_REQUEST['ep']) ? preg_replace('/[^a-z0-9]/', '', $_REQUEST['ep']) : 'ep1';
$body = json_decode(file_get_contents('php://input'), true);
if (!is_array($body)) $body = $_POST;
$d = load();

if ($a === 'auth') {
  $raw = clean(isset($body['code']) ? $body['code'] : '', 40);
  $code = strtoupper($raw);
  $role = '';
  if ($raw !== '' && hash_equals($KEY, $raw)) $role = 'oktato';
  elseif ($code !== '' && in_array($code, array_map('strtoupper', $NEPTUN))) $role = 'hallgato';
  if ($role === '') fail('nincs ilyen kód');
  $secure = !empty($_SERVER['HTTPS']);
  setcookie('omauth', auth_token($role, $role === 'oktato' ? 'oktato' : $code), array('expires' => time() + 180 * 86400, 'path' => '/', 'secure' => $secure, 'httponly' => true, 'samesite' => 'Lax'));
  echo json_encode(array('ok' => true, 'role' => $role)); exit;
}
if ($a === 'me') { $u = auth_read(); echo json_encode(array('ok' => true, 'role' => $u ? $u['role'] : '', 'code' => ($u && $u['role'] === 'hallgato') ? $u['code'] : '')); exit; }
if ($a === 'logout') { setcookie('omauth', '', array('expires' => time() - 3600, 'path' => '/')); echo json_encode(array('ok' => true)); exit; }

if ($a === 'state') { echo json_encode(state($d, $ep), JSON_UNESCAPED_UNICODE); exit; }

if ($a === 'team') {
  $name = clean(isset($body['name']) ? $body['name'] : '', 80);
  $client = clean(isset($body['client']) ? $body['client'] : '', 80);
  $members = clean(isset($body['members']) ? $body['members'] : '', 500);
  if ($name === '' || $client === '') fail('csapatnév és ügyfél kell');
  foreach ($d['teams'] as $tm) if (mb_strtolower($tm['name']) === mb_strtolower($name)) fail('ez a csapatnév már foglalt');
  $id = substr(md5($name . microtime(true)), 0, 8);
  $d['teams'][] = array('id' => $id, 'name' => $name, 'client' => $client, 'members' => $members, 'ts' => date('c'));
  save($d);
  echo json_encode(array('ok' => true, 'id' => $id), JSON_UNESCAPED_UNICODE); exit;
}

if ($a === 'getsub') {
  $tid = clean(isset($_REQUEST['team']) ? $_REQUEST['team'] : '', 16);
  $s = isset($d['subs'][$ep][$tid]) ? $d['subs'][$ep][$tid] : null;
  echo json_encode(array('ok' => true, 'sub' => $s), JSON_UNESCAPED_UNICODE); exit;
}

if ($a === 'submit') {
  $tid = clean(isset($body['team']) ? $body['team'] : '', 16);
  $found = false; foreach ($d['teams'] as $tm) if ($tm['id'] === $tid) $found = true;
  if (!$found) fail('nincs ilyen csapat');
  if (!empty($d['locks'][$ep])) fail('a leadás le van zárva; ha javítani szeretnétek, kérjétek az oktatót, hogy oldja fel');
  $s = array('ts' => date('c'));
  foreach (array('f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8') as $f) $s[$f] = clean(isset($body[$f]) ? $body[$f] : '');
  if ($s['f3'] === '') fail('a mondat hiányzik');
  if (!isset($d['subs'][$ep])) $d['subs'][$ep] = array();
  $d['subs'][$ep][$tid] = $s;
  save($d);
  echo json_encode(array('ok' => true)); exit;
}

if ($a === 'vote') {
  $voter = clean(isset($body['voter']) ? $body['voter'] : '', 16);
  $token = clean(isset($body['token']) ? $body['token'] : '', 64);
  $ids = array(); foreach ($d['teams'] as $tm) $ids[] = $tm['id'];
  if (!in_array($voter, $ids)) fail('add meg, melyik csapatban vagy');
  $in = isset($body['ratings']) && is_array($body['ratings']) ? $body['ratings'] : array();
  $ratings = array(); $seen = array();
  foreach ($in as $r) {
    $team = clean(isset($r['team']) ? $r['team'] : '', 16);
    $stars = isset($r['stars']) ? (int)$r['stars'] : 0;
    $reason = clean(isset($r['reason']) ? $r['reason'] : '', 1000);
    if (!in_array($team, $ids) || isset($seen[$team])) continue;
    if ($team === $voter) fail('a saját csapatodra nem szavazhatsz');
    if ($stars < 1 || $stars > 5) fail('egy és öt csillag között értékelhetsz');
    if (mb_strlen($reason) < 15) fail('indoklás nélkül nincs szavazat, minden értékelt csapathoz legalább egy mondat');
    $seen[$team] = 1;
    $ratings[] = array('team' => $team, 'stars' => $stars, 'reason' => $reason);
  }
  if (!count($ratings)) fail('legalább egy csapatot értékelj');
  if (!isset($d['votes'][$ep])) $d['votes'][$ep] = array();
  if ($token !== '') foreach ($d['votes'][$ep] as $v) if (isset($v['token']) && $v['token'] === $token) fail('erről az eszközről már érkezett szavazat');
  $d['votes'][$ep][] = array('voter' => $voter, 'token' => $token, 'ratings' => $ratings, 'ts' => date('c'));
  save($d);
  echo json_encode(array('ok' => true, 'tally' => tally($d, $ep)), JSON_UNESCAPED_UNICODE); exit;
}

// oktatói műveletek
$key = isset($_REQUEST['key']) ? $_REQUEST['key'] : (isset($body['key']) ? $body['key'] : '');
if ($key !== $KEY) fail('oktatói kulcs kell', 403);

if ($a === 'check') { echo json_encode(array('ok' => true)); exit; }

if ($a === 'deleteteam') {
  $id = clean(isset($body['id']) ? $body['id'] : '', 16);
  $d['teams'] = array_values(array_filter($d['teams'], function ($t) use ($id) { return $t['id'] !== $id; }));
  foreach ($d['subs'] as $e => $subs) unset($d['subs'][$e][$id]);
  foreach ($d['votes'] as $e => $votes) {
    $keep = array();
    foreach ($votes as $v) {
      if ($v['voter'] === $id) continue;
      if (isset($v['ratings'])) $v['ratings'] = array_values(array_filter($v['ratings'], function ($r) use ($id) { return $r['team'] !== $id; }));
      elseif (isset($v['team']) && $v['team'] === $id) continue;
      $keep[] = $v;
    }
    $d['votes'][$e] = $keep;
  }
  save($d);
  echo json_encode(array('ok' => true)); exit;
}

if ($a === 'lock') {
  $on = !empty($body['on']);
  $d['locks'][$ep] = $on;
  save($d);
  echo json_encode(array('ok' => true, 'locked' => $on)); exit;
}

if ($a === 'reset') {
  $what = isset($body['what']) ? $body['what'] : '';
  if ($what === 'votes') $d['votes'][$ep] = array();
  elseif ($what === 'subs') $d['subs'][$ep] = array();
  elseif ($what === 'teams') $d = array('teams' => array(), 'subs' => array(), 'votes' => array(), 'locks' => array());
  else fail('what: votes | subs | teams');
  save($d);
  echo json_encode(array('ok' => true)); exit;
}

if ($a === 'export') {
  header('Content-Type: text/csv; charset=utf-8');
  header('Content-Disposition: attachment; filename="leadandok-' . $ep . '.csv"');
  echo "\xEF\xBB\xBF";
  $out = fopen('php://output', 'w');
  fputcsv($out, array('csapat', 'ugyfel', 'tagok', 'bekuldve', 'ki_mit_csinalt', 'amit_neztunk', 'marka', 'celcsoport', 'mondat', 'bizonyitek', 'itelet', 'ami_hianyzik', 'atlag_csillag', 'szavazatok_szama', 'indoklasok'), ';');
  $t = tally($d, $ep);
  foreach ($d['teams'] as $tm) {
    $s = isset($d['subs'][$ep][$tm['id']]) ? $d['subs'][$ep][$tm['id']] : array();
    fputcsv($out, array($tm['name'], $tm['client'], $tm['members'], isset($s['ts']) ? $s['ts'] : '',
      isset($s['f1']) ? $s['f1'] : '', isset($s['f2']) ? $s['f2'] : '', isset($s['f7']) ? $s['f7'] : '', isset($s['f8']) ? $s['f8'] : '',
      isset($s['f3']) ? $s['f3'] : '', isset($s['f4']) ? $s['f4'] : '',
      isset($s['f5']) ? $s['f5'] : '', isset($s['f6']) ? $s['f6'] : '', $t[$tm['id']]['avg'], $t[$tm['id']]['n'], implode(' | ', array_map(function ($r) { return $r['stars'] . '★ ' . $r['reason']; }, $t[$tm['id']]['reasons']))), ';');
  }
  fclose($out); exit;
}

if ($a === 'full') { echo json_encode($d, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT); exit; }

fail('ismeretlen művelet');
