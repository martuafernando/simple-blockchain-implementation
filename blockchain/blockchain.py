import datetime
import hashlib
import json

class Blockchain:
  def __init__(self) -> None:
    self.chain = []
    
    self.create_block(proof=1, data=None)
    
  def create_block(
    self,
    proof,
    prev_hash = "0",
    data=None,
  ):
    block = {
      "id_block": len(self.chain),
      "timestamp": str(datetime.datetime.now()),
      "proof": proof,
      "data": data,
      "prev_hash": prev_hash,
    }
    
    block['hash'] = self.get_hash(block=block)
    
    self.chain.append(block)
    return block
  
  def get_latest_block(self):
    return self.chain[-1]
  
  def modify_block_hash(self, id, hash):
    block = self.chain[id]
    block['hash'] = hash
    
  def modify_block_data(self, id, data):
    block = self.chain[id]
    block['data'] = data
    block['hash'] = self.get_hash(block)

  def proof_of_work(self, prev_proof):
    new_proof = 1
    check_proof = False
    
    while check_proof is False:
      hash_operation = hashlib.sha256(
        str(new_proof**2 - prev_proof**2).encode()
      ).hexdigest()
      
      if hash_operation[:4] == '0000':
        check_proof = True
      else :
        new_proof += 1
    return new_proof
  
  def get_hash(self, block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()
  
  def is_chain_valid(self):
    prev_block = self.chain[0]
    i = 1
    
    while i < len(self.chain):
      block = self.chain[i]
      
      if block['prev_hash'] != self.get_hash(prev_block):
        return False
      
      prev_proof = prev_block['proof']
      proof = block['proof']
      hash_operation = hashlib.sha256(
        str(proof**2 - prev_proof**2).encode()
      ).hexdigest()
      
      if hash_operation[:4] != '0000':
                return False
      prev_block = block
      i += 1
      
    return True
      
      