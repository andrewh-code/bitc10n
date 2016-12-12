import pickle
import pyelliptic
class input:
    def __init__(self):
        self.prev = 99
        self.index = 88
        self.signature = 7
        self.nonce = 0
        
    def get_nonce():
        return self.nonce
        
        
alice = pyelliptic.ecc()
bob = pyelliptic.ecc()
a = input()
name = 'sample.pk1'

output = open(name, 'wb')
c = pickle.dump(a, output)
output.close()

cipher = alice.encrypt("such mystery", bob.get_pubkey())
print(cipher)

print(bob.decrypt(cipher))

sign = bob.sign("Hello alice")

print(pyelliptic.ecc(pubkey=bob.get_pubkey()).verify(sign, "Hello alice"))



