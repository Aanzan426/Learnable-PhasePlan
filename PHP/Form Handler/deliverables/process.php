<?php
if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    header("Location: form.html");
    exit;
}

$name  = trim($_POST["name"] ?? "");
$email = trim($_POST["email"] ?? "");

$errors = [];

if ($name === "") {
    $errors[] = "Name is required.";
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = "Invalid email address.";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form Result</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<main class="container">
    <?php if (!empty($errors)): ?>
        <h2>Errors</h2>
        <ul>
            <?php foreach ($errors as $error): ?>
                <li><?= htmlspecialchars($error) ?></li>
            <?php endforeach; ?>
        </ul>
        <a href="form.html">Go back</a>
    <?php else: ?>
        <h2>Thank You!</h2>
        <p>Name: <?= htmlspecialchars($name) ?></p>
        <p>Email: <?= htmlspecialchars($email) ?></p>
    <?php endif; ?>
</main>

</body>
</html>