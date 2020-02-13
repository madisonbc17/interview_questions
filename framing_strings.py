#find the longest string in the list of strings
#add the length + 4 *s to create the top/bottom of the frame
#print the top frame, each word with correct spacing, then the bottom frame

#for testing, I would test the individual functions of the class and see if they are outputting the correct values
def test_function():
    strings = ["What's","up","?"]
    test_frame = rectangular_frame(strings)
    
    test_frame.longest_string()
    if test_frame.max == 6:
        print("Longest_string succes!")
    else:
        print("Fail")
    
    test_frame.construct_top_of_frame()
    if test_frame.top_frame == "**********":
        print("construct_top_of_frame success!")
    else:
        print("construct_top_of_frame fail.")
        
    return

class rectangular_frame:
    def __init__(self, list_of_strings):
        self.string_list = list_of_strings
        self.max = 0
        self.total_length = 0
        #the top frame should be equal to the bottom frame, so I'm not going to add a bottom frame variable
        self.top_frame = ""
    
    def longest_string(self):
        for i in self.string_list:
            if len(i) > self.max:
                self.max = len(i)
        return
        
    def construct_top_of_frame(self):
        self.total_length = self.max + 4
        length = self.total_length
        while length > 0:
            self.top_frame += "*"
            length -= 1
        
    def print_total_frame(self):
        self.longest_string()
        self.construct_top_of_frame()
        print(self.top_frame)
        for word in self.string_list:
            line = "* " + str(word)
            if len(line) == self.total_length - 1:
                print(line + "*")
            else:
                num_spaces = (self.total_length - 1) - len(line)
                while num_spaces > 0:
                    line += " "
                    num_spaces -= 1
                print(line + "*")
        print(self.top_frame)

#here is the "main" part of my function
example = rectangular_frame(["Hello", "World", "in", "a", "frame"])
example.print_total_frame()

example2 = rectangular_frame(["Table of Contents", "Start................1","Middle...............2","End..................3"])
example2.print_total_frame()

example3 = rectangular_frame(["Magician","In a Box","    ___   ","   |   |  ","   |   |  ","----------","   ^  ^   ","    v     ","--      --","  \    /  ",])
example3.print_total_frame()