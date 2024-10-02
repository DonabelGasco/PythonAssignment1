"""
Gasco, Donabel V.
3-F2
Python Assignment
"""

print('1. Print student name using inputted specific index in a Sets')
students = {'John', 'Maria', 'David', 'Samantha'}
students_list = list(students) 

index = int(input("Enter the index of the student: ")) 
print("Student at index", index, "is", students_list[index]) 

print('2. Get the average of all odd numbers in a tuple')
numbers = (1, 4, 7, 10, 13, 16)
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
sum_odd_numbers = 0
for num in odd_numbers:
    sum_odd_numbers += num
average = sum_odd_numbers / len(odd_numbers)
print("Average of odd numbers:", average)


print('3. Print names of people older than 19 in a dictionary')
people = {'profile':{'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}
for name, age in people['profile'].items():
    if age > 19:
        print(name)

print('4. Print numbers that appear more than once in the list:')
numbers = [1, 3, 2, 4, 3, 1, 2, 5, 10]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num, freq in frequency.items():
    if freq > 1:
        print(num)

print('5. Print name and score of the student with the highest score')
students_scores = [[('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]]
max_score = students_scores[0][0][1]
max_student = students_scores[0][0][0]
for name, score in students_scores[0]:
    if score > max_score:
        max_score = score
        max_student = name
print("Name:", max_student, "Score:", max_score)


