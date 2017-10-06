games = ["Копатель Онлайн", "Overwatch", "Civilization VI"]
print(games[0])
games[1] = "Копатель Онлайн 2"
print(games)
games.append("WatchDogs")
print(games)
games.insert(2,"Dota")
print(games)
amin_games = ["Sonic", "Mario", "Crash"]
#games.append(amin_games)
#print(games)
#print(games[-1][0])
games.extend(amin_games)
print(games)
games.remove('Crash')
print(games)
del games[5:]
print(games)
fraer = games.pop(4)
print(fraer)
print(games)

games2 = games[:]
print(games2)
del games[2]
print(games)
print(games2)
