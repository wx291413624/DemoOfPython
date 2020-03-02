class RectangleCoordinate(object):

    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def getAverageY(self):
        return (self.y0 + self.y1) / 2

    def getAverageX(self):
        return (self.x0 + self.x1) / 2

    def getSplitRectangleList(self):
        """count=1000"""
        splitRectangleList = []
        splitRectangleList.append(RectangleCoordinate(self.x0, self.y0, self.getAverageX(), self.getAverageY()))
        splitRectangleList.append(RectangleCoordinate(self.getAverageX(), self.y0, self.x1, self.getAverageY()))
        splitRectangleList.append(RectangleCoordinate(self.x0, self.getAverageY(), self.getAverageX(), self.y1))
        splitRectangleList.append(RectangleCoordinate(self.getAverageX(), self.getAverageY(), self.x1, self.y1))
        return splitRectangleList
