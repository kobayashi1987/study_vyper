from web3 import Web3
import sys

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
print("Chain ID:", w3.eth.chain_id)          # usually 1337 in dev mode
accounts = w3.eth.accounts
print("Accounts:", accounts)         # pre-funded dev accounts
if len(accounts) < 2:
    print(f"Not enough accounts (found only {len(accounts)}), please create or fund a second account.")
    sys.exit(1)
tx_hash = w3.eth.send_transaction({
    "from": accounts[0],
    "to": accounts[1],
    "value": w3.to_wei(1, "ether")
})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Mined in block:", receipt.blockNumber)