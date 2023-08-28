data = input().split('/')
data = [int(data[0]), int(data[1])]

if (data[0] >= 21 and data[1] == 3) or (data[0] <= 20 and data[1] == 4):
    print("aries")
elif (data[0] >= 23 and data[1] == 9) or (data[0] <= 22 and data[1] == 10):
    print("libra")
elif (data[0] >= 21 and data[1] == 4) or (data[0] <= 20 and data[1] == 5):
    print("touro")
elif (data[0] >= 23 and data[1] == 10) or (data[0] <= 21 and data[1] == 11):
    print("escorpiao")
elif (data[0] >= 21 and data[1] == 5) or (data[0] <= 20 and data[1] == 6):
    print("gemeos")
elif (data[0] >= 22 and data[1] == 11) or (data[0] <= 21 and data[1] == 12):
    print("sagitario")
elif (data[0] >= 21 and data[1] == 6) or (data[0] <= 22 and data[1] == 7):
    print("câncer")
elif (data[0] >= 22 and data[1] == 12) or (data[0] <= 19 and data[1] == 1):
    print("capricornio")
elif (data[0] >= 23 and data[1] == 7) or (data[0] <= 22 and data[1] == 8):
    print("leao")
elif (data[0] >= 20 and data[1] == 1) or (data[0] <= 18 and data[1] == 2):
    print("aquario")
elif (data[0] >= 23 and data[1] == 8) or (data[0] <= 22 and data[1] == 9):
    print("virgem")
elif (data[0] >= 19 and data[1] == 2) or (data[0] <= 20 and data[1] == 3):
    print("peixes")