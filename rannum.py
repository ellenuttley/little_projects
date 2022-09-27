import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again! Too low.")
        elif guess > random_number:
            print ("Sorry, guess again. Answer too high!")
    
    print(f"Yayy! {random_number} is correct!")
        
<<<<<<< HEAD

guess(10)
 
=======
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        guess = random.rantint(low,high)
        


guess(10)
 
>>>>>>> 4ac2b38119bb01f33193372df5602a013473da94
