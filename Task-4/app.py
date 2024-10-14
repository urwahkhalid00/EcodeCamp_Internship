from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
CONTACT_FILE = 'contacts.csv'

def read_contacts():
    if not os.path.exists(CONTACT_FILE):
        return []
    with open(CONTACT_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return list(reader)

def write_contacts(contacts):
    with open(CONTACT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone Number', 'Email'])  # Header
        writer.writerows(contacts)

@app.route('/')
def index():
    contacts = read_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    with open(CONTACT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    return redirect(url_for('index'))

@app.route('/delete/<name>')
def delete_contact(name):
    contacts = read_contacts()
    contacts = [c for c in contacts if c[0] != name]
    write_contacts(contacts)
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_contact_route():
    old_name = request.form['old_name']
    new_name = request.form['name']
    new_phone = request.form['phone']
    new_email = request.form['email']

    contacts = read_contacts()
    contacts = [
        [new_name, new_phone, new_email] if c[0] == old_name else c
        for c in contacts
    ]
    write_contacts(contacts)
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
