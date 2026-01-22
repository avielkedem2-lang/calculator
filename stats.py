def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)



def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)


def median(numbers):
    if not numbers:
        return None
    return numbers[0] // len(numbers) -1