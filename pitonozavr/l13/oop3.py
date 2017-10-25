class Jokers:
	def __init__(self, name, nose_color, bad_jokes, equipment):
		self.name = name
		self.nose_color = nose_color
		self.bad_jokes = bad_jokes
		self.equipment = equipment

	def joke(self):
		print(self.name + " почесал свой "+ self.nose_color + " нос и заорал: " + self.bad_jokes + ", достав из карманов " + self.equipment)

def funnies(person):
	person.joke()

suslo = Jokers("Сулеймэн", "сизый", " А ТВОЙ ПАПА НА СТЕКОЛЬНОМ ЗАВОДЕ РАБОТАЕТ?!АААХААА!!", 
	"сборник дедовских анекдотов про Хрущева")
amin = Jokers("Амин", "кривой", "Так бл*т!!! (Соре за м*т)", 
	"Пистолет, который выстреливает, и БЭНГ!")

funnies(suslo)
funnies(amin)

class Antijokers:
	def __init__(self, name, ring, nice_haircut):
		self.name = name
		self.ring = ring
		self.nice_haircut = nice_haircut

	def joke(self):
		print(self.name + " спросил 'Кто тебе подарил сборник анекдотов, а?Азаза. Кстати, у тебя ошибка в слове.\
У меня глаза кровью исходят!!' \nИ почесал " + self.ring +
" свою " + self.nice_haircut)

starii = Antijokers("Эльдарыч", "Обручальным перстнем", "роскошный горшок")

funnies(starii)