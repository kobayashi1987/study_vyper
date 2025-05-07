#!/usr/bin/env python3
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from vyper import compile_code
from web3 import Web3

def main():
    # 1. Load secrets from .env
    load_dotenv()
    rpc_url = os.getenv("SEPOLIA_RPC_URL")
    priv_key = os.getenv("DEPLOYER_PRIVATE_KEY")
    if not rpc_url or not priv_key:
        raise RuntimeError("Please set SEPOLIA_RPC_URL and DEPLOYER_PRIVATE_KEY in .env")

    # 2. Connect to Sepolia
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise RuntimeError(f"Unable to connect to {rpc_url}")

    # 3. Prepare account
    account = w3.eth.account.from_key(priv_key)
    print(f"Deploying from address: {account.address}")

    # 4. Compile the Vyper contract
    vyper_path = Path("PiggyBank.vy")
    source = vyper_path.read_text()
    compiled = compile_code(source, output_formats=["abi", "bytecode"])
    abi = compiled["abi"]
    bytecode = compiled["bytecode"]

    # 5. Calculate unlock time (e.g. 24h from now)
    unlock_time = int((datetime.now(timezone.utc) + timedelta(seconds=10)).timestamp())

    # 6. Build the contract object
    Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    construct_txn = Contract.constructor(
        account.address, unlock_time
    ).build_transaction({
        "chainId": 11155111,               # Sepolia chain ID
        "from": account.address,
        "nonce": w3.eth.get_transaction_count(account.address),
        "gas": 2_000_000,
        "gasPrice": w3.to_wei("50", "gwei"),
    })

    # 7. Sign and send the transaction
    signed = account.sign_transaction(construct_txn)
    tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
    print(f"Transaction submitted: {tx_hash.hex()}")

    # 8. Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Contract deployed at: {receipt.contractAddress}")
    print(f"   Block number: {receipt.blockNumber}")

if __name__ == "__main__":
    main() 