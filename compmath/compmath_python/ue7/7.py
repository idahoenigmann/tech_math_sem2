from collections import OrderedDict, Counter


def f_a(dictionary, new_elem):
    dictionary.update({new_elem[0]: new_elem[1]})
    dictionary.move_to_end(new_elem[0], last=False)


def f_b(l1, l2, l3):
    # & = intersection (see https://www.guru99.com/python-counter-collections-example.html#10)
    return list(e for e in (Counter(l1) & Counter(l2) & Counter(l3)).elements())


def f_c(dictionary):
    res = []
    for key, val in dictionary.items():
        lst = [key]
        for e in val:
            lst.append(e)
        res.append(lst)
    return res


def f_d(dictionary):        # works for depth 2
    res = {}
    for key_o, val_o in dictionary.items():
        for key_i, val_i in val_o.items():
            res[key_i] = {key_o: val_i}
    return res


if __name__ == "__main__":
    dictionary = OrderedDict(a=1, b=2)
    print(dictionary)
    f_a(dictionary, ('c', 3))
    print(dictionary)

    print(f_b([1, 5, 5], [3, 4, 5, 5, 10], [5, 5, 10, 20]))

    print(f_c({'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}))

    print(f_d({"a": {"b": {}}, "d": {"e": {}}, "f": {"g": {}}}))

    print(f_d({"a": {"b": {}, "c": {}}, "d": {"e": {}}, "f": {"g": {}}}))
