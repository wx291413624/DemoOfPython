# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import pymongo
from sshtunnel import SSHTunnelForwarder


class AliyunMongoDebug(object):
    def __init__(self):
        self._record = {}

    def get_aliyun_mongo_client(self, only_read=True):
        # 跳板机参数
        ecs_host = "39.96.73.116"
        ecs_user = "root"
        ecs_password = "Oooo0000"

        # 云mongo 配置
        aliyun_mongo_master_host = "<mongo 副本集 主服务器>"
        aliyun_mongo_slave_host = "<mongo 副本集 副本>"
        aliyun_mongo_database = "<mongo 数据库>"
        aliyun_mongo_account = "<mongo 账号>"
        aliyun_mongo_password = "<mongo 密码>"

        host = aliyun_mongo_slave_host if only_read else aliyun_mongo_master_host
        server = SSHTunnelForwarder(
            (ecs_host, 22),
            ssh_password=ecs_password,
            ssh_username=ecs_user,
            remote_bind_address=(host, 3717))

        server.start()

        client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
        mongo_database = client[aliyun_mongo_database]
        mongo_database.authenticate(aliyun_mongo_account, aliyun_mongo_password)

        self._record[client] = server

        return client

    def return_aliyun_mongo_client(self, client):
        if client in self._record:
            server = self._record.pop(client)
        else:
            server = None

        client.close()
        if server:
            server.close()


if __name__ == '__main__':
    mongo_debug_manager = AliyunMongoDebug()
    mongo_client = None
    try:
        mongo_client = mongo_debug_manager.get_aliyun_mongo_client(only_read=False)
        mongo_client["Test"]["ssh_test"].insert({"msg": "Hello World!"})
    finally:
        if mongo_client:
            mongo_debug_manager.return_aliyun_mongo_client(mongo_client)
