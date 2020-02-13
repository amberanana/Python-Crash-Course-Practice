# Chapter 4 Working with Lists
# 4.1 Loop through the list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 我们定义了一个for 循环这行代码让Python从列表magicians 中取出一个名字，并将其存储在变量magician 中。
# 最后，我们让Python打印前面存储到变量magician 中的名字。
# 这样，对于列表中的每个名字，Python都将重复执行❷处和❸处的代码行。
# 你可以这样解读这些代码：对于列表magicians 中的每位魔术师，都将其名字打印出来。输出很简单，就是列表中所有的姓名。

#4.1.1 research loop
# Examples: for cat in cats
# for dog in dogs
# for item in list_of_items

# 4.1.2 Execute more works in the for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#4.1.3 Works after the end of for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")
# 开头两条print 语句针对列表中每位魔术师重复执行。然而，由于第三条print 语句没有缩进，因此只执行一次。
