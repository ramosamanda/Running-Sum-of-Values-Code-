# CSCI220L-F18-Lab9-fileSum-APR.py
# Amanda Ramos
# A program that reads a collection of numbers for a file and maintains a
# running sum of the values.

def main():
    datafile = open("CSCI220L-F18-Lab9-1in.txt", "r")
    Sum = 0
    for number in datafile:
        RealNumbers = eval(number)
        Sum = Sum + RealNumbers
    # end for 
    print("Sum of values in file =",Sum)
    datafile.close()
#end main
main()
    
