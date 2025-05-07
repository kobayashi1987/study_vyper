#!/usr/bin/env python3
from web3 import Web3
from vyper import compile_code
from pathlib import Path

def main():
    # 1. Connect to Anvil
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
    if not w3.is_connected():
        raise RuntimeError("Unable to connect to Anvil. Make sure it's running.")

    # 2. Contract address
    contract_address = w3.to_checksum_address("0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0")

    # 3. Compile contract to get ABI
    vyper_path = Path("PiggyBank.vy")
    source = vyper_path.read_text()
    compiled = compile_code(source, output_formats=["abi"])
    abi = compiled["abi"]

    # 4. Create contract instance
    contract = w3.eth.contract(address=contract_address, abi=abi)

    # 5. Prepare transaction
    tx = contract.functions.withdraw().build_transaction({
        "from": w3.eth.accounts[0],
        "nonce": w3.eth.get_transaction_count(w3.eth.accounts[0]),
        "gas": 100_000,
        "gasPrice": w3.to_wei("1", "gwei"),
        "chainId": 31337
    })

    # 6. Sign and send transaction
    signed = w3.eth.account.sign_transaction(
        tx,
        private_key="0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
    )
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    print(f"Withdrawal transaction submitted: {tx_hash.hex()}")

    # 7. Wait for receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Withdrawal confirmed in block {receipt.blockNumber}")

if __name__ == "__main__":
    main() 