from web3 import Web3

with open("abi.json") as f:
    abi = f.read().strip()

w3 = Web3(Web3.IPCProvider('/tmp/geth.ipc'))

address = "0x1166c7A8fE10389d0E285977B0C34824dE35BC28"
contract = w3.eth.contract(address=address, abi=abi)

logs = contract.events.Donation().get_logs(from_block = 0)

for log in logs:
    print(f"The donatur address is {log.args.donatur}")
    print(f"The donation amount is {log.args.amount}")