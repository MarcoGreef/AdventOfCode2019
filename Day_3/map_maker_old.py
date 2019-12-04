class MapMaker:
    def __init__(self, map=None):
        self.map = map if map else ['O']

    def add_route(self, route: list):
        self.calculate_points()
        x = self.origin[0]
        y = self.origin[1]

        for i in route:
            direction = i[0]
            points = int(i[1:])

            if direction == 'R':
                if len(self.map[y]) < x + points:
                    for height in range(0, len(self.map)):
                        self.map[height] += ''.join(['.' for i in range(0, x + points - len(self.map[height]) + 1)])

                for z in range(x + 1, x + points + 1):
                    self.map[y][z] = '-' if self.map[y][z] == '.' else 'X'
                    x += 1
            # elif direction == 'U':
            #     if (y - points) < 0:
            #         for z in range(0, points - y):
            #             y += 1
            #             self.map.insert(0, [''.join(['.' for i in range(0, len(self.map[-1]))])])
            #
            #     for z in range(y - points, y):
            #         print(x, z)
            #         print(self.map[z])
            #         self.map[z][x] = '|' if self.map[z][x] == '.' else 'X'
                    # y -= 1
            # elif d == 'L':
            #     if (x - p) < 0:
            #         for z in range(0, -1 * (x - p)):
            #             for q in self.map:
            #                 q.insert(0, '.')
            #     for z in range(x - p, x):
            #         self.map[y][z] = '-' if self.map[y][z] == '.' else 'X'
            #         x -= 1
            # elif d == 'D':
            #     if len(self.map) < (x + p):
            #         for z in range(0, x + p - len(self.map)):
            #             self.map += [['.' for q in range(0, len(self.map[0]))]]
            #     for z in range(y + 1, y + p + 1):
            #         self.map[z][x] = '|' if self.map[z][x] == '.' else 'X'
            #         y += 1
            # self.map[y][x] = '+' if self.map[y][x] != 'X' else 'X'

    def print(self):
        for i in self.map:
            print(''.join(i))
        print('\n\n')

    def calculate_points(self):
        self.origin = [0, 0]
        self.crossings = []

        for y in range(0, len(self.map)):
            for x in range(0, len(self.map[0])):
                if self.map[y][x] == 'X':
                    self.crossings.append([x, y])
                if self.map[y][x] == 'O':
                    self.origin = [x, y]

    def calculate_distance(self):
        self.calculate_points()
        distances = []
        for cross in self.crossings:
            distances.append(abs(cross[0] - self.origin[0]) + abs(cross[1] - self.origin[1]))

        return min(distances)
