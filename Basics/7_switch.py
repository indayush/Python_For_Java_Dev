# Python by default dosent have a switch statement/Functionality. 
# Makeshift of such scenario by creating our own function capable of working like switch -

def switch_Function(case):
    switch = {
            0:'Number',
            1:'',
            2:3,                            # Numbers dont need to be put in single quotes
            3:'$'                           # Switch Case can use Special Chars only in Value side of Key-Value Pair, 
                                            # that too ONLY within single quotes.
            #Z:'Special Char'               # Only Numbers allowed in the key side of Switch Case
        }
    return switch.get(case,"Default")       # get() sends the value if case is matched else sends the "Default" if nothing matched.

print(switch_Function(0))
print(switch_Function(1))
print(switch_Function(2))
print(switch_Function(3))

print('===================================================================')


# Example of Switch in Days of a Week
def week(case):
    switch =    {
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
                }
    return switch.get(case,"Default")

print(week(4))
print(week(9))
