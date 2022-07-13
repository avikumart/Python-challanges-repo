import random

class Guessthe_num:
    
    def findthenum(self, guess, num):
        while guess != num:
            guess = int(input("Enter your guessing number between 1 to 10: "))
            if guess == num:
                print("Congrats! you won!")
                break
            else:
                print("Try again one more time")
                

if __name__ == '__main__':
    a = input("Enter your number:")
    b = random.randint(1,6)
    
    number_guessing = Guessthe_num()
    number_guessing.findthenum(a,b)  
