w = 0
q = 0
sh = []
by = []
def calculate_structure_sum(b):
    global sh, by
    by = by * 0
    c = [dict(c) for c in b if isinstance(c, dict)]
    c = str(c)
    d = [(d) for d in b if isinstance(d, (str, int))]
    for i in range(len(d)):
        if isinstance(d[i], str):
            by = len(d[i])
        else:
            sh.append(d[i])
            global q
            q = sum(sh)
            sh = sh * 0
    global w
    w = w + sum([int(ui) for ui in c if ui.isdigit()]) + len(([c for c in str (c) if c.isalpha()])) +q+ by
    m = [m for m in b if isinstance(m, (set, tuple, list))]
    from itertools import chain
    m = list(chain.from_iterable(m))
    b = m
    if len(b) > 1:
        calculate_structure_sum(b)
    elif len(b) == 1:
        from itertools import chain
        b = list(chain.from_iterable(b))
        calculate_structure_sum(b)
    return w
print(calculate_structure_sum([[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]))
