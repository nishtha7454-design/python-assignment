try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number")

else:
    print("Square:", num ** 2)

finally:
    print("Program completed")
