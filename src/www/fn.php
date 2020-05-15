<?php

class mystring{
    public function split_name($name) {
        $parts = array();
    
        while ( strlen( trim($name)) > 0 ) {
            $name = trim($name);
            $string = preg_replace('#.*\s([\w-]*)$#', '$1', $name);
            $parts[] = $string;
            $name = trim( preg_replace('#'.$string.'#', '', $name ) );
        }
    
        if (empty($parts)) {
            return false;
        }
    
        $parts = array_reverse($parts);
        $name = array();
        $name['first_name'] = $parts[0];
        $name['middle_name'] = (isset($parts[2])) ? $parts[1] : '';
        $name['last_name'] = (isset($parts[2])) ? $parts[2] : ( isset($parts[1]) ? $parts[1] : '');

        $_SESSION['loggedin'] = true;
    
        return $name;
    }

    public function saltPass($pass){
        $pass = strrev($pass); #Reversing a string
        $salted = 'T2F3R5DT2G3S652RR'; #ALL USER HAVE SAME SALT
        return $salted.$pass;
    }
}