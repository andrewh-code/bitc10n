import random
import pyelliptic
import pickle

class _CONST:
    def __init__:
        self.lock_size = 0xFFFFFFF


class unspent_tx(self):
    #assume transactions are hashed values that we can cmp directly
	def __init__(self):
		self.tree = avl_tree.AVLTree()
        self.total = 0;
		return

	def insert(self, tx):
        self.tree.insert(tx)
        self.total += tx.amount
		return
        
	def delete_key(self, key):
        self.total -= self.tree.get_node(key).amount
        self.tree.delete(key)       
        return
        
    def get_node_key(self, key):
        return self.tree.get_node(key)
        
	def rebalance(self):
        self.tree.rebalance()
        return
   
def hash(data, pubkey):
    cereal = pickle.dumps(data)
    return pyelliptic.ecc.encrypt(cereal, pubkey)

class block:
    def __init__(self, prev_hash, merkle_hash, miner, diff=10):
        self.version = 1
        self.prev = prev_hash
        self.merkle_hash = merkle_hash
        self.nonce = 0
        self.difficulty = diff
        self.miner = miner
        self.tx = None
        
class input:
    def __init__(self, prev_tx, index, signature):
        self.prev_tx_hash = prev_tx #an output struct
        self.index = index
        self.signature = signature
    
    
class output:
    def __init__(self, amount, destination, lock=None):
        self.amount = amount      
        #Compare verify that the priv key owner signed the required msg
        self.destination = destination
        self.lock = str(random.nextInt(CONST.lock_size))
        
class transaction:
    def __init__(self):
        self.version = 1
        self.input_count = 0
        self.output_count = 0
        self.inputs = []
        self.outputs = []
        
    def add_input(self, prev_tx, key_ring):
    #todo: add more complicated locks
        signature = key_ring.sign(prev_tx.lock)      
        prev_tx = hash(prev_tx)
        input = input(prev_tx, self.input_count, signature)
        self.input_count += 1
        self.inputs.append(input)
    
    #lock will be customized locks for the future
    def add_output(coins, destination, lock=None):
    #todo: add more complicated locks
        out = output(coins, destination)
        self.outputs.append(out)
        self.output_count += 1
    
    def get_change():
        coin_out = 0
        for a in self.outputs:
            out = out + a.amount
            
        coin_in = 0
        for a in self.inputs:
            node = utx.get_node(a.prev_tx_hash)
            coin_in = coin_in + node.amount
        return (coin_in - coin_out)
    