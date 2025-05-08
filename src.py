n = int(input("Enter a number (n < 15): "))

# Determine square size and number of layers based on input
if n < 5:
    size = n + 1
    layers = 1
elif n < 10:
    size = n + 2
    layers = 2
elif n < 15:
    size = n + 3
    layers = 3
else:
    print("Input out of allowed range (< 15)")
    exit()

for i in range(size):
    row = ""
    for j in range(size):
        carve = False

        # Carve bottom-left corner: diagonal from bottom-left upward-right
        for l in range(1, layers + 1):
            if i == size - l + j and j < l:
                carve = True
                break

        # Carve top-right corner: diagonal from top-right downward-left
        for l in range(1, layers + 1):
            if i == j - (size - l) and j >= size - l:
                carve = True
                break

        row += "  " if carve else "* "
    print(row)
