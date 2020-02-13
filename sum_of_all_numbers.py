#given a list of numbers, return a sum of all the numbers
#for-loop
#while-loop
#recursion

class sum_of_numbers:
    def __init__(self, list_of_numbers):
        self.number_list = list_of_numbers
    
    def for_loop(self):
        sum = 0
        for i in self.number_list:
            sum += i
        return sum

    def while_loop(self):
        sum = 0
        new_list = self.number_list
        while len(new_list) > 0:
            sum += new_list[0]
            new_list.pop(0)
        return sum

    #for this recursion function, you must pass in the original sum as 0
    def recursion(self, current_sum):
        list_new = self.number_list
        if len(list_new) > 0:
            current_sum += list_new[0]
            list_new.pop(0)
            return self.recursion(current_sum)   
        else:
            return current_sum

def test_number_list_functions():
    number_list = []
    number_list.append(1)
    number_list.append(2)
    number_list.append(3)
    total_sum = 6
    
    example = sum_of_numbers(number_list)
    if total_sum == example.for_loop():
        print("For loop success!")
    
    example2 = sum_of_numbers(number_list)
    if total_sum == example2.while_loop():
        print("While loop success!")
    
    number_list.append(1)
    number_list.append(2)
    number_list.append(3)

#need to fixxxxx
    example3 = sum_of_numbers(number_list)
    result = example3.recursion(0)
    
    if total_sum == result:
        print("Recursion success!")

#I am not sure what example to give for a "main" section, but I provided a test case- so I will just call that
test_number_list_functions()