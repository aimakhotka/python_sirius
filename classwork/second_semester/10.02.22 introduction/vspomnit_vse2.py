def schet(slovar, znach):
    kolvo = 0

    for i in slovar.values():
        if i == znach:
            kolvo += 1
    return kolvo