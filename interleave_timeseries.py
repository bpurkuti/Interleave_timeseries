#Interleave Timeseries
import random

#TimeData Object, Each associated with its time and value
class TimeData:
    def __init__(self, time, value):
        self.time = time
        self.value = value

#Sort/interleave function
#combine two sorted list into 1 sorted list and return it
def interleave(l1, l2):
    combinedList = []

    #Run the loop until both list are not empty
    #First two if statements are there in case another list is empty
    #In that case keep pushing objects to the combinedlist and pop from original
    #3rd and 4th if statements: Compares the first objects of each list with each other and 
    #whichever object is smaller gets added to the combined list and popped from original
    #list
    while len(l1)>0 or len(l2)>0:
        if(len(l1)==0):
            combinedList.append(l2[0])
            l2.pop(0)
        elif(len(l2)==0):
            combinedList.append(l1[0])
            l1.pop(0)
        elif(l1[0].time < l2[0].time):
            combinedList.append(l1[0])
            l1.pop(0)
        else:
            combinedList.append(l2[0])
            l2.pop(0)
        
    return combinedList

#print function
def printl(list):
    for i in list:
        print(i.time, i.value)

if __name__ == '__main__':
    list1 = []
    list2 = []

    #Generating List 1 and List 2 with TimeData Object
    for i in range(10):
        #Time is in range from 0000 to 2400 i.e 24 hour format
        #Value is in from 0 till 500
        time = random.randint(0,2400)
        value = random.randrange(0,500)
        list1.append(TimeData(time, value))
        time = random.randint(0,2400)
        value = random.randrange(0,500)
        list2.append(TimeData(time, value))

    print("Sorted List 1:")
    #Sort the objects in the list based on time variable
    list1.sort(key = lambda TimeData: TimeData.time)
    printl(list1)
    print("\n")

    print("Sorted List 2:")
    list2.sort(key = lambda TimeData: TimeData.time)
    printl(list2)
    print("\n")

    #call interleave func
    list3 = interleave(list1, list2)
    print("Sorted Combined List:")
    printl(list3)
