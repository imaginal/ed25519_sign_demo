<?php

if (file_exists("keyseed.dat")) {
    echo "Load key seed from file\n";
    $sign_seed = file_get_contents("keyseed.dat");
} else if (file_exists("keypair.dat")) {
    echo "Load key pair from file\n";
    $sign_pair = file_get_contents("keypair.dat");
    $sign_seed = substr($sign_pair, 0, 32);
} else {
    echo "Generate key seed\n";
    $sign_seed = random_bytes(SODIUM_CRYPTO_SIGN_SEEDBYTES);
    echo "Save keyseed.dat\n";
    file_put_contents("keyseed.dat", $sign_seed);
}

$sign_pair = sodium_crypto_sign_seed_keypair($sign_seed);
$sign_secret = sodium_crypto_sign_secretkey($sign_pair);
$sign_public = sodium_crypto_sign_publickey($sign_pair);

if (!file_exists("keypair.dat")) {
    echo "Save keypair.dat\n";
    $keypair = substr($sign_pair, 0, 64);
    file_put_contents("keypair.dat", $keypair);
}

$sign_secret32 = substr($sign_secret, 0, 32);
echo "--- Private key ---\n";
echo "HEX: ".bin2hex($sign_secret32)."\n";
echo "B64: ".base64_encode($sign_secret32)."\n";
echo "--- Public key ---\n";
echo "HEX: ".bin2hex($sign_public)."\n";
echo "B64: ".base64_encode($sign_public)."\n";
echo "---\n";

if (!file_exists("hello.msg")) {
    $message = 'hello';
    echo "Save message to file hello.msg\n";
    file_put_contents("hello.msg", $message);
} else {
    echo "Load message from file hello.msg\n";
    $message = file_get_contents("hello.msg");
}

echo "Message to sign: ".$message."\n";

if (!file_exists("hello.sig")) {
    $signature = sodium_crypto_sign_detached($message, $sign_secret);
    $signature_encoded = base64_encode($signature);
    echo "Sinature of message:\n";
    echo $signature_encoded."\n";
    file_put_contents("hello.sig", $signature_encoded);
} else {
    echo "Load signature from file hello.sig\n";
    $signature_encoded = file_get_contents("hello.sig");
    echo $signature_encoded."\n";
    $signature = base64_decode($signature_encoded);
}

echo "Verify signature\n";
$res = sodium_crypto_sign_verify_detached($signature, $message, $sign_public);
var_dump($res); # true or false

?>
