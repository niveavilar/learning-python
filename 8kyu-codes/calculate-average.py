def find_average(numbers):
    if not numbers:
        return 0
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)
