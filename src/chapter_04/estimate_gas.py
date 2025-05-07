from web3 import Web3

with open("bytecode.txt") as f:
    bytecode = f.read().strip()

with open("abi.json") as f:
    abi = f.read().strip()

deployer_address = "0x1b054EA9026E9354E8EC41eA733598bCF3BCafE0"

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

contract = w3.eth.contract(abi=abi, bytecode=bytecode)

total_gas = contract.constructor().estimate_gas({
    'from': deployer_address,
    'nonce': w3.eth.get_transaction_count(deployer_address),
    'gas': 200000,
    'gasPrice': Web3.to_wei('50', 'gwei')
})

print(total_gas)