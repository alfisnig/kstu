import math
import random


alphabet = "0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
P = math.pow(10, -6)
V = 11  # паролей в минуту
T = 2   # недели
passwordsPerWeek = V * 60 * 24 * 7

S = (passwordsPerWeek * T) / P
A = len(alphabet)
L = 0


while math.pow(A, L) <= S:
    L += 1


password = ""
for _ in range(L):
    password += alphabet[random.randint(0, A-1)]
print(f"Ваш пароль:\n{password}")

input("Нажмите enter, чтобы закрыть консоль.")