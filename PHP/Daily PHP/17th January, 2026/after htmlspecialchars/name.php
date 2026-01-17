<?php
$name = $_GET['name'];
echo 'Welcome to PHP, '.htmlspecialchars($name, ENT_QUOTES, 'UTF-8').'!';
?>