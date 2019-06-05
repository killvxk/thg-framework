import hashlib


class Hash_encode:
    """
    suport para hash_encode
    =>sha3_256
    =>ha256
    =>blake2b
    =>sha384
    =>md5
    =>sha3_512
    =>sha512
    =>sha512
    =>sha1
    =>sha3_224
    =>blake2s
    =>sha3_384
    =>sha224
    """

    def __init__(self, sha3_256, sha256, blake2b, sha384, md5, sha3_512, sha512, sha1, sha3_224, blake2s, sha3_384,
                 sha224):
        self.sha3_256 = sha3_256
        self.sha256 = sha256
        self.blake2b = blake2b
        self.sha384 = sha384
        self.md5 = md5
        self.sha3_512 = sha3_512
        self.sha512 = sha512
        self.sha512 = sha512
        self.sha1 = sha1
        self.sha3_224 = sha3_224
        self.blake2s = blake2s
        self.sha3_384 = sha3_384
        self.sha224 = sha224

    def sha3_256(self):
        hash = hashlib.sha3_256()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha256(self):
        hash = hashlib.sha256()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def blake2b(self):
        hash = hashlib.blake2b()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha384(self):
        hash = hashlib.sha384()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def md5(self):
        hash = hashlib.md5()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha3_512(self):
        hash = hashlib.sha3_512()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha512(self):
        hash = hashlib.sha512()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha1(self):
        hash = hashlib.sha1()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha3_224(self):
        hash = hashlib.sha3_224()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def blake2s(self):
        hash = hashlib.blake2s()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha3_384(self):
        hash = hashlib.sha3_384()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())

    def sha224(self):
        hash = hashlib.sha224()
        hash.update(self.encode('utf-8'))
        print(hash.hexdigest())
