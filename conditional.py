#python condition if elif
while True:
    try:
        mark = int(input("Enter your mark "))
        if mark <= 80 and mark <= 100:
            print("A+")
        elif mark <= 70 and mark <= 79:
            print("A")
        elif mark <= 60 and mark <= 69:
            print("A-")
        elif mark <= 50 and mark <= 59:
            print("B")
        elif mark <= 40 and mark <= 49:
            print("C")
        elif mark <= 33 and mark <= 39:
            print("D")
        elif mark <0 or mark >100:
            print("invalid")
        else:
            print("F")
        pass
    except ValueError:
        print("Enter Only number 0 to 100")
    
