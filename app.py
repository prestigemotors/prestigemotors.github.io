from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Replace this with your actual data retrieval logic
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
