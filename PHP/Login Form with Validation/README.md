# Difficulty 3 — Login Form with Validation



## Overview



This project implements a basic **login system** that demonstrates the complete client–server authentication flow using **HTML, JavaScript, and PHP**.  

It focuses on understanding **input validation, server-side authentication, and session-based access control**, rather than UI complexity or database integration.



The project is designed as a **fundamentals exercise** to clearly separate responsibilities between frontend validation and backend authority.



---



## Features



- Login form with username and password fields

- Client-side validation using JavaScript

- Server-side authentication using PHP with hardcoded credentials

- Session initialization on successful login

- Protection against direct access to restricted pages

- Session persistence across page refreshes



---



## Project Structure



deliverables/
├── main/
│ ├── login.html # Login form (frontend)
│ ├── login.js # Client-side validation logic
│ ├── auth.php # Server-side authentication & session setup
│ └── dash.php # Protected page (requires active session)
│
├── branch/
│ └── data.php # Session-based data handling (support file)
│
docs/
├── problem_statement.md
│
README.md




---



## How It Works (Request–Response Flow)



1. The user accesses `login.html` and submits credentials.

2. `login.js` intercepts the form submission and validates:

&nbsp;  - Empty fields

&nbsp;  - Minimum input length

3. If validation passes, the form submits to `auth.php`.

4. `auth.php`:

&nbsp;  - Validates request method

&nbsp;  - Authenticates against hardcoded credentials

&nbsp;  - Initializes a session on success

5. Authenticated users are redirected to `dash.php`.

6. Direct access to protected pages is blocked unless a valid session exists.

7. Session data persists across refreshes until explicitly destroyed.



---



## Security & Design Principles



- JavaScript validation improves user experience but is **never trusted**

- PHP acts as the **final authority** for authentication

- Sessions are used to maintain login state across requests

- Direct URL access is restricted via session checks

- Input is trimmed and validated on both client and server



---



## Learnings



This project helped solidify the following concepts:



### JavaScript Fundamentals

- `addEventListener()` listens for browser events without relying on inline handlers

- Form-level `submit` events are preferred over button `onclick`

- `.value` accesses user input stored in form fields

- `.trim()` removes leading and trailing whitespace

- `event.preventDefault()` stops default browser behavior when validation fails

- `.length` is used to enforce minimum input constraints



### PHP & Backend Concepts

- `session_start()` must be called at the beginning of every session-dependent PHP file

- `$_SESSION` is a server-side associative array used to persist user state

- Session variables can be dynamically created, accessed, and removed

- `header("Location: file.php")` redirects execution to another page

- `exit;` is required after headers to prevent further script execution

- PHP must re-validate all input regardless of client-side checks



### Authentication & State

- Hardcoded credentials are suitable for learning authentication flow

- Sessions solve HTTP statelessness

- Refresh persistence confirms session continuity

- Protected routes must explicitly verify authentication state

- Logout is achieved by unsetting session data and destroying the session



---



## Key Takeaway



This project is not about building a production-ready login system.  

It is about **understanding how authentication works end-to-end**:



> JavaScript checks input quality  

> PHP verifies authenticity  

> Sessions maintain state  



These fundamentals apply universally across backend frameworks and technologies.



---



## Notes



This repository reflects **learning-focused implementation choices**.  

Clarity, correctness, and conceptual understanding are prioritized over optimization or advanced security patterns.



---

