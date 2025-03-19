def fractal_print(fractal):
    print([elem for elem in fractal])

fractal = [3]
fractal.append(fractal)
fractal.append(2)

fractal_print(fractal)
