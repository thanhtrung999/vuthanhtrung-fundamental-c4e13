from pymongo import MongoClient
uri ='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
#Connect
client = MongoClient(uri)
#get default db
db = client.get_database()
#3:get collection
posts = db['post']
customers = db['cutomers']
#4:Creat data
new_posts = {
    "title": "Thành Trung",
    "author": "cảm nhận",
    "content": "Chọn teckid để học là một điều đúng đắn nhé!",
}
#5:insert data
posts.insert_one(new_post)
#6 close
client.close()