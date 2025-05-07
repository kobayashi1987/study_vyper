#!/usr/bin/env python3
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from vyper import compile_code
from web3 import Web3

def main():
    # 1. Connect to Anvil (local chain)
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if not w3.is_connected():
        raise RuntimeError("Unable to connect to Anvil. Make sure it's running.")

    # 2. Use the first Anvil account (it comes with 10000 ETH)
    account = w3.eth.accounts[0]
    print(f"Using account: {account}")

    # 3. Compile the Vyper contract
    vyper_path = Path("PiggyBank.vy")
    source = vyper_path.read_text()
    compiled = compile_code(source, output_formats=["abi", "bytecode"])
    abi = compiled["abi"]
    bytecode = compiled["bytecode"]

    # 4. Calculate unlock time (e.g. 24h from now)
    unlock_time = int((datetime.now(timezone.utc) + timedelta(seconds=10)).timestamp())
    print(f"Contract will unlock at: {datetime.fromtimestamp(unlock_time)}")

    # 5. Build the contract object
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    construct_txn = Contract.constructor(
        account, unlock_time
    ).build_transaction({
        "chainId": 31337,  # Anvil's chain ID
        "from": account,
        "nonce": w3.eth.get_transaction_count(account),
        "gas": 2_000_000,
        "gasPrice": w3.to_wei("1", "gwei"),
    })

    # 6. Sign and send the transaction
    signed = w3.eth.account.sign_transaction(construct_txn, private_key="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")  # Anvil's first account private key
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Transaction submitted: {tx_hash.hex()}")

    # 7. Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Contract deployed at: {receipt.contractAddress}")
    print(f"   Block number: {receipt.blockNumber}")

if __name__ == "__main__":
    main()