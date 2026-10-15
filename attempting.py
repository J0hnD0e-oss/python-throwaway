#Write a program that displays the numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

#Display only even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

#Modify the program to display numbers from 1 to 20
for i in range(1, 21):
    print(i)

#Display numbers in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i)

print('----------------------------------------------')

#Write a program that calculates the sum of all numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print('total =', total)

#Calculate the sum from 1 to 50
total = 0
for i in range(1, 51):
    total += i
print('total =', total)

print('----------------------------------------------')

#Ask the user to enter the upper limit
limit = int(input('Enter max limit: '))
total = 0

for i in range(1, limit + 1):
    total += i

print('total =', total)

#Calculate the sum of even numbers only
limit = int(input('Enter max limit: '))
total = 0

for i in range(2, limit + 1, 2):
    total += i

print('Sum of even numbers =', total)

#Calculate the sum of only odd numbers
limit = int(input('Enter max limit: '))
total = 0

for i in range(1, limit + 1, 2):
    total += i

print('Sum of odd numbers =', total)

print('----------------------------------------------')

#Write a program that asks the user for a number and displays its multiplication table up to 10.
number = int(input('Enter a number: '))

for i in range(1, 11):
    print(number, 'x', i, '=', number * i)

#Display the table up to 12 instead of 10
number = int(input('Enter a number: '))

for i in range(1, 13):
    print(number, 'x', i, '=', number * i)

#Allow the user to choose the maximum multiplier
number = int(input('Enter a number: '))
maximum = int(input('Enter the maximum multiplier: '))

for i in range(1, maximum + 1):
    print(number, 'x', i, '=', number * i)

print('----------------------------------------------')

#Ask the user to enter their name and display each character on a separate line.
name = input('Enter your name: ')

for letter in name:
    print(letter)

#Count the total number of characters
print('Total characters:', len(name))

#Display each character with its position number
for i in range(len(name)):
    print(i, name[i])

#Display characters in reverse order
for letter in name[::-1]:
    print(letter)

#Convert all characters to uppercase before displaying
print(name.upper())

print('----------------------------------------------')

#Write a program that counts the number of characters in a word entered by the user
word = input('Enter a word: ')
print('Number of characters:', len(word))

#Ignore spaces when counting
text = input('Enter some text: ')
print('Characters without spaces:', len(text.replace(' ', '')))

#Count vowels separately.
word = input('Enter a word: ')
vowels = 0

for letter in word.lower():
    if letter in 'aeiou':
        vowels += 1

print('Vowels:', vowels)

#Count consonants separately.
word = input('Enter a word: ')
consonants = 0

for letter in word.lower():
    if letter.isalpha() and letter not in 'aeiou':
        consonants += 1

print('Consonants:', consonants)

#Display the longest word if a sentence is entered
sentence = input('Enter a sentence: ')
words = sentence.split()

if words:
    longest = max(words, key=len)
    print('Longest word:', longest)
else:
    print('No words entered.')

print('----------------------------------------------')

#Write a program that displays the first and last character of a word
word = input('Enter a word: ')

if word:
    print('First character:', word[0])
    print('Last character:', word[-1])
else:
    print('No word entered.')

#Also display the middle character
word = input('Enter a word: ')

if word:
    middle = len(word) // 2
    if len(word) % 2 == 1:
        print('Middle character:', word[middle])
    else:
        print('Middle characters:', word[middle - 1:middle + 1])

#Test with words of different lengths
for word in ['cat', 'book', 'hello']:
    print(word, 'has', len(word), 'characters')

#Display the ASCII value of the first and last character
word = input('Enter a word: ')

if word:
    print('First character ASCII:', ord(word[0]))
    print('Last character ASCII:', ord(word[-1]))
else:
    print('No word entered.')

print('----------------------------------------------')

#Write a program that displays the first four characters of a word
word = input('Enter a word: ')
print('First four characters:', word[:4])

#Display the first five characters instead
print('First five characters:', word[:5])

#Ask the user how many characters should be displayed
amount = int(input('How many characters should be displayed? '))
print(word[:amount])

#What happens if the word is shorter than four characters
print('First four characters:', word[:4])
print('If the word is shorter than four characters, Python displays the whole word.')

print('----------------------------------------------')

#Ask the user for their first name and surname. Create a username using the first three letters of each.
first_name = input('Enter first name: ')
surname = input('Enter surname: ')

username = first_name[:3].lower() + surname[:3].lower()
print(username)

#Convert the username to lowercase
print(username.lower())

#Add a random number at the end
import random
print(username + str(random.randint(0, 99)))

#Use four letters instead of three
username = first_name[:4].lower() + surname[:4].lower()
print(username)

#Display the username in uppercase.
print(username.upper())

print('----------------------------------------------')

