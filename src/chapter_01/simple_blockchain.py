
import hashlib
import json

class Block:
    id = None
    history = None
    parent_id = None
    parent_hash = None


block_A = Block()
block_A.id = 1
block_A.hitory = "Nelson likes cat"

block_B = Block()
block_B.id = 2
block_B.history = "Marie likes dog"
block_B.parent_id = block_A.id
block_B.parent_hash = hashlib.sha256(json.dumps(block_A.__dict__).encode('utf-8')).hexdigest()

block_C = Block()
block_C.id = 3
block_C.history = "Jack likes dog"
block_C.parent_id = block_B.id
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()


block_D = Block()
block_D.id = 4
block_D.history = "Miyuki likes cat"
block_D.parent_id = block_C.id
block_D.parent_hash = hashlib.sha256(json.dumps(block_C.__dict__).encode('utf-8')).hexdigest()

block_E = Block()
block_E.id = 5
block_E.history = "Janice likes cat"
block_E.parent_id = block_D.id
block_E.parent_hash = hashlib.sha256(json.dumps(block_D.__dict__).encode('utf-8')).hexdigest()


print(block_B.__dict__)
print()

print(json.dumps(block_B.__dict__))
print()

print(json.dumps(block_B.__dict__).encode('utf-8'))
print()

print(hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')))
print()

print(hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest())
print()

print(block_B.parent_hash)



