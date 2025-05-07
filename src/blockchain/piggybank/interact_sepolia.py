#!/usr/bin/env python3
from web3 import Web3
from dotenv import load_dotenv
import os
from vyper import compile_code
from pathlib import Path

def main():
    # 1. Load environment variables
    load_dotenv()
    rpc_url = os.getenv("SEPOLIA_RPC_URL")
    contract_address = os.getenv("SEPOLIA_CONTRACT_ADDRESS")  # Add this to your .env file
    
    if not rpc_url or not contract_address:
        raise RuntimeError("Please set SEPOLIA_RPC_URL and CONTRACT_ADDRESS in .env")

    # 2. Connect to Sepolia
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise RuntimeError(f"Unable to connect to {rpc_url}")

    # 3. Compile contract to get ABI
    vyper_path = Path("PiggyBank.vy")
    source = vyper_path.read_text()
    compiled = compile_code(source, output_formats=["abi"])
    abi = compiled["abi"]

    # 4. Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=abi)

    # 5. Read contract state
    print("Contract State:")
    print("Beneficiary:", contract.functions.beneficiary().call())
    print("Unlock time:", contract.functions.unlock_time().call())
    print("Contract balance:", w3.from_wei(w3.eth.get_balance(contract_address), "ether"), "ETH")

if __name__ == "__main__":
    main() 