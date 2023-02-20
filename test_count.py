import count


def test_count_zeros():
    assert count.counter.count([0, 0, 0], 0) == 3


def test_count_string():
    assert count.counter.count(["a", "a", "a"], "a") == 3


def test_count_string2():
    assert count.counter.count(["Aidan", "Aidan", "Aidan", "Aidan", "Aidan"], "Aidan") == 5


def test_count_minus():
    assert count.counter.count([-1, -3, -5, -4], -1) == 1


def test_count_normal_num():
    assert count.counter.count([1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1], 1) == 2
