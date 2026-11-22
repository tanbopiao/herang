"""合壤（HERANG）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_resolve_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.resolve(None)

    def test_converge_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.converge(None)


if __name__ == "__main__":
    unittest.main()
