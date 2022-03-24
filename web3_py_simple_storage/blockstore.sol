pragma solidity ^0.6.0;

// SPDX-License-Identifier: MIT

contract simpleStorage {
    //Initialized to 0
    uint256 favoriteNumber;
    bool bigBool;
    bool bigBool2;

    //Struct ==  Object
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;

    mapping(string => uint256) public nametoFavNumber;

    function add(uint256 _favoriteNumber) public returns(uint256){
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    function store2() public returns (uint256) {
        return favoriteNumber;
    }

    //View, pure functions just view data or do some math respectively
    function retrieve(uint256 _favoriteNumber) public view returns (uint256) {
        return favoriteNumber;
    }

    //Memory vs storage defines how you store data. Volatile or non-volatile

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nametoFavNumber[_name] = _favoriteNumber;
    }
}
