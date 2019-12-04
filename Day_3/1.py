from Day_3.map_maker import MapMaker

if __name__ == '__main__':
    # map = MapMaker()
    # with open('input.txt', 'r') as f:
    #     for cnt, line in enumerate(f):
    #         input = line.split(',')
    #         map.add_route(input)
    # map.count_junctions()
    # print()
    # print('Solution:', map.find_closest())




    map = MapMaker()
    map.add_route([i for i in 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')])
    map.add_route([i for i in 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')])
    map.count_junctions()
    print(map.junctions)
    # map.print()
    print('Solution:', map.find_closest())
    #
    map = MapMaker()
    map.add_route([i for i in 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')])
    map.add_route([i for i in 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')])
    map.count_junctions()
    print('Solution:', map.find_closest())
