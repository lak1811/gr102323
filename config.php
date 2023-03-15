<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'Admin');
define('DB_PASSWORD', 'ADMINPASSWORD');
define('DB_NAME', 'gr102023');
 
/* Attempt to connect to MySQL database */
$CONN = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if($CONN === false){
    die("ERROR: Could not connect to the database " . mysqli_connect_error());
}



?>