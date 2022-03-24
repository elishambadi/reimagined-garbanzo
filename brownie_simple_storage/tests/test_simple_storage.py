from brownie import simpleStorage, accounts

# Tests should have assert section
# For more tests, check pytest documentation

def test_deploy():
    # Arrange
    account = accounts[0]

    # Act
    simple_storage = simpleStorage.deploy({"from":account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected

def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = simpleStorage.deploy({"from":account})
    # Act
    expected = 200
    simple_storage.add(expected, {"from":account})
    # Assert
    assert expected == simple_storage.retrieve()