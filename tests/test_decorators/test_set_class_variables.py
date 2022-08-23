# -*- coding:utf-8 -*-
# @FileName :test_set_class_variables.py
# @Author   :Deyu He
# @Time     :2022/8/23 11:35

from unittest import TestCase

from pyutils.decorators import set_class_variables


class TestSetClassVariables(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_set_class_variables(self):
        m, n = 100, 50
        a, b = 3, 5

        @set_class_variables(variable_dict=dict(m=m, n=n))
        class TestClass1(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        assert TestClass1.m == m
        assert TestClass1.n == n
        assert TestClass1.__name__ == "TestClass1"

        tc1 = TestClass1(a, b)
        assert tc1.a == a
        assert tc1.b == b
        assert tc1.m == m
        assert tc1.n == n

        @set_class_variables(variable_dict=dict(m=m, n=n))
        class TestClass2(object):
            m = 1
            n = 0

            def __init__(self, a, b):
                self.a = a
                self.b = b

        assert TestClass2.m == m
        assert TestClass2.n == n

        @set_class_variables(variable_dict=dict(m=m, n=n), force=False)
        class TestClass3(object):
            m = 1
            n = 0

            def __init__(self, a, b):
                self.a = a
                self.b = b

        assert TestClass3.m == 1
        assert TestClass3.n == 0
