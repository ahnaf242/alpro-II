from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  
        return redirect(url_for('dashboard', name=user))
    return render_template('login.html')  

# Halaman dashboard
@app.route('/dashboard/<name>')
def dashboard(name):
    return render_template('dashboard.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, port=5002)

