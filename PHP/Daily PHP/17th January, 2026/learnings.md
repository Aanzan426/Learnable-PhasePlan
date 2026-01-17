1\. Comments are written via // for single lined comments, and /\* - \*/ for multi lined comments

2\. String concatenation happens using the dot (.) operator between 2 or more strings:

&nbsp;	- $testvar = 'Hello'.'World!'; echo $testvar; // Output would be Hello World!

&nbsp;	- Adding a single quote changes that => echo '$testvar' would print $testvar and not Hello World!, whereas adding a double quote => echo "$testvar" would print Hello World!

3\. Syntax for Control Statements (if...else if...else):

&nbsp;	- if(condition){

&nbsp;		// conditional code to be executed if condition is true

&nbsp;	  } else if (condition){

&nbsp;	  	// conditional code to be executed if main condition is false but next condition is true

&nbsp;	  } else {

&nbsp;	  	// conditional code to be execute if none of the conditions are true

&nbsp;	  }

4\. Equal Operator => '=' is for assigning values to variables, '==' is for comparison and validation if certain entities are equal

5\. The use of '\\', also known as Backlash, allows the user to use quotes (single and double) in strings letting the server know that thats not the point where the string ends:

&nbsp;	- echo '<p> Sorry you didn\\'t win, better luck next time</p>';

6\. The double pipe (||) operator entails the OR logic (PHP allows use of OR as well but smallcase), which simply to say, either this or that:

&nbsp;	- Used in control conditions... logic=> T or T is T, T or F is T, F or T is T, F or F is F

7\. The double ampersand (\&\&) operator entails the AND logic (PHP allows use of AND as well but smallcase), which simply to say, this and that then only some third thing:

&nbsp;	- Used in control statements... logic-> T and T is T, T and F is F, F and T is F, F and F is F

8\. There are comparison operators like '<' less than, '>' greater than, '<=' less than or equal to, '>=' greater than or equal to, and, '!=' not equal to.

8\. Beginning of Loops...

9\. Syntax for FOR LOOP:

&nbsp;	- for (declare counter; condition ; increment counter){

&nbsp;		// statement(s) to execute repeatedly as long as the condition is true

&nbsp;	  }

&nbsp;	- eg: for ($count = 1; $count <= 10; $count++){...}  // ++ indicates '+1', -- indicates '-1'

10\. Syntax for WHILE LOOP:

&nbsp;	- while (condition){

&nbsp;		// statement(s) to execute repeatedly as long as the condition is true

&nbsp;	  }

&nbsp;	- eg: while ($count <= 10){...}

&nbsp;	-  If the ++ is before the variable name, the counter is incremented before the value is read; ie. When $count is zero, the code echo ++$count; will print 1; whereas echo $count++; will print 0.

11\. There is a variant of the while loop known as the DO...WHILE LOOP:

&nbsp;	- do{

&nbsp;		// statement(s) to execute once before running the condition and then repeatedly as long as the condition is true

&nbsp;	  } while (condition);

&nbsp;	- Traditional 'while' loops force the program to check the condition even for the first run, in 'do...while' you can run the loop before running the condition (like a trial run but its real)

12\. Beginning of Arrays...

13\. Any variable is like a box that can hold values, thats why it holds not just one but many too. The variable that we allow to hold multiple values are known as Arrays.

14\. Syntax:

&nbsp;	- (1) $array1 = \['one', 2, '3']       // More preferred

&nbsp;	- (2) $array2 = array('one', 2, '3')  // Less preferred

15\. Accessing the elements in the arrays is easy, you need to use the INDEX of the element, starts from 0 for the 1st element... (n-1) for the nth element:

&nbsp;	- We can create new elements externally => \&array1 \[3] = 'four';   // this creates the fourth element as 'four'

&nbsp;	- |--|--| and add them at the end (append) => \&array1 \[] = 'five';    // this creates the element 'five' and adds it at the end of the array ; $array1 = \['one', 2, '3', 'four', 'five']

16\. Key-value pairs can also be created inside arrays:

&nbsp;	- We use the '=>' operator to assign values to the key (essentially can change the indexing itself)

&nbsp;	- Eg: \&array1 = \[ 1 => 'one', 2 => 2, 3 => '3', 4 => 'four', 5 => 'five']  // now if we echo \&array1 \[3] it'll print '3' and not 'four'

17\. Theres a special type of array that specializes in associating values to meaningful keys (doesnt change index in this type but value access gets 2 options; index and key):

&nbsp;	- They are called Associative Arrays

&nbsp;	- eg: \&array2 = \['Kevin' => '2023-04-12', 'Shalini' => '2002-05-07']   // Date format is always Year-Month-Day

18\. Beginning of Passing Variables in Links...

19\. The easiest way to send information with a page request is by using a URL query string; A query string starts after a question mark in the URL and contains key-value pairs.

20\. You can create your own link:

&nbsp;	- <a href="name.php?name=Kevin">Hi, I’m Kevin!</a>  // which passes the variable name with the value Kevin.

&nbsp;	- When this link is clicked, the browser requests name.php and includes the variable in the query string.

21\. name.php program:

&nbsp;	- <?php

&nbsp;	  	 $name = $\_GET\['name'];

&nbsp;		 echo 'Welcome to PHP,'.$name;

&nbsp;	  ?>

&nbsp;	- In name.php, PHP retrieves the value using $\_GET\['name'] and assigns it to a variable $name; The script then outputs a message such as Welcome to PHP, Kevin.

22\. But that's where the issue begins, in the query string link. When we open the name.html and click the link, the name.php page opens, but the url shows:

&nbsp;	- http://localhost:8000/name.php?name=Kevin

&nbsp;	- If I add <b> tags before and after Kevin, the resulting page would show => Welcome to PHP, **Kevin**

23\. And that leads to the entire content being under the control of the user, even the malicious ones who want to and can send incorrect values to the php page.



Note: You might notice that some browsers will automatically convert the < and > characters into URL escape sequences (%3C and %3E respectively), but either way, PHP will receive the same value.



24\. That's where the php built-in function **htmlspecialchars** comes in:

&nbsp;	- Syntax: htmlspecialchars (var\_name, constant, encoding);

&nbsp;	- In this case its => htmlspecialchars ($name, ENT\_QUOTES, 'UTF-8');   // ENT\_QUOTES  tells htmlspecialchars to convert single and double quotes in addition to other special characters.

&nbsp;	- Many of PHP’s built-in functions, such as htmlspecialchars, assume you’re using the much simpler ISO-8859-1 (or Latin-1) character encoding by default. 

&nbsp;	- Therefore, you need to let them know you’re using UTF-8 when utilizing these functions.

25\. Now if you change Kevin to <b>Kevin</b>, that's what itll show in the page and not **Kevin.**

26\. When we use FORMS, for inputting user data, and use the method = "get", the resulting action = "name.php" page shows this url when accessed => http://localhost:8000/name.php?firstname=Zatch\&lastname=Winston   // If name inputting is Zatch Winston

27\. |-||-| method = "post", the resulting action = "name.php" page shows a difference in the url => http://localhost:8000/name.php   // That's it!!

28\. So simply to put it, POST is always safer than GET.

