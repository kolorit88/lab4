def defractalize(fractal):
    for elem in fractal[:]:
        if elem == fractal:
            fractal.remove(elem)

fractal = [1, 2]
fractal.append(fractal)
fractal.append(fractal)
fractal.append(3)
print(fractal)
defractalize(fractal)
print(fractal)