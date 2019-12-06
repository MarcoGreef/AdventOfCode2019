def find_roots(current, holder):
    target = holder[current]
    data = [k for k, v in holder.items() if v == target] + [holder[target]]
    data.remove(current)
    return data


def check_trace(orbits, holder):
    for orbit in orbits:
        if 'SAN' in find_roots(orbit, holder):
            return True
    return False


if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split('\n')

    # input = 'COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN'.split(',')
    holder = {}
    for i in input:
        holder[i.split(')')[1]] = i.split(')')[0]
    print(holder)

    route_san = None
    route_you = None
    for start, end in holder.items():
        current_route = [start]
        while True:
            result = holder[start]
            current_route.append(result)
            if result == 'COM':
                if current_route[0] == 'SAN':
                    route_san = current_route
                elif current_route[0] == 'YOU':
                    route_you = current_route
                break
            start = result
    for point in route_you:
        if point in route_san:
            print('Result:', route_you.index(point) + route_san.index(point) - 2)
            break


