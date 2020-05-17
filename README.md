# MD5 Brute Force

<p>Python 3.8.2</p>
<p>Programming and Security</p>
<p>Polytechnic Institute of Guarda</p>
<br/>
<p>Please install:</p>
<p>&nbsp; install python v3.8.2</p>
<p>&nbsp; install pip</p>
<p>&nbsp; pip install bs4</p>
<p>&nbsp; pip install requests</p>
<p>&nbsp; install Xampp (SERVER)</p>
<p>&nbsp; XAMPP: change the path from xampp to <code>../BruteforceMD5/src/www<code></p>

<code>
  <p>Example: </p>
  <p>> Please write the web page with an input? http://localhost/login.php</p>
  <img src="" ></img>
  <br/>
  <p>[+] Threads: 24</p>
  <p>[+] Try: 27284127</p>
  <p>[+] Found: 10</p>
  <p>[+] Finished in 184.72 second(s)</p>
  <p>[+] File: C:../../src/data/hash.json</p>
</code>

<img src="" ></img>

<h4>How to decrypt MD5 cipher?</h4>
The MD5 is based on non-linear (and sometimes non-reversible) functions, so there is no decryption method.
However, a stupid and brute method, the most basic but also the longest and most costly method, is to test one by one all the possible words in a given dictionary to check if their fingerprint is the matching one.
dCode uses its databases of words (2 million potential passwords) whose MD5 hash has already been pre-calculated. These tables are called rainbow tables.

<h4>What is a MD5 collision?</h4>
Statistically speaking, for any string (and there is an infinite number), the MD5 associates for a given value a 128-bit fingerprint (a finite number of possibilities). It is therefore mandatory that there are collisions (2 strings with the same hash). Several research works on the subject have demonstrated that the MD5 algorithm, although creating a large entropy of data, could be attacked, and that it was possible to generate chains with the same fingerprints (after several hours of neat calculations).

Example: Discovered by Wang & Yu in How to break MD5 and other hash functions, the two hexadecimal values (the values and not the ASCII string)
<code>
<strong>4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2</strong>
<strong>4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2</strong>
</code>

have the same hash: <code>008ee33a9d58b51cfeb425b0959121c9</code> (they only differ by 8 hexadecimal digits)
<br/>
Since this publication in 2005, MD5 encryption is no longer considered cryptographically, giving way to its successors: SHA1 then SHA256.