posNumber = int(input("Enter a positive number: "))

def run(poseNumber):
    if poseNumber > 0: 
        for num in range(0, poseNumber):
            if(num % 2 == 0):
                print(num)
        if poseNumber % 2 == 0:
            print(poseNumber)
    else: 
        posNumber = int(input("Please enter a positive number: "))
        run(posNumber)
run(posNumber)