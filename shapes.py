# python

# This will calculate the shares areas.
def calculateRectangleArea(width, height):
    area = width * height
    return area

def main():
    print('This is our shapes program')

def calc_tri_area(h,b):
    area = 1/2 * h * b
    return area

main()
rectangle_area = calculateRectangleArea(10,20)
print(f'the area of the rectangle is {rectangle_area}')
tri_area = calc_tri_area(20,79)
print(f'the area of the triangle is {tri_area}')