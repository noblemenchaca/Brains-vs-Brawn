'''
>>> Description: This program will open and read a file with brain and body weight specifications of different animals, then it will organize those numbers into lists and convert them from kilograms and grams to pounds. Then write those weight values in a new output file

'''


def find_insert_position(s, sA): #finds where and what information about whatever animal to manipulate, returning an integer refering to that position
    sN = s.lower()

    i = 0;
    for sI in sA:
        if sI.lower() == sN:
            return i;
        i = i + 1
    return -1;

def write_converted_csv(sN, sMAry, sBoAry, sBrAry): #takes each pf the parameter values from the given file and writes them into pound format
    oFile = open (sN, 'w')
    i = 0
    for s in sMAry:
        oFile.write(s + "," + "{0:.2f}".format((sBoAry[i] * 2.2)) + "," + "{0:.2f}".format((sBrAry[i] * 100 * 2.2)) + "\n")
        i = i + 1
    oFile.close()

def main(): #starts the lists for each of the specific values to be categorized and listed, then opens the csv files where each of those values might be read. The values are then split upline by line into indeces to be converted and written to a new file.
    sMAry = []
    sBoAry = []
    sBrAry = []

    oFile = open("BrainBodyWeightKilos.csv", "r")

    for s in oFile:
        sAry = s.split(',')
        sMAry.append(sAry[0])
        sBoAry.append(float(sAry[1]))
        sBrAry.append(float(sAry[2]))
    print(sBoAry)
    while True:
        sInput = input("Enter animal name (or \"q\" to quit): ")
        if sInput == "q" or sInput == "Q":
            write_converted_csv("BrainBodyWeightPounds.csv", sMAry, sBoAry, sBrAry)
            break
        iIndex = find_insert_position(sInput, sMAry)
        if iIndex != -1:
            print(sInput + ": body = {0:.2f}".format(sBoAry[iIndex]) + "kg, brain = {0:.2f}".format(sBrAry[iIndex]) + "g")
            sI = input('Delete'+ ' " ' + sInput + ' " ?\t(y|n)')
            if sI == "y" or sI == "Y":
                sMAry.pop(iIndex)
                sBoAry.pop(iIndex)
                sBrAry.pop(iIndex)
        if iIndex == -1:
            print("File does not contain \"" + sInput + "\".")
            sI = input("Add \"" + sInput + "\" to file? (y|n)")
            if  sI == "y" or sI == "Y":
                fBody = float(input("Enter body weight for \"" + sInput + "\" in kilograms:"))
                fBrain = float(input("Enter brain weight for \"" + sInput + "\" in grams:"))
                sMAry.append(sInput)
                sBoAry.append(fBody)
                sBrAry.append(fBrain)
                
    
if __name__ == "__main__":
    main()
