import datetime
import hashlib
import json


class Blockchain:
    """A class representing the entire blockchain.

        chain : List
            A list containing all blocks in the blockchain.

        leading_zeros: int
            The number of leading zeros in the obtained hash
            needed to validate the proof.

        data: dictionary
            Data contained in the blockchain (ledger).

        create_block : Function
            The function that create blocks and starts with the genesis block.
    """
    def __init__(self):
        self.chain = []
        self.leading_zeros = 4
        self.data = {}
        self.create_block(proof=1, previous_hash='0')

    def create_data(self, key, value):
        """Adds information to the data contained in the blockchain.

        :param key: str
            Keyword defining the specific data included
        
        :param value: To be determined
            value corresponding to the keyword
        """
        self.data[key] = value

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
                data: dictionary
                    data contained in the block
        """
        block = {'index': len(self.chain) + 1,
                 'time_stamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'data': self.data}
        self.chain.append(block)

        return block

    def get_previous_block(self):
        """Gets the very last block in the blockchain.

        :return block: dictionary
            A dictionary that represents the previous
            block in the blockchain
        """
        return self.chain[-1]

    def _SHA256(self, to_be_encoded):
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
            hash_operation = self._SHA256(self.pow_function(
                proof, previous_proof))

            if hash_operation[:self.leading_zeros] == '0'*self.leading_zeros:
                return proof
            else:
                proof += 1

    def tohash(self, block):
        """First creates a string out of a block then
        Creates a hash of a block in the blockchain.

        :param block: dic
            A block in the blockchain.
        :return encoded_block: str
            A hash of the selected block.
        """
        return self._SHA256(json.dumps(block, sort_keys=True))

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
            hash_operation = self._SHA256(self.pow_function(
                proof, previous_proof))

            if block['previous_hash'] != self.tohash(previous_block) or\
                    hash_operation[:self.leading_zeros] !=\
                    '0'*self.leading_zeros:
                return False

        return True

    def mine_block(self):
        """Mines a block in the blockchain.

        :return: dictionary
            A dictionary containing the current block.
        """
        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        previous_hash = self.tohash(previous_block)

        proof = self.proof_of_work(previous_proof)
        block = self.create_block(proof, previous_hash)

        return {'message': 'Block Mined!',
                'index': block['index'],
                'time_stamp': block['time_stamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'data': block['data']}

    def get_chain(self):
        """Gets the whole blockchain.

        :return: dictionary
            A dictionary with the blockchain and its length.
        """
        return {'chain': self.chain,
                'length': len(self.chain)}
    
    def is_valid(self):
        """Checks the validity of the blockchain.

        :return: JSON string
            returns a successful HTTP request of
            the response in a JSON format
        """
        validity = self.is_chain_valid(self.chain)
        if validity:
            return {'message': 'The chain is valid!'}

        return {'message': 'The chain is NOT valid!'}


if __name__ == "__main__": 
    import pprint as pp
    bc = Blockchain()
    print("="*84)
    print("CREATING A BLOCKCHAIN!")
    print("="*84)
    print("\n")
    print("the Initial Blockchain with the genesis block is:\n")
    pp.pprint(bc.chain)
    print("\n")
    print("Mining one coin!")
    print("The second coin is:\n")
    block_2 = bc.mine_block()
    pp.pprint(block_2)
    print("\n")
    print("Displaying the current Chain!\n")
    pp.pprint(bc.chain)
    print("\n")
    print("Is the chain valid?\n")
    pp.pprint(bc.is_valid())
    print("\n")
    print("Modifying the proof of the last block.")
    print("pay attention to the proof value!")
    print("The chain now is:")
    print("\n")
    bc.chain[1]["proof"] = 1
    pp.pprint(bc.chain)
    print("\n")
    print("Is the chain valid?\n")
    pp.pprint(bc.is_valid())
    print("\n")
    print("="*84)
    print("END OF EXAMPLE!")
    print("="*84)
    



