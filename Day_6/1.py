if __name__ == '__main__':
    f = open('input.txt', 'r')
    input = f.read().split('\n')
    # input = 'COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L'
    holder = {}
    for i in input:
        holder[i.split(')')[1]] = i.split(')')[0]
    print(holder)

    counter = 0
    for start, end in holder.items():
        while True:
            result = holder[start]
            counter += 1
            if result == 'COM':
                break
            start = result

    print('Number of orbits is', counter)
