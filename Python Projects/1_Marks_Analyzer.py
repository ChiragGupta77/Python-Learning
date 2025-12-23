# Subject marks analyzer
sub = input("Number of subjects:")
marks = []
r = ""
gd = ""
if sub.isnumeric():
    sub = int(sub)
    if sub > 0:
        for i in range(sub):
            mark = int(input(f"Marks in subject {i+1}:"))
            marks.append(mark)
        print(f"Total marks:{sum(marks)}")
        avg = sum(marks)/sub
        print(f"Average:{round(avg, 2)}")
        for j in marks:
            if j<33:
                r = "Fail"
                break
        if r != "Fail":
            r = "Pass"
        print(f"Result:{r}")
        if avg >= 90:
            gd = "A+"
        elif avg >= 75:
            gd = "A"
        elif avg >= 60:
            gd = "B"
        elif avg >= 45:
            gd = "C"
        elif avg >= 33:
            gd = "D"
        if r == "Fail":
            gd = "F"
        print(f"Grade:{gd}")
    else:
        print("Enter a valid integer please")
else:
    print("Enter an integer value")
