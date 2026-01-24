<?php
	session_start();
	try{
		$pdo = new PDO('mysql:host=localhost;dbname=introdb;charset=utf8','introdb_user','mypassword1!');
		$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$output = 'Database connected established successfully';
		
		if ($_SERVER['REQUEST_METHOD'] === 'POST'){
			$action = $_POST['action'] ?? '';
			if ($action === 'add'){
				$name = trim($_POST['name'] ?? '');
				$phone = trim($_POST['phone'] ?? '');
				$email = trim($_POST['email'] ?? '');
				
				if ($name === '' || $phone === '') {
					$output = 'Name and phone are required.';
				}else {
					$sql_add = "INSERT INTO `contacts` (`name`, `phone`, `email`) VALUES (:name, :phone, :email)";
					$stmt = $pdo->prepare($sql_add);
					$stmt->execute([
						':name'=>$name,
						':phone'=>$phone,
						':email'=>$email
					]);
					$output = 'Data Inserted';
				}

			} else if ($action === 'delete'){
				$id = (int)($_POST['id'] ?? 0);
				
				if ($id <= 0) {
					$output = 'ID is invalid.';
				} else{
					$sql_delete = "DELETE FROM `contacts` WHERE `id` = :id";
					$stmt = $pdo->prepare($sql_delete);
					$stmt->execute([
						':id'=>$id
					]);
					$output = 'Data Deleted';
				}

			} else if ($action === 'update'){
				$colname = trim($_POST['colname'] ?? '');
				$newvalue = trim($_POST['newvalue'] ?? '');
				$id = (int)($_POST['id'] ?? 0);

				$colAllowedValues = ['name','phone','email'];
				
				if (!in_array($colname, $colAllowedValues, true)) {
					$output = 'Invalid column name. Allowed: name, phone, email.';
				} else if ($newvalue === '') {
					$output = 'New value cannot be empty';
				} else if ($id <= 0) {
					$output = 'ID is invalid';
				} else {
					$sql_update = "UPDATE `contacts` SET $colname = :newvalue WHERE `id` = :id";
					$stmt = $pdo->prepare($sql_update);
					$stmt->execute([
						':newvalue'=>$newvalue,
						':id'=>$id
					]);
					$output = 'Data Updated';
				}

			} else if ($action === 'view'){
				$sql_view = 'SELECT `id`,`name`,`phone`,`email` FROM `contacts` ORDER BY `id` ASC';
				$result = $pdo->query($sql_view);
			
				echo "<h3>Contacts Table</h3>";
            			echo "<table border='1' cellpadding='6'>";
            			echo "<tr><th>ID</th><th>Name</th><th>Phone</th><th>Email</th></tr>";

           			while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
                			echo "<tr>";
                			echo "<td>" . htmlspecialchars($row['id']) . "</td>";
                			echo "<td>" . htmlspecialchars($row['name']) . "</td>";
                			echo "<td>" . htmlspecialchars($row['phone']) . "</td>";
                			echo "<td>" . htmlspecialchars($row['email']) . "</td>";
                			echo "</tr>";
           			}

            			echo "</table>";
			}
		}

	}catch (PDOException $e){
		$output = 'Database Error:'.$e->getMessage().'in'.$e->getFile().':'.$e->getLine();
	}
	include __DIR__.'/../branch/output.html.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CRUD Operation</title>
    <link rel = "stylesheet" href = "style.css">
</head>

<body>
    <header>
        <nav>
            <a href="#Add">Add Data</a>
            <a href="#Delete">Delete Data</a>
            <a href="#Update">Modify Table</a>
            <a href="#View_Table">View Table</a>
        </nav>
    </header>

    <!-- ADD SECTION -->
    <section id="Add">
        <h2>Add Contact</h2>
        <form action="index.php" method="post">
            <input type="hidden" name="action" value="add">

            <label>Name:</label>
            <input type="text" name="name">

            <label>Phone:</label>
            <input type="number" name="phone">

            <label>Email:</label>
            <input type="email" name="email">

            <button type="submit">Add Contact</button>
        </form>
    </section>

    <!-- DELETE SECTION -->
    <section id="Delete">
        <h2>Delete Contact</h2>

        <a href="#View_Table">View Table First</a>

        <form action="index.php" method="post">
            <input type="hidden" name="action" value="delete">

            <label>Enter Contact ID to Delete:</label>
            <input type="number" name="id">

            <button type="submit">Delete Contact</button>
        </form>
    </section>

    <!-- VIEW TABLE SECTION -->
    <section id="View_Table">
        <h2>View Table</h2>
        <form action="index.php" method="post">
            <input type="hidden" name="action" value="view">
            <button type="submit">View Contacts</button>
        </form>
    </section>

    <!-- UPDATE SECTION -->
    <section id="Update">
        <h2>Modify Table</h2>

        <a href="#View_Table">View Table First</a>

        <form action="index.php" method="post">
            <input type="hidden" name="action" value="update">

            <label>Column name:</label>
            <input type="text" name="colname">

            <label>New value:</label>
            <input type="text" name="newvalue">

            <label>ID:</label>
            <input type="number" name="id">

            <button type="submit">Update Contact</button>
        </form>
    </section>
    <footer>
        @ 2026 Zatch CRUD Operations;
    </footer>

</body>
</html>			 