#Write a program that displays a word in reverse
word = input('Enter word: ')
print('Reversed word:', word[::-1])

#Check whether the word is a palindrome
if word.lower() == word[::-1].lower():
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')

#Count the vowels in the word.
vowels = 0

for letter in word.lower():
    if letter in 'aeiou':
        vowels += 1

print('Number of vowels:', vowels)

#Display each character of the reversed word on a new line
for letter in word[::-1]:
    print(letter)

print('----------------------------------------------')

#Write a program that counts the number of vowels in a word
word = input('Enter a word: ')
count = 0

for letter in word.lower():
    if letter in 'aeiou':
        count += 1

print('Number of vowels:', count)

#Count consonants as well.
consonants = 0

for letter in word.lower():
    if letter.isalpha() and letter not in 'aeiou':
        consonants += 1

print('Number of consonants:', consonants)

#Display each vowel found.
for letter in word.lower():
    if letter in 'aeiou':
        print(letter)

#Determine which vowel appears most frequently.
vowel_counts = {}

for letter in word.lower():
    if letter in 'aeiou':
        vowel_counts[letter] = vowel_counts.get(letter, 0) + 1

if vowel_counts:
    most_common = max(vowel_counts, key=vowel_counts.get)
    print('Most frequent vowel:', most_common)
    print('Occurrences:', vowel_counts[most_common])
else:
    print('No vowels found.')

#Ignore upper/lower case differences
word = input('Enter a word: ')
count = sum(1 for letter in word.lower() if letter in 'aeiou')
print('Number of vowels:', count)

print('----------------------------------------------')



word = input('Enter a word: ')

for letter in word:
    if letter in 'aeiou':
        print(letter)

print('Python requires indentation to show which statements belong inside a loop, function, or conditional.')

print('----------------------------------------------')

#Create a tuple containing five countries and display each country using a loop
countries = ('UK', 'France', 'Spain', 'Italy', 'Norway')

for country in countries:
    print(country)

#Display the countries in reverse order.
for country in reversed(countries):
    print(country)

#Count the number of countries.
print('Number of countries:', len(countries))

#Display only countries starting with a chosen letter.
letter = input('Enter a starting letter: ').lower()

for country in countries:
    if country.lower().startswith(letter):
        print(country)

#Ask the user to search for a country
search = input('Enter a country to search for: ').lower()

if search in [country.lower() for country in countries]:
    print('Country found.')
else:
    print('Country not found.')

print('----------------------------------------------')

#Create a tuple of five student marks and display the highest, lowest and average mark
marks = (65, 70, 82, 45, 91)

print('Highest:', max(marks))
print('Lowest:', min(marks))
print('Average:', sum(marks) / len(marks))

#Count how many students scored above 70.
above_70 = sum(1 for mark in marks if mark > 70)
print('Above 70:', above_70)

#Count how many students failed.
failed = sum(1 for mark in marks if mark < 40)
print('Failed:', failed)

#Display marks in ascending order.
print(sorted(marks))

#Display marks in descending order
print(sorted(marks, reverse=True))

print('----------------------------------------------')

#Display the following pattern:
#1
#12
#123
#1234
#12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end='')
    print()

#Extend the pattern to 10 rows.
for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end='')
    print()

#Create the reverse pattern.
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

#Display stars (*) instead of numbers.
for i in range(1, 6):
    print('*' * i)

#Create a square pattern
for i in range(5):
    print('*' * 5)

print('----------------------------------------------')

#Ask the user for a password and check whether it contains at least 8 characters
password = input('Enter password: ')

if len(password) >= 8:
    print('Password valid')
else:
    print('Password too short')

#Check for uppercase letters.
has_upper = any(ch.isupper() for ch in password)
print('Contains uppercase:', has_upper)

#Check for digits.
has_digit = any(ch.isdigit() for ch in password)
print('Contains digits:', has_digit)

#Check for special characters.
has_special = any(not ch.isalnum() for ch in password)
print('Contains special characters:', has_special)

#Report why a password is weak
if len(password) < 8:
    print('Password needs at least 8 characters.')
if not has_upper:
    print('Password needs an uppercase letter.')
if not has_digit:
    print('Password needs a digit.')
if not has_special:
    print('Password needs a special character.')

print('----------------------------------------------')

#Write a program that:
#1. Asks the user for a word.
#2. Displays its length.
#3. Displays the first and last characters.
#4. Prints each character on a separate line.
#5. Displays the word in reverse.
word = input('Enter a word: ')

print('Length:', len(word))

if word:
    print('First:', word[0])
    print('Last:', word[-1])

for letter in word:
    print(letter)

print('Reversed:', word[::-1])

#Count vowels and consonants.
vowels = sum(1 for ch in word.lower() if ch in 'aeiou')
consonants = sum(
    1 for ch in word.lower()
    if ch.isalpha() and ch not in 'aeiou'
)

