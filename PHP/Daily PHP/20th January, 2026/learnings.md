## Beginning with MYSQL...

1. Using backlits (`) helps clarify the term used whether it is a reserved word or is it a variable.

2. INSERT functions =>  
   `INSERT INTO \`tablename\` (column1, column2,...,column\`n\`) VALUES (value_corresponding_to_column1, value_corresponding_to_column2,...);`

2. Commands:
   - To view everything (all columns) =>  
     `SELECT * FROM <tablename>;`
   - To view selected columns =>  
     `SELECT column1, column2,..., column'n' FROM <tablename>;`
   - To see a limited number of characters, we use the function LEFT to specify the number of visible chars =>  
     `LEFT(column_name, number_of_chars_to_be_visible);`
   - Another useful function is the COUNT function that allows the user to see the number of returned results =>  
     `SELECT COUNT('column_name (preferably index)`) FROM \`table_name\`;`

3. Adding the WHERE clause to the SELECT function:
   - WHERE acts like a condition that the statement follows inorder to return the required data =>  
     `SELECT \`statement\` FROM \`tablename\` WHERE \`condition\``
   - Eg:  
     `SELECT \`jokedate\` FROM \`tablename\` WHERE \`jokedate\` >= "2017-01-01";`
   - Adding the LIKE variation to the SELECT...WHERE function:
     - LIKE acts like a case insensitive search function that finds particular pieces of text in the database and returns only those values along with the condition
     - Eg:  
       `SELECT \`joketext\` FROM \`tablename\` WHERE \`joketext\` LIKE "programmer%";`
     - We have used `%...%`, they are called Wildcards.
     - Indicate that the text “inside_the_wildcards” may be preceded and/or followed by any string of text.
   - Composite conditions may be created using AND operator:
     - Eg:  
       `SELECT \`joketext\` FROM \`tablename\` WHERE \`joketext\` LIKE "%knock%" AND \`jokedate\` >= "2017-04-01" AND \`jokedate\` < "2017-05-01";\`

4. Beginning Data Modification...

5. Syntax =>  
   `UPDATE \`tablename\` SET 'column1\` = value,... (optional but recommended) WHERE \`condition(s)\` (optional) LIKE \`specific(s)\`;`
   - Eg:  
     `UPDATE \`tablename\` SET \`jokedate\` = "2018-04-01" WHERE \`id\` = "1";`
   - Eg:  
     `UPDATE \`tablename\` SET \`jokedate\` = "2018-04-01" WHERE \`joketext\` LIKE "%programmer%";`

6. Beginning Data Deletion...

7. Syntax =>  
   `DELETE FROM \`tablename\` WHERE \`condition(s)\`;`
   - Eg:  
     `DELETE FROM \`tablename\` WHERE \`joketext\` LIKE "%programmer%";`
   - Though WHERE is optional here as well, removing WHERE and committing the command can delete the entire table in one move, swoosh and gone.

8. Done (joke.sql is used for practicing commands)

