###    crypto_xor.so
######    m = b"hello, world"
######    k = xki( len(m.decode('utf')) )
######    x = xor( m.decode('utf'), k )


<br />


###    crypto_aes.so
######    m = b"hello, world"
######    k, i = aes_k()
######    e = aes_e( m, k, i )
######    d = aes_d( e, k, i )


<br />


###    crypto_cha.so
######    m = b"hello, world"
######    k, n = cha_k()
######    e = cha_e( m, k, n )
######    d = cha_d( e, k, n )


<br />


###    crypto_rsa.so
######    m = b"hello, world"
######    s, v = rsa_k()
######    e = rsa_e( m, v )
######    d = rsa_d( e, s )
