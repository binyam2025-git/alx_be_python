size = int(input("Enter the size of the pattern:"))

row_count = 0

print("\n --- Your pattern ---")

while row_count < size:

    for col_count in range(size):
        print("*", end="")

   print()
   row_count +=1


