class Point:

    # initializator
    # self 
    def __init__(self, x, y, z):
        # x и y - это instance attributes, то есть аттрибуты экземпляра
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'Point: x= {}, y = {}, z = {}'.format(self.x, self.y, self.z)


point = Point(4, 6, 5)

print(point, '\n', point.x, point.y, point.z)


# https://www.tutorialsteacher.com/python/magic-methods-in-python
