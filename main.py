def BMI_Score(BMI):
    if BMI < 18.5:
        print("Masz niedowagę")
    elif 18.5 <= BMI < 25:
        print("Jesteś w normie, tak trzymaj!")
    elif 25 <= BMI < 30:
        print("Masz nadwagę, czas wziąć się za siebie")
    else:
        print("Teraz to już musisz")

height = int(input("What is your height ? "))
weight = int(input("What is your weight ? "))

convert = (height / 100)

BMI = weight / (convert * convert)

message = BMI_Score(BMI)

print("Twoje BMI wynosi ", BMI, message)


