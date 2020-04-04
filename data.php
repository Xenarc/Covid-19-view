<?php
	$message=shell_exec("/bin/bash /var/www/webscripts/run.sh");
	echo $message;
?>
<img src="./plot.png" alt="COVID GRAPHS" style="width:100%;">
