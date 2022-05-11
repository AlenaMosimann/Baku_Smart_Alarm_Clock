from baku.read_data.from_mi import summ


def test_summ():
    result = summ(2,3)
    expected = 5
    assert result == expected
