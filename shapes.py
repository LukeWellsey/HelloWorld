# python

# This will calculate the shares areas.
def calculateRectangleArea(width, height):
    area = width * height
    return area

def main():
    print('This is our shapes program')

def calculateTriangleArea(height, base):
    area = 1/2 * base * height
    return area

main()
rectangle_area = calculateRectangleArea(10,20)
print(f'the area of the rectangle is {rectangle_area}')
triangle_area = calculateTriangleArea(20,40)
print(f'the area of the object or triangle is {triangle_area}')
