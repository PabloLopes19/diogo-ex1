from ex2 import calc_data

def test_ex2():
    data1 = "01/01/2024"
    data2 = "10/01/2024"

    data3 = "15/01/2024"
    data4 = "16/01/2024"

    data5 = "20/01/2024"
    data6 = "24/01/2024"

    assert calc_data(data1, data2) == 9
    assert calc_data(data3, data4) == 1
    assert calc_data(data5, data6) == 4
