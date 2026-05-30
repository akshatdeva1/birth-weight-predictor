from flask import   Flask, jsonify
app = Flask(__name__)

#CRUD Operations

@app.route('/create_user', methods=['POST'])
def create_user():
    return jsonify({"msg": "User created successfully"})



@app.route('/get_user', methods=['GET'])
def get_user():
    return jsonify({"msg": "User retrieved successfully"})



@app.route('/update_user', methods=['PUT'])
def update_user():
    return jsonify({"msg": "User updated successfully"})



@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    return jsonify({"msg": "User deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
