from web3 import Web3

with open("abi.json") as f:
    abi = f.read().strip()

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

address = "0x1166c7A8fE10389d0E285977B0C34824dE35BC28"
contract = w3.eth.contract(address=address, abi=abi)

number = contract.functions.retrieve().call()
print(number)