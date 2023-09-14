<?php
 
 $users = array('luidy','pedro','breno','bruno');

 foreach ($users as $key => $value) {
    echo $key;
    echo '=>';
    echo $value;
    echo '<hr>';
 }

 $user = array('luid','pedr','bren','brun');

 $total = count($user);

 for ($i=0; $i < $total; $i++) { 
    echo $user[$i];
    echo '<br />';
    echo '<hr/>';
 }

?>