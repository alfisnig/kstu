import math

def getRate(score: int, rateName: str):
    """На основе количественного значения даёт качественную оценку уровня опасности"""
    report = "Данные по {} оценке:\n\tКоличественная оценка: {}\n\tКачественная оценка: уровень опасности {}\n"

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
    return answer

def roundHalfUp(num, decimals=0):
    """
    Решает проблему с округлением в большую сторону (функция round работает не так, как нужно
    в этой ситуации)
    """
    multiplier = 10 ** decimals
    return math.floor(num * multiplier + 0.5) / multiplier

def calcBaseScore(C: int, I: int, A: int, AV: int, AC: int, PR: int, UI: int, S: int,
                  returnNum=False):
    """Вычисляет базовую оценку"""
    impactBase = 1 - ((1 - C) * (1 - I) * (1 - A))
    exploitability = 8.22 * AV * AC * PR * UI

    if S == 0:
        impact = 6.42 * impactBase
    elif S == 1:
        impact = 7.52 * (impactBase - 0.029) - 3.25 * ((impactBase - 0.02) ** 15)
    if S == 0:
        baseScore = roundHalfUp(min(impact + exploitability, 10), 1)
    elif S == 1:
        baseScore = roundHalfUp(min(1.08 * (impact + exploitability), 10), 1)

    if impact <= 0:
        baseScore = 0

    return getRate(baseScore, "базовой") if not returnNum else baseScore

def calcTempScore(C: int, I: int, A: int, AV: int, AC: int, PR: int, UI: int, S: int,
                  E: int, RL: int, RC: int):
    """Вычисляет временную оценку"""
    baseScore = calcBaseScore(C, I, A, AV, AC, PR, UI, S, returnNum=True)
    temporalScore = roundHalfUp(baseScore * E * RL * RC, 1)
    return getRate(temporalScore, "временной")

if __name__ == "__main__":
    # Оставляю этот закомментированный код на случай, если значения должны вводиться с консоли
    # C = float(input("Введите C: "))
    # I = float(input("Введите I: "))
    # A = float(input("Введите A: "))
    # AV = float(input("Введите AV: "))
    # AC = float(input("Введите AC: "))
    # PR = float(input("Введите PR: "))
    # UI = float(input("Введите UI: "))
    # S = float(input("Введите S: "))
    # E = float(input("Введите E: "))
    # RL = float(input("Введите RL: "))
    # RC = float(input("Введите RC: "))
    C = 0.56
    I = 0.56
    A = 0.56
    AV = 0.85
    AC = 0.77
    PR = 0.85
    UI = 0.62
    S = 1
    E = 0.94
    RL = 0.95
    RC = 1
    print(calcBaseScore(C, I, A, AV, AC, PR, UI, S))
    print(calcTempScore(C, I, A, AV, AC, PR, UI, S, E, RL, RC))
    input("\nВведите любой символ, чтобы закрыть консоль. ")
