## Beginning with PHP TEMPLATES...

1. If you work in a team of not-so-savvy web designers, PHP-wise, having large blocks of cryptic PHP code intermingled with the HTML is a recipe for disaster.

2. It’s far too easy for designers to accidentally modify the PHP code, causing errors they’ll be unable to fix.

3. The ".=" operator is a shorthand (shortcut) to add values at the end of an existing string value; The longhand of this would be =>  
   `$value1 .= $value2` → `$value1 = $value1 . $value2`

4. The "INCLUDE" template helps the program include another program or rather the file contents of another program into this file itself:
   - say theres one program: `count.php`, we can include another program called `count.html.php`'s content into this file using =>  
     `include 'count.html.php';`

5. When we want to include files from another directory, we add the file path too for the include template to work correctly =>  
   eg:  
   `include 'C:/Program Files/Apache Software/Foundation/Apache2.2/<filename.php>'`

6. `'../<filename.php>'` is the operator that allows the users to operate one level above the directory the file has been stored in to include the `filename.php` (searching the directory one level above)

6. The `__DIR__` template allows the system to derive the file path there and then and combining it with the `'../<filename.php>'` operator, we can essentially solve the server change, file location change and directory change problems.
   - Eg:  
     `include __DIR__.'/../count.html.php';`

7. And its good practice to keep the direct required images and other web scripts in the same folder as the php script, but the include files required in separate directories (safety, security, and cleanliness purposes)

8. A PHP script that acts as the script taking inputs from browsers and using include statements to access other php scripts, essentially a mediator, is known as the **Controller**.

9. A controller contains the logic that controls which template is sent to the browser.

10. An easier understanding of the `__DIR__` and the `'../'` operator is:
   - We got a Tree from A->B, A->C, B->D, B->E, C->F, C->G
   - Our `file1.php` is stored in G and wants to include `file2.php` that's stored in D
   - The syntax would be =>  
     `include __DIR__.'/../B/D/file2.php';`
   - Why? That's because when we use `__DIR__` it shows the entire current file path ie `A/C/G/file1.php`
   - To access `file2.php`, we know it branches out from A, thus `__DIR__` acts as the main stem via which horizontal traversal is possible. Adding `/../` allows us to tell the branched path to go one step up to link to the dir from which the branching takes place
   - And that's how things really are.

**Note:** We open the controller script (always) so that every other script can be accessible from there via include templates.  
(If using localhost, open terminal and start server in the controller script folder)

11. The reason I used `index.php` is because it has a special meaning. `index.php` is known as a directory index.

12. If you don’t specify a filename when you visit the URL in your browser, the server will look for a file named `index.php` and display that.  
Try typing just `http://192.169.10.10` into your browser and you’ll see the index page.

13. Done
