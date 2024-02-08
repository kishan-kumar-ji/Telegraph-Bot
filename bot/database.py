from pymongo import MongoClient
from . import DATABASE_URL, DATABASE_NAME, LOGGER

try:
    myclient = MongoClient(DATABASE_URL)
    mydb = myclient[DATABASE_NAME]
    col = mydb["Telegraph Bot"]
    LOGGER.info("Successfully established database connection.")
except:
    LOGGER.warn("Coudn't establish database connection.")

def new_user(id, name):
    return dict(
        _id=id,
        name=name
    )


async def is_user_exist(id):
    query = col.find_one({"_id":id})
    return bool(query)


async def add_user(id, name):
    isuser = await is_user_exist(id)
    if isuser:
        filter_query = {"_id": id}
        update_query = {"$set": {"name": name}}
        col.update_one(filter_query, update_query)
    else:
        user = new_user(id, name)
        col.insert_one(user)