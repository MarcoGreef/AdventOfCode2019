from collections import Counter

class MapMaker:
    def __init__(self):
        self.points = []
        self.junctions = []
        self.x = 0
        self.y = 0

    def add_route(self, route):
        self.x = 0
        self.y = 0

        for i in route:
            distance = int(i[1:])
            if i[0] == 'U':
                for pos in reversed(range(self.y - distance, self.y)):
                    self.points.append('{}*{}'.format(self.x, pos))
                self.y -= distance
            elif i[0] == 'D':
                for pos in range(self.y + 1, self.y + distance + 1):
                    self.points.append('{}*{}'.format(self.x, pos))
                self.y += distance
            elif i[0] == 'L':
                for pos in reversed(range(self.x - distance, self.x)):
                    self.points.append('{}*{}'.format(pos, self.y))
                self.x -= distance
            elif i[0] == 'R':
                for pos in range(self.x + 1, self.x + distance + 1):
                    self.points.append('{}*{}'.format(pos, self.y))
                self.x += distance

    def count_junctions(self):
        # c = Counter(self.points)
        # for p in self.points:
        #     if c[p] > 1:
        #         self.junctions.append(p.split('*'))
        print()

    def print(self):
        max_x = 0
        min_x = 0
        max_y = 0
        min_y = 0
        for coordinates in self.points:
            coordinates = coordinates.split('*')
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            max_x = coordinates[0] if coordinates[0] > max_x else max_x
            max_y = coordinates[1] if coordinates[1] > max_y else max_y

            min_x = coordinates[0] if coordinates[0] < min_x else min_x
            min_y = coordinates[1] if coordinates[1] < min_y else min_y
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                if [x, y] == [0, 0]:
                    print('O', end='')
                elif [str(x), str(y)] in self.junctions:
                    print('X', end='')
                elif '{}*{}'.format(x, y) in self.points:
                    print('*', end='')
                else:
                    print('.', end='')
            print()

    def find_closest(self):
        closest = None
        for junction in self.junctions:
            x = abs(int(junction[0]))
            y = abs(int(junction[1]))
            print(x, y, x + y)
            distance = x + y
            if not closest or distance < closest:
                closest = distance
        return closest
