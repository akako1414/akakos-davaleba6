for i in range(1, 101):
    if i % 5 == 0 or i % 3 == 0:
        print(i)



names = []


name = input("შემოიტანეთ სახელი: ")
surname = input("შემოიტანეთ გვარი: ")


names.append(name)
names.append(surname)


print(names)


number = int(input("შემოიტანეთ რიცხვი: "))


sum_of_numbers = 0
for i in range(1, number + 1):
    print(i)
    sum_of_numbers += i


print("რიცხვების ჯამი:", sum_of_numbers)
print("საშუალო არითმეტიკული:", sum_of_numbers / number)


even_numbers = []


for i in range(2, 51, 2):
    even_numbers.append(i)


print(even_numbers)


number = int(input("შემოიტანეთ რიცხვი: "))


is_prime = True
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break
