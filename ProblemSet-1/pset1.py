# Problem 1

vowels = 'aeiou'
count = 0
for letter in s:
    if letter in vowels:
        count += 1

print("Number of vowels: " + str(count))

# Problem 2

count = 0
for i in range(len(s)):
    if s[i:i + 3] == 'bob':
        count += 1

print("Number of times bob occurs is: " + str(count))

# Problem 3

last = ord(s[0])
substring = ''
ans = ''

for letter in s:
    if ord(letter) >= last:
        substring += letter
    else:
        if len(substring) > len(ans):
            ans = substring
            substring = ''
            substring += letter
        else:
            substring = ''
            substring += letter
    last = ord(letter)

if len(substring) > len(ans):
    ans = substring

print("Longest substring in alphabetical order is: " + ans)