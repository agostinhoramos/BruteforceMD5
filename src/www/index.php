<?php
session_start();
include 'lib.php';
$html = new html;
$html->header("IPG - Welcome page");
?>
<div class="limiter">
<div class="container-login100">
<div class="wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55">
<div class="login100-form validate-form" style="overflow:hidden;">

	<div style="text-align:center;">Polytechnic Institute of Guarda</div>
	<br/><br/><br/>
	<div class="container-login100-form-btn w-100">
		<a class="login100-form-btn bg-danger" 
			style="width: 100% !important;color:white;" href="/vuln_signup.php" >SIGNUP</a>
			<br/><br/><br/>
			<div class="container-login100-form-btn w-100">
		<a class="login100-form-btn bg-primary" 
			style="width: 100% !important;color:white;" href="/login.php" >LOGIN</a>

</div>
</div>
</div>
</div>
<?php
$html->footer();
?>