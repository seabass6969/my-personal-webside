from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test/index.html')
@app.route('/test')
def test():
    return "test"

if __name__ == '__main__':
    app.run()
