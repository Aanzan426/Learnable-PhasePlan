# Difficulty 1 — Basic HTML Form Handler

## Overview

This project is a beginner-level exercise to understand how **HTML, CSS, and PHP** work together in a real **request–response flow**.

The goal is to:
- Collect user input via an HTML form
- Submit the data to a PHP script using **POST**
- Validate and safely display the submitted data
- Understand why certain PHP functions and patterns are necessary

This README documents the **key learnings and mental models** developed while building this project.

---

## New Learnings

### Request Method Awareness (POST vs GET)

- **POST** → when the form is submitted  
- **GET** → when the user types the URL directly in the browser  

This distinction is critical to prevent users from directly accessing processing scripts.

---

### Null Coalescing Operator (`??`)

- `?? ""` means: **If this key doesn’t exist, use an empty string**
- Prevents undefined index errors when accessing `$_POST`

---

### `trim()`

- Removes leading and trailing spaces from input  
- Example:  " John " → "John"

---

### `filter_var(value, rule)`

- Used to validate or sanitize input using PHP’s built-in filters

#### `FILTER_VALIDATE_EMAIL`

- A **PHP constant** (not a variable)
- Internally defined by PHP as: define("FILTER_VALIDATE_EMAIL", 274);
- Meaning:
- Take this value
- Apply PHP’s email validation rule to it

- Other examples of PHP constants:
- `FILTER_VALIDATE_INT`
- `FILTER_SANITIZE_STRING`
- `PHP_VERSION`
- `PHP_INT_MAX`

---

### `htmlspecialchars()`

- A PHP function that makes user input **safe to display in HTML**

#### Why it is needed
- The browser cannot tell the difference between:
- User input
- Your HTML code
- If not escaped, the browser may execute user input as code

#### Important Notes
- Anything that comes from the user is **untrusted**
- User input is just text
- HTML is also text
- Browsers interpret text as code

#### What happens when output is not escaped
- User input may run as HTML or JavaScript
- Even if that was never intended

#### Example Conversion
<script> → "&lt;script&gt";

---

#### Golden Rule
> **Validate input. Escape output. Always.**

- Validation → Is this acceptable?  
- Escaping → Is this safe to display?

---

### `var_dump()`

- A debugging function that shows:
  - The variable’s type
  - Its length
  - Its actual value
- Shows what the variable truly is, not what you assume it is

#### Common debugging questions it answers
- “Why is this empty?”
- “Is this a string or an array?”
- “Why isn’t my logic working?”

`var_dump()` answers all of that instantly.

#### Example
- var_dump($name); → string(4) "John"
- (Type → string, Length → 4 characters, Value → "John")

#### Common usage
- `var_dump($_POST);`
- `var_dump($_GET);`
- `var_dump($errors);`
- `var_dump($_SESSION);`
- `var_dump($result_from_db);`

---

### `die();`

- Immediately ends script execution
- Commonly used during debugging to stop processing and inspect output

---

## Project Files

- `form.html` — User input form  
- `style.css` — Basic styling for layout and readability  
- `process.php` — Handles form submission, validation, and safe output  

---

## Key Takeaway

This project is not about building a feature — it is about **understanding fundamentals**:

- How requests reach PHP
- How PHP processes data
- Why validation and escaping exist
- Why browsers are dangerous if assumptions are made

These concepts apply far beyond this project and remain valid regardless of frameworks or language trends.

---

