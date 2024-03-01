# question 1
a = 6
a = a - 2
print(a * 2)
a = a * 2
print(a + 1)
a = a // 3
print(a)

# question 2
print(2 + 3 * 6 / 2)

# question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)


# question 4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


words = [
    "4257304920394478392772938744930294037524",
    "0974101607733149676776769413377061014790",
    "7798338247658278460338648728567428338977",
    "2704702208931031198668911301398022074072"
]

for word in words:
    if not palindrome(word):
        print(f'The string that is NOT a palindrome is: "{word}"')
        break

# question 6

my_list = [1, 2, 3]
print("Original list:", my_list)
my_list[1] = 200
print("List after modification:", my_list)
my_list.append(4)
print("List after adding an element:", my_list)

my_string = "hello"
print("Original string:", my_string)
try:
    my_string[1] = 'a'
except TypeError as e:
    print("Error:", e)
new_string = my_string.replace('e', 'a')
print("New string after replace:", new_string)
print("Original string remains unchanged:", my_string)

# question 7
import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
processed_numbers = [num * 2 for num in random_numbers if num % 2 == 0]

print(processed_numbers)


# question 8

def is_valid_url(url):
    if '://' not in url:
        return False

    scheme, rest = url.split('://', 1)

    if scheme not in ['http', 'https']:
        return False

    if not rest or not url.endswith('.com'):
        return False

    return True


print(is_valid_url("https://www.example.com"))  # Expected: True
print(is_valid_url("http://example"))  # Expected: False, does not end with .com
print(is_valid_url("justastring"))  # Expected: False
print(is_valid_url("ftp://example.com"))  # Expected: False, invalid scheme
print(is_valid_url("https://example.net"))  # Expected: False, does not end with .com


# question 9
def days_since_birthday(birthday_str):
    day, month, year = map(int, birthday_str.split('-'))
    current_year = 2024
    year_difference = current_year - year - 1
    days_passed = year_difference * 365

    return days_passed


birthday = "26-02-2003"
print(days_since_birthday(birthday))

# question 5

def find_pattern_occurrences(text):
    pattern_start = "C"
    pattern_end = "jeb"
    count = 0
    start_index = 0

    # Loop through the text to find each occurrence of the pattern
    while True:
        # Find the starting index of the pattern
        start_index = text.find(pattern_start, start_index)

        if start_index == -1:
            # No more "C" found in the text, break the loop
            break

        # Try to find the ending of the pattern starting from the current start_index
        end_index = text.find(pattern_end, start_index)

        if end_index != -1 and (
                end_index + len(pattern_end) == len(text) or text[end_index + len(pattern_end)] in ' .,;!?'):
            # A complete pattern is found
            count += 1
            # Update start_index to search for the next pattern
            start_index = end_index + len(pattern_end)
        else:
            # No complete pattern found, move to the next character
            start_index += 1

    return count


# Example usage
text = "This is a test for Cabcjeb and Cdefghijeb patterns."
print(find_pattern_occurrences(text))
