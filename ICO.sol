// DeBraineChain (DBC) ICO

pragma solidity ^0.4.23;

contract DBC_ICO {
    
    // Maximum number of DBC available for sale
    uint public max_DBC = 1000000;

    // USD to DBC conversion rate
    uint public USD_to_DBC = 1000;

    // Total number of DBC bought by investors
    uint public total_DBC_bought = 0;

    // Mapping from the investor address to its equity in DBC and USD
    mapping(address => uint) equity_DBC;
    mapping(address => uint) equity_USD;

    // Checking if an investor can buy DBC
    modifier can_buy_DBC(uint USD_invested) {
        require (USD_invested * USD_to_DBC + total_DBC_bought <= max_DBC);
        _;
    }

    // Getting the equity in DBC of an investor
    function equity_in_DBC(address investor) external view returns (uint) {
        return equity_DBC[investor];
    }

    // Getting the equity in USD of an investor
    function equity_in_USD(address investor) external view returns (uint) {
        return equity_USD[investor];
    }

    // Buying DBC
    function buy_DBC(address investor, uint USD_invested) external
    can_buy_DBC(USD_invested) {
        uint DBC_bought = USD_invested * USD_to_DBC;
        equity_DBC[investor] += DBC_bought;
        equity_USD[investor] = equity_DBC[investor] / USD_to_DBC;
        total_DBC_bought += DBC_bought;
    }

    // Selling DBC
    function sell_DBC(address investor, uint DBC_sold) external {
        equity_DBC[investor] -= DBC_sold;
        equity_USD[investor] = equity_DBC[investor] / USD_to_DBC;
        total_DBC_bought -= DBC_sold;
    }
}
