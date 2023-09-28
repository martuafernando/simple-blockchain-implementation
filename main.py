from blockchain.blockchain import Blockchain

from flask import Flask, jsonify, request

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine_block', methods=['GET'])
def mine_block():
  prev_block = blockchain.get_latest_block()
  prev_proof = prev_block['proof']
  proof = blockchain.proof_of_work(prev_proof)
  prev_hash = prev_block['hash']
  block = blockchain.create_block(proof=proof, prev_hash=prev_hash)
  block['hash'] = blockchain.get_hash(block)
  
  response = {
    'message': 'block created successfully',
    'index': block['id_block'],
    'timestamp': block['timestamp'],
    'data': block['data'],
    'proof': block['proof'],
    'previous_hash': block['prev_hash'],
    'hash': block['hash']
  }
  
  return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
  
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.is_chain_valid()
    
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

@app.route('/block', methods=['POST'])
def post_block():
  content_type = request.headers.get('Content-Type')
  if (content_type != 'application/json'):
    return jsonify({
      "message": "Content-Type not supported!"
    }), 400
  
  data = request.json
  
  if not (('data' in data)):
    return jsonify({
    "message": "data is required"
  }), 200  
  
  
  prev_block = blockchain.get_latest_block()
  prev_proof = prev_block['proof']
  proof = blockchain.proof_of_work(prev_proof)
  prev_hash = prev_block['hash']
  block = blockchain.create_block(proof=proof, prev_hash=prev_hash, data=data['data'])
  block['hash'] = blockchain.get_hash(block)
  
  response = {
    'message': 'block created successfully',
    'index': block['id_block'],
    'timestamp': block['timestamp'],
    'data': str(data['data']),
    'proof': block['proof'],
    'previous_hash': block['prev_hash'],
    'hash': block['hash']
  }
  
  return jsonify(response), 200

@app.route('/block/<int:id>', methods=['PUT'])
def modify_block(id):
  content_type = request.headers.get('Content-Type')
  if (content_type != 'application/json'):
    return jsonify({
      "message": "Content-Type not supported!"
    }), 400

  data = request.json
  if not id:
    return jsonify({
      "message": "id and hash are required"
    }), 400
  
  
  if (id >= len(blockchain.chain)):
    return jsonify({
      "message": "block not found"
    }), 400
  
  if not (('hash' in data) or 'data' in data):
    return jsonify({
    "message": "must provide hash or data"
  }), 200  
  
  if 'hash' in data:
    blockchain.modify_block_hash(id, data['hash'])
  if 'data' in data:
    blockchain.modify_block_data(id, data['data'])
  
  return jsonify({
    "message": "block has modified successfully"
  }), 200

app.run(host='127.0.0.1', port=5000)