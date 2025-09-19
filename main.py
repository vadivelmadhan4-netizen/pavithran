from flask import Flask, render_template, request, redirect, url_for, session, flash
from users import User
from votes import VotingSystem

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.add_user(username, password):
            flash('Registration successful. Please login.')
            return redirect(url_for('login'))
        else:
            flash('Username already exists.')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            session['username'] = username
            flash('Login successful.')
            return redirect(url_for('vote'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if 'username' not in session:
        flash('Please login to vote.')
        return redirect(url_for('login'))
    user = User.users_db.get(session['username'])
    if request.method == 'POST':
        choice = request.form['party']
        success, message = VotingSystem.vote(user, choice)
        flash(message)
        if success:
            return redirect(url_for('results'))
    return render_template('vote.html', parties=VotingSystem.parties, user=user)

@app.route('/results')
def results():
    results = VotingSystem.get_results()
    return render_template('results.html', results=results)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
