marks = [12, 11 ,12,  10, 14, 16 ,19]
name = ["Sanjeet", "Void", "Magar"]
print(marks)
pop_item = marks.pop(1)
print(pop_item)
marks.append(88) #Use when we want to add the value at last
marks.pop(1) #Pop the last element or  provide index then we can pop that also. Show the value which we pop
print(marks.extend(name)) #Its modified marks by adding name list we can also use + sign to add or also use unpacked method to get same result
print(marks)

marks.insert(0, "Sanjeet") #First mention the index where you want to add and at last mention what you want to add
marks.remove(12) #remove use when we know exact we want to remove it remove the first appereance of the value
print(marks)
marks.sort() #we cant sort when string and int are there in single list
print(marks)
marks.reverse()
print(marks)
print(marks)
count = marks.count(12) #Count the apperance of given number
print(count)
indexCount = marks.index(19)
print(indexCount)
print(marks)
print(len(marks))
marks.clear()

# print(pop_item)