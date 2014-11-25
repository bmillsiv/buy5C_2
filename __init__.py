from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('landing.html')

@app.route('/login/')
def login_page():
	return render_template('login.html')

@app.route('/footer')
def footer_page():
	return render_template('footer.html')

#practicing git merge - It worked! Boo ya!

if __name__ == '__main__':
	app.run(debug=True)