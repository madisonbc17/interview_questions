#for this program, the input is a Roman numeral (string) and the output is the equivalent number (int).
#the only possibilities for Roman numeral characters are I, V, X and L.
#there is a max string length of four for each Roman numeral input- so the highest value would be LXXX or 80

#first step: take Roman numeral string and break it up
#second step: put a numerical value to the individual roman numerals
#third step: calculate what the total value of all the characters are
#fourth step: return

#step 1

def roman_numeral_break_up(roman_numeral_string):
    numeral_list = []
    for i in roman_numeral_string:
        numeral_list.append(i)
    return numeral_list

def numerals_to_integers(numeral_list):
    for i in numeral_list:
        if i == "I":
            numeral_list[numeral_list.index(i)] = 1
        elif i == "V":
            numeral_list[numeral_list.index(i)] = 5
        elif i == "X":
            numeral_list[numeral_list.index(i)] = 10
        elif i == "L":
            numeral_list[numeral_list.index(i)] = 50
        else:
            print("Invalid input")
            return 0
    return numeral_list

def add(last_total, add_int):
    return last_total + add_int

#this is my first attempt, but I can tell there are some issues with my logic
def calculate_integer(numeral_list):
    last_int = 0
    current_int = 0
    total = 0
    for i in numeral_list:
        current_int = i
        if last_int == 0:
            last_int = i
            continue
        if last_int != 0 and current_int > last_int:
            #subtract the last_int from the current int and add it to the total
            add_value = current_int - last_int
            total = add(total, add_value)
        else:
            total = add(last_int, current_int)
            last_int = current_int


