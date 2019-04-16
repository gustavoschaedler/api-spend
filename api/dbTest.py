from tinydb import TinyDB, Query

database = "../db/SpendDB.json"

db = TinyDB(database)

db.insert(
    {
        'type': 'apple',
        'count': 7
    }
)

allData = db.all()

print(allData)
