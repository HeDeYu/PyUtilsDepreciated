# -*- coding:utf-8 -*-
# @FileName :test_set_member_variables.py
# @Author   :Deyu He
# @Time     :2022/8/23 11:16

from unittest import TestCase

from pyutils.decorators import set_member_variables


class TestSetMemberVariables(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_set_member_variables(self):
        m, n = 100, 50
        a, b = 3, 5

        @set_member_variables(variable_dict=dict(m=m, n=n))
        class TestClass1(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        tc1 = TestClass1(a, b)
        assert not hasattr(TestClass1, "m")
        assert tc1.a == a
        assert tc1.b == b
        assert tc1.m == m
        assert tc1.n == n

        @set_member_variables(variable_dict=dict(a=m, b=n, m=m, n=n))
        class TestClass2(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        tc2 = TestClass2(a, b)
        assert tc2.a == m
        assert tc2.b == n
        assert tc2.m == m
        assert tc2.n == n

        @set_member_variables(variable_dict=dict(a=m, b=n, m=m, n=n), force=False)
        class TestClass3(object):
            def __init__(self, a, b):
                self.a = a
                self.b = b

        tc3 = TestClass3(a, b)
        assert tc3.a == a
        assert tc3.b == b
        assert tc3.m == m
        assert tc3.n == n
