from datetime import date 

def printDate():

    todayDate = date.today()
    print("Current date: {}".format(todayDate.strftime("%Y-%m-%d")))
printDate()




