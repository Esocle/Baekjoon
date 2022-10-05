def self_number():
    numbers = []
    for num in range(1, 10001):
        for each_num in str(num):
            num += int(each_num)
        numbers.append(num)
    numbers = set(numbers)
    range_numbers = set(range(1, 10001))
    return sorted(range_numbers-numbers)

if __name__ == "__main__":
    self_numbers = self_number()

    for self_num in self_numbers:
        print(self_num)