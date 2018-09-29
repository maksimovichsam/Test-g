size = int(input("Enter size of pyramid: "))
for n in range(size, 0, -1):
    line = (' ' * (n - 1)) + 'x' + ('x' * 2 * (size - n))
    print(line)
