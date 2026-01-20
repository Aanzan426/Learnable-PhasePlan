\## Beginning with MYSQL...



1\. Using backlits (`) helps clarify the term used whether it is a reserved word or is it a variable.



2\. INSERT functions =>  

&nbsp;  `INSERT INTO \\`tablename\\` (column1, column2,...,column\\`n\\`) VALUES (value\_corresponding\_to\_column1, value\_corresponding\_to\_column2,...);`



2\. Commands:

&nbsp;  - To view everything (all columns) =>  

&nbsp;    `SELECT \* FROM <tablename>;`

&nbsp;  - To view selected columns =>  

&nbsp;    `SELECT column1, column2,..., column'n' FROM <tablename>;`

&nbsp;  - To see a limited number of characters, we use the function LEFT to specify the number of visible chars =>  

&nbsp;    `LEFT(column\_name, number\_of\_chars\_to\_be\_visible);`

&nbsp;  - Another useful function is the COUNT function that allows the user to see the number of returned results =>  

&nbsp;    `SELECT COUNT('column\_name (preferably index)`) FROM \\`table\_name\\`;`



3\. Adding the WHERE clause to the SELECT function:

&nbsp;  - WHERE acts like a condition that the statement follows inorder to return the required data =>  

&nbsp;    `SELECT \\`statement\\` FROM \\`tablename\\` WHERE \\`condition\\``

&nbsp;  - Eg:  

&nbsp;    `SELECT \\`jokedate\\` FROM \\`tablename\\` WHERE \\`jokedate\\` >= "2017-01-01";`

&nbsp;  - Adding the LIKE variation to the SELECT...WHERE function:

&nbsp;    - LIKE acts like a case insensitive search function that finds particular pieces of text in the database and returns only those values along with the condition

&nbsp;    - Eg:  

&nbsp;      `SELECT \\`joketext\\` FROM \\`tablename\\` WHERE \\`joketext\\` LIKE "programmer%";`

&nbsp;    - We have used `%...%`, they are called Wildcards.

&nbsp;    - Indicate that the text “inside\_the\_wildcards” may be preceded and/or followed by any string of text.

&nbsp;  - Composite conditions may be created using AND operator:

&nbsp;    - Eg:  

&nbsp;      `SELECT \\`joketext\\` FROM \\`tablename\\` WHERE \\`joketext\\` LIKE "%knock%" AND \\`jokedate\\` >= "2017-04-01" AND \\`jokedate\\` < "2017-05-01";\\`



4\. Beginning Data Modification...



5\. Syntax =>  

&nbsp;  `UPDATE \\`tablename\\` SET 'column1\\` = value,... (optional but recommended) WHERE \\`condition(s)\\` (optional) LIKE \\`specific(s)\\`;`

&nbsp;  - Eg:  

&nbsp;    `UPDATE \\`tablename\\` SET \\`jokedate\\` = "2018-04-01" WHERE \\`id\\` = "1";`

&nbsp;  - Eg:  

&nbsp;    `UPDATE \\`tablename\\` SET \\`jokedate\\` = "2018-04-01" WHERE \\`joketext\\` LIKE "%programmer%";`



6\. Beginning Data Deletion...



7\. Syntax =>  

&nbsp;  `DELETE FROM \\`tablename\\` WHERE \\`condition(s)\\`;`

&nbsp;  - Eg:  

&nbsp;    `DELETE FROM \\`tablename\\` WHERE \\`joketext\\` LIKE "%programmer%";`

&nbsp;  - Though WHERE is optional here as well, removing WHERE and committing the command can delete the entire table in one move, swoosh and gone.



8\. Done (joke.sql is used for practicing commands)



