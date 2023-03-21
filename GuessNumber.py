import random 

print("=========Number Guessing Game=========")
number = random.randrange(50,150)
count = 1 
def numberGenerator(deductionRange,guessedNumber):
    deductionNumber = random.randrange(0,deductionRange)
    if guessedNumber !=0 and guessedNumber == number:
        print("Correct!!! you have guessed right")
    else:
        if count !=3:
            print('Number is less than',(number+deductionNumber),' and greater than',(number-deductionNumber))
        return False
numberGenerator(50,0)
guess_One = int(input("First Guess : "))
if (numberGenerator(50,guess_One) == False):
    count=count+1
    guess_Two = int(input("Second Guess : "))
    if(numberGenerator(25,guess_Two) == False):
        count=count+1
        guess_three = int(input("Last Guess : "))
        if(numberGenerator(12,guess_three) == False):
            print("Sorry you lost all of your chances... Better Luck Next Time")

