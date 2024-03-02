num_input = input('Enter num:')
num = int(num_input)

first_dig = num // 100
second_dig = (num % 100) //10
third_dig = num % 10

zbir_cifara = first_dig + second_dig + third_dig
proizvod = first_dig * second_dig * third_dig

print (proizvod-zbir_cifara)
