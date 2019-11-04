"""
@author: Johnny and Thanh
"""
import time
start = time.time()


# Main Program
def main():
    contents = read_file()
    month_vector = split_year(contents)
    
    # Prints Main Display.
    print('Month\tAverage\tMinimum\tMaximum')
    print('================================')
    
    # Prints line by line.
    for number in range(1, len(month_vector) + 1):
        ave = average(month_vector[int(number) - 1])
        small = minimum(month_vector[int(number) - 1])
        large = maximum(month_vector[int(number) - 1])
        print(number, '\t', ave, '\t', small, '\t', large)

# Opens and copies contents of file and returns it.
def read_file():
    step_file = open('steps.txt', 'r')
    
    contents = step_file.read()
    
    step_file.close()
    
    return contents

# Splits year into appropriate months and returns 12 sets in 1 big set.
def split_year(contents):
    year_set = contents.split()
    months = [year_set[0:31], year_set[31:59], year_set[59:90], year_set[90:120],
              year_set[120:151], year_set[151:181], year_set[181:212], 
              year_set[212:243], year_set[243:273], year_set[273:304],
              year_set[304:334], year_set[334:365]]
    return months

# Returns average of month i.
def average(monthi):
    total = 0
    for number in monthi:
        total = total + int(number)
    return round(total / len(monthi))

# Returns maximum of month i.
def maximum(monthi):
    largest = None
    for number in monthi:
        if largest == None or largest < int(number):
            largest = int(number)
    return largest

# Returns minimum of month i.
def minimum(monthi):
    smallest = None
    for number in monthi:
        if smallest == None or smallest > int(number):
            smallest = int(number)
    return smallest

#  Call on Main Program
main()

end = time.time()

print(end - start)