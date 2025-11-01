from flask import Flask, url_for, render_template, redirect, request, jsonify
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

@app.route('/pendidikan')
def pendidikan():
    return render_template('pendidikan.html')

@app.route('/pengalaman')
def pengalaman():
    return render_template('pengalaman.html')

@app.route('/keterampilan')
def keterampilan():
    return render_template("keterampilan.html")
    
@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    fib = []
    ind = [0,1]
    a = 0
    b = 1
    banyak = None
    if request.method == 'POST':
        banyak = int(request.form['angka'])
        for i in range(banyak):
            if i == 0:
                fib.append(0)
            elif i == 1:
                fib.append(1)
            else:
                fib.append(fib[-1]+fib[-2])
        return redirect(url_for('hasil', name=fib))
    return render_template('fibonacci.html')

@app.route('/hasil/<name>')
def hasil(name):
    return render_template('hasil.html', name=name)

@app.route('/csv')
def change():
    data = []
    with open ("D:/SEM 3/Alpro 2/Data.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i in reader:
            data.append(i)
    return jsonify(data)

@app.route('/form', methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        email = request.form['email']
        return redirect(url_for('isi', nama=nama, nim=nim, email=email))
    return render_template('form.html')

@app.route('/isi/<nama>/<nim>/<email>')
def isi(nama, nim, email):
    return render_template('isi.html', nama=nama, nim=nim, email=email)     

if __name__ == '__main__':
    app.run(debug=True, port=5000)