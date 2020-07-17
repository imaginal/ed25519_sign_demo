ed25519 signature interoperability demo
=======================================

This is ed25519 signature interoperability demo between python and PHP libraries


Requirements
------------
 * python 3.5 or later
 * PHP 7.3 or later


Preparation
-----------
1. Verify that libsodium support is enabled in PHP
```
    $ php -i | grep sodium
    sodium
    sodium support => enabled
    libsodium headers version => 1.0.18
    libsodium library version => 1.0.18
```

2. Install python ed25519 library
```
    sh install_pyenv.sh
```

3. Activate virtual environment
```
    . venv/bin/activate
```


Run
---
```
php sign_demo.php
# or #
python sign_demo.py
```
These examples can be run in any order.


Files
-----
Once started, several files will be created

 * keypair.dat (size 64 bytes) - ed25519 private and public key

 * keyseed.dat (size 32 bytes) - sodium key seed for ed25519

Hint: first 32 byets of keypair.dat == keyseed.dat

  * hello.msg - message to sign (you can edit this file)

  * hello.sig - signature of message (in base64 encoding)

Hint: you can modify hello.msg to sign a custom message but
don't forget to delete hello.sig 



Troubleshooting
---------------

PHP
---
```
PHP Fatal error:  Uncaught Error: Call to undefined function sodium_crypto_sign_keypair() in ...
```
You use PHP older than 7.2 or the sodium library support is disabled



Python
------
```
ImportError: No module named ed25519
```
You have not installed dependencies or activated the virtual environment, please use install_pyenv.sh



Copyright
---------

(c) 2020 Volodymyr Flonts

Licensed under MIT

