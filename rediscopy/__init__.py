# coding=utf-8

from redis import Redis

A = Redis(host='39.96.73.116', db=0)
B = Redis(host='r-2zejx4qwml5jc5lcob.redis.rds.aliyuncs.com', db=0, password='3tz9w8csXKc67Br7')


def copydb():
    for key in A.keys():
        # 转成字符串形式
        key = key
        key_type = A.type(key)
        print('*' * 30)
        print('A:', 'key=' + key, '---------type=' + key_type)
        # 对字符串类型的键值对执行操作------------------------------------------
        if key_type == 'string':
            print(A.get(key))
            B.set(key, str(A.get(key))[2:-1])
            print('写入到数据库B成功，{}'.format(B.get(key)))
        # 对哈希字典类型的键值对执行操作-----------------------------------------
        elif key_type == 'hash':
            print(A.hgetall(key))
            for son_key in A.hkeys(key):
                son_key = str(son_key)[2:-1]
                son_value = str(A.hget(key, son_key))[2:-1]
                B.hset(key, son_key, son_value)
            print('写入到数据库B成功，{}'.format(B.hgetall(key)))
            # 对列表类型的键值对执行操作---------------------------------------------
        elif key_type == 'list':
            print('A:', A.lrange(key, 0, A.llen(key)))
            for value in A.lrange(key, 0, A.llen(key)):
                v1 = str(value)[2:-1]
                B.rpush(key, v1)
            print('写入到数据库B成功，{}'.format(B.llen(key)))
            # 对集合类型的键值对执行操作---------------------------------------------
        elif key_type == 'set':
            print('A:', key, A.scard(key))
            for value in A.smembers(key):
                value = str(value)[2:-1]
                B.sadd(key, value)
            print('写入到数据库B成功，{}'.format(B.scard(key)))
        # 对有序集合类型的键值对执行操作------------------------------------------
        elif key_type == 'zset':
            print('A:', key, A.zcard(key))
            for value in A.zrangebyscore(key, 0, 100):
                value = str(value)[2:-1]
                score = A.zscore(key, value)
                print(value, score, '----')
                B.zadd(key, value, score)
            print('\n写入到数据库B成功，{}'.format(B.zcard(key)))


if __name__ == '__main__':
    copydb()
