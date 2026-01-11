# Continue - to skip iterations. Skips only the current iteration

for num in range (1, 11):
    if num % 2 == 0:
        print("What are the numbers being skipped", num)
        continue

    print(num)