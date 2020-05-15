<?php

# /login.php
if($_POST){
    
    require __DIR__ . '/db.php'; // DB Connection
    require __DIR__ . '/fn.php';

    $mail = $_POST["mail"];
    $vulnhash = md5($_POST["pass"]); // Parse to MD5
    
    $sql = "SELECT id, mail, firstname, lastname, pass, safeway
    FROM tb_student where mail = '".$mail."' AND pass = '".$vulnhash."'";

    $result = mysqli_query($conn, $sql);
    if(mysqli_num_rows($result) <= 0){
        $string = new mystring;
        $mail = $_POST["mail"];

        $plain_text_password = $_POST['pass'];
        $salted = $string->saltPass($plain_text_password); #salt
        $safehash = md5($salted); // Parse to MD5

        $sql = "SELECT id, mail, firstname, lastname, pass, safeway
        FROM tb_student where mail = '".$mail."' AND pass = '".$safehash."'";
        $result = mysqli_query($conn, $sql);
    }


    $success = FALSE;
    if (mysqli_num_rows($result) > 0) {
        // output data of each row
        while($row = mysqli_fetch_assoc($result)) {
            $id = $row["id"];
            $mail = $row["mail"];
            $firstname = $row["firstname"];
            $lastname = $row["lastname"];
            $pass = $row["pass"];
            $safeway = $row["safeway"];
            $success = TRUE;
        }
    }
    mysqli_close($conn);
    
    if($success){
        session_start();
        $_SESSION['id'] = $id;
        $_SESSION['mail'] = $mail;
        $_SESSION['firstname'] = $firstname;
        $_SESSION['lastname'] = $lastname;
        $_SESSION['pass'] = $pass;
        $_SESSION['safeway'] = $safeway;
        $_SESSION['loggedin'] = true;
        header("Location: /home.php");
        exit(0);
    }else{
        header("Location: /login.php?message=wrong_credentials");
    }
}


?>


<?php
include 'lib.php';
$html = new html;
$html->header("IPG - Login");
?>

	<div class="limiter">
		<div class="container-login100">
			<div class="wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55">
				<form class="login100-form validate-form flex-sb flex-w" id="post" method="POST" action="<?php echo $_SERVER["PHP_SELF"]; ?>" >
                    <span class="login100-form-title p-b-32">
                        <a href="/">
                            <i class="fa fa-arrow-left" style="padding:10px;font-size:23px;"></i>
                        </a>
                        Login Account
					</span>

					<span class="txt1 p-b-11">
						Email
					</span>
					<div class="wrap-input100 validate-input m-b-36" data-validate = "Email is required">
						<input class="input100" type="text" name="mail" >
						<span class="focus-input100"></span>
					</div>
					
					<span class="txt1 p-b-11">
						Password
					</span>
					<div class="wrap-input100 validate-input m-b-12" data-validate = "Password is required">
						<span class="btn-show-pass">
							<i class="fa fa-eye"></i>
						</span>
						<input class="input100" type="password" name="pass" >
						<span class="focus-input100"></span>
					</div>
					
					<div class="flex-sb-m w-full p-b-48">
						<div class="contact100-form-checkbox">
							<input class="input-checkbox100" id="ckb1" type="checkbox" name="remember-me">
							<label class="label-checkbox100" for="ckb1">
								Remember me
							</label>
						</div>

						<div>
							<a href="#" class="txt3">
								Forgot Password?
							</a>
						</div>
					</div>

					<div class="container-login100-form-btn w-100">
							<button class="login100-form-btn bg-primary" 
							style="width: 100% !important;"
							>LOGIN</button>
					</div>
				</form>
			</div>
		</div>
    </div>
    
<?php
$html->footer();
?>