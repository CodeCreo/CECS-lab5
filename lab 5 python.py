#Alex Hwang
#018306793

#First create all of the defs
def get_magnitude(x):
    earthquake_num = x
    number = -1
    #Set number = -1 first to begin the while loop
    while(number<=0):
        number = float(input("Please enter the magnitude of earthquake {0}:".format(earthquake_num)))
    return number

def compare_magnitude(x, y):
    f = 10 ** (1.5 * (x - y))
    return f
#Only send True if user inputs 1, else return False
def get_run_again():
    z = int(input("Try again? Type 1 for yes:"))
    if(z==1):
        return True
    else:
        return False

def main():
    again = True
    #Start the while loop by assigning True to again
    while(again == True):
        mag1 = get_magnitude(1)
        mag2 = get_magnitude(2)
        #To set mag1 as always greater than mag2
        if(mag2 > mag1):
            mag3 = mag2
            mag2 = mag1
            mag1 = mag3
            mag_compare = compare_magnitude(mag1, mag2)
        else:
            mag_compare = compare_magnitude(mag1, mag2)
        print("An earthquake of magnitude {0} is {1:.1f} times more powerful than an earthquake of magnitude {2}.".format(mag1, mag_compare, mag2))
        again = get_run_again()
    print("Bye!")
#Run the single main
main()


#Tohoku earthquake magnitude is 9
#Loma Preieta earthquake magnitude is 6.9
#Haiti earthquake magnitude is 7
#Tohoku earthquake is 1000 times more powerful than Haiti
#Around 100000 people died in the Haiti earthquake, while around 15896 people died in the Tohoku earthquake. Yes, it is quite amazing
