# MD5 Brute Force

<p>Python 3.8.2</p>
<p>Programming and Security</p>
<br/>
<p>Please install:</p>

### - install python v3.8.2
### - install pip
### - pip install bs4
### - pip install requests
### - install Xampp (SERVER)
### - XAMPP: change the path from xampp to ../BruteforceMD5/src/www
<br/>
<code>
  <p>Example: </p>
  <p> Please write the web page with an input? http://localhost/login.php</p>
  <img src="assets/login.png" ></img>
  <br/><br/>
  <p>[+] Threads: 24</p>
  <p>[+] Try: 27284127</p>
  <p>[+] Found: 10</p>
  <p>[+] Finished in 184.72 second(s)</p>
  <p>[+] File: C:../../src/data/hash.json</p>
</code>
<p>Some developers, when creating a login system using MD5, do not do it in a secure way, the password entered by the application user is the same password that goes into the database. as shown in the figure below</p>
<br/>
# Front End
<img src="assets/unsafe.png" ></img>
<br/><br/>
# Back End
<img src="assets/unsafecode.jpg" ></img>
<br/>
<img src="assets/unsafedb.png" ></img>
<br/>
<br/>
<code>
  md5('liverpool1994') == '93322a1066d78e71db3bc180e2de1693'
</code>
<br/>
<br/>
<img src="assets/hacker.jpg" ></img>
<br/>
<p>The bad news is that this form of encryption can be easily broken, with some technical help:</p>

### - [BruteForce Attack](https://en.wikipedia.org/wiki/Brute-force_attack)

### - [Dictionary Attack](https://en.wikipedia.org/wiki/Dictionary_attack)

### - [RainbowTable Attack](https://en.wikipedia.org/wiki/Rainbow_table)

### - [WordList Attack](https://securityonline.info/collection-great-wordlist-for-brute-force-attackwordlist-brute-force-attackword-list-downloads/)

<hr/><br/>
Don't worry, there is a solution for this type of problem.
<br/>

# Front End
<img src="assets/safe.png" ></img>
<br/><br/>
# Back End
<img src="assets/safecode.jpg" ></img>
<br/>
<img src="assets/safedb.png" ></img>
<br/><br/>
<code>
  md5('anyPassword05') != '2740726e14066e180a2dd40c8cf7f2ad'
</code>
<br/><br/>

# How this algorithm works?

### 1st - You need to add the web page with input.<br/>
<img src="assets/input.png" ></img>
<br/><br/>
### 2nd - Copy the URL http://localhost/login.php<br/><br/>
### Add URL
<img src="assets/addinput.png" /><br/><br/>
### Add type
<img src="assets/addtype.png" /><br/><br/>
### Wait for the result
<img src="assets/result.png" ></img>