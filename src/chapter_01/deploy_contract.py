# deploy_contract.py

from web3 import Web3
from vyper import compile_code

# Step 1. Read the Vyper contract source code
with open('SimpleStorage.vy', 'r') as file:
    contract_source_code = file.read()

# Step 2. Compile the Vyper contract using the named parameter `output_formats`
compiled_contract = compile_code(contract_source_code, output_formats=["bytecode", "abi"])
bytecode = compiled_contract["bytecode"]
abi = compiled_contract["abi"]

# Step 3. Connect to a local Ethereum network (e.g., Ganache)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
if not w3.is_connected():
    raise ConnectionError("Unable to connect to the Ethereum network. Make sure Ganache is running.")
print("Connected to Ethereum network.")

# Step 4. Set the default account for transactions (use the first Ganache account)
w3.eth.default_account = w3.eth.accounts[0]

# Step 5. Create a Contract object with the compiled bytecode and ABI
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Step 6. Deploy the contract (initial stored value 42)
print("Deploying contract...")
tx_hash = SimpleStorage.constructor(42).transact()

# Wait for the transaction to be mined and get the transaction receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress
print("Contract deployed at address:", contract_address)

# Step 7. Interact with the deployed contract
contract_instance = w3.eth.contract(address=contract_address, abi=abi)

# Retrieve the initial stored value
stored_value = contract_instance.functions.get().call()
print("Initial stored value (should be 42):", stored_value)

# Update the stored value to 100
print("Updating stored value to 100...")
tx_hash_set = contract_instance.functions.set(100).transact()
w3.eth.wait_for_transaction_receipt(tx_hash_set)

# Verify the updated value
updated_value = contract_instance.functions.get().call()
print("Updated stored value (should be 100):", updated_value)