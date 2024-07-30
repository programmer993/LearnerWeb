from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        dob = request.form['dob']
        captcha = request.form['captcha']

        if len(password) < 8:
            return render_template('signup_form.html', error="Password must be at least 8 characters long")

        if captcha.lower() != 'yes':
            return render_template('signup_form.html', error="Please confirm you are human by typing 'yes'")

        # Handle signup logic here, e.g., store the user data in the database
        session['user'] = email
        return redirect(url_for('resources'))
    return render_template('signup_form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        email = request.form['username']  # Assuming email as username
        session['user'] = email
        return redirect(url_for('resources'))
    return render_template('login_form.html')

@app.route('/resources')
def resources():
    if 'user' in session:
        return render_template('resources.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
