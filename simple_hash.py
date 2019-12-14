import hashlib, json

block_genesis = {
    'prev_hash' : None,
    'transactions' : [1,2,4,3]
    }
block_2 = {
    'prev_hash' : None,
    'transactions' : [1,3,4,5]
    }
block_3 = {
    'prev_hash' : None,
    'transactions' : [4,3,1,5]
    }

def hash_blocks(blocks):
 prev_hash = None
 for block in blocks:
  block['prev_hash'] = prev_hash
  block_serialized = json.dumps(block, sort_keys=True).encode('utf-8')
  block_hash = hashlib.sha256(block_serialized).hexdigest()
  prev_hash = block_hash
 return prev_hash


print("Orignal hash")
print(hash_blocks([block_genesis, block_2, block_3]))

print("Let's tamper with data")
block_genesis['transactions'][0] = 3


print("After blocks being tampered")
print(hash_blocks([block_genesis, block_2, block_3]))

