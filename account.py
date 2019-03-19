import sqlite3


DB_FILE_PATH = "data/atm.db"

class Account():
	def __init__(self):
		self.conn = sqlite3.connect(DB_FILE_PATH)
		self.conn.row_factory = sqlite3.Row
		self.cursor = self.conn.cursor()

	def get_account(self, account_no, PIN_no):
		query = "SELECT * FROM accounts WHERE account_no = ? and PIN_no = ?"
		self.cur.execute(query, (account_no, PIN_no))
		account = self.cur.fetchone()
		return account

test_account = Account()
account_info = test_account.get_account(1111111, "TS5588")
print(account_info.value)