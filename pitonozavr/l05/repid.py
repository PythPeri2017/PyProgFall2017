# text = "скажи-ка, дядя, ведь не даром "
# print(text)
# print(text[10:14])
# print(text[0])
# text = "облом"
# print(text)
text2=[1, 2, 3, 4, 5]
print(text2)
text2.append(6)
print(text2)
text2.insert(3,3.5)
print(text2)
del text2[4]
print(text2)
text2.remove(5)
print(text2)
print(text2[:2])
text = ["Фэнтези", "Боевики", "Триллеры"]
print(text+text2)
text2 += text
text2.extend(text)
print(text2)
