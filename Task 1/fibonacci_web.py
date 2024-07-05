from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sequence = []
    if request.method == 'POST':
        n = request.form.get('n')
        if n:
            try:
                response = requests.get(f'http://127.0.0.1:5000/api/fibonacci?n={n}')
                if response.status_code == 200:
                    sequence = response.json()
                else:
                    error = response.json().get('error', 'An error occurred')
                    return render_template('index.html', error=error)
            except Exception as e:
                return render_template('index.html', error=str(e))
    return render_template('index.html', sequence=sequence)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
