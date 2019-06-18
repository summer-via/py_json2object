import json
jsonstr = r'{"a":1,"b":"2","c":{"d":"2"}}'
class JsonObject:
    __type__ = 'json'
def json2class(jsonstr:str)->JsonObject:
    dic = json.loads(jsonstr)
    res  = JsonObject()
    for k in dic:
        print(type(dic[k]))
        if type(dic[k]) is dict:
            setattr(res,k,json2class(json.dumps(dic[k])))
        else:
            setattr(res,k,dic[k])
    return res
jc = json2class(jsonstr)
print(jc.a)
print(jc.b)
print(jc.c.d)
