# Runs on http://127.0.0.1:5000/

from flask import Flask, jsonify, request
import blockchain as bc

app = Flask(__name__)
blockchain = bc.Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    """Mines a block in the blockchain.

    :return: JSON string
        returns a successful HTTP request of
        the response in a JSON format
    """
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    previous_hash = blockchain.tohash(previous_block)

    proof = blockchain.proof_of_work(previous_proof)
    block = blockchain.create_block(proof, previous_hash)

    response = {'message': 'Block Mined!',
                'index': block['index'],
                'time_stamp': block['time_stamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'hash_operation': block['hash_operation'],
                'data': block['data']}

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

app.run(host='0.0.0.0', port=5000)
