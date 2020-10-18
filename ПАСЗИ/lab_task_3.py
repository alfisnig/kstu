"""Реализация мандатной модели. Количество субъектов: 5, количество объектов: 3"""


tags = ["ОВ", "СС", "С", "ДСП", "НС"]


class Tag:
    def __init__(self, tagValue):
        self.tagValue = tagValue

    def __lt__(self, other):
        return tags.index(self.tagValue) > tags.index(other.tagValue)

    def __gt__(self, other):
        return tags.index(self.tagValue) < tags.index(other.tagValue)

    def __le__(self, other):
        return tags.index(self.tagValue) >= tags.index(other.tagValue)

    def __ge__(self, other):
        return tags.index(self.tagValue) <= tags.index(other.tagValue)

    def __eq__(self, other):
        return tags.index(self.tagValue) == tags.index(other.tagValue)


class User:
    def __init__(self, name: str, tagValue: Tag):
        self.name = name
        self.tag = tagValue


class FileObject:
    def __init__(self, name: str, tagValue: Tag):
        self.name = name
        self.tag = tagValue

    def __str__(self):
        return self.name


object1 = FileObject("object1", Tag("ОВ"))
object2 = FileObject("object2", Tag("С"))
object3 = FileObject("object3", Tag("НС"))
objects = [object1, object2, object3]

valera = User("Валера", Tag("ОВ"))
dima = User("Дима", Tag("СС"))
alex = User("Алекс", Tag("С"))
maximus = User("Максимус", Tag("ДСП"))
jhon = User("Джон", Tag("НС"))
users = [valera, dima, alex, maximus, jhon]


while True:
    currentUser: User
    exitLogin = False
    while True:
        userName = input("User ")
        for user in users:
            if userName == user.name:
                currentUser = user
                exitLogin = True
        if exitLogin:
            break
        print("Пользователя с таким логином не существует.")
    availableObjects = [fileObject for fileObject in objects if fileObject.tag <= currentUser.tag]
    availableObjects = ", ".join([str(item) for item in availableObjects])
    print(f"Идентификация прошла успешно, добро пожаловать в систему.\nПеречень доступных объектов: {availableObjects}")
    while True:
        command = input("Жду ваших указаний > ")
        if command == "request":
            while True:
                fileNum = input("К какому объекту хотите осуществить доступ? ")
                if fileNum.isdigit() and int(fileNum) > 0 and int(fileNum) <= len(objects):
                    if objects[int(fileNum) - 1].tag <= currentUser.tag:
                        print("Операция прошла успешно")
                        break
                    else:
                        print("Отказ в выполнении операции. Недостаточно прав.")
                        break
        elif command == "read":
            while True:
                fileNum = input("Какой объект вы хотите прочитать? ")
                if fileNum.isdigit() and int(fileNum) > 0 and int(fileNum) <= len(objects):
                    if objects[int(fileNum) - 1].tag <= currentUser.tag:
                        print("Операция прошла успешно")
                        break
                    else:
                        print("Отказ в выполнении операции. Недостаточно прав.")
                        break
        elif command == "write":
            while True:
                fileNum = input("В какой объект вы хотите сделать запись? ")
                if fileNum.isdigit() and int(fileNum) > 0 and int(fileNum) <= len(objects):
                    if objects[int(fileNum) - 1].tag >= currentUser.tag:
                        print("Операция прошла успешно")
                        break
                    else:
                        print("Отказ в выполнении операции. Недостаточно прав.")
                        break
        elif command == "grant":
            if currentUser.tag.tagValue != "ОВ":
                print("У вас нед доступа к этой команде")
                continue
            while True:
                num = input("Чему вы хотите присвоить право? 1 - субъекту, 2 - объекту. ")
                if num.isdigit():
                    num = int(num)
                    if num == 1:
                        changedUser: User
                        currentTag: str
                        while True:
                            userNum = input("Какому пользователю вы хотите поменять право?\n" + "\n".join([f"{i} - {str(user.name)}" for i, user in enumerate(users, start=1)]) + "\n")
                            # print("\n".join([f"{i} - {str(user)}" for user in enumerate(users)])
                            if userNum.isdigit() and int(userNum) > 0 and int(userNum) <= len(users):
                                changedUser = users[int(userNum) - 1]
                                break
                        while True:
                            tagNum = input("Какое право вы хотите ему установить?\n" + "\n".join([f"{i} - {str(tag)}" for i, tag in enumerate(tags, start=1)]) + "\n")
                            # print("\n".join([f"{i} - {str(user)}" for user in enumerate(users)])
                            if tagNum.isdigit() and int(tagNum) > 0 and int(tagNum) <= len(tags):
                                currentTag = tags[int(tagNum) - 1]
                                break
                        changedUser.tag = Tag(currentTag)
                        print("Операция прошла успешно.")
                        break
                    elif num == 2:
                        changedObject: FileObject
                        currentTag: str
                        while True:
                            userNum = input("Какому объекту вы хотите поменять право?\n" + "\n".join([f"{i} - {str(user)}" for i, user in enumerate(objects, start=1)]) + "\n")
                            # print("\n".join([f"{i} - {str(user)}" for user in enumerate(users)])
                            if userNum.isdigit() and int(userNum) > 0 and int(userNum) <= len(objects):
                                changedObject = objects[int(userNum) - 1]
                                break
                        while True:
                            tagNum = input("Какое право вы хотите ему установить?\n" + "\n".join([f"{i} - {str(tag)}" for i, tag in enumerate(tags, start=1)]) + "\n")
                            # print("\n".join([f"{i} - {str(user)}" for user in enumerate(users)])
                            if tagNum.isdigit() and int(tagNum) > 0 and int(tagNum) <= len(tags):
                                currentTag = tags[int(tagNum) - 1]
                                break
                        changedObject.tag = Tag(currentTag)
                        print("Операция прошла успешно.")
                        break
        elif command == "quit":
            print(f"Работа пользователя {currentUser.name} завершена. До свидания!")
            break