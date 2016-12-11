import pickle
import pyelliptic

class cucumber:

    def __init__(self, x):
        self.x = x
        
    def get_x(self):
        return self.x
        
a = cucumber(10)
key = pyelliptic.ecc()

name = 'sample.pk1'

output = open(name, 'wb')
b = pickle.dumps(a)
output.close()

print(b)

cipher = key.encrypt(b, pubkey=key.get_pubkey())
print(cipher)

print(key.decrypt(cipher))



