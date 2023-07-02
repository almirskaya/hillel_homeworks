def arrows_count(s):
    directions = ['^', 'v', '<', '>']
    counts = [s.count(d) for d in directions]
    max_count = max(counts)
    return len(s) - max_count


s1 = "^vv<v"
s2 = "v>>>vv"
s3 = "<<<"
if __name__ == '__main__':
    print(arrows_count(s1))

if __name__ == '__main__':
    print(arrows_count(s2))

if __name__ == '__main__':
    print(arrows_count(s3))
