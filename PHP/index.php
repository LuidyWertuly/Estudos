<?php

define('NOME','Luidy');

 $numero1 = 20;

 $numero2 = 40;

 $total = $numero1 + $numero2;

 echo $total;
 echo '<br />';
 echo NOME;

 $contas = array('luidy','bruno','pedro','henrique','breno');

 echo '<br />';

 echo $contas[1];

 echo '<br />';

 if ($numero1 > $numero2){
    echo "primeiro";
 }

 else if($numero1 == $numero2){
    echo "segundo";
 }

 else if($numero1 !== $numero2){
    echo "terceiro";
 }

 else{
    echo "não é";
 }

 echo '<br />';
 echo '<br />';
 
 for($contador = 0; $contador <10; $contador++){
    echo 'Ola mundo';
    echo '<hr />';
 }

 $contador2 = 0;

 while($contador2 <= 10){
    echo 'Ola mundo';
    echo '<hr />';
    $contador2++;
 }

 $contador3 = 2;

 do{
    echo 'Ola mundo';
    echo '<hr />';
 }while($contador3 === 5)

?>