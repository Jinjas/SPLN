from ftk.freq import ratio
def test_ratio():
    f1 = [("a", 49.3), ("b", 78.4)]
    f2 = [("a", 49.3), ("b", 100.8)]

    x = ratio(f1,f2)
    assert x["a"] == 1