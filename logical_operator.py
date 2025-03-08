#logical operator
#if,elif,else

#if
age = 20
city = "Pune"

if age > 18 and city == "Pune":
    print("Eligible for voting in Pune")

#elif
age = 16
city = "Mumbai"

if age > 18 and city == "Pune":
    print("Eligible for voting in Pune")
elif age > 18 or city == "Mumbai":
    print("Eligible for voting in Mumbai")
else:
    print("Not eligible for voting")


#else
is_raining = False

if not is_raining:
    print("Let's go outside!")
else:
    print("Stay indoors.")


#nested-if-else
x = 10
y = 5

if x > y:
    if x % 2 == 0:
        print("x is greater and even")
    else:
        print("x is greater and odd")
else:
    print("x is not greater")


#and,or,not
marks = 85
attendance = 90
assignment = False

if marks >= 80 and attendance >= 75 and not assignment:
    print("Eligible for final exam")
elif marks >= 80 or attendance >= 75:
    print("Conditionally eligible for final exam")
else:
    print("Not eligible for final exam")
