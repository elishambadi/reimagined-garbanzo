// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe{

    //Crowdscourcing Application

    using SafeMathChainlink for uint256;

    mapping(address => uint256) public addressToAmountFunded;
    address public owner;

    address[] public funders;

    constructor() public {
      owner = msg.sender;
    }

    function fund() public payable{
      uint256 minimumUSD = 5 * 10 ** 18;

      require(getConversionRate(msg.value) >= minimumUSD,"You need to spend more ETH");

        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);

    }

    function getVersion() public view returns(uint256){
      AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
      return priceFeed.version();
    }

    function getPrice() public view returns(uint256){
      AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
      (,int256 answer,,,) = priceFeed.latestRoundData();

      return uint256(answer * 10000000000); //Returns price in Wei 
    }

    function getConversionRate(uint256 ethAmount) public view returns(uint256){
      uint256 ethPrice = getPrice();

      uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000; //Converts price from WEI to dollars
      return ethAmountInUsd;
    }
    
    //Similar to a validator
    modifier onlyOwner{
      require(msg.sender == owner);
      _;
    }

    function withdraw() public onlyOwner payable{
      //Withdraw all the crowdsourced funds

      //Allow only owner to withdraw funds
      msg.sender.transfer(address(this).balance);

      //After withdrawing everyones balance should be set to 0
      for (uint256 funderIndex = 0;
       funderIndex < funders.length; funderIndex++){
         address funder = funders[funderIndex];
         addressToAmountFunded[funder] = 0;
       }

       funders = new address[](0);
    }
}
