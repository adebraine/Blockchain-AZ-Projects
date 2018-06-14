import datetime
import hashlib
from flask import Flask, jsonify, request
import json
import requests
from uuid import uuid4
from urllib.parse import urlparse
import pprint as pp

class Blockchain:
    """A class representing the entire blockchain.

        chain : List
            A list containing all blocks in the blockchain.

        leading_zeros: int
            The number of leading zeros in the obtained hash
            needed to validate the proof.

        data: dictionary
            Data contained in the blockchain (ledger).

        hash_operation: str
            the POW hash

        create_block : Function
            The function that create blocks and starts with the genesis block.
    """
    def __init__(self):
        self.chain = []
        self.leading_zeros = 4
        self.transactions_per_block = 4
        self.miner_reward = 100
        self.transactions = []
        self.mempool = []
        self.UTOX = []
        self.hash_operation = '0'
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        """Creates a block in the blockchain and returns said block.

        :param proof: Function
            proof based on the proof of work (POW).
        :param previous_hash: str
            key element that links two blocks in a row in a blockchain.
        :return block: dictionary
            A dictionary that defines each block in the blockchain:
                index: int
                    index number of the block
                time_stamp: str
                    exact time when the block was mined
                proof: int
                    proof gotten by mining the block from
                    the proof of work (POW)
                previous_hash: str
                    key element that links two blocks in a row in a blockchain.
                hash_operation: str
                    the POW hash
                data: dictionary
                    data contained in the block
        """
        block = {'index': len(self.chain) + 1,
                 'time_stamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'hash_operation': self.hash_operation,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)

        return block

    def get_previous_block(self):
        """Gets the very last block in the blockchain.

        :return block: dictionary
            A dictionary that represents the previous
            block in the blockchain
        """
        return self.chain[-1]

    def encrypt_to_hash(self, to_be_encoded):
        """Creates a SHA256 hash from a string.

        :param to_be_encoded: str
            string to be encoded
        :return: str
            A SHA256 hash
        """
        return hashlib.sha256(to_be_encoded.encode()).hexdigest()

    def pow_function(self, proof, previous_proof):
        """The proof of work function passed through
        the cryptographic hash

        :param proof: int
            current calculated proof
        :param previous_proof: int
            proof of the previous block
        :return POW: str
            a string to be passed through the cryptographic hash
        """

        # TODO: Implement a better POW function.

        POW = proof**2 - previous_proof**2

        return str(POW)

    def proof_of_work(self, previous_proof):
        """Problem that miners need to solve to create a new valid
        block in the blockchain. A number that is hard to find
        but easy to verify.

        The problem currently implemented is to solve the
        cryptographic hash to obtain a specifc amount of leading zeros.

        :param previous_proof: int
            Proof from the previous block.
        :return proof: int
            Proof of the new block.
        """
        proof = 1
        while True:
            self.hash_operation = self.encrypt_to_hash(self.pow_function(
                proof, previous_proof))

            if self.hash_operation[:self.leading_zeros] ==\
                    '0'*self.leading_zeros:
                return proof
            else:
                proof += 1

    def block_to_str(self, block):
        """Creates a string out of a block.

        :param block: dic
            A block in the blockchain.
        :return: str
            A string of the selected block.
        """
        return json.dumps(block, sort_keys=True)

    def is_chain_valid(self, chain):
        """Checks if the chain is a valid chain
        based on the POW.

        :param chain: list
            The blockchain list containing all blocks.
        :return: bool
            A check of the validity of the blockchain.
        """
        for index, block in list(enumerate(chain))[1:]:
            previous_block = chain[index - 1]
            previous_proof = previous_block['proof']
            proof = block['proof']
            self.hash_operation = self.encrypt_to_hash(self.pow_function(
                proof, previous_proof))

            if block['previous_hash'] != self.encrypt_to_hash(
                    self.block_to_str(previous_block)) or\
                    self.hash_operation[:self.leading_zeros] !=\
                    '0'*self.leading_zeros:
                return False

        return True

    def commit_transaction(self, sender, receiver, amount, fee):
        """Adds a transaction to the mempool.

        :param sender: str
            Address of the sender
        :param receiver: str
            Address of the receiver
        :param amount: float
            amount traded
        :param amount: float
            fee added to the transaction
        """
        cost = 0
        enough_money = 0
        for index, transaction in enumerate(self.UTOX):
            enough_money += transaction['amount']

        if enough_money > amount + fee:
            for index, transaction in enumerate(self.UTOX):
                if cost >= amount + fee:
                    break
                cost += transaction['amount']
                self.UTOX.remove(transaction)

            if cost - amount - fee > 0:
                return_transaction = self.create_transaction(
                    sender, receiver, cost - amount - fee, fee)
                self.UTOX.append(return_transaction)
            elif cost - amount - fee >= 0:
                output_transaction = self.create_transaction(
                    sender, receiver, amount, fee)
                self.mempool.append(output_transaction)

            return True
        return False

    def create_transaction(self, sender, receiver, amount, fee):
        """Create a transaction

        :param sender: str
            Address of the sender
        :param receiver: str
            Address of the receiver
        :param amount: float
            amount traded
        :param amount: float
            fee added to the transaction
        :return: dictionary
            A transaction
        """
        return {"sender": sender,
                "receiver": receiver,
                "amount": amount,
                "fee": fee}

    def add_transactions_to_block(self):
        """Fills the block with transactions with the highest fee.

        :return: int
            index of the block that contains the transactions
        """
        if not self.mempool:
            return
        for n in range(self.transactions_per_block):
            max_fee = 0
            for index, transaction in enumerate(self.mempool):
                if transaction['fee'] > max_fee:
                    max_fee = transaction['fee']
                    max_fee_transaction = transaction

            print(max_fee_transaction)
            print(self.mempool)

            self.transactions.append(max_fee_transaction)
            self.mempool.remove(max_fee_transaction)

    def add_node(self, address):
        """Adds the node containing the address to the set of nodes

        :param address: str
            address of the node
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        """Checks if the chain on any node is longer than the current chain.
        if it is longer, then set the longest chain as the valid chain.

        :return bool:
            True if the Blockchain was replaced
        """
        longest_chain = None
        max_length = len(self.chain)

        for node in self.nodes:
            response = requests.get('http://{}/get_chain'.format(node))
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain

        if longest_chain:
            self.chain = longest_chain
            return True


if __name__ == "__main__":
    from webapp_DeBraineChain import *
    port_number = 5000
    main()
