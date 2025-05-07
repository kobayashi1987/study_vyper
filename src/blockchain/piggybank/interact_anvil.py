#!/usr/bin/env python3
from web3 import Web3
from vyper import compile_code
from pathlib import Path

def main():
    # 1. Connect to Anvil
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if not w3.is_connected():
        raise RuntimeError("Unable to connect to Anvil. Make sure it's running.")

    # 2. Contract address (replace with your deployed contract address)
    contract_address = w3.to_checksum_address("0xc6e7DF5E7b4f2A278906862b61205850344D4e7d")  # Anvil's first contract address

    # 3. Compile contract to get ABI
    vyper_path = Path("PiggyBank.vy")
    source = vyper_path.read_text()
    compiled = compile_code(source, output_formats=["abi"])
    abi = compiled["abi"]

    # 4. Create contract instance
    try:
        contract = w3.eth.contract(address=contract_address, abi=abi)
        
        # 5. Read contract state
        print("Contract State:")
        print("Beneficiary:", contract.functions.beneficiary().call())
        print("Unlock time:", contract.functions.unlock_time().call())
        print("Contract balance:", w3.from_wei(w3.eth.get_balance(contract_address), "ether"), "ETH")
    except Exception as e:
        print(f"Error interacting with contract: {e}")
        print("Make sure the contract is deployed and the address is correct")

if __name__ == "__main__":
    main() 