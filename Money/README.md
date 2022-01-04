# Smart_House - Money

Vytvořeno v Qt Creator 6.0.1 (Qt 6.2.2)

Pro úpravu projektu je potřeba nainstalovat Qt Creator (https://www.qt.io/download)
Poté je také potřeba Perl pro překompilování Qt (https://strawberryperl.com/)
Pro kompilování mysql knihovny je potřeba MariDB, nebo MySQL (https://mariadb.org/download/) 

```
C:\Qt\6.2.2\Src> configure -plugin-mysql --MYSQL_INCDIR="C:/Program Files/MySQL/MySQL Connector C 6.1/include" --MYSQL_LIBDIR="C:/Program Files/MySQL/MySQL Connector C 6.1/lib"
```

```
C:\Qt\6.2.2\Src> mingw32-make
``` > ERROR > ```
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp: In member function 'bool QOpcUaKeyPairPrivate::generateRsaKey(QOpcUaKeyPair::RsaKeyStrength)':
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:140:25: error: 'q_EVP_PKEY_CTX_new_id' was not declared in this scope; did you mean 'EVP_PKEY_CTX_new_id'?
  140 |     EVP_PKEY_CTX *ctx = q_EVP_PKEY_CTX_new_id(EVP_PKEY_RSA, nullptr);
      |                         ^~~~~~~~~~~~~~~~~~~~~
      |                         EVP_PKEY_CTX_new_id
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:145:43: error: 'q_EVP_PKEY_CTX_free' was not declared in this scope; did you mean 'EVP_PKEY_CTX_free'?
  145 |     Deleter<EVP_PKEY_CTX> ctxDeleter(ctx, q_EVP_PKEY_CTX_free);
      |                                           ^~~~~~~~~~~~~~~~~~~
      |                                           EVP_PKEY_CTX_free
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:147:9: error: 'q_EVP_PKEY_keygen_init' was not declared in this scope; did you mean 'EVP_PKEY_keygen_init'?
  147 |     if (q_EVP_PKEY_keygen_init(ctx) <= 0) {
      |         ^~~~~~~~~~~~~~~~~~~~~~
      |         EVP_PKEY_keygen_init
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:152:9: error: 'q_EVP_PKEY_CTX_set_rsa_keygen_bits' was not declared in this scope; did you mean 'EVP_PKEY_CTX_set_rsa_keygen_bits'?
  152 |     if (q_EVP_PKEY_CTX_set_rsa_keygen_bits(ctx, static_cast<int>(strength)) <= 0) {
      |         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      |         EVP_PKEY_CTX_set_rsa_keygen_bits
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:157:9: error: 'q_EVP_PKEY_keygen' was not declared in this scope; did you mean 'EVP_PKEY_keygen'?
  157 |     if (q_EVP_PKEY_keygen(ctx, &m_keyData) <= 0) {
      |         ^~~~~~~~~~~~~~~~~
      |         EVP_PKEY_keygen
In file included from C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\openssl_symbols_p.h:250,
                 from C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:38:
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp: In member function 'QOpcUaKeyPair::KeyType QOpcUaKeyPairPrivate::keyType() const':
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qsslsocket_opensslpre11_symbols_p.h:181:41: error: invalid use of incomplete type 'EVP_PKEY' {aka 'struct evp_pkey_st'}
  181 | #define q_EVP_PKEY_base_id(pkey) ((pkey)->type)
      |                                         ^~
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qsslsocket_opensslpre11_symbols_p.h:181:41: note: in definition of macro 'q_EVP_PKEY_base_id'
  181 | #define q_EVP_PKEY_base_id(pkey) ((pkey)->type)
      |                                         ^~
In file included from C:/Strawberry/c/include/openssl/crypto.h:25,
                 from C:/Strawberry/c/include/openssl/bio.h:20,
                 from C:/Strawberry/c/include/openssl/asn1.h:16,
                 from C:/Strawberry/c/include/openssl/rsa.h:16,
                 from C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_p.h:54,
                 from C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:37:
C:/Strawberry/c/include/openssl/ossl_typ.h:93:16: note: forward declaration of 'EVP_PKEY' {aka 'struct evp_pkey_st'}
   93 | typedef struct evp_pkey_st EVP_PKEY;
      |                ^~~~~~~~~~~
C:\Qt\6.2.2\Src\qtopcua\src\opcua\x509\qopcuakeypair_openssl.cpp:216:1: warning: control reaches end of non-void function [-Wreturn-type]
  216 | }
      | ^
mingw32-make[2]: *** [qtopcua\src\opcua\CMakeFiles\OpcUa.dir\build.make:1054: qtopcua/src/opcua/CMakeFiles/OpcUa.dir/x509/qopcuakeypair_openssl.cpp.obj] Error 1
mingw32-make[1]: *** [CMakeFiles\Makefile2:56795: qtopcua/src/opcua/CMakeFiles/OpcUa.dir/all] Error 2
mingw32-make: *** [Makefile:145: all] Error 2
```