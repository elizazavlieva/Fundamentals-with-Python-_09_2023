numbers = [int(num) for num in input().split(', ')]
positive = [str(num) for num in numbers if num >= 0]
negative = [str(num) for num in numbers if num < 0]
even = [str(num) for num in numbers if num % 2 == 0]
odd = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(positive)} \n"
      f"Negative: {', '.join(negative)} \n"
      f"Even: {', '.join(even)} \n"
      f"Odd: {', '.join(odd)}")