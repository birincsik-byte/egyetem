<?php
// Online marketing, Pannon Egyetem, 2026 ősz. Csapatregiszter, leadandók, szavazás.
// Egy fájl, JSON-tár. Tedd a deck mellé, és hozz létre mellé egy írható "data" mappát.
// Oktatói kulcs: ezt írd át, ezzel lehet törölni és exportálni.
$KEY = 'valtoztasd-meg';
// Ha van key.php a mappában (nincs a gitben), az felülírja: <?php $KEY = 'sajat-kulcs';
if (file_exists(__DIR__ . '/key.php')) { include __DIR__ . '/key.php'; }

$DIR = __DIR__ . '/data';
$FILE = $DIR . '/store.json';
if (!is_dir($DIR)) { @mkdir($DIR, 0755, true); }
if (!file_exists($DIR . '/.htaccess')) { @file_put_contents($DIR . '/.htaccess', "Require all denied\n"); }

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function load() {
  global $FILE;
  if (!file_exists($FILE)) return array('teams' => array(), 'subs' => array(), 'votes' => array());
  $d = json_decode(file_get_contents($FILE), true);
  if (!is_array($d)) $d = array();
  foreach (array('teams', 'subs', 'votes') as $k) if (!isset($d[$k])) $d[$k] = array();
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
  foreach ($d['teams'] as $tm) $t[$tm['id']] = 0;
  if (isset($d['votes'][$ep])) foreach ($d['votes'][$ep] as $v) foreach ($v['choices'] as $c) if (isset($t[$c])) $t[$c]++;
  return $t;
}
function state($d, $ep) {
  $subs = isset($d['subs'][$ep]) ? $d['subs'][$ep] : array();
  $public = array();
  foreach ($subs as $tid => $s) {
    $row = array('team_id' => $tid, 'sentence' => isset($s['f3']) ? $s['f3'] : '', 'ts' => $s['ts']);
    foreach (array('f1', 'f2', 'f3', 'f4', 'f5', 'f6') as $f) $row[$f] = isset($s[$f]) ? $s[$f] : '';
    $public[$tid] = $row;
  }
  return array(
    'ok' => true,
    'teams' => array_values($d['teams']),
    'subs' => $public,
    'tally' => tally($d, $ep),
    'votes' => isset($d['votes'][$ep]) ? count($d['votes'][$ep]) : 0
  );
}

$a = isset($_REQUEST['a']) ? $_REQUEST['a'] : 'state';
$ep = isset($_REQUEST['ep']) ? preg_replace('/[^a-z0-9]/', '', $_REQUEST['ep']) : 'ep1';
$body = json_decode(file_get_contents('php://input'), true);
if (!is_array($body)) $body = $_POST;
$d = load();

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
  $s = array('ts' => date('c'));
  foreach (array('f1', 'f2', 'f3', 'f4', 'f5', 'f6') as $f) $s[$f] = clean(isset($body[$f]) ? $body[$f] : '');
  if ($s['f3'] === '') fail('a mondat hiányzik');
  if (!isset($d['subs'][$ep])) $d['subs'][$ep] = array();
  $d['subs'][$ep][$tid] = $s;
  save($d);
  echo json_encode(array('ok' => true)); exit;
}

if ($a === 'vote') {
  $voter = clean(isset($body['voter']) ? $body['voter'] : '', 16);
  $token = clean(isset($body['token']) ? $body['token'] : '', 64);
  $choices = isset($body['choices']) && is_array($body['choices']) ? array_values(array_unique(array_map('strval', $body['choices']))) : array();
  $ids = array(); foreach ($d['teams'] as $tm) $ids[] = $tm['id'];
  $choices = array_values(array_filter($choices, function ($c) use ($ids, $voter) { return in_array($c, $ids) && $c !== $voter; }));
  if (count($choices) < 1 || count($choices) > 3) fail('egy és három közötti szavazat kell, saját csapatra nem');
  if (!isset($d['votes'][$ep])) $d['votes'][$ep] = array();
  if ($token !== '') foreach ($d['votes'][$ep] as $v) if (isset($v['token']) && $v['token'] === $token) fail('erről az eszközről már érkezett szavazat');
  $d['votes'][$ep][] = array('voter' => $voter, 'token' => $token, 'choices' => $choices, 'ts' => date('c'));
  save($d);
  echo json_encode(array('ok' => true, 'tally' => tally($d, $ep))); exit;
}

// oktatói műveletek
$key = isset($_REQUEST['key']) ? $_REQUEST['key'] : (isset($body['key']) ? $body['key'] : '');
if ($key !== $KEY) fail('oktatói kulcs kell', 403);

if ($a === 'reset') {
  $what = isset($body['what']) ? $body['what'] : '';
  if ($what === 'votes') $d['votes'][$ep] = array();
  elseif ($what === 'subs') $d['subs'][$ep] = array();
  elseif ($what === 'teams') $d = array('teams' => array(), 'subs' => array(), 'votes' => array());
  else fail('what: votes | subs | teams');
  save($d);
  echo json_encode(array('ok' => true)); exit;
}

if ($a === 'export') {
  header('Content-Type: text/csv; charset=utf-8');
  header('Content-Disposition: attachment; filename="leadandok-' . $ep . '.csv"');
  echo "\xEF\xBB\xBF";
  $out = fopen('php://output', 'w');
  fputcsv($out, array('csapat', 'ugyfel', 'tagok', 'bekuldve', 'amit_neztunk', 'mondat', 'bizonyitek', 'itelet', 'ami_hianyzik', 'szavazat'), ';');
  $t = tally($d, $ep);
  foreach ($d['teams'] as $tm) {
    $s = isset($d['subs'][$ep][$tm['id']]) ? $d['subs'][$ep][$tm['id']] : array();
    fputcsv($out, array($tm['name'], $tm['client'], $tm['members'], isset($s['ts']) ? $s['ts'] : '',
      isset($s['f2']) ? $s['f2'] : '', isset($s['f3']) ? $s['f3'] : '', isset($s['f4']) ? $s['f4'] : '',
      isset($s['f5']) ? $s['f5'] : '', isset($s['f6']) ? $s['f6'] : '', $t[$tm['id']]), ';');
  }
  fclose($out); exit;
}

if ($a === 'full') { echo json_encode($d, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT); exit; }

fail('ismeretlen művelet');
