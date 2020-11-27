import sys

min_number = sys.maxsize
max_number = -sys.maxsize

for i in range(6):
    number = float(input("?: "))
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number
print("Минимальное число:", round(min_number, 2))
print("Максимальное число:", round(max_number, 2))
