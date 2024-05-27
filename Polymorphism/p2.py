# Create a function total_area(shapes) that takes a list of shapes (objects of classes derived from Shape) and returns the total area of all shapes.

def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total
