def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count +=1
    return count

word = "Programming"
res = count_vowels(word)
print("number  of vowels: ", res)