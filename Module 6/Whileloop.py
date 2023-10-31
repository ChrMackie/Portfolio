count = 1
while count <= 5:
    #This code will execute as long as the condition (count<=5) is true
    if count == 3:
        #Add a condition to skip printing when count is 3
        count+=1
        #increase value of count by 1 for the next iteration
        continue
    print(count) #This will print current value of count
    count+=1 #increase the value of count by 1 for the next iteration