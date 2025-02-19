numbers = [2, 3]
numero = [2]

RESULT = numero > numbers
print(RESULT) 

sum_result = sum(numbers)
product_result = 1
for num in numbers:
    product_result *= num 


results = [sum_result, product_result]

average = sum_result / len(numbers)
results.append(average)

results.insert(1,max(numbers))

squares = [num ** 2 for num in numbers]
results.extend(squares)

results.remove(min(results))

print("Final Results:", results)
