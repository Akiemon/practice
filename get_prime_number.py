def get_prime_number(max_val):
    numbers = []
    for i in range(2, max_val + 1):
        flag = True

        for j in numbers:
            if i % j == 0:
                flag = False
                break

        if flag == True:
                numbers.append(i)
                
    numbers.insert(0, 1)
                
    return numbers

numbers = get_prime_number(10000)
print(numbers)