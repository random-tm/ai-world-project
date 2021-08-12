# Command line arguments
import getopt
import sys

# Total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

# Arguments Passed
print("\nName of Python script: ", sys.argv[0])

print("\nArguments passed: ", end=" ")
for i in range(1,n):
    print(sys.argv[i], end=" ")

# List of command line arguments
argument_List = sys.argv[1:]

# Options
options = "flpia:"

long_options = ["File_Path", "Lore_Folder", "Persona_Type", "Input_Path", "AI_Type"]

# Doing of things
try:
    # Parsing Argument:
    arguments, values = getopt.getopt(argument_List, options, long_options)

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-f", "--File_Path"):
            print("File_Path is:" + currentValue)
        elif currentArgument in ("-l", "--Lore_folder"):
            print("Lore_Folder is: " + currentValue)
        elif currentArgument in ("-p", "--Persona_Type"):
            print("Persona_Type is: " + currentValue)
        elif currentArgument in ("-i", "--Input_Path"):
            print("Input_Path is: " + currentValue)
        elif currentArgument in ("-a", "--AI_Type"):
            print("AI_Type is: " + currentValue)

except getopt.error as err:
    # Output error, return with error code
    print(str(err))
