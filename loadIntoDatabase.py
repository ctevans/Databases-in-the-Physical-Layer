from bsddb3 import db 
#Get an instance of BerkeleyDB 
database = db.DB() 
database.open("sc.idx", None, db.DB_BTREE, db.DB_CREATE)
database.close()
