<?php
	$firstname = $_POST['firstname'];
	$lastname = $_POST['lastname'];
	echo 'Welcome to PHP,'.htmlspecialchars($firstname, ENT_QUOTES, 'UTF-8').' '.htmlspecialchars($lastname, ENT_QUOTES, 'UTF-8').'!';
?>