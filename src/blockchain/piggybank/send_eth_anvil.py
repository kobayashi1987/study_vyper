#!/usr/bin/env python3
from web3 import Web3
from web3.exceptions import TimeExhausted
import time

def main():
    # 1. Connect to Anvil
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if not w3.is_connected():
        raise RuntimeError("Unable to connect to Anvil. Make sure it's running.")

    # 2. Contract address
    contract_address = w3.to_checksum_address("0xc6e7DF5E7b4f2A278906862b61205850344D4e7d")

    # 4. Prepare transaction
    tx = {
        "from": w3.eth.accounts[0],  # Add the from address
        "to": contract_address,
        "value": w3.to_wei(10, "ether"),  # Send 1 ETH
        "nonce": w3.eth.get_transaction_count(w3.eth.accounts[0]),
        "gas": 100_000,
        "gasPrice": w3.to_wei("1", "gwei"),
        "chainId": 31337  # Anvil's chain ID
    }

    # 5. Sign and send transaction
    signed = w3.eth.account.sign_transaction(
        tx, 
        private_key="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"  # Anvil's first account private key
    )
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Transaction submitted: {tx_hash.hex()}")
    print("Waiting for transaction confirmation...")

    # 6. Wait for receipt with custom timeout and status updates
    try:
        # Set a custom timeout of 300 seconds (5 minutes)
        timeout = 300
        start_time = time.time()
        
        while True:
            try:
                receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=10)
                print(f"✅ Transaction confirmed in block {receipt.blockNumber}")
                break
            except TimeExhausted:
                elapsed = time.time() - start_time
                if elapsed >= timeout:
                    raise TimeExhausted(f"Transaction not confirmed after {timeout} seconds")
                print(f"Still waiting for confirmation... ({int(elapsed)} seconds elapsed)")
                continue

    except TimeExhausted as e:
        print(f"❌ Error: {str(e)}")
        print("Transaction might still be pending. You can check its status later.")
        return

    # 7. Verify the contract balance
    balance = w3.eth.get_balance(contract_address)
    print(f"Contract balance: {w3.from_wei(balance, 'ether')} ETH")

if __name__ == "__main__":
    main() 