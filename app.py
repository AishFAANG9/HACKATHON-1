from flask import Flask,render_template, send_from_directory, request, jsonify

app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/basicsamplegen')
def basicsamplegen():
    return render_template('basicsamplegen.html')

@app.route('/volpay3x')
def volpay3x():
    return render_template('volpay3x.html')

@app.route('/volpay2x')
def volpay2x():
    return render_template('volpay2x.html')

@app.route('/advancesamplegen')
def advancesamplegen():
    return render_template('advancesamplegen.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)