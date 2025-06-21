# # задача 19
# def pointlnRect(x, x1, x2, y, y1, y2):
#     return (x1 <= x <= x2) and (y1 <= y <= y2)
# print(pointlnRect(1,1,2,4,4,6,))

# # задача 20
# def pointlnTriangle( x, x1, x2, x3,y , y1, y2, y3):
#     a = ((y2-y3)*(x-x3)+(x3-x2)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x1)*(y1-y3))
#     b =((y3-y1)*(x-x3)+(x1-x3)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x1)*(y1-y3))
#     y = 1 - a - b
#     return 0 < a < 1, 0 < b < 1, 0 < y < 1, a + b + y + 1
# print(pointlnTriangle(0,4,1,0,4,1,0,4,))

