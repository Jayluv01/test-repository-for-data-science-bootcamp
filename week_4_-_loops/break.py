
# for num in range (1, 10):
#     guess = int(input("Guess the number: "))
#     if guess == 42:
#         print("Correct! You've found the number!")
#         break # This ends/exits the parent loop.
#     else:
#         print("Try again!")

for num in range (1, 1001):
    if num > 20:
        break
    if num % 2 == 0:
        print(num)
