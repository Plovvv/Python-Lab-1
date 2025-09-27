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
    if line<2:
        print(f'{WHITE}{" "*18}{RESET}')
    else:
        print(f'{RED}{" "*18}{RESET}')

print('-'*70)

#Узор
length = 24
hight = 5 #нечетное число
for line in range(hight):
    if line%2==0:
        print(f'{WHITE}{" "*length}{RESET}')
    elif line%5==1:
        print((f'{" "*8}{WHITE} {RESET} ')*(length//10))
    else:
        print((f'   {WHITE} {RESET}      ')*(length//10))

print('-'*70)

#График
import math
width = 40
height = 12
x_max = 16
y_max = math.sqrt(x_max)

graph = [[" " for _ in range(width)] for _ in range(height)]

y_axis = 2
x_axis = height - 2
for r in range(height):
    graph[r][y_axis] = "|"
for c in range(y_axis, width):
    graph[x_axis][c] = "-"


for i in range(width - y_axis - 1):
    x = (i / (width - y_axis - 2)) * x_max
    y = math.sqrt(x)
    row = int(round((1 - y / y_max) * (x_axis - 1)))
    col = y_axis + 1 + i
    if 0 <= row < height:
        graph[row][col] = ED

for row in graph:
    print("".join(row))

print('-'*70)

#Процентное соотношение данных
file = [abs(float(i.strip())) for i in open('sequence.txt')]
perv = []
vtor = []
for i in range(len(file)):
    if i<125:
        perv.append(file[i])
    else:
        vtor.append(file[i])

srp = sum(perv)/len(perv)
srvt = sum(vtor)/len(vtor)

procperv = int((srp/(srp+srvt))*100)
procvt = 100-procperv

print(f'Первые 125: {procperv}% {RED}{" "*(procperv//5)}{RESET}{"-"*(20-procperv//5)}|')
print(f'Вторые 125: {procvt}% {GREEN}{" "*(procvt//5)}{RESET}{"-"*(20-procvt//5)}|')