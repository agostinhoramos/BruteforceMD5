<?php

$servername = "localhost";
$username = "user_admin";
$password = "R4984HU78EWYJHFWE";

$dbname = "db_ipg";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

$need_seed = false;
// Check connection
if ($conn->connect_error) {
    $need_seed = true;
}

?>