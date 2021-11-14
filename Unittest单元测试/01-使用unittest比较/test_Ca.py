from calculator import Calculator


def test_add():
    c=Calculator(3,5)
    result= c.add()
    assert result==8,'加法计算失败'
def test_sub():
    c=Calculator(5,3)
    result= c.sub()
    assert result==2,'减法计算失败'
test_sub()


if __name__ == '__main__':
    test_add()
    test_sub()

