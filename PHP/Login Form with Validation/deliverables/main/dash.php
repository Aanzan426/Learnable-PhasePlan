<?php
	session_start();

	if (!isset($_SESSION['logged_in'])) {
    		header('Location: login.html');
    		exit;
	}
?>

<!DOCTYPE html>
<html lang="en">
	<head>
    		<meta charset="UTF-8">
    		<title>Dashboard</title>
	</head>
	<body>
		<h2>You are logged in!</h2>
	</body>
</html>
