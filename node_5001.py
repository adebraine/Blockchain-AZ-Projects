# Runs on http://127.0.0.1:5000/

from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse
import DeBraineChain as DB


def main():
    app = Flask(__name__)
    blockchain = DB.Blockchain()
    node_address = str(uuid4()).replace('-', '')

    @app.route('/mine_block', methods=['GET'])
    def mine_block():
        """Mines a block in the blockchain.

        :return: JSON string
            returns a successful HTTP request of
            the response in a JSON format
        """
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block['proof']
        previous_hash = blockchain.encrypt_to_hash(
                blockchain.block_to_str(previous_block))
        fee_reward = 0
        blockchain.add_transactions_to_block()
        for transaction in blockchain.transactions:
            fee_reward += transaction['fee']
        miner_reward = fee_reward + blockchain.miner_reward
        blockchain.UTOX.append(blockchain.create_transaction(
            sender=node_address,
            receiver='Miner_{}'.format(port_number),
            amount=miner_reward,
            fee=0))

        proof = blockchain.proof_of_work(previous_proof)
        block = blockchain.create_block(proof, previous_hash)

        response = {'message': 'Block Mined!',
                    'index': block['index'],
                    'time_stamp': block['time_stamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash'],
                    'hash_operation': block['hash_operation'],
                    'transactions': block['transactions'],
                    'Miner_UTOX': blockchain.UTOX}

        return jsonify(response), 200

    @app.route('/get_chain', methods=['GET'])
    def get_chain():
        """Gets the whole blockchain.

        :return: JSON string
            returns a successful HTTP request of
            the response in a JSON format
        """
        response = {'chain': blockchain.chain,
                    'length': len(blockchain.chain)}

        return jsonify(response), 200

    @app.route('/is_valid', methods=['GET'])
    def is_valid():
        """Checks the validity of the blockchain.

        :return: JSON string
            returns a successful HTTP request of
            the response in a JSON format
        """
        validity = blockchain.is_chain_valid(blockchain.chain)
        if validity:
            return jsonify({'message': 'The chain is valid!'}), 200

        return jsonify({'message': 'The chain is NOT valid!'}), 200

    @app.route('/add_transaction', methods=['POST'])
    def add_transaction():
        """Adds a transaction to the Mempool

        :return: JSON string
            returns a successful HTTP request of
            the response in a JSON format
        """
        json = request.get_json()
        transaction_keys = ['sender', 'receiver', 'amount', 'fee']
        if not all(key in json for key in transaction_keys):
            return jsonify({'message': 'Some elements of the\
                transaction are missing'}), 400
        if json['amount'] <= json['fee']:
            return jsonify({'message': 'fee cannot be higher\
                than the amount'}), 400
        is_transaction = blockchain.commit_transaction(
            json['sender'],
            json['receiver'],
            json['amount'],
            json['fee'])
        
        money = 0
        for index, transaction in enumerate(blockchain.UTOX):
            money += transaction['amount']

        if is_transaction:
            response = {'message': 'This transaction will be added to the Mempool',
                        'wallet': blockchain.UTOX,
                        'balance': money}
        else:
            response = {'message': 'Not Enough Money',
                        'wallet': blockchain.UTOX,
                        'balance': money}
        return jsonify(response), 201

    @app.route('/connect_node', methods=['POST'])
    def connect_node():
        """Connects nodes to the network

        :return: JSON string
                returns a successful HTTP request of
                the response in a JSON format
        """
        json = request.get_json()
        nodes = json.get("nodes")
        if nodes is None:
            return jsonify({'message': 'No node'}), 400
        for node in nodes:
            blockchain.add_node(node)
        response = {'message': 'All the following nodes are now connected:',
                    'total_nodes': list(blockchain.nodes)}
        return jsonify(response), 201

    @app.route('/replace_chain', methods=['GET'])
    def replace_chain():
        """Checks for the longest blockchain.

        :return: JSON string
            returns a successful HTTP request of
            the response in a JSON format
        """
        is_chain_replaced = blockchain.replace_chain()
        if is_chain_replaced:
            return jsonify({'message': 'Chain replaced by the longest one!',
                            'new_chain': blockchain.chain}), 200

        return jsonify({'message': 'Current chain is the largest one!',
                        'Chain': blockchain.chain}), 200

    app.run(host='0.0.0.0', port=port_number)


if __name__ == "__main__":
    port_number = 5001
    main()
