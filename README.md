# Blockchain-AZ-Projects

Based on the incredible course: [Blockchain A-Z on Udemy](https://www.udemy.com/build-your-blockchain-az/)

## Table of Contents

1. [Summary](#Summary)
2. [Notes](#Notes)
    1. [The blockchain](#THE-BLOCKCHAIN)
    2. [The Cryptocurrency](#THE-CRYPTOCURRENCY)
    3. [The Smart Contract](#THE-SMART-CONTRACT)
3. [Output Examples](#Output-Examples)
4. [Resources](Resources)

## Summary

### THE BLOCKCHAIN
- **Version 1.0: Creating the Basic Blockchain**
    - **Codes involved:**
        - `blockchain.py`
        - `webapp_blockchain.py`
    - **Progress**
        - Blockchain class created (without stored data)
        - Able to rudimentarily: 
            - display the chain
            - mine a block
            - check the validity of the chain
    - **Instructions**
        - run `python blockchain.py`
    
- **Version 2.0: Creating the Basic Cryptocurrency**
    - **codes involved:**
        - `DeBraineChain.py`
        - `webapp_DeBraineChain.py`
            - Other Copies:
                - `node_5001.py`
                - `node_5002.py`
                - `node_5003.py`
        - `nodes.json`
        - `transaction.json`
    - **Progress**
        - Built upon V1.0, added:
            - transactions
                - transactions include:
                    - miner rewards
                    - fees
                    - amount transfered
            - UTOX
            - Mempool
            - Creation of nodes features to allow multiple individuals and/or miners
            - Consensus protocol
            - Mining a block validates transactions
    - **Instructions**
        - run `python node_5001.py` and/or `python node_5002.py` etc...
            - to create multiple nodes
        - Following commands are available:
            - GET:
                - `http://127.0.0.1:5001/get_chain`
                - `http://127.0.0.1:5001/mine_block`
                - `http://127.0.0.1:5001/replace_chain`
                - `http://127.0.0.1:5001/is_valid`
            - POST:
                - `http://127.0.0.1:5001/add_transaction`
                    - example JSON: `transactions.json`
                - `http://127.0.0.1:5001/connect_node`
                    - example JSON: `nodes.json`

### THE SMART CONTRACT
- **Version 1.0: Created a basic Smart Contract in `Solidity`**
    - **codes involved:**
        - `ICO.sol`
    - **Progress**
        - Created a basic Smart Contract in solidity:
            - Able to:
                - Invest USD
                - Buy Token with USD
                - Sell Token back to USD
                - Check Balances

## Notes

### THE BLOCKCHAIN

- **SHA256**
    - "finger print" of the current block
    - any change to the data will completely change the hash
    - a piece of data has a unique hash
    - 5 requirements
        - one way
        - deterministic
        - fast computation
        - avalanche effect
            - any change to the data will completely change the hash
        - must withstand collisions
            - collisions: different pieces of data that have the same hash
            - cannot purposefully create a different piece of data with the same hash
- **immutable ledger**
    - the impossibility to change the data in a blockchain without changing the entire blockchain
- **distributed P2P network**
    - everyone participating has a copy of the blockchain
    - the blockchain owned by the majority is the valid blockchain
- **mining: Nonce**
    - "Number used only once"
    - a way to manipulate the block hash by changing the Nonce (data, previous hash, and block number cannot be changed)
- **Consensus Protocol**
    - in case of two valid blocks mined at once, the one with the longest chain is chosen (more hashing power).
    - **Proof of Work (POW)**
        - A series of check to validate a block based on the work done to solve the cryptographic puzzle (hard to solve but easy to verify)
        - All you need to verify is to check that the block data does output the right hash
    - **Proof of Stake (POS)**
        - to be determined

### THE CRYPTOCURRENCY

- **What is Bitcoin?**
    - 3 layers:
        - technology
            - blockchain
        - protocol/coin: 
            - A set of rules that guides how participants in the networks to communicate with each other
            - Contains a coin
            - can be mined, typically the basis of the mining rewards.
            - examples of protocols:
                - Bitcoin, Ethereum, etc...
        - token: ICOs offer tokens and not coins
            - rely on smart contract that rely on protocols
            - represents the "idea" behind what they are building
            - Bitcoin, and Ripple have no tokens
            - there is no mining involved with tokens
    - Invented by Satoshi Nakamoto
    - Bitcoin Ecosystem:
        - Nodes: People
        - Miners
        - Large mines
        - Mining Pools
- **Bitcoin's monetary policy**
    - Entirely controlled by the software
    - The halving
        - The number of Bitcoins released into the system (bitcoins per block) is halved every 210,000 blocks
        - 21 Million Bitcoins by 2140 (Since there is a finite number of decimals allowed)
        - If the number of Bitcoins users increase then the transaction fees should increase which should counter balance the loss of rewards from halving to the miners
    - inflation:
        - coinbase * BlocksPerYear / ExistingCoins
    - The Block Frequency
        - Average block time:
            - Bitcoin: 10min, Ethereum: 15s, etc...
- **Understanding mining difficulty**
    - Current target: leading zeros
        - If the Results space encompasses all possible hash (hexadecimal):
            - TotalResultsSpace*(1/16)^NumberLeadingZeros is the reduced results space
        - Bitcoin: As of 6/13/2018, the target is 18 leading zeros
            - Probability: 
                - Total possible hashes: 16^64
                - Total valid hashes: 16^46
                - Probability of randomly pick a valid hash: 2*10^-22
    - How is mining difficulty calculated:
        - Difficulty = current target / max target
        - Difficulty is adjusted every 2016 blocks (~2 weeks)
        - max target = 00000000FFFF0000000000000000000000000000000000000000000000000000
            - created at the very start of Bitcoin
        - adjusted so that it takes 10min to mine a bitcoin on average
            - However, power needed increases
        - currently 5 trillion times harder to mine a block than at the start:
            - [https://blockchain.info/charts/difficulty](https://blockchain.info/charts/difficulty)
- **Bitcoin mine**
    - Images of a large Bitcoin mine:
        - [Large Chinese Bitcoin Mine](https://qz.com/1055126/photos-china-has-one-of-worlds-largest-bitcoin-mines/)
- **Mining pools**
    - Personal computer mining is very unlikely to solve the cryptographic puzzle before large industrial mines
    - To solve that problem mining pools are created
        - several people combine their hashing power to compete
        - Distribution of the cryptographic puzzle to all participants to avoid double work
            - Not working on the same Nonce
        - Reward split depending on the hashing power contributed
    - Removes headache of programming and taking care of the mining
    - mining pool services take care of the computation entirely
- **Nonce range and how miners pick transactions**
    - Nonce: a field in the block that can be changed to allow miners to compute different hashes to solve the cryptographic puzzle
    - Nonce is not infinite: 32-bit number
        - 0 -> 4 bil
    - total possible 64 bit hexadecimal numbers: 10^64
    - total valid hashes: 16^46
    - probability that a random picked hash is valid: 2^-22
    - Total possible 32-bit Nonce numbers: 2^32
        - Assuming no collisions: 4*10^9 different hashes
    - Probability that ONE Nonce leads to a valid hash: 10^-12
        - MEANING: **One Nonce range is not enough to find a golden Nonce**
    - A modest miner does 100 Million hashes per second (MH/s)
        - a total Nonce range is then computed in 40seconds
        - A solution to this problem is the use of the **Unix Time** in the hashing.
            - since the time stamp is constantly changing every second, the hash also changes. Therefore, even if the Nonce range is limited, the hash is constantly changing with the changing time stamp allowing for the Nonce to be reset.
    - If the mining rate goes beyond 4 bil hashes per second (BH/s):
        - every node has a list of transactons stored in a **Mempool**
        - A miner will choose which transactions are stored in the block from the Mempool
            - Will choose the transactions with the highest fees.
        - If the miner is not able to solve the cryptographic puzzle he will change the transactions included (replace a single transaction with the lowest fee by another transaction).
        - He will do that until a second has passed then resets the transactions included to the transactions with the highest fees.
        - Therefore No matter the mining rate, the miner is not constrained by the finite Nonce range.
    - Blocks have a maximum size (Bitcoin: 1MB)
        - People have to specify higher fees if they want their transactions to be pushed into a block by miners.
- **CPU vs GPU vs ASIC**
    - As of 6/13/2018 the Bitcoin mining rate is 36 mil TH/s (million trillion hashes per second)
    - CPU: Central Processing Unit -> General
        - Can solve the SHA256 < 10 MH/s
    - GPU: Graphics Processing Unit -> Specialized (Matrix operations)
        - Can solve the SHA256 < 1 GH/s
    - ASIC: Application-Specific Integrated Circuit -> Specialized (SHA256 Hash)
        - Can solve the SHA256 > 1,000 GH/s
    - Cloud Mining: Pay a fee to use someone else's equipment
    - No one has been successful yet to create an ASIC for Ethereum mining as it is memory dependent and doesn't use SHA256
- **How do Mempools work**
    - A Mempool is attached to each participant (miner or individual)
    - A Mempool is not the blockchain it's a staging area for transactions before they are added to a block
    - Blocks are added at a certain regularity (Bitcoin around every 10min)
    - When a transaction is conducted, it is added to the participant's Mempool then propagated to the whole network Mempools if it is a valid transaction (see details further down)
    - The Mempools are then filled with transactions and are identical between each participant (Considering each transaction is a valid transaction)
    - A block can contain around 2000 transactions (1MB)
    - Once a new block is mined, it contains a set of transactions that was selected based on their assigned fees which are given to the miner as a reward.
    - These transactions are removed from the Mempools.
    - In conclusion, transactions are more likely to go through faster if assigned fees are higher.
    - NOTE: Transactions on the Mempools are called **Unconfirmed Transactions**
- **Orphaned blocks**
    - When two different miners find a new block at which point two versions of the chain are created
    - Whoever finds the next block first confirms the chain and the other chain becomes invalid
    - Transactions contained in the dropped chain go back to the Mempool except transactions that were also in the valid chain
    - Therefore typically transactions are only successful after a couple of blocks were created.
    - Rule of thumb for Bitcoin: wait for 6 confirmations (mined blocks)
    - [Bitcoin Orphaned Blocks](https://blockchain.info/orphaned-blocks)
    - Exchanges will not send you your money until a couple confirmations occur
- **The 51% attack**
    - Hypothetical attack
    - It is not an attack designed to temper with already made blocks
    - Refers to 51% of the hash rate
    - Consider:
        - a new blockchain with a few miners with their mempools
        - a set of new miners then joins the network with their own mempools
        - then the new set of miners decide to isolate themselves from the network and continue mining by themselves (not broadcast their new blocks)
        - Now consider that these new miners have more than 51% of the hashing power (therefore mine faster than the regular blockchain network)
        - Then after a while broadcast their **longer** blockchain
        - Therefore all the new blocks mined (hence validated transactions) by the original miners become invalid because as said above, the **longer chain becomes the valid chain** and all the transactions go back to the mempool
        - It creates a **double spend problem**
        - While the blocks of the new miners become valid, so do their transactions and with the anonymity that blockchain provides no one can contest. 
- **Bits to target conversion**
    - Deriving the current target:
        - We talked about the difficulty and the max target but what about the current target?
    - Where is the current target stored:
        - Bits: a field stored in the Bitcoin Block
        - The Bits is then converted to Hexadecimal
        - The first two values are then converted back to decimals
        - example:
            - Bits: 392009692
            - Bits in hex: 175D97DC
            - first two values in hex: 17
            - first two values in decmials: 23
            - That number becomes the number of bytes: 23 bytes -> 46 hex digits
            - Becomes: 0000000000000000000000000000000000000000000000
            - Replace the first values in that new hex number by the previous bits in hex:
            - Becomes: 5D97DC0000000000000000000000000000000000000000
            - Add missing leading zeros: 64 - 46 = 18 leading zeros as SHA256 is 64 bits
            - The current target becomes:
                - 0000000000000000005D97DC0000000000000000000000000000000000000000
        - In conclusion, the current target is stored in this Bits format in each block to save space
- **Transacitons and UTXOs (Unspent transactions outputs)**
    - The transaction lives on until another transaction builds on the previous UTXO
    - Since in a Blockchain there is no "Bank account" that contains money.
    - Transaction rule of thumb: no input can be unspent meaning that when a certain amount of coins from the UTXOs are taken as input to "buy" something the difference between the input and the "price" is placed back into the UTXOs.
    - Transaction example:
        - UTXOs:
            - friend 1 -> me 0.6 BTC
            - friend 2 -> me 0.1 BTC
            - friend 3 -> me 0.4 BTC
            - friend 4 -> me 0.3 BTC
        - Transaction 1: Buy item 1 for 0.5 BTC
            - Input:   
                - 0.6 BTC from friend 1
            - Output:
                - 0.5 BTC to shop
                - 0.05 BTC back to myself (back to UTXOs)
            - Fee:
                - 0.05 BTC
        - UTXOs:
            - friend 2 -> me 0.1 BTC
            - friend 3 -> me 0.4 BTC
            - friend 4 -> me 0.3 BTC
            - me       -> me 0.05 BTC
        - Transaction 2: Buy item 2 for 0.6 BTC
            - Input:
                - 0.4 BTC from friend 3
                - 0.3 BTC from friend 4
            - Output:
                - 0.6 BTC to shop
                - 0.05 BTC back to myself (back to UTXOs)
            - Fee:
                - 0.05 BTC
        - UTXOs:
            - friend 2 -> me 0.1 BTC
            - me       -> me 0.05 BTC
            - me       -> me 0.05 BTC
- **Where do transaction fees come from?**
    - Anything not included in the output and input of a transaction becomes a fee.
    - A fee needs to be volunteered (or bid) for your transactions to be selected by the miner in their new block
- **How wallets work?**
    - Since a block in a blockchain only contains transactions how is the balance calculated?
    - The balance is just the sum of all your UTXOs
    - In reality there is no "coins" there is only a list of transactions
- **Signatures: Private and Public Keys**
    - Consider:
        - Private key: 
            - an individual unique identifier which you can generate a public key from.
            - a chosen number of chosen length (adds security)
            - Cannot be reversed engineered
        - Public key: 
            - can be shared with others and is generated from a private key through an elliptic function
            - a hexadecimal number based on the private key
        - Message: Could be a transaction
        - Signature: The private key is used to sign the message (combined)
        - Verification function: takes input signature, Public key, Message and outputs a yes or a no
    - The private key cannot be found through the verification function but the combination of the public key, private key and message can be checked whether it is valid or not.
        - example:
            - transaction goes into the Mempool (which contains the public key, signature and the message)
            - The verification function can then check whether the transaction (message + signature) was created by the private key which issued the public key.
- **What is Segregated Witness? (SegWit)**
    - Separate the signature and public key from the blocks as they are long hexadecimal numbers that take 60% of the size of the block.
    - Have the signature and public key in their own network (messaging channel)
    - can use the freed space to add more transactions
- **Public Key vs Bitcoin Address**
    - Bitcoin address: derived from the public key by applying the SHA256 hash
    - People can send transactions to either the public key or the bitcoin address
    - While the public key is shared it shouldn't be exposed too much and that is the purpose of the bitcoin address
    - If the elliptic function is reversed engineered then the private key can be obtained
    - if the SHA256 is used on top of the elliptic function, additional security is added to the private key
- **Hierarchically Deterministic (HD) wallets**
    - Purpose of the private key is to keep the identity of the own private
    - People shouldn't be able to monitor other's transactions
    - Contains:
        - Master Private key: used to generate private keys
        - both private keys and master private keys should be kept secrect
    - The master private key can generate new private keys by incrementing the the master private key by 1. 
    - The master private key can find out everything about every transactions from every private key generated but a generated private key cannot be used to find out about transactions from other generated private keys.
    - A master public key can also be used to check all public keys generated from all the private keys but it cannot be used to check the other private keys (keeps these private keys secure)

### THE SMART CONTRACT

- **What is Ethereum?**
    - Created by Vitalik Buterin (at 19 years old)
    - It is a protocol but designed not as a coin but as a platform for other projects to build on
    - Holds not only transactions but also smart contracts (programs)
    - imagine running Facebook not on a server but on a blockchain (i.e. on everyone's computer)
    - The idea: build a super computer on everyone's computer through a blockchain
- **What is a Smart Contract?**
    - It is a program (code) stored on the blockchain
    - The framework (script) that allows code to be stored on Ethereum is called "solidify"
    - Solidify is **turing-complete**
        - meaning you can code any logic on that language
        - Can avoid problems from infinite loops or heavy loops that might significantly slow down the blockchain (since programs run off the whole chain).
    - Each node has:
        - History of all smart contracts
        - history of all transactions
        - current state of all smart contracts
- **Decentralized Applications (Dapps)**
    - Interface for people to interact with something on the blockchain
        - the API for smart contracts
    - Dapp: Front end
    - Smart contract: back end
- **Ethereum Virtual Machine & Gas**
    - Security threats of smart contracts:
        - what if infinite loops or heavy computation programs are stored on the blockchain?
        - what if a virus is stored as a smart contract and could potentially infect all participants?
        - what if a smart contract is designed to access personal information of everyone on the blockchain?
    - viruses and access to private information:
        - Ethereum virtual Machine (EVM)
            - A virtual machine running on a computer meaning the smart contract only runs on that virtual environement and not on the actual computer
            - meaning if anything is wrong, only the secluded virtual environement is affected
            - Not able to leave the confinment of the virtual environement
    - Heavy calculations and infinite loop
        - GAS:
            - For any computation that is run on the blockchain, the developer (or smart contractor) need to pay (hence the concept of GAS).
            - Any operation costs a certain units of GAS (Refer to [https://ethgasstation.info](https://ethgasstation.info))
            - Forces people to write efficient code to minimize GAS cost
    - The idea behind Ethereum:
        - Use Ether to pay to run a code on the blockchain Ethereum: a Platform
- **Decentralized Autonomous Organizations (DAOs)**
    - An organization structure where "people/employees" are replaced by smart contracts
    - An organization that runs itself on a blockchain
- **The DAO Attack**
    - The DAO: 
        - one of the first decentralized autonomous organization created by vitalik himself
        - Investor-directed venture capital fund on Ethereum
        - was stateless (not run by any country)
        - May 2016: most successful crowdfunded project in history: $150,000,000
    - The error in the code:
        - An error in the code allowed for a hack of $50,000,000
        - The perpetrators didn't actually do anything illegal, they just find a flaw in the code that allowed them to siphon money out of the DAO account to theirs.
        - No one could stop it because the DAO was autonomous and the flaw was there.
        - The contracts by definition are immutable so couldn't be stopped.
    - The failsafe:
        - Funds cannot be taken out entirely from the DAO but first have to wait 30 days in a child company of the DAO.
    - The dilemna:
        - The code is LAW?
        - Should it be stopped or not?
        - A hard fork was proposed to change the code (change the smart contract).
        - The hard fork was done.
    - Ethereum was split into ETH and ETC
        - ETH: the money taken was redirected to their respective owners
        - ETC: the money stayed with the hacker
            - The hacker walked away with $67,000,000 worth of ETC
    - The problem was in the DAO code and not Ethereum
- **Soft and Hard Forks**
    - A fork refers to making a copy of the software in order to make a change (refers to the software not the blockchain per say)
    - A fork can lead to a split of the blockchain, meaning the creation of a new blockchain containing the history of the older blockchain but with the software change included and the old blockchain continuing on without the software change.
    - Soft Fork:
        - A rule of thumb: Tightens up the rules
        - meaning that the changes don't need the blockchain to split (but can if people wish to continue with the old rules) as the new blocks that follow new rules validate both the new and old rules and so does not need a split. The new rules validate the old rules too. This only happens if prior agreement happen and the people that follow the new rule have the majority of the hashing power and their chain will always be the longest one.
        - Bitcoin Example: 
            - The introduction of SegWit (july 2017) on block 476768
            - SegWit stores the signature of each transaction in another parallel system to free space from each block
    - Hard Fork:
        - Changes significant enough that new blocks that follow the old rules don't validate the new rules or that a new block created by the new block doesn't follow the old rules forcing a split.
        - A rule of thumb: Loosens up the rules
        - Bitcoin Example 1:
            - The split occured (july 20 2017) and created Bitcoin Cash
            - The increase from 2Mb to 8Mb of memory for transactions in each block
            - Bitcoin remained at 2Mb, Bitcoin Cash had 8Mb
        - Bitcoin Example 2:
            - Changed the software to be ASIC resistant (october 24 2017)
            - Split between Bitcoin Gold and Bitcoin
- **Initial Coin Offerings (ICOs)**
    - Equivalent of IPOs for blockchains except you receive tokens instead of shares.

## Output Examples

### BlockChain With Transactions

```json
    {
        "chain": [
            {
                "hash_operation": "0",
                "index": 1,
                "previous_hash": "0",
                "proof": 1,
                "time_stamp": "2018-06-14 10:04:04.239609",
                "transactions": []
            },
            {
                "hash_operation": "0000c00870f23a23ae80377298491b091db400d575be0efbde5b310f2f763ed1",
                "index": 2,
                "previous_hash": "f5b429ea032d12820f01912e515c52597466b343f5d94dd0234392cc12ebefc6",
                "proof": 533,
                "time_stamp": "2018-06-14 10:04:12.364284",
                "transactions": []
            },
            {
                "hash_operation": "0000b8318b7ca4e2bc9be063d7dfcb0d0e70f1b27133001f714f11c058c31e99",
                "index": 3,
                "previous_hash": "9668b6707a5115b0548e3b23a89a457f15a3370276b76dbeb5c64f2b2ca06504",
                "proof": 45293,
                "time_stamp": "2018-06-14 10:04:12.735498",
                "transactions": []
            },
            {
                "hash_operation": "000012c643d9610a15e350cb92ec6386b2b15e9d4170a0f06a4fd8525e440207",
                "index": 4,
                "previous_hash": "7162d29b67aa71d78a492cb5fa58023f97f45dbba1f0f79e088124590efca7a0",
                "proof": 21391,
                "time_stamp": "2018-06-14 10:04:13.192597",
                "transactions": []
            },
            {
                "hash_operation": "00004bd97b406d4c157b1f3293466d414711218bf9b44502fc96208a9ad4b3fb",
                "index": 5,
                "previous_hash": "d59e8664e525ce2f90278cbb3ad61350c758482460d10c944304fb2e0fc8bcca",
                "proof": 8018,
                "time_stamp": "2018-06-14 10:04:13.598482",
                "transactions": []
            },
            {
                "hash_operation": "00000f1a0dbcb6f6e74d8b2e15153e0320119ed7cb7519683bc116851d6d4fc3",
                "index": 6,
                "previous_hash": "278bd6d64a5c643ba55efd910d23e1f822a54b7d208d0c213de5022fa26c8731",
                "proof": 48191,
                "time_stamp": "2018-06-14 10:05:01.929271",
                "transactions": [
                    {
                        "amount": 83.75,
                        "fee": 0.5,
                        "receiver": "Miner_5002",
                        "sender": "Miner_5001"
                    },
                    {
                        "amount": 83.75,
                        "fee": 0.5,
                        "receiver": "Miner_5002",
                        "sender": "Miner_5001"
                    },
                    {
                        "amount": 83.75,
                        "fee": 0.5,
                        "receiver": "Miner_5002",
                        "sender": "Miner_5001"
                    },
                    {
                        "amount": 83.75,
                        "fee": 0.5,
                        "receiver": "Miner_5002",
                        "sender": "Miner_5001"
                    }
                ]
            },
            {
                "hash_operation": "0000da4012ef88a954b83b6d188fca1d354973ded35762e3fabb875024aa2768",
                "index": 7,
                "previous_hash": "808566074db718a57649fcfb617dbb708128799953f4e4e610eefdeb5025e951",
                "proof": 19865,
                "time_stamp": "2018-06-14 10:05:38.318547",
                "transactions": []
            }
        ],
        "length": 7
    }
```

### Transaction from UTOX to the Mempool

**Transaction Example**
```json
    {
        "sender": "Miner_5001",
        "receiver": "Miner_5002",
        "amount": 83.75,
        "fee": 0.5
    }
```
**Transaction from UTOX to Mempool Example**
```json
    {
        "balance": 47.25,
        "message": "This transaction will be added to the Mempool",
        "wallet": [
            {
                "amount": 15.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 15.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 15.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            }
        ]
    }
```

### Mining a Block after a Transaction

```json
    {
        "Miner_UTOX": [
            {
                "amount": 15.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 15.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 15.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 102,
                "fee": 0,
                "receiver": "Miner_5001",
                "sender": "79b8ff71911a43c5932baaaf472c90a3"
            }
        ],
        "hash_operation": "00004bd97b406d4c157b1f3293466d414711218bf9b44502fc96208a9ad4b3fb",
        "index": 5,
        "message": "Block Mined!",
        "previous_hash": "9ad41f80734c7f24016b71ea28ba9dd5291b01381a2d7a45968339db035264ab",
        "proof": 8018,
        "time_stamp": "2018-06-14 17:04:09.756132",
        "transactions": [
            {
                "amount": 83.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 83.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 83.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            },
            {
                "amount": 83.75,
                "fee": 0.5,
                "receiver": "Miner_5002",
                "sender": "Miner_5001"
            }
        ]
    }
```

## Resources

- **Blockchain**
    - Current Blockchain Information: [https://blockchain.info/](https://blockchain.info/)
    - What is a Blockchain
        - Stuart Haber & W. Scott Stornetta, (1991). [How to Time Stamp a Digital Document](https://www.anf.es/pdf/Haber_Stornetta.pdf)
    - Understanding a SHA256 Hash
        - Wouter Penard & Tim van Werkhoven, (2008), [On the Secure Hash Algorithm family](https://www.staff.science.uu.nl/~tel00101/liter/Books/CrypCont.pdf)
    - Immutable Ledger
        - Chris Berg, Sinclair Davidson & Jason Potts (2017),[The Blockchain Economy: A beginner’s guide to institutional cryptoeconomics](https://medium.com/@cryptoeconomics/the-blockchain-economy-a-beginners-guide-to-institutional-cryptoeconomics-64bf2f2beec4)
    - Distributed P2P Network
        - Vitalik Buterin, (2017), [The Meaning of Decentralization](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274)
    - Byzantine Fault Tolerance
        - Leslie Lamport, Robert Shostak, & Marshall Pease, (1982). [The Byzantine Generals Problem](https://people.eecs.berkeley.edu/~luca/cs174/byzantine.pdf)
        - Georgios Konstantopoulos, (2017). [Understanding Blockchain Fundamentals, Part 1: Byzantine Fault Tolerance](https://medium.com/loom-network/understanding-blockchain-fundamentals-part-1-byzantine-fault-tolerance-245f46fe8419)
    - Consensus Protocol
        - Satoshi Nakamoto, (2008). [Re: Bitcoin P2P e-cash paper](https://www.mail-archive.com/cryptography@metzdowd.com/msg09997.html)
        - Amy Castor, (2017). [A (Short) Guide to Blockchain Consensus Protocols](http://www.coindesk.com/short-guide-blockchain-consensus-protocols)
    - Decentralized or Distributed?
        - Vitalik Buterin, (2017), [The Meaning of Decentralization](https://medium.com/@VitalikButerin/the-meaning-of-decentralization-a0c92b76a274)
- **Cryptocurrency**
    - Bitcoin Stats
        - Satoshi Nakamoto, (2008). [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf)
    - Bitcoin's Monetary Policy
        - Mark E. Jeftovic, (2017). [The Time is Different Part 2: What Bitcoin Really Is](https://hackernoon.com/this-time-is-different-part-2-what-bitcoin-really-is-ae58c69b3bf0)
    - Mining Pools
        - Leo Weese, (2017). [Bitcoin mining and energy consumption](https://blog.bitcoin.org.hk/bitcoin-mining-and-energy-consumption-4526d4b56186)
    - How Miners Pick Transactions
        - Noelle Acheson, (2018). [How Bitcoin Mining Works](https://www.coindesk.com/information/how-bitcoin-mining-works/)
    - CPU's vs GPU's VS ASIC's
        - Vijay Pradeep, (2017). [Ethereum's Memory Hardness Explained, and the Road to Mining it with Custom Hardware](https://www.vijaypradeep.com/blog/2017-04-28-ethereums-memory-hardness-explained/)
    - How do Mempools Work?
        - Marion Deneuville, (2016), [An in-depth guide into how the mempool works](https://blog.kaiko.com/an-in-depth-guide-into-how-the-mempool-works-c758b781c608)
    - The 51% Attack
        - David Vorick, (2017), [Choosing ASICs for Sia (Read the comments too)](https://blog.sia.tech/choosing-asics-for-sia-b318505b5b51)
    - The Dao Attack
        - Richard Sutton, (1988), [Learning to Predict by the Methods of Temporal Differences](https://link.springer.com/article/10.1007/BF00115009)
    - Soft and Hard Forks
        - Richard Sutton, (1988), [Learning to Predict by the Methods of Temporal Differences](https://link.springer.com/article/10.1007/BF00115009)
    - What is Segregated Witness (SEGWIT)
        - Jimmy Song, (2017), [Understanding Segwit Block Size](https://medium.com/@jimmysong/understanding-segwit-block-size-fd901b87c9d4)
    - Public Key vs Bitch Address
        - hksupport, (2016), [What's the difference between public key and public address?](https://www.reddit.com/r/Bitcoin/comments/3filud/whats_the_difference_between_public_key_and/)
    - Hierarchically Deterministic (HD) Wallets
        - Vitalik Buterin, (2013), [Deterministic Wallets, Their Advantages and their Understated Flaws](https://bitcoinmagazine.com/articles/deterministic-wallets-advantages-flaw-1385450276/)
- **Smart Contract**
    - What is Ethereum
        - Alex Moskov, (2017), [What is Ethereum? | The Ultimate Beginners’ Guide](https://coincentral.com/what-is-ethereum/)
    - What is a Smart Contract
        - Nik Custodio, (2017), [Smart Contracts for Dummies](https://medium.freecodecamp.org/smart-contracts-for-dummies-a1ba1e0b9575)
    - Ethereum Virtual Machine and Gas
        - Danny Ryan, (2017), [Calculating Costs in Ethereum Contracts](https://hackernoon.com/ether-purchase-power-df40a38c5a2f)
    - Decentralized Autonomous Organizations (DAOS)
        - Vitalik Buterin, (2014), [DAOs, DACs, DAs and More: An Incomplete Terminology Guide](https://blog.ethereum.org/2014/05/06/daos-dacs-das-and-more-an-incomplete-terminology-guide/)
    - The DAO Attack
        - Matthew Leising, (2017), [The Ether Thief](https://www.bloomberg.com/features/2017-the-ether-thief/)
    - Soft and Hard Forks
        - Khaleel Kazi, (2017), [Complete Guide on Bitcoin and Blockchain Forks](https://coinpickings.com/complete-guide-bitcoin-blockchain-forks/)
    - Initial Coin Offerings (ICO)
        - Alex Wilhelm, (2017), [WTF is an ICO?](https://techcrunch.com/2017/05/23/wtf-is-an-ico/)
    - ICO Case Study
        - Praveen Krishnan, (2018), [What the heck is an ICO?](https://hackernoon.com/what-the-heck-is-an-ico-6f3736d5f5a)
        - Andrew Finn, (2018), [How Crypto Tokens will Enable the Disruption of Businesses like Uber and Airbnb](https://finnscave.com/2018/02/07/how-crypto-tokens-will-enable-the-disruption-of-businesses-like-uber-and-airbnb/)
    - Blockchain and WEB 3.0
        - Matteo Gianpietro Zago, (2018), [Why the Web 3.0 Matters and you should know about it](https://medium.com/@matteozago/why-the-web-3-0-matters-and-you-should-know-about-it-a5851d63c949)






