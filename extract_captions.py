import pickle
import DBSetup
import sqlite3

def extract_captions():
	dbmgr = DBSetup.DatabaseManager("NN.db")
	select_stmt = 'select mid, caption from crowd_raw_captions;'
	rows = (dbmgr.query(select_stmt)).fetchall()
	captions = {}
	for row in rows:
		captions[row[0]] += row[1]
	pickle.dump(captions, open( "captions.p", "wb" ))
	dbmgr.closedDb()

extract_captions()
