from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run_python_code', methods=['POST'])
def run_code():
    # Example Python code execution
    input_data = request.json.get('data')
    result = input_data * 2  # Example: multiplying the input data
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
