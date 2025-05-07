import hashlib, json, time

def mine_block(block_data, difficulty):

    nonce = 1
    attempts = 0
    prefix = '0' * difficulty

    start = time.time()

    serialized = json.dumps(block_data, sort_keys=True).encode('utf-8')
    

    while True:
        attempt = str(nonce).encode('utf-8') + serialized
        hash_hex = hashlib.sha256(attempt).hexdigest()

        if hash_hex.startswith(prefix):
            return nonce, hash_hex, attempts, time.time() - start
        
        nonce += 1
        attempts += 1
        
block_data = {"name": "jack", "age": 38, "city": "zurich", "country": "switzerland"}

nonce, hash_hex, attempts, elapsed = mine_block(block_data, 5)

print(f"Nonce: {nonce}")
print(f"Hash: {hash_hex}")
print(f"Attempts: {attempts}")
print(f"Elapsed: {elapsed} seconds")

