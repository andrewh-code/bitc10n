import pyelliptic
import avl_tree
import data_structures

CONST = _CONST()
utx = unspent_tx()

class wallet:
	#I gotta research more
	# see https://asecuritysite.com/encryption/elc
	
	def __init__(self):
		self.key_ring = pyelliptic.ECC()
        self.unspent = unspent_tx()
	
	def get_addr(self):
		return self.key_ring.get_pubkey()
		
    def rec_coins(self, block):
    #analyze a block and see if we got anything
    #only analyze blocks that are verified
        if False == verify(block):
            return   
        for output in block.tx.outputs:
            if output.destination == self.key_ring.get_pubkey():
                utx.insert(output)
        
	def send(self, amount, destination, change):
        if (amount + change) > self.unspent.amount):
            return False
        
    #support one destination for now
		return 0
        
def verify_block(block):
    if block
    
class miner:
    def __init__(self, miner_pubkey, prev_block):
        self.block = block(hash(prev_block, miner_pubkey), merkle_hash, miner_pubkey)
    
    def mine(self):
        self.block.nonce += 1
        return verify_block(self.block)
    
    def add_tx(self, tx):
    
    def remove_tx(self, tx):
    
    