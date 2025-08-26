from flask import Flask, render_template, request, redirect, url_for, session
import os
import config

app = Flask(__name__)
app.secret_key = 'drmnef_secret_key'

@app.before_request
def require_login():
    allowed_routes = ['login', 'static']
    if request.endpoint not in allowed_routes and not session.get('logged_in'):
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == config.USERNAME and request.form['password'] == config.PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='اسم المستخدم أو كلمة المرور غير صحيحة')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/people')
def people():
    return render_template('people.html')

@app.route('/domain')
def domain():
    return render_template('domain.html')

@app.route('/social', methods=['GET', 'POST'])
def social():
    return render_template('social.html')

@app.route('/ip')
def ip():
    return render_template('ip.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/url')
def url():
    return render_template('url.html')

if __name__ == '__main__':
    app.run(debug=True)