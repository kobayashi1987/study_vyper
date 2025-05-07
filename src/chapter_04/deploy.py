from web3 import Web3

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

with open("bytecode.txt") as f:
    bytecode = f.read().strip()

with open("abi.json") as f:
    abi = f.read().strip()

with open("mykey/UTC--2025-05-07T15-52-02.599585000Z--1b054ea9026e9354e8ec41ea733598bcf3bcafe0") as keyfile:
    encrypted_key = keyfile.read()
    password = "password456"
    deployer_private_key = w3.eth.account.decrypt(encrypted_key, password)

deployer_address = "0x1b054EA9026E9354E8EC41eA733598bCF3BCafE0"

contract = w3.eth.contract(abi=abi, bytecode=bytecode)

transaction = contract.constructor().build_transaction({
    'from': deployer_address,
    'nonce': w3.eth.get_transaction_count(deployer_address),
    'gas': 200000,
    'gasPrice': Web3.to_wei('50', 'gwei')
})

signed_transaction = w3.eth.account.sign_transaction(transaction, deployer_private_key)

transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash)

