"""合壤（HERANG）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from herang import Herang


class TestHerang(unittest.TestCase):
    def setUp(self):
        self.op = Herang()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "herang")
        self.assertEqual(d["code"], "HERANG")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_resolve(self):
        plan = self.op.resolve([{"key": "k", "versions": [1, 1, 2]}])
        self.assertEqual(plan[0]["resolved"], 1)
        self.assertTrue(plan[0]["quorum"])

    def test_converge(self):
        merged = self.op.converge([{"a": 1, "b": 2}, {"a": 1, "b": 3}, {"a": 1, "b": 3}])
        self.assertEqual(merged, {"a": 1, "b": 3})
        with self.assertRaises(ValueError):
            self.op.converge([])


if __name__ == "__main__":
    unittest.main()
