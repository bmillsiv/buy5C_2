from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('landing.html')

@app.route('/login/')
def login_page():
	return render_template('login.html')

@app.route('/browse')
def browse_page():
	return render_template('browse.html')

@app.route('/feedback')
def feedback_page():
	return render_template('feedback.html')

@app.route('/signup')
def signup_page():
	return render_template('signup.html')

@app.route('/sell')
def sell_page():
	return render_template('sell.html')

@app.route('/test')
def test_page():
	return render_template('test.html')

if __name__ == '__main__':
	app.run(debug=True)