import collections


def String(x):
    d = collections.defaultdict(int)

    for c in str1:
        d[c] += 1

    for c in sorted(d, key=d.get, reverse=True):
        if d[c] > 1:
            print('%s %d ' % (c, d[c]))

str1 = "Betahasha dil me tujhko hi chaha hai tera "


String(str1)
