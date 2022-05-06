# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import FileReader
import FileWriter
import Transform


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def performETL():
    # part 1 begins here..........
    filePath = "Data.txt"
    data = FileReader.getData(filePath)
    fileWritePath = "WriteData.txt"
    file = open(fileWritePath, "w+")
    for line in data:
        line = Transform.performCapitalization(str(line))
        FileWriter.writeDataInFile(line, file)
    # close the file
    file.close()

    # part 2 begins here...................

    filePath = "WriteData.txt"
    data = FileReader.getData(filePath)
    summary = Transform.getSummary(data)
    # print("summary " + str(summary))

    # write summary data to Summary file
    SummaryFile = "Summary.txt"
    file = open(SummaryFile, "w+")
    FileWriter.writeDataInFile(str(summary), file)
    file.close()

    file = open(SummaryFile, "r")
    print("summary " + file.read())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('This is ETL DEMO ..... ')
    performETL()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
