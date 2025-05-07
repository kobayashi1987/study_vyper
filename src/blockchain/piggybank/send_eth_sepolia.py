#!/usr/bin/env python3
from web3 import Web3
from dotenv import load_dotenv
import os

def main():
    # 1. Load environment variables
    load_dotenv()
    rpc_url = os.getenv("SEPOLIA_RPC_URL")
    priv_key = os.getenv("DEPLOYER_PRIVATE_KEY")
    contract_address = os.getenv("SEPOLIA_CONTRACT_ADDRESS")
    
    if not all([rpc_url, priv_key, contract_address]):
        raise RuntimeError("Please set SEPOLIA_RPC_URL, DEPLOYER_PRIVATE_KEY, and CONTRACT_ADDRESS in .env")

    # 2. Connect to Sepolia
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise RuntimeError(f"Unable to connect to {rpc_url}")

    # 3. Prepare account
    account = w3.eth.account.from_key(priv_key)
    print(f"Sending from address: {account.address}")

    # 4. Prepare transaction
    tx = {
        "to": contract_address,
        "value": w3.to_wei(0.01, "ether"),
        "nonce": w3.eth.get_transaction_count(account.address),
        "gas": 100_000,
        "gasPrice": w3.to_wei("50", "gwei"),
        "chainId": 11155111  # Sepolia chain ID
    }

    # 5. Sign and send transaction
    signed = account.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Transaction submitted: {tx_hash.hex()}")

    # 6. Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Transaction confirmed in block {receipt.blockNumber}")

if __name__ == "__main__":
    main() 