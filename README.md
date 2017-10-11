# RSA

## Background

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. To understand RSA one
must first understand public-key cryptosystems, a _very_ elegant attempt invented by Diffie and Hellman to solve secure transmission of data over an unsecure channel. 

As an analogy to understand a public-key cryptosystem, consider a physical lock that requires two keys side by side to open. Now say Bob wants people to communicate with him. He leaves in his front porch an opened box, the previous mentioned
physical lock, and one of the two keys. He then leaves for work. Alice then comes and needs to privately tell Bob a very important message. She will write the message, put it inside the box, and shut the box with the lock. She then can leave, because only the owner
of the second key can open that lock and therefore read the message. That is (very roughly) a public-key cryptosystem.

## R, S, and A's Method
The method they propose in their [paper](https://people.csail.mit.edu/rivest/Rsapaper.pdf) is the following:
Choose two large primes p and q.
