<?php
	session_start();

	include __DIR__ '\..\branch\data.php';

	if($_SERVER["REQUEST_METHOD"]!= "POST"){
		header("Location: login.html");
		exit;
	}

	$username = trim($_POST["username"] ?? "");
	$password = trim($_POST["password"] ?? "");
	
	if (isset($_Data[$username] && $_Data[$password]){
		$_SESSION ['logged_in'] = true;
		$_SESSION ['username'] = $username;

		echo "Welcome 'O Great Leader, Zatch!";
		header('Location: dash.php');
		exit;
	}else{
		echo "New User...!...Invalid username or password...Try Again";
	}
?>

<!DOCTYPE html>
<html lang = "en">
	<head>
		<meta charset = "UTF-8">
	</head>
	<body>
		<form action = "login.html" method = "get">
			<input type = "submit" value = "Back to Home Page">
		</form>
	</body>
</html>
	