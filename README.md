# RSA

## Background

RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. To understand RSA one
must first understand public-key cryptosystems, a _very_ elegant attempt invented by Diffie and Hellman to solve secure transmission of data over an unsecure channel. 

As an analogy to understand a public-key cryptosystem, consider a physical lock that requires two keys side by side to open. Now say Bob wants people to communicate with him. He leaves in his front porch an opened box, the previous mentioned
physical lock, and one of the two keys. He then leaves for work. Alice then comes and needs to privately tell Bob a very important message. She will write the message, put it inside the box, and shut the box with the lock. She then can leave, because only the owner
of the second key can open that lock and therefore read the message. That is (very roughly) a public-key cryptosystem.

## R, S, and A's Method
The method they propose in their [paper](https://people.csail.mit.edu/rivest/Rsapaper.pdf) is the following:

Choose two large primes `p` and `q` (these will be, of course, kept private). Set `n = p * q` and `phi = (p - 1) * (q - 1)`. Choose a number `e` that is prime to `phi`, and set `d` to be the multiplicative inverse of `e` mod `phi`. Finally, give out to the world
the pair `(n, e)`, and keep private the pair `(n, d)`.

The beauty comes now. For Alice to send a message `M` (which we assume is already a number), she looks in Bob's directory, and finds
the pair `(n, e)`. She then computes `C = M ^ e mod n`, and sends `C` to Bob. Notice that nobody knows what `C` means, it is just 
apparent gibberish in the eyes of somebody who is snooping over the network. However, once Bob receives `C`, he can find out what it means. First notice that since `e * d = 1 mod phi` then `phi * k + 1 = e * d` for some `k`. We use this along Euler's theorem that states that for any `a` prime to `n`, `a ^ phi(n) = 1 mod n`, where `phi` is Euler's function. With all of this, Bob does the following:
`C ^ d = M ^ (ed) = M ^ (phi * k + 1) = M ^ (phi * k) * M = 1 * M = M mod n`, and he finally has `M`.
