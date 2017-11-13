import json

content = {}
content["log"] = "Aslan_lion"
content["pass"] = "12345"

f = open("database2.txt","w")

json.dumps(content, f)
f.close()
f = open("database2.txt","r")

jObj = json.loads(f)
print(jObj["log"])
f.close()