start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

squares = [x**2 for x in range(start, end + 1)]
evens = [x for x in squares if x % 2 == 0]
odds = [x for x in squares if x % 2 != 0]

print("Squares:", squares)
print("Even squares:", evens)
print("Odd squares:", odds)
