import random
from time import sleep
import time

print('загрузка кода...')
sleep(3)
symbols = ["0", "1", "1 ", "1"]
print("\033[32m")
start_time = time.time()
while time.time() - start_time < 15:
    line = "".join(random.choice(symbols) for _ in range(40))
    print(line)
    sleep(0.01)
print("\033[0m")
sleep(2)
print("загрузка завершина!")
sleep(2)

print('\033[31m')
print(f"{'-' * 58} \nприветствую это игра угадай число \n{'-' * 58}")
sleep(1.9)
print('правила игры просты')
sleep(1.9)
print('я загадал число а ты должен его угадать')
sleep(1.9)
print('всего чисел 973 😈')
sleep(1.9)
print('начнëм?')
sleep(1.9)
print('напиши "play" чтобы начать игру ')
sleep(1.9)
print('или')
sleep(1.9)
print('напиши "exit" чтобы закончить игру ')
sleep(1.9)
ты = input('начнëм? ')

if ты == 'play':
	print('загрузка...')
	sleep(0.5)
	print('загрузка...')
	sleep(0.5)
	print('загрузка...')
	sleep(0.5)
	print('готово!')	
elif ты == 'exit':
	sleep(3)
	print('до свидания')
	exit()
else:
	sleep(3)
	print('😡ну чо ты пишешь я попросил либо play либо exit')
	exit()

число = random.randint(1, 973)
ответ = 0
попытка = 0

while ответ != число:
    sleep(0.1)
    ответ = input('\nКакое число я загадал? ')
    sleep(0.1)
    if ответ == 'exit':
        sleep(0.1)
        print('\nНу ты чо сдался')
        break
    
    try:
        ответ = int(ответ)
    except:
        sleep(0.1)
        print('\nЭто не цифры 😜')
        sleep(0.1)
        continue
    
    попытка += 1
    
    if ответ > число:
        sleep(0.1)
        print(f"{'-'}\nПопытка №{попытка}. Я загадал число поменьше 🤛")
        sleep(0.1)
    elif ответ < число:
        sleep(0.1)
        print(f"{'+'} \nПопытка №{попытка}. Я загадал число побольше 💪")
        sleep(0.1)
    else:
        sleep(0.1)
        print(f"{'😎' * 58} \nМолодец Ты угадал с {попытка} попытки \n{'😎' * 58}")
sleep(0.1)
print(f"{'-' * 58} \nИгра окончена 👋 \n{'-' * 58}")
			
		