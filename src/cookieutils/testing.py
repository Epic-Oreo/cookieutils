from discord import DefaultAvatar
import database


db = database.db()


db["test"] = 100

print(db["test"])

print(db)