alphabet = "abcdefghijklmnopqrstuvwxyz"


firstWord = input("Введите первое слово: ")
secondWord = input("Введите второе слово: ")
thirdWord = input("Введите третье слово: ")

result = ""
result += alphabet[(alphabet.index(firstWord[-1]) + 1 % (len(alphabet) - 1))]
result += alphabet[(alphabet.index(secondWord[-1]) - 1 % (len(alphabet) - 1))]
if len(thirdWord) % 2 != 0:
    result += alphabet[(alphabet.index(thirdWord[1]) + 1 % (len(alphabet) - 1))]
else:
    symbol = thirdWord[(len(thirdWord) // 2)]
    result += alphabet[(alphabet.index(symbol) - 1 % (len(alphabet) - 1))]

index = len(firstWord) + len(secondWord)
if index > 26:
    index %= 26
result += alphabet[index - 1]
print(result)