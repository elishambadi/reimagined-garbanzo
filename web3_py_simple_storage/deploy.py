# My first python script

from rsa import PrivateKey
from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./blockStore.sol", "r") as file:
    simple_storage_file = file.read()

    # print(simple_storage_file)

# Compiling ssolidity

install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"blockStore.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

# Viewing compiled code
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# Deploying
# Get bytecode
bytecode = compiled_sol["contracts"]["blockStore.sol"]["simpleStorage"]["evm"][
    "bytecode"
]["object"]

# Get Abi
abi = compiled_sol["contracts"]["blockStore.sol"]["simpleStorage"]["abi"]

# print(abi)

# Connect to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 1337
my_address = "0xDc1A2CDc7fD59ba80180261ef5EB9CC00ACc7642"
# 0x added before private key, so py can get hex version


# private_key = os.getenv("PRIVATE_KEY") Gets from os variables
private_key = os.getenv("PRIVATE_KEY_1")  # Gets from env file

print(private_key)

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)

# Build a transaction to deploy contracts
# Get latest transaction

nonce = w3.eth.getTransactionCount(my_address)
gasPrice = w3.eth.gas_price

transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce, "gasPrice": gasPrice}
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print(transaction)

# Now sending our compiled, signed transaction having our contract to the blockchain
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
