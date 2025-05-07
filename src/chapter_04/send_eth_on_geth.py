
from web3 import Web3

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

with open("mykey/UTC--2025-05-07T15-52-02.599585000Z--1b054ea9026e9354e8ec41ea733598bcf3bcafe0") as keyfile:
    encrypted_key = keyfile.read()
    password = "password456"
    sender_private_key = w3.eth.account.decrypt(encrypted_key, password)

sender_address = Web3.to_checksum_address("0x1b054EA9026E9354E8EC41eA733598bCF3BCafE0")

recipient_address = Web3.to_checksum_address("0xd30561464ee30ff007e8e1c49aa950448db485bd")

amount = Web3.to_wei(2, 'ether')

transaction = {
    'chainId': 1337,
    'from': sender_address,
    'to': recipient_address,
    'value': amount,
    'gas': 21000,
    'gasPrice': Web3.to_wei('50', 'gwei'),
    'nonce': w3.eth.get_transaction_count(sender_address),
}

signed_transaction = w3.eth.account.sign_transaction(transaction, sender_private_key)

transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash)
print(transaction_hash.hex())