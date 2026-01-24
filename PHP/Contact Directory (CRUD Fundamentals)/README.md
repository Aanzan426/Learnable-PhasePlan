# Difficulty 4 — Contact Directory (CRUD Fundamentals)







## Overview







This project is a **fundamental CRUD-based Contact Directory** built using:







- **PHP (PDO)**



- **MySQL**



- **HTML (Forms + Sections)**



- (Optional) CSS for readability







The goal of this project is to build a **working contact management system** where a user can:







- **Add contacts**



- **Delete contacts by ID**



- **Update contact values**



- **View the current contacts table**







This project is intentionally focused on **core backend fundamentals**, not heavy UI design.







---







## Problem Statement







Develop a contact directory that allows users to add, view, delete, and update contacts stored in a MySQL database using PHP and PDO.







---







## Features Implemented







### Create



- Add a new contact with:



&nbsp; - `name`



&nbsp; - `phone`



&nbsp; - `email`







### Read



- Display all contacts from the database in a table format







### Update



- Modify a contact by:



&nbsp; - choosing a column to update (`name`, `phone`, `email`)



&nbsp; - entering a new value



&nbsp; - specifying the contact `id`







### Delete



- Delete a contact using a unique `id`







---







## Project Files







| File | Purpose |



|------|---------|



| `index.php` | Main program (Single Entry Controller that performs CRUD + renders UI) |



| `style.css` | Styling (optional, improves readability and layout) |



| `output.html.php` | Output template to print status messages (`$output`) |



| `db.sql` / MySQL Console | Schema setup (`CREATE TABLE`) executed once |







---







## Database Setup (Run Once)







This project uses a MySQL table:







- `contacts (id, name, phone, email)`







The table was created **once** using the MySQL console / SQL file.







&nbsp;Reason:



Running `CREATE TABLE` repeatedly inside PHP would cause an error like:







> table already exists







So table creation belongs to **one-time setup**, not repeated runtime logic.







---







## Core Concepts Learned (Learning Notes)







### 1) PHP Must Come Before HTML (Execution Flow)







In a PHP web application, the server reads the file from **top to bottom**.







That means:







1. PHP logic executes first (database connection, request handling, security)



2. HTML is rendered and returned to the browser



3. On form submission, the browser sends a **new request**



4. PHP runs again from the top







This builds the classic flow:







> Request → PHP executes → Output → Browser → New Request







---







### 2) Placeholders Replace Values (Not Identifiers)



Prepared statement placeholders like:



- `:name`, `:id`  

- or `?`  



can only be used to replace **data values**, not SQL structure.



---



&nbsp;**Allowed (values):**



```sql

WHERE id = :id

```



---



&nbsp;**Not allowed (identifiers):**



```sql

SET :col = :value

```



---

&nbsp;

That means:



- Column names / table names are part of SQL structure


- Values are safely replaceable







---







### 3) Why `prepare()` is Required (Security + Correctness)



Using `$pdo->prepare()` creates a SQL statement that is ready for execution while keeping:



- user input separated from SQL structure  

- SQL injection attacks blocked by design  

- Instead of putting user values directly inside SQL text, placeholders are used:



```sql

INSERT INTO contacts (name, phone, email) VALUES (:name, :phone, :email)

```



- Then values are safely passed during execution.

- This makes the program secure and reliable.







---







### 4) `PDO::FETCH\_ASSOC` Meaning



- When fetching rows from the database, the mode:



- `PDO::FETCH\_ASSOC` means:



&nbsp; - fetch rows as an associative array, like:



   ```php

   $row['name']

   $row['email']

   ```



- This makes data handling clean and readable.









---







### 5) `<input type="hidden">` (Key Link Between HTML and PHP)



- A hidden input is invisible to the user but included in the form submission.

- Example:



 ```html

 <input type="hidden" name="action" value="add">

 ```



- This was used to connect HTML forms to PHP logic by telling PHP what operation to run:



&nbsp; - add  

&nbsp; - delete  

&nbsp; - update  

&nbsp; - view  



- Without hidden inputs, PHP would not know which section triggered the request.







---







### 6) No Need to `echo` Output After Every Update



- Instead of echoing text after every operation, the program uses:



&nbsp; - one `$output` message variable  

&nbsp; - one shared output template file (`output.html.php`)  



- So output behavior becomes:



&nbsp; - Set `$output`  

&nbsp; - Include template once  

&nbsp; - Display cleanly  



- This avoids repetitive and messy output printing.







---







### 7) Single Entry Controller Concept



- This project follows a structure where one file controls everything:



&nbsp; - `index.php`



- A complete working PHP page that handles:



&nbsp; - routing  

&nbsp; - logic  

&nbsp; - UI rendering  



is known as a:



- Single Entry Controller Page



- This is a powerful beginner pattern and is very common in real web applications.







---







### 8) Two Types of Placeholders in PDO



- There are two valid placeholder styles:



&nbsp; - Named placeholders (used here)



   ```sql

   WHERE id = :id

   ```



&nbsp; - Question mark placeholders



   ```sql

   WHERE id = ?

   ```



- Both work, but named placeholders were used because they are:



&nbsp; - beginner friendly  

&nbsp; - easier to read and debug  







---







### 9) `CREATE TABLE` Should Not Run Inside Runtime PHP



- Creating database tables inside PHP request logic is inefficient because:



&nbsp; - PHP runs per request  

&nbsp; - table creation happens only once  

&nbsp; - repeated execution causes errors like:



&nbsp;   - table already exists  



- So schema is created once using SQL, then PHP only performs:



&nbsp; - CRUD commands (INSERT / SELECT / UPDATE / DELETE)







---







### 10) Form Action Redirects to Same File



- Using:



 ```html

  <form action="index.php" method="post">

```


- Means the form submits back to the same PHP file, which allows:



&nbsp; - user stays on one page  

&nbsp; - PHP handles logic cleanly  

&nbsp; - UI reloads with updated database result  



This is the foundation of the single-page CRUD workflow.





---







### Summary



- This project demonstrates the fundamentals of backend development:



&nbsp; - handling HTTP POST requests  

&nbsp; - using PHP PDO for MySQL interaction  

&nbsp; - writing secure SQL with prepared statements  

&nbsp; - building CRUD operations with clean control flow  

&nbsp; - learning real-world file structure and execution order  



- It is a practical foundation for:



&nbsp; - larger web apps  

&nbsp; - authentication systems  

&nbsp; - dashboards  

&nbsp; - MVC architecture  

