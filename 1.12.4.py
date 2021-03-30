type_figure = input()
if type_figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    area_triangle = (p * (p - a) * (p - b) *(p - c)) ** 0.5
    print(area_triangle)
elif type_figure == "прямоугольник":
    a = int(input())
    b = int(input())
    area_square = a * b
    print(area_square)
elif type_figure == "круг":
    radius = int(input())
    area_circle = 3.14 * (radius ** 2)
    print(area_circle)