print('Vowels:', vowels)
print('Consonants:', consonants)

#Convert the word to uppercase.
print(word.upper())

#Determine whether the word is a palindrome.
if word.lower() == word[::-1].lower():
    print('Palindrome')
else:
    print('Not a palindrome')

#Display the ASCII value of each character.
for ch in word:
    print(ch, ord(ch))

print('----------------------------------------------')

#Write a program that asks the user to enter a password and reports:
#Total length
#Number of uppercase letters
#Number of lowercase letters
#Number of digits
#Whether the password is strong

#A password is strong if:
#Length ≥ 8
#Contains at least one uppercase letter
#Contains at least one lowercase letter
#Contains at least one digit

password = input('Enter password: ')

upper = sum(1 for ch in password if ch.isupper())
lower = sum(1 for ch in password if ch.islower())
digits = sum(1 for ch in password if ch.isdigit())
special = sum(1 for ch in password if not ch.isalnum())

print('Length:', len(password))
print('Uppercase:', upper)
print('Lowercase:', lower)
print('Digits:', digits)
print('Special characters:', special)

strong = (
    len(password) >= 8
    and upper > 0
    and lower > 0
    and digits > 0
)

if strong:
    print('Strong password')
else:
    print('Weak password')

#Count special characters.
print('Special characters:', special)

#Display suggestions to improve weak passwords.
if len(password) < 8:
    print('Use at least 8 characters.')
if upper == 0:
    print('Add an uppercase letter.')
if lower == 0:
    print('Add a lowercase letter.')
if digits == 0:
    print('Add a digit.')
if special == 0:
    print('Consider adding a special character.')

#Continue asking until a strong password is entered.
while not strong:
    password = input('Enter a stronger password: ')
    upper = sum(1 for ch in password if ch.isupper())
    lower = sum(1 for ch in password if ch.islower())
    digits = sum(1 for ch in password if ch.isdigit())

    strong = (
        len(password) >= 8
        and upper > 0
        and lower > 0
        and digits > 0
    )

print('Strong password accepted.')

#Calculate a password strength score
score = 0

if len(password) >= 8:
    score += 1
if upper > 0:
    score += 1
if lower > 0:
    score += 1
if digits > 0:
    score += 1
if any(not ch.isalnum() for ch in password):
    score += 1

print('Password strength score:', score, '/ 5')

print('----------------------------------------------')

#Ask the user to enter a sentence and calculate:
#Number of vowels
#Number of consonants
#Number of spaces
#Number of digits

text = input('Enter a sentence: ')

vowels = 0
consonants = 0
spaces = 0
digits = 0

for ch in text:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == ' ':
        spaces += 1
    elif ch.isdigit():
        digits += 1

print('Vowels:', vowels)
print('Consonants:', consonants)
print('Spaces:', spaces)
print('Digits:', digits)

#Count punctuation marks.
punctuation = sum(
    1 for ch in text
    if not ch.isalnum() and not ch.isspace()
)
print('Punctuation:', punctuation)

#Count uppercase and lowercase letters separately.
uppercase = sum(1 for ch in text if ch.isupper())
lowercase = sum(1 for ch in text if ch.islower())

print('Uppercase letters:', uppercase)
print('Lowercase letters:', lowercase)

#Find the most common vowel.
vowel_counts = {}

for ch in text.lower():
    if ch in 'aeiou':
        vowel_counts[ch] = vowel_counts.get(ch, 0) + 1

if vowel_counts:
    common_vowel = max(vowel_counts, key=vowel_counts.get)
    print('Most common vowel:', common_vowel)
else:
    print('No vowels found.')

#Display all digits found in the sentence
found_digits = [ch for ch in text if ch.isdigit()]
print('Digits found:', found_digits)

print('----------------------------------------------')

#Given a tuple of student marks:
#marks = (65, 82, 45, 91, 72, 88, 59)
#Calculate:
#Average mark
#Number of passes (≥ 40)
#Number of distinctions (≥ 70)
#Highest mark
#Lowest mark

marks = (65, 82, 45, 91, 72, 88, 59)

average = sum(marks) / len(marks)
passes = sum(1 for mark in marks if mark >= 40)
distinctions = sum(1 for mark in marks if mark >= 70)

print('Average mark:', average)
print('Passes:', passes)
print('Distinctions:', distinctions)
print('Highest mark:', max(marks))
print('Lowest mark:', min(marks))

#Sort the marks.
print('Sorted marks:', sorted(marks))

#Calculate the median mark.
sorted_marks = sorted(marks)
middle = len(sorted_marks) // 2

if len(sorted_marks) % 2 == 1:
    median = sorted_marks[middle]
