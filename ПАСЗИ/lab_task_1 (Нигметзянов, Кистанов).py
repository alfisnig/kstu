import math


def getS():
    sValues = {
        "влияние на другие компоненты системы (S)": {
            "U": 0,
            "C": 1
        },
    }

    return  sValues


def getMS():
    msValues = {
        "Скорректированное влияние на другие компоненты системы (MS)": {
            "X": 0,
            "U": 0,
            "C": 1
        }
    }
    return  msValues


def getValueFromUser(data: dict):
    result = []
    for key, value in data.items():
        while True:
            options = ", ".join(value.keys())
            userValue = input('Введите значение для "{}" (возможные варианты: {}): '.format(key, options))
            if userValue in value:
                result.append(value[userValue])
                break
    return result


def getBaseVectorValues(S: int) -> dict:
    baseVectorValues = {
        "вектор атаки (AV)": {
            "N": 0.85,
            "A": 0.62,
            "L": 0.55,
            "P": 0.2
        },
        "сложность атаки (AC)": {
            "L": 0.77,
            "H": 0.44
        },
        "уровень привилегий (PR)": {
            "N": 0.85,
            "L": 0.68 if S == 1 else 0.62,
            "H": 0.50 if S == 1 else 0.27
        },
        "взаимодействие с пользователем (UI)": {
            "N": 0.85,
            "R": 0.62
        },
        "влияние на конфиденциальность (C)": {
            "N": 0.0,
            "L": 0.22,
            "H": 0.56
        },
        "влияние на целостность (I)": {
            "N": 0.0,
            "L": 0.22,
            "H": 0.56
        },
        "влияние на доступность (A)": {
            "N": 0.0,
            "L": 0.22,
            "H": 0.56
        },
    }
    return baseVectorValues


def getEnvVectorValues(MS: float) -> dict:
    envVectorValues = {
        "скорректированный вектор атаки (MAV)":
            {
                "X": 0.85,
                "N": 0.85,
                "A": 0.62,
                "L": 0.55,
                "P": 0.2
            },
        "скорректированная сложность атаки (MAC)":
            {
                "X": 0.77,
                "L": 0.77,
                "H": 0.44
            },
        "скорректированный уровень привилегий (MPR)": {
            "X": 0.85,
            "N": 0.85,
            "L": 0.68 if MS == 1 else 0.62,
            "H": 0.50 if MS == 1 else 0.27
        },
        "скорректированное взаимодействие с пользователем (MUI)": {
            "X": 0.62,
            "N": 0.85,
            "R": 0.62
        },
        "скорректированное влияние на конфиденциальность (MС)": {
            "X": 0.0,
            "N": 0.0,
            "L": 0.22,
            "H": 0.56
        },
        "скорректированное влияние на целостность (MI)": {
            "X": 0.0,
            "N": 0.0,
            "L": 0.22,
            "H": 0.56
        },
        "скорректированное влияние на доступность (MA)": {
            "X": 0.0,
            "N": 0.0,
            "L": 0.22,
            "H": 0.56
        },
        "требования к конфиденциальности (CR)": {
            "X": 1.0,
            "H": 1.5,
            "M": 1.0,
            "L": 0.5
        },
        "требования к целостности (IR)": {
            "X": 1.0,
            "H": 1.5,
            "M": 1.0,
            "L": 0.5
        },
        "требования к доступности (AR)": {
            "X": 1.0,
            "H": 1.5,
            "M": 1.0,
            "L": 0.5
        }
    }
    return envVectorValues


def getTempVectorValues() -> dict:
    tempVectorValues = {
        "Доступность средств эксплуатации (E)": {
            "X": 1.0,
            "U": 0.91,
            "P": 0.94,
            "F": 0.97,
            "H": 1.0
        },
        "Уровень исправления (RL)": {
            "X": 1.0,
            "O": 0.95,
            "T": 0.96,
            "W": 0.97,
            "U": 1.0
        },
        "Степень достоверности источника (RC)": {
            "X": 1.0,
            "U": 0.92,
            "R": 0.96,
            "C": 1.0
        }
    }
    return tempVectorValues


def getRate(score: float, rateName: str) -> str:
    """На основе количественного значения даёт качественную оценку уровня опасности"""
    report = "\nДанные по {} оценке:\n\tКоличественная оценка: {}\n\tКачественная оценка: уровень опасности {}\n"

    if 0.1 <= score <= 3.9:
        answer = report.format(rateName, score, "низкий")
    elif 4 <= score <= 6.9:
        answer = report.format(rateName, score, "средний")
    elif 7.0 <= score <= 8.9:
        answer = report.format(rateName, score, "высокий")
    elif 9.0 <= score:
        answer = report.format(rateName, score, "критический")
    else:
        answer = report.format(rateName, score, "информационный (опасность отсутствует)")
    return "=" * 50 + answer + "=" * 50


