
<?php
session_start();
include 'lib.php';
$html = new html;
$html->header("IPG - Home page");
if(!isset($_SESSION['loggedin']) OR $_SESSION['loggedin'] !== true){
    header("Location: /login.php");
    exit(0);
}
?>
<div class="limiter">
<div class="container-login100">
<div class="wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55">
<div class="login100-form validate-form" style="overflow:hidden2;">
    
    <div class="other">
        <a href="/login.php">
            <i class="fa fa-arrow-left" ></i>
        </a>
    </div>
            
    <div><strong>ID:</strong> <?php echo $_SESSION['id']; ?></div>
    <br>
    <div><strong>Mail:</strong> <?php echo $_SESSION['email']; ?></div>
    <br>
    <div><strong>First Name:</strong> <?php echo $_SESSION['firstname']; ?></div>
    <br>
    <div><strong>Last Name:</strong> <?php echo $_SESSION['lastname']; ?></div>
    <br>
    <div><strong>Password:</strong> <?php echo $_SESSION['password']; ?></div>
    <br>
    <div><strong>Safeway:</strong> <?php echo $_SESSION['safeway']; ?></div>

</div>
</div>
</div>
</div>
<?php
$html->footer();
?>