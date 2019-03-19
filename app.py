from flask import Flask 
from flask import redirect, render_template, request, url_for

import sqlite3

app = Flask(__name__)

DB_FILE_PATH = "data/atm.db"

@app.route("/", methods = ['POST'], ['GET'])
def index():
	if request.method == 'POST':
		account_no = request.form['account_no']
		PIN_no = request.form['PIN_no']

	return render_template('index.html')


def login(account_no, PIN_no):
	conn = sqlite3.conn(DB_FILE_PATH)
	cur = conn.cur()
	user = (account_no, PIN_no)
	query = "SELECT * FROM accounts WHERE account_no = ? and PIN_no = ?"
	cur.execute(query, user)
	# account = self.cur.fetchone()
	if cur.fetchone() != None:
		return render_template('account.html', account=cur.fetchone())

	return render_template(url_for('index'))


# Create a web interface for an ATM using Bootstrap
# We should be able to login with a account number and PIN
# We do not need to have a signup form, you can insert the data in the db manually
# When a user tries to log in, you need to check that their account number and PIN are correct based on the info you have in the db
# When the add / remove money from the account you need to take it off or add it to the balance