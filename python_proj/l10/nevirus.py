# Вирус переименовывает все файлы папки, в которой находится.

# Для этого сначала получаем список всех файлов 
#(os.listdir(path =".")). 

# Перебираем список, меняя названия файлов 
# (os.rename(начальное, конечное имя)).