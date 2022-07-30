currentTimeStr = int(input("What is the current time (in hours 0-22)?"))
waitTimeStr = int(input("How many hours do you want to wait?"))

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)

