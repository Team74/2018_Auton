class Interpreter:
    def Interprate(FileName):
        str(FileName)
        file = open(FileName,"r")
        masterList = []
        with open(FileName) as f:
            data = f.readlines()
            for line in data:
                temp = line.split(", ")
                temp.remove("\n")
                masterList.append(temp)
        file.close()
        for i in masterList:
            if i[0] == "1":
                i[0] = "driveCommand"
            elif i[0] == "2":
                i[0] = "turnCommand"
            elif i[0] == "3":
                i[0] = "genericCommand"
        return masterList
    print(Interpreter.Interprate("TestFile.py"))