def roundHalfUp(num, decimals=0) -> float:
    """
    Решает проблему с округлением в большую сторону (функция round работает не так, как нужно
    в этой ситуации)
    """
    multiplier = 10 ** decimals
    return math.floor(num * multiplier + 0.5) / multiplier


def getBaseScore(C: float, I: float, A: float, AV: float, AC: float, PR: float, UI: float, S: float,
                  returnNum=False):
    """Вычисляет базовую оценку"""
    impactBase = 1 - ((1 - C) * (1 - I) * (1 - A))
    exploitability = 8.22 * AV * AC * PR * UI

    if S == 0:
        impact = 6.42 * impactBase
        baseScore = roundHalfUp(min(impact + exploitability, 10), 1)
    elif S == 1:
        impact = 7.52 * (impactBase - 0.029) - 3.25 * ((impactBase - 0.02) ** 15)
        baseScore = roundHalfUp(min(1.08 * (impact + exploitability), 10), 1)
    if impact <= 0:
        baseScore = 0

    return getRate(baseScore, "базовой") if not returnNum else baseScore


def getTempScore(baseScore: float, E: float, RL: float, RC: float, returnNum=False) -> str:
    """Вычисляет временную оценку"""
    temporalScore = roundHalfUp(baseScore * E * RL * RC, 1)
    return getRate(temporalScore, "временной") if not returnNum else temporalScore


def getEnvScore(MAV: float, MAC: float, MPR: float, MUI: float, MS: int, MC: float,
                MI: float, MA: float, CR: float, IR: float, AR: float, E: float, RL: float, RC: float, returnNum=False):
    mImpactBase = min(1 - ((1 - (MC * CR)) * (1 - (MI * IR)) * (1 - (MA * AR))), 0.915)
    mExploitability = 8.22 * MAV * MAC * MPR * MUI
    if MS == 1:
        mImpact = (7.52 * (mImpactBase - 0.029)) - (3.25 * ((mImpactBase - 0.02)**15))
        environmentalScore = roundHalfUp(roundHalfUp(min(1.08 * (mImpact + mExploitability), 10), 1) * E * RL * RC, 1)
    elif MS == 0:
        mImpact = 6.42 * mImpactBase
        environmentalScore = roundHalfUp(roundHalfUp(min((mImpact + mExploitability), 10), 1) * E * RL * RC, 1)
    if mImpact <= 0:
        environmentalScore = 0

    return getRate(environmentalScore, "контекстной") if not returnNum else environmentalScore


def calculateBaseScore(returnNum=False):
    sValues = getS()
    S = getValueFromUser(sValues)[0]
    baseScoreValues = getBaseVectorValues(S)
    AV, AC, PR, UI, C, I, A = getValueFromUser(baseScoreValues)
    baseScore = getBaseScore(C, I, A, AV, AC, PR, UI, S, returnNum=returnNum)
    return baseScore


def calculateTempScore() -> str:
    baseScore = calculateBaseScore(returnNum=True)
    tempScoreValues = getTempVectorValues()
    E, RL, RC = getValueFromUser(tempScoreValues)
    tempScore = getTempScore(baseScore, E, RL, RC)
    return tempScore


def calculateEnvScore() -> str:
    msValues = getMS()
    MS = getValueFromUser(msValues)[0]
    envScoreValues = getEnvVectorValues(MS)
    MAV, MAC, MPR, MUI, MC, MI, MA, CR, IR, AR = getValueFromUser(envScoreValues)
    tempScoreValues = getTempVectorValues()
    E, RL, RC = getValueFromUser(tempScoreValues)
    envScore = getEnvScore(MAV, MAC, MPR, MUI, MS, MC, MI, MA, CR, IR, AR, E, RL, RC)
    return envScore


def start():
    while True:
        userChoice = input("Выберите что вы хотите сделать:\n\t1 - Вычислить базовую оценку"
                           "\n\t2 - Вычислить временную оценку\n\t3 - Вычислить контекстную оценку"
                           "\n\t4 - Закрыть консоль\n")
        if userChoice == "1":
            print(calculateBaseScore())
        elif userChoice == "2":
            print(calculateTempScore())
        elif userChoice == "3":
            print(calculateEnvScore())
        elif userChoice == "4":
            break
        else:
            print("Пункта с таким номером не существует!")


if __name__ == "__main__":
    start()