def return_fractal_list(n=10):
    if n == 0:
        return [0, "-", "-", 2]
    return [0, return_fractal_list(n-1), return_fractal_list(n-1), 2]

fractal = return_fractal_list()
print(fractal)