from pymongo import MongoClient
uri = 'mongodb://admin:admin1@ds249873.mlab.com:49873/c4e-23-blog'

#1:Connect
client = MongoClient(uri)
#2:get default db
db = client.get_database()
#3:get collection
posts = db['post']
movies = db['movies']
#4:Creat data
new_post = {
    'title':'hôm nay trời nắng',
    'content':'tôi vẫn ở nhà code',
}
new_movies = {
    'title':'on',
    'content':'off'
}
#5:insert data
# posts.insert_one(new_post)
# movies.insert_one(new_post)

#5 : read data
post_list = posts.find()
#p = post_list[2]
for p in post_list:

    print(p['title'])
    print(p['content'])

#6:close
client.close()