else:
    median = (sorted_marks[middle - 1] + sorted_marks[middle]) / 2

print('Median:', median)

#Count distinctions and passes.
print('Distinctions:', sum(1 for mark in marks if mark >= 70))
print('Passes:', sum(1 for mark in marks if mark >= 40))

#Display all marks above the average
for mark in marks:
    if mark > average:
        print(mark)

print('----------------------------------------------')

#Create the following tuple:
#students = ("Ali", "Sara", "John", "Ahmed", "Fatima")
#Ask the user to enter a name.
#Display:
#Position of the name if found
#Appropriate message if not found

students = ("Ali", "Sara", "John", "Ahmed", "Fatima")
target = input('Enter name to search: ').strip()

if target.lower() in [student.lower() for student in students]:
    index = [student.lower() for student in students].index(target.lower())
    print('Found at position:', index)
else:
    print('Student not found')


#Display all student names alphabetically.
print(sorted(students))

#Count total students.
print('Total students:', len(students))

#Allow repeated searches without restarting
while True:
    target = input('Enter a name to search, or type quit: ').strip()

    if target.lower() == 'quit':
        break

    if target.lower() in [student.lower() for student in students]:
        print('Student found')
    else:
        print('Student not found')

print('----------------------------------------------')

#Convert consecutive repeated characters into a count.
#Example: Input: aaabbbbccdd
#Output: a3b4c2d2

text = input('Enter a string: ')
result = ''

if text:
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)

print('Output:', result)


#Calculate the compression ratio.
if text:
    ratio = len(result) / len(text)
    print('Compression ratio:', ratio)
else:
    print('Compression ratio cannot be calculated for empty text.')

#Decode the compressed output.
decoded = ''
i = 0

while i < len(result):
    character = result[i]
    i += 1
    number = ''

    while i < len(result) and result[i].isdigit():
        number += result[i]
        i += 1

    decoded += character * int(number)

print('Decoded:', decoded)

#Ignore differences between uppercase and lowercase letters
text = input('Enter a string: ').lower()
result = ''

if text:
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)

print('Output:', result)

print('----------------------------------------------')

#Write a program that:
#1. Accepts a sentence from the user.
#2. Counts:
# o Total characters
# o Total words
# o Total vowels
# o Total consonants
#3. Finds the longest word.
#4. Displays the sentence in reverse.
#5. Displays each word on a separate line together with its length.

sentence = input('Enter a sentence: ')

print('Total characters:', len(sentence))

words = sentence.split()
print('Total words:', len(words))

vowels = sum(1 for ch in sentence.lower() if ch in 'aeiou')
consonants = sum(
    1 for ch in sentence.lower()
    if ch.isalpha() and ch not in 'aeiou'
)

print('Total vowels:', vowels)
print('Total consonants:', consonants)

if words:
    longest_word = max(words, key=len)
    print('Longest word:', longest_word)
else:
    print('Longest word: None')

print('Sentence in reverse:', sentence[::-1])

for word in words:
    print(word, '- length:', len(word))

print('----------------------------------------------')

#4. Find the route with the fewest stops from Sheffield to London. Use breadth-first search: keep a list of paths to explore as a queue, take the oldest path with pop(0), and add a new path for each unvisited neighbour.

#Use the connections supplied in your worksheet.
#The exact route depends on the complete graph of connections.

graph = {
    'Birmingham': ['Derby', 'Sheffield'],
    'Derby': ['Birmingham', 'Nottingham'],
    'Leicester': ['Nottingham', 'London'],
    'Lincoln': ['Nottingham', 'Newark'],
    'Newark': [],
    'Nottingham': ['Derby', 'Leicester', 'Sheffield', 'Lincoln'],
    'Sheffield': ['Nottingham', 'Birmingham'],
    'London': ['Leicester']
}

def breadth_first_search(graph, start, destination):
    queue = [[start]]
    visited = {start}

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current == destination:
            return path

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = path + [neighbour]
                queue.append(new_path)

    return None

route = breadth_first_search(graph, 'Sheffield', 'London')

if route is not None:
    print(route)
else:
    print('No route found from Sheffield to London.')

#5. Try the route from Newark to London. What happens, and why? How should the program handle this?

route = breadth_first_search(graph, 'Newark', 'London')

if route is not None:
    print(route)
else:
    print('No route found from Newark to London.')


#One-way: Lincoln -> Newark
graph['Lincoln'].append('Newark')



from collections import deque

def breadth_first_search_deque(graph, start, destination):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == destination:
            return path

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None

route = breadth_first_search_deque(graph, 'Sheffield', 'London')

if route is not None:
    print(route)
else:
    print('No route found from Sheffield to London.')

route = breadth_first_search_deque(graph, 'Newark', 'London')

if route is not None:
    print(route)
else:
    print('No route found from Newark to London.')