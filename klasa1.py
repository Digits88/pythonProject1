ndryshore1 = "test"


def metodaTest():
    # print("test")
    return "test"


class TestClass:
    """
    Kjo eshte nje klas test per te krijuar nje objekt.
    """
    ndryshore2 = "test2"

    var2 = metodaTest()

    def metodaTest2(self):
        """
        kjo eshte nje metode
        :return:
        """
        print("test2")
        return self


objektTest = TestClass()
print(objektTest.var2)

