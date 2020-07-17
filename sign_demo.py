#!/usr/bin/env python
import os.path
import ed25519


def main():
    keyfile = "keypair.dat"
    keyseed = "keyseed.dat"
    if not os.path.exists(keyfile):
        if os.path.exists(keyseed):
            print("Load key seed from", keyseed)
            with open(keyseed, "rb") as fp:
                seed = fp.read()
            if len(seed) != 32:
                print("Bad seed size, must be 32 bytes")
                return
            print("Create key from 32 bytes seed")
            sk = ed25519.SigningKey(seed)
            vk = sk.get_verifying_key()
        else:
            print("Generate new keypair...")
            sk, vk = ed25519.create_keypair()
        skb = sk.to_bytes()
        print("Save", len(skb), "bytes to", keyfile)
        skb = sk.to_bytes()
        with open(keyfile, "wb") as fp:
            fp.write(skb)
        seed = skb[:32]
        print("Save", len(seed), "bytes to", keyseed)
        with open(keyseed, "wb") as fp:
            fp.write(seed)
    else:
        print("Load key pair from", keyfile)
        keydata = open(keyfile, 'rb').read()
        if len(keydata) != 64:
            print("Bad key file size, must be 64 bytes")
            return
        sk = ed25519.SigningKey(keydata)
        vk = sk.get_verifying_key()

    print("--- Secret key ---")
    print("HEX:", sk.to_ascii(encoding="hex").decode())
    print("B64:", sk.to_ascii(encoding="base64").decode())
    print("--- Public key ---")
    print("HEX:", vk.to_ascii(encoding="hex").decode())
    print("B64:", vk.to_ascii(encoding="base64").decode())
    print("---")

    msgfile = "hello.msg"
    if not os.path.exists(msgfile):
        message = b"hello"
        with open(msgfile, "wb") as fp:
            fp.write(message)
    else:
        print("Load message from", msgfile)
        message = open(msgfile, "rb").read()

    print("Message to sign:", message)

    sigfile = "hello.sig"
    if not os.path.exists(sigfile):
        sig = sk.sign(message, encoding="base64")
        print("Sign message, signature in base64:")
        print(sig.decode())
        print("Save signature to", sigfile)
        with open(sigfile, "wt") as fp:
            fp.write(sig.decode())
    else:
        print("Load signature from", sigfile)
        sig = open(sigfile).read().encode()
        print("Signature of message in base64:")
        print(sig.decode())

    print("Verify signature")
    vk.verify(sig, message, encoding="base64")
    print("SUCCESS")


if __name__ == '__main__':
    main()

