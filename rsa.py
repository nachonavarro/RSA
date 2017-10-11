"""
RSA is a public cryptosystem that relies on number theory.
It works for both encryption of messages as well as digital
signatures.

The main two functions to encrypt and decrypt a message.
For simplicity, we will assume that the message is already
transformed into a number ready for RSA.

It should be the case that

decrypt(encrypt(msg, public_key), private_key) == msg

"""


def encrypt(msg, public_key):
	"""Encrypt the message using the public key.
	In other words, given that msg is already a number,
	compute msg ^ public_key.pub mod public_key.n

    Args:
        msg (int): Message to securely send.
        public_key (namedtuple(PublicKey)): A namedtuple
        consisting of two parameters, n and pub.

    Returns:
        int: The ciphered message as an int between 1 and n.

    """
	return pow(msg, public_key.pub, public_key.n)

def decrypt(cipher, private_key):
	"""Decrypt the message using the private key.
	In other words, given the cipher C, compute
	C ^ private_key.priv mod private_key.n.
	By the discussion on keygen.py, Only you can decipher C, as
    C ^ d = M ^ (ed) = M ^ (phi * k + 1) = M ^ (phi * k) * M
    = 1 * M = M mod n. The key is that due to Euler's Theorem,
    M ^ phi = 1 mod n.

    Args:
        msg (int): Message to securely send.
        private_key (namedtuple(PrivateKey)): A namedtuple
        consisting of two parameters, n and priv.

    Returns:
        int: The deciphered message as an int between 1 and n.

    """
	return pow(cipher, private_key.priv, private_key.n)