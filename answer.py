import math


CSI = '\x1b['
RESET = f'{CSI}0m'
ZERO = f'{CSI}0G'
ERASE = f'{CSI}2k'
RED = f'{CSI}48;5;9m'
WHITE = f'{CSI}48;5;15m'
GREEN = f'{CSI}48;5;10m'
ED = f'{WHITE} {RESET}'
END = f'{CSI}0m'

#Флаг Польши
for line in range(4):
    if line < 2:
        print(f'{WHITE}{" " * 18}{RESET}')
    else:
        print(f'{RED}{" "*18}{RESET}')

print('-'*70)

#Узор
LENGHT = 24
HIGHT = 5 #нечетное число
for line in range(HIGHT):
    if line%2==0:
        print(f'{WHITE}{" "*LENGHT}{RESET}')
    elif line%5==1:
        print((f'{" " * 8}{WHITE} {RESET} ')*(LENGHT//10))
    else:
        print((f'   {WHITE} {RESET}      ')*(LENGHT//10))

print('-'*70)

#График
WIDTH = 40
HEIGHT = 12
X_MAX = 16
Y_MAX = math.sqrt(X_MAX)

graph = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

y_axis = 2
x_axis = HEIGHT - 2
for r in range(HEIGHT):
    graph[r][y_axis] = "|"
for c in range(y_axis, WIDTH):
    graph[x_axis][c] = "-"


for i in range(WIDTH - y_axis - 1):
    x = (i / (WIDTH - y_axis - 2)) * X_MAX
    y = math.sqrt(x)
    row = int(round((1 - y / Y_MAX) * (x_axis - 1)))
    col = y_axis + 1 + i
    if 0 <= row < HEIGHT:
        graph[row][col] = ED

for row in graph:
    print("".join(row))

print('-'*70)

#Процентное соотношение данных
seq_file = open('sequence.txt')
file = [abs(float(i.strip())) for i in seq_file]
perv = []
vtor = []
for i in range(len(file)):
    if i < 125:
        perv.append(file[i])
    else:
        vtor.append(file[i])

srp = sum(perv) / len(perv)
srvt = sum(vtor) / len(vtor)

procperv = int((srp/(srp+srvt)) * 100)
procvt = 100 - procperv

print(f'Первые 125: {procperv}% {RED}{" " * (procperv//5)}{RESET}{"-" * (20-procperv//5)}|')
print(f'Вторые 125: {procvt}% {GREEN}{" " * (procvt//5)}{RESET}{"-" * (20-procvt//5)}|')

seq_file.close()