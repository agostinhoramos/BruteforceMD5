<?php
if ($_POST){
    require __DIR__ . '/db.php'; // DB Connection
    require __DIR__ . '/fn.php';

    $string = new mystring;
    $name = $string->split_name($_POST['name']);

    $plain_text_password = $_POST['pass'];
    $vulnhash = md5( $plain_text_password ); #md5
    $safeway = "False";

    $sql = "INSERT INTO tb_student (email, firstname, lastname, password, safeway)
    VALUES ('".$_POST['mail']."', '".$name['first_name']."', '".$name['last_name']."', '".$vulnhash."', '".$safeway."')";

    if ($conn->query($sql) === TRUE) {
        header("Location: /login.php?message=success"); exit;
    } else {
        header("Location: ".$_SERVER["PHP_SELF"]."?message=error"); exit;
    }
    $conn->close();
}
?>

<?php
include 'lib.php';
$html = new html;
$html->header("IPG - Vulnerable Signup Page");
?>
<div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55">
				<form class="login100-form validate-form flex-sb flex-w" id="post" method="POST" action="/vuln_signup.php" autocomplete="off">
					<span class="login100-form-title p-b-32">
						<p style="color:red;">Vulnerable</p>
						<a href="/">
							<i class="fa fa-arrow-left" style="padding:10px;font-size:23px;"></i>
						</a>
						Signup
                    </span>
                    <div class="other">
                        <a href="/safe_signup.php">
                            <i class="fa fa-lock" style="color:green;"></i>
                        </a>
                    </div>

                    <span class="txt1 p-b-11">
						Name
					</span>
					<div class="wrap-input100 validate-input m-b-36">
						<input class="input100" type="text" name="name" >
						<span class="focus-input100"></span>
					</div>

					<span class="txt1 p-b-11">
						Email
					</span>
					<div class="wrap-input100 validate-input m-b-36" >
						<input class="input100" type="text" name="mail" >
						<span class="focus-input100"></span>
                    </div>
                    
					<span class="txt1 p-b-11">
						Password
					</span>
					<div class="wrap-input100 validate-input m-b-12" >
						<span class="btn-show-pass">
							<i class="fa fa-eye"></i>
						</span>
						<input class="input100" type="password" name="pass" >
						<span class="focus-input100"></span>
					</div>
					
					<div class="container-login100-form-btn w-100" style="margin-top:20px;" >
							<button class="login100-form-btn bg-danger" 
							style="width: 100% !important;"
							>SUBMIT</button>
					</div>
				</form>
			</div>
		</div>
    </div>
    <style>.container-login100{background-color:rgba(153,0,0,0.3)}</style>

<?php
$html->footer();
?>