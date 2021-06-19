from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<test>/')
def homepage(test):
    #test = test.upper()
    f = open('goods.txt', 'r+', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', txt=txt)

app.run()