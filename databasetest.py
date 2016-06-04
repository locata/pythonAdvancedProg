
import sqlite3

def Main():
	
	try:

		con = sqlite3.connect('test.db')
		cur = con.cursor()
		cur.execute('CREATE TABLE Pets(Id INT, Name TEXT, Price INT)')
		cur.execute("INSERT INTO Pets VALUES(1, 'CAT', 400)")
		cur.execute("INSERT INTO Pets VALUES(2, 'Dog', 600)")

		con.commit()

		cur.execute("SELECT * FROM Pets")

		data = cur.fetchall()

		for row in data:
			print row 

	except sqlite3.Error, e:
		if con:
			con.rollback()
			print "There was a problem with the SQL"
	finally:
		if con:
			con.close()

if __name__ == '__main__':
	Main()

