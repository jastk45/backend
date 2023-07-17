from pymongo import MongoClient

string_connection = "mongodb+srv://jaimeastudillo:D11UTgfBLHbKQUM4@cluster0.bk3fivh.mongodb.net/?retryWrites=true&w=majority"
db_client = MongoClient(string_connection)