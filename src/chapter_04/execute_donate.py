from web3 import Web3

with open("abi.json") as f:
    abi = f.read().strip()

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

account_address = "0x1b054EA9026E9354E8EC41eA733598bCF3BCafE0" 

with open("mykey/UTC--2025-05-07T15-52-02.599585000Z--1b054ea9026e9354e8ec41ea733598bcf3bcafe0") as keyfile:
    encrypted_key = keyfile.read()
    password = "password456"
    account_private_key = w3.eth.account.decrypt(encrypted_key, password)

address = "0x1166c7A8fE10389d0E285977B0C34824dE35BC28"
contract = w3.eth.contract(address=address, abi=abi)

transaction = contract.functions.donate().build_transaction({
    'from': account_address,
    'value': Web3.to_wei('1', 'ether'),
    'nonce': w3.eth.get_transaction_count(account_address),
    'gas': 200000,
    'gasPrice': Web3.to_wei('50', 'gwei')
})

signed_transaction = w3.eth.account.sign_transaction(transaction, account_private_key)

transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print(transaction_hash)