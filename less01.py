value_1 = int(input("Введіть 4-х значне число: "))


if value_1 < 1000 or value_1 > 9999:
    print("Будь ласка, введіть 4-х значне число.")
else:
    result_too = value_1 // 1000
    result_yoo = value_1 % 1000 // 100
    result_boo = value_1 % 100 // 10
    result_goo  = value_1 % 10

print(result_too)
print(result_yoo)
print(result_boo)
print(result_goo)

