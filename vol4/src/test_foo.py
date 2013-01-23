# -*- coding:utf-8 -*-
import unittest
import mock

import app.foo as foo


class FooTest(unittest.TestCase):
    def _callFUT(self, x):
        return foo.sample(x)

    def test(self):
        result = self._callFUT(2)
        self.assertEqual(result, 20)

    def test_with_mock(self):
        with mock.patch("app.foo.sample") as M:
            M.return_value = "A string."
            self.assertNotEqual(self._callFUT(2), 20)
        self.assertEqual(self._callFUT(2), 20)


class Sample2Test(unittest.TestCase):
    def _callFUT(self, x):
        return foo.sample2(x)

    def test(self):
        result = self._callFUT(2)
        self.assertEqual(result, 30)

    def test_with_mock(self):
        with mock.patch("app.foo.sample") as M:
            M.side_effect = IndexError
            self.assertRaises(ValueError, self._callFUT, 2)


class EMailTest(unittest.TestCase):
    def _makeOne(self):
        return foo.EMail()

    def test(self):
        email = self._makeOne()
        self.assertNotEqual(email.send(*range(6))["sent"], None)

    def test_with_mock(self):
        email = self._makeOne()
        with mock.patch.object(email, "sending_at") as M:
            M.return_value = None
            self.assertEqual(email.send(*range(6))["sent"], None)
        self.assertNotEqual(email.send(*range(6))["sent"], None)

    @unittest.skip("Failure example.")
    def test_with_mock2(self):
        with mock.patch("app.foo.EMail") as M:
            M.return_value.sending_at.return_value = None
            email = self._makeOne()
            # AssertionError:
            #   <MagicMock name='EMail().send().__getitem__()'
            #       id='3071979372'> != None
            self.assertEqual(email.send(*range(6))["sent"], None)
        self.assertNotEqual(email.send(*range(6))["sent"], None)

    def test_with_mock3(self):
        with mock.patch.object(foo.EMail, "sending_at") as M:
            M.return_value = None
            email = self._makeOne()
            self.assertEqual(email.send(*range(6))["sent"], None)
        self.assertNotEqual(email.send(*range(6))["sent"], None)
