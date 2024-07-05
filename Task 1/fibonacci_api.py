from flask import Flask, request, jsonify

app = Flask(__name__)

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

@app.route('/api/fibonacci', methods=['GET'])
def fibonacci():
    try:
        n = int(request.args.get('n'))
        if n <= 0:
            raise ValueError("Number must be positive")
        sequence = generate_fibonacci(n)
        return jsonify(sequence)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
