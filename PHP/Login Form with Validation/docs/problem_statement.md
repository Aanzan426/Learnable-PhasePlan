## Difficulty 3 — Login Form with Validation 



### Problem Statement



Design and implement a basic login system that demonstrates the complete authentication flow using **HTML, JavaScript, and PHP**.  

The system must validate user input on the client side, authenticate credentials on the server side using hardcoded values, and maintain login state across requests using PHP sessions.



The objective of this project is to understand **separation of concerns**, **client vs server responsibilities**, and **session-based access control** in a traditional web application.



---



### Requirements



- **Frontend (HTML)**

&nbsp; - Create a login form with username and password fields.

&nbsp; - Submit credentials securely using the POST method.



- **Client-Side Validation (JavaScript)**

&nbsp; - Validate empty input fields.

&nbsp; - Enforce minimum length constraints before form submission.

&nbsp; - Prevent form submission when validation fails.



- **Server-Side Authentication (PHP)**

&nbsp; - Authenticate user credentials against hardcoded values.

&nbsp; - Re-validate input regardless of client-side checks.

&nbsp; - Initialize a session on successful authentication.



- **Session Management**

&nbsp; - Store authentication state using PHP sessions.

&nbsp; - Restrict access to protected pages unless a valid session exists.

&nbsp; - Preserve login state across page refreshes.



---



### Edge Cases Handled



- Incorrect username or password.

- Direct access to protected pages without authentication.

- Session persistence on page refresh.

- Prevention of direct access to authentication scripts without form submission.



---



### Deliverables



- `login.html` — Login form (frontend)

- `login.js` — Client-side validation logic

- `auth.php` — Server-side authentication and session initialization

- `dash.php` — Protected page accessible only to authenticated users



