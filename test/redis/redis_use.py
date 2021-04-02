import json
import redis

# connection redis
rd = redis.StrictRedis(host='localhost', port=6379, db=0)

# # save key-value in Redis
# rd.set("kkk", "vvv")
# # get key in Redis
# print(rd.get("kkk"))
# # delete all
# rd.flushdb()


# json data
dataDict = {
    "key1": "test1",
    "key2": "test2",
    "key3": "test3"
}
# json dump
jsonDataDict = json.dumps(dataDict, ensure_ascii=False).encode("utf-8")

# json dump set
rd.set("dict", jsonDataDict)

# json get
resultData = rd.get("dict")
resultData = resultData.decode("utf-8")

# json load
result = dict(json.loads(resultData))
print(result)