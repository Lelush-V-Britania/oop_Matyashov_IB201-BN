class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h

    def intersection(self, other):
        left1 = self.x
        right1 = self.x + self.w
        bottom1 = self.y
        top1 = self.y + self.h

        left2 = other.x
        right2 = other.x + other.w
        bottom2 = other.y
        top2 = other.y + other.h

        left = left1
        if left2 > left:
            left = left2
        right = right1
        if right2 < right:
            right = right2
        bottom = bottom1
        if bottom2 > bottom:
            bottom = bottom2
        top = top1
        if top2 < top:
            top = top2

        if left < right and bottom < top:
            return Rectangle(left, bottom, right - left, top - bottom)
        return None