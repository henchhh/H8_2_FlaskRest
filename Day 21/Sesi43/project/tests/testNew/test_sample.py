def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_my_stuff(benchmark):
    result = benchmark(test_sum)
    assert result == 123
    