# coding=utf-8
from pymongo import MongoClient

conn = MongoClient('localhost', 27017, username="root", password="f2KrUTwjzEwmL4kjphf7x87b6fhxkN")
db = conn.test  # 连接mydb数据库，没有则自动创建
my_set = db.copygas  # 使用test_set集合，没有则自动创建

conns = MongoClient('39.96.73.116', 27017)
dbs = conns.gas  # 连接mydb数据库，没有则自动创建
my_sets = dbs.dingtalkgas  # 使用test_set集合，没有则自动创建

if __name__ == '__main__':
    lists = my_sets.find()
    print lists.count()
    for i in lists:
        my_set.insert(i)
