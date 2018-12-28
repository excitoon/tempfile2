import os
import unittest

import tempfile2


class test_tempfile2(unittest.TestCase):
    def test_delete_and_close(self):
        with tempfile2.NamedTemporaryFile(delete=True, close=True) as temp_file:
            self.assertTrue(temp_file.closed)
            self.assertTrue(os.path.isfile(temp_file.name))
        self.assertTrue(temp_file.closed)
        self.assertFalse(os.path.isfile(temp_file.name))

    def test_not_delete_and_close(self):
        with tempfile2.NamedTemporaryFile(delete=False, close=True) as temp_file:
            self.assertTrue(temp_file.closed)
            self.assertTrue(os.path.isfile(temp_file.name))
        self.assertTrue(temp_file.closed)
        self.assertTrue(os.path.isfile(temp_file.name))
        os.unlink(temp_file.name)

    def test_delete_and_not_close(self):
        with tempfile2.NamedTemporaryFile(delete=True, close=False) as temp_file:
            self.assertFalse(temp_file.closed)
            self.assertTrue(os.path.isfile(temp_file.name))
        self.assertTrue(temp_file.closed)
        self.assertFalse(os.path.isfile(temp_file.name))

    def test_not_delete_and_not_close(self):
        with tempfile2.NamedTemporaryFile(delete=False, close=False) as temp_file:
            self.assertFalse(temp_file.closed)
            self.assertTrue(os.path.isfile(temp_file.name))
        self.assertTrue(temp_file.closed)
        self.assertTrue(os.path.isfile(temp_file.name))
        os.unlink(temp_file.name)
