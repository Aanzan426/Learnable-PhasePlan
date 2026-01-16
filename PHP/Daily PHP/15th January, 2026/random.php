<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Random Number</title>
</head>
<body>
    <p>
        PHP will generate a random number between 1 and 10:
        <?php
            // PHP runs on the server and generates a number
            echo rand(1, 10);
        ?>
    </p>

    <!--
        IMPORTANT NOTE:

        If you right-click → View Page Source in the browser,
        you will NOT see any PHP code.

        You will see something like this instead:

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Random Number</title>
        </head>
        <body>
            <p>
                PHP will generate a random number between 1 and 10:
                7
            </p>
        </body>
        </html>

        This proves:
        - PHP executed on the server
        - Only HTML was sent to the browser
    -->

</body>
</html>
