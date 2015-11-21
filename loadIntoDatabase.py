from bsddb3 import db 
#Get an instance of BerkeleyDB 
database = db.DB() 
database.set_flags(db.DB_DUP)
database.open("sc.idx", None, db.DB_HASH, db.DB_CREATE)
cur = database.cursor()

cur.put(b'blue', "berry", db.DB_KEYFIRST)
cur.put(b'blue', "lemon",db.DB_KEYFIRST)
cur.first()

print(cur.count())
print(cur.next_dup())


database.close()
