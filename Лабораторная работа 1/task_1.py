numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

uniq_numbers1 = numbers[:4]
uniq_numbers2 = numbers[5:]
uniq_numbers = uniq_numbers1 + uniq_numbers2
average = sum(uniq_numbers) / len(numbers)
numbers[4] = average
print("Измененный список:", numbers)
