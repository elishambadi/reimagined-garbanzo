# Deploying our compiled contracts
from brownie import accounts, config, simpleStorage
import os

def deploy_simple_storage():
    account = accounts[0]
    # # print(account)
    # # account = accounts.load("metamask1")
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    simple_storage = simpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.add(200, {"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def main():
    deploy_simple_storage()