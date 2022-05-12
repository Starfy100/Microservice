import time

isrunning = True

while (isrunning == True):
    commandfile = open("C:/Users/legom/Desktop/School/Notes Spring 2022/CS361 SOFTWARE ENGINEERING/NewUI/commands.txt","r")
    print("waiting")
    #time.sleep(5)

    if (commandfile.read() == 'sort'):
        commandfile.close()
        print("sorting")
        isrunning = False
        datafile = open("C:/Users/legom/Desktop/School/Notes Spring 2022/CS361 SOFTWARE ENGINEERING/NewUI/data.txt","r+")
        filearray = datafile.readlines()
        filearray.sort()
        print(filearray)
        datafile.close()

        datafile = open("C:/Users/legom/Desktop/School/Notes Spring 2022/CS361 SOFTWARE ENGINEERING/NewUI/data.txt","w+")
        
        for i in range(len(filearray)):
            print(i)
            datafile.write(filearray[i])

        datafile.close()
        commandfile = open("C:/Users/legom/Desktop/School/Notes Spring 2022/CS361 SOFTWARE ENGINEERING/NewUI/commands.txt","w")
        commandfile.write('done')
    time.sleep(5)
