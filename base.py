from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def select():
    return render_template('select.html')

@app.route('/one_pages')
def write():
    return render_template('one_pages.html')

@app.route('/two_pages')
def search():
    return render_template('two_pages.html')

if __name__ == '__main__':
    app.run(debug=True)