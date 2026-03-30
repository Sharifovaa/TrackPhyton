numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
tuple_ = (numbers)
numbers_1 = tuple_[:4]
numbers_2 = tuple_[5:]
numbers_3 = numbers_1 + numbers_2
sum_3 = sum(numbers_3)
count_of_numbers = len(tuple_)
average = sum_3 / count_of_numbers
numbers[4] = average

print("Измененный список:", numbers)