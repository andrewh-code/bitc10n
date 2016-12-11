import pickle
import pyelliptic


class cucumber:

    def __init__(self, x):
        self.x = x
        
    def get_x(self):
        return self.x
key = pyelliptic.ecc()   


a = cucumber(10)
cereal = pickle.dumps(a)
print(cereal)
cipher = key.encrypt(cereal, pubkey=key.get_pubkey())
print(cipher)
print(key.decrypt(cipher))



