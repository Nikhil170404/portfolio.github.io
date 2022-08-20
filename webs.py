from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    return render_template('index.html')

@app.route("/about")
def prashant():
    name = prashant
    return render_template('inner-page.html',name2=name)

@app.route("/bootstrap")
def portfolio():
    return render_template('portfolio-details.html')

if __name__=="__main__":
    app.run(debug=False,host='0,0,0,0' )


