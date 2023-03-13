# Exercise 4 - Dictionary Comprehension 1
# Description: You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence
# and calculates the number of letters in each word.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# # for word in sentence.split():
# #     print(word)
#
# result = {word:len(word) for word in sentence.split()}
# #
# print(result)


# Exercise 5 - Dictionary Comprehension 2
# Description: You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in 
# degrees Celsius and converts it into degrees Fahrenheit.
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# How to calculate Celsius to Fahrenheit = (temp_c * 9/5) + 32 = temp_f

#weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

#print(weather_f)



# How to Iterate of a Pandas DataFrame

import random
student_dict = {
    "student": ["Steve", "Matt", "Julie"],
    "score": [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
}
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
