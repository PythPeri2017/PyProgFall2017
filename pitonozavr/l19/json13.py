import json

f = open("database.txt","r+")
my_orda = f.read()
jObj = json.loads(my_orda)
print(jObj['Price'])
new_ord = {}
new_ord["Login"] = "Sabir"
new_ord["Address"] = "Canning Town"
new_ord["Phone number"] = "458"
new_ord["Product"] = "GorGorod"
new_ord["Price"] = "priceless"
pObj = json.dumps(new_ord)
f.write(pObj)
f.close()