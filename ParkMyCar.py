from ParkingLot import ParkingLot
import fileinput
import sys

if sys.version_info[0] == 2:
	input = raw_input

def parkMyCar():  
    parkinglot = ParkingLot()

    print("=" * 25, "Welcome to Parking Lot system", "=" * 25)
    print("\nChoose an Option for Input Method:\n1. Command Line as Input\n2. Filename as Input")
    input_method = int(input("Enter your choice: "))

    if input_method == 1:
        while True:
            command = input("$ ")
            parkinglot.processInput(command)   
    else:
        filename = input("Enter the Filename\n")
        file = open(filename)
        for command in file.readlines():
            parkinglot.processInput(command)  

if __name__ == '__main__':
    parkMyCar()