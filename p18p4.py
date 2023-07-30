#¨Practical 18
#found the structure and endswith function here: https://stackoverflow.com/questions/4779790/python-tutorial-question-ends-with-function
#define function putting strings in lower case, then returns with endswith function whether either string ends the other
#prints function

def ends_with(string_a, string_b):
    string_a = string_a.lower()
    string_b = string_b.lower()
    return string_a.endswith(string_b) or string_b.endswith(string_a)

string_a = input('Enter the 1st string: ')
string_b = input('Enter the 2nd string: ')

print(ends_with(string_a, string_b))
