<?php

class html{
    public function header($title = 'IPG'){
        $html = '<!DOCTYPE html>'.
        '<html lang="en">'.
        '<head>'.
            '<title>'.$title.'</title>'.
            '<meta charset="UTF-8">'.
            '<meta name="viewport" content="width=device-width, initial-scale=1">'.
            '<link rel="icon" href="https://cloud.sysnovare.pt/ipg/imagens/pageicon" type="image/x-icon" />'.
            '<link rel="stylesheet" type="text/css" href="src/vendor/bootstrap/css/bootstrap.min.css">'.
            '<link rel="stylesheet" type="text/css" href="src/fonts/font-awesome-4.7.0/css/font-awesome.min.css">'.
            '<link rel="stylesheet" type="text/css" href="src/fonts/Linearicons-Free-v1.0.0/icon-font.min.css">'.
            '<link rel="stylesheet" type="text/css" href="src/vendor/animate/animate.css">'.
            '<link rel="stylesheet" type="text/css" href="src/vendor/css-hamburgers/hamburgers.min.css">'.
            '<link rel="stylesheet" type="text/css" href="src/vendor/animsition/css/animsition.min.css">'.
            '<link rel="stylesheet" type="text/css" href="src/vendor/select2/select2.min.css">'.
            '<link rel="stylesheet" type="text/css" href="src/vendor/daterangepicker/daterangepicker.css">'.
            '<link rel="stylesheet" type="text/css" href="src/css/util.css">'.
            '<link rel="stylesheet" type="text/css" href="src/css/main.css">'.
        '</head>'.
        '<body>';
        echo $html;
    }

    public function footer(){
        $html = '<div id="dropDownSelect1"></div>'.
        '<script src="src/vendor/jquery/jquery-3.2.1.min.js"></script>'.
        '<script src="src/vendor/animsition/js/animsition.min.js"></script>'.
        '<script src="src/vendor/bootstrap/js/popper.js"></script>'.
        '<script src="src/vendor/bootstrap/js/bootstrap.min.js"></script>'.
        '<script src="src/vendor/select2/select2.min.js"></script>'.
        '<script src="src/vendor/daterangepicker/moment.min.js"></script>'.
        '<script src="src/vendor/daterangepicker/daterangepicker.js"></script>'.
        '<script src="src/vendor/countdowntime/countdowntime.js"></script>'.
        '<script src="src/js/main.js"></script>'.
        '<style>div.other{position:relative;width:100%;text-align:right;}'.
        'div.other i{cursor:pointer;font-size:20px;}</style>'.
        '</body>'.
        '</html>';
        echo $html;
    }
}

?>