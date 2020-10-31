p = 991
n = 3
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def generatePolynomial(n: int, x: int):
    polynomialValue = 0
    for i, digit in enumerate(range(n, 0, -1), start=1):
        polynomialValue += i * (x ** digit)
    polynomialValue += n + 1
    polynomialValue %= p
    return polynomialValue


while True:
    choice = input("1 - Хочу зашировать текст\n2 - Хочу расшифровать текст\n")
    if choice == "1" or choice == "2":
        break

choice = int(choice)
if choice == 1:
    with open("plain_text.txt", encoding='utf-8') as f:
        mes = f.read().strip()

    plainMessage = []

    for symbol in mes:
        position = alphabet.find(symbol.lower())
        if position > -1:
            plainMessage.append(str(generatePolynomial(n, position + 1)))
        else:
            plainMessage.append(symbol)

    open("crypted_text.txt", "w", encoding='utf-8').write(" ".join(plainMessage))
elif choice == 2:
    with open("crypted_text.txt", encoding='utf-8') as f:
        mes = f.read().strip()

    decryptedMessage = ""
    for num in mes.split(" "):
        if not num.isdigit():
            decryptedMessage += num
            continue
        num = int(num)
        for letterPos in range(len(alphabet)):
            if num == generatePolynomial(n, letterPos + 1):
                decryptedMessage += alphabet[letterPos]

    with open("decrypted_text.txt", "w", encoding='utf-8') as f:
        f.write("".join(decryptedMessage))

