class Solution:
    def __init__(self, radius: float, x: float, y: float):
        self.r  = radius
        self.x = x
        self.y = y
    def randPoint(self) -> List[float]:
        R = self.r * math.sqrt(random.uniform(0,1))
        theta = random.uniform(0,2*math.pi)
        return [self.x + R*math.cos(theta), self.y + R*math.sin(theta)]