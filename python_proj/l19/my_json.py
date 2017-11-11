import json

class pObj(object):
	pass

myJson = pObj()
myJson.content = {}
myJson.content["log"] = "Aslan_lion"
myJson.content["pass"] = "12345"

f = open("database2.txt","a")

json.dump(myJson.content, f)
f.close()
f = open("database2.txt","r")
jObj = json.load(f)
print(jObj["log"])
f.close()