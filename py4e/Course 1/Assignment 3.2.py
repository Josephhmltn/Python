score = input("Enter Score: ")
iscore = float(score)
if 1 >= iscore >= 0.9 :
    print("A")
elif 0.9 > iscore >= 0.8 :
    print("B")
elif 0.8 > iscore >= 0.7 :
    print("C")
elif 0.7 > iscore >= 0.6 :
    print("D")
elif iscore < 0.6 :
    print("F")
else :
    print("Please input number between 0.0 and 1.0")
    quit()