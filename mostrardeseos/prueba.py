from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    messages = [
        "Mensaje 1",
        "Mensaje 2",
        "Mensaje 3"
        # ... y así sucesivamente
    ]
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
