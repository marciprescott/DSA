# Create a list of squares from numbesr 1 to 20 but only includen the squares that are divisible by 3.
squares = []
for i in range(1, 21):
    if i**2 % 3 == 0:
        squares.append(i**2)
print(squares)
squareslc = [i**2 for i in range(1, 21) if i % 3 == 0]
print(squareslc)
