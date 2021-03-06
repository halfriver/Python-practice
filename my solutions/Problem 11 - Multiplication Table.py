'''
Problem 11 - Multiplication Table
- Create a program that prints out a multiplication table for the numbers 1
through 9.
- It should include the numbers 1 through 9 on the top and left axes, and it
should be relatively easy to find the product of two numbers. Do not simply
write out every line manually (i.e. print('7 14 21 28 35 49 56 63') ).
- As your products get larger, your columns will start to get crooked from the
number of characters on each line. Clean up your table by evenly spacing
columns so it is very easy to find the product of two numbers.
- Bonus: Allow the user to choose a number to change the size of the table
(so if they type in 12, the table printed out should be a 12x12 multiplication
table).
'''

# Original: 12 Oct 2019
# Edited: 25 November 2020


def table(n):
    table = [[" "]]
    # fill in first row (unique)
    for x in range(1, n+1):
        table[0].append(str(x))
    # add and populate new rows
    for y in range(1, n+1):
        table.append([str(y)])
        for z in range(1, n+1):
            table[y].append(str(y*z))
    # add spaces so that the table is consistent
    space = len(table[n][n])
    for row in range(n+1):
        for cell in range(n+1):
            while len(table[row][cell]) < space:
                table[row][cell] = " " + table[row][cell]
    return table


# error testing for input
while True:
    try:
        n = int(input("Give me a number and I'll make a multiplication table with that many rows and columns.\n").replace(" ", ""))
        if n < 0:
            print("You must give a positive number. Try again.")
            continue
        break
    except ValueError:
        print("That's not a valid number. Try again.")

for row in table(n):
    print(row)
