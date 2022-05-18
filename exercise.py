# pay computation
hours = int(input("Enter hours:"))
rate = float(input("Enter rate:"))
try:
    hours = int(hours)
    rate = float(rate)
    if hours >= 40:
        pay = (hours * rate) + 20
        print(pay)
    else:
        pay = hours * rate
        print(pay)
except:
        print("Please enter numeric input:")


# Score grade
score = float(input("Enter score:"))
p = "perfect score"
f = "Fail"
if score >= 0.9:
    print("A", p)
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F", f)
else:
    print("Out of Range")



