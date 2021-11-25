last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#creating a variable subjects to store lists of subjects
subjects = ["physics","calculus","poetry","history"]


#initializing grades to store scores
grades = [98,97,85,88]



#Initializing a 2D Array to combine grades and subjects
gradebook =[["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]



#Adding Computer Science and its scores to gradebook
gradebook.append(["computer science", 100])


#Adding Visual Art and its scores to gradebook
gradebook.append(["visual arts", 93])



#Modifying grade the grade for Visual Art at the last index of the list
gradebook[-1][1]= 98



#Removing the grade value for poetry and replacing it with Pass
gradebook[2].remove(85)
gradebook[2].append('Pass')

print(gradebook)

# combining last_semester_gradebook and gradebook into one book, full_gradebook
full_gradebook = last_semester_gradebook + gradebook


print(full_gradebook)
