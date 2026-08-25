def union(a, b):
    return set(a) | set(b)


def intersection(a, b):
    return set(a) & set(b)


def difference(a, b):
    return set(a) - set(b)


def complement(a, universe):
    a, universe = set(a), set(universe)
    if not a <= universe:
        raise ValueError("The set must be a subset of the declared universe.")
    return universe - a


def cartesian_product(a, b):
    return {(x, y) for x in a for y in b}


def implies(p, q):
    return (not bool(p)) or bool(q)


def truth_table_2(operator):
    return [{"P": p, "Q": q, "result": bool(operator(p, q))}
            for p in (True, False) for q in (True, False)]


def relation_domain(relation):
    return {x for x, _ in relation}


def relation_range(relation):
    return {y for _, y in relation}


def is_function(relation, declared_domain=None):
    mapping = {}
    for x, y in relation:
        if x in mapping and mapping[x] != y:
            return False
        mapping[x] = y
    return declared_domain is None or set(mapping) == set(declared_domain)


def evaluate_predicate(records, predicate):
    return [record for record in records if predicate(record)]
