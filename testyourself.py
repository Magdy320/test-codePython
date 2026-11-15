scores = [45,82,19,95,67,34]
large = scores[0]

for num in scores:
    if num > large:
        large = num

print("Largest number is:", large)
