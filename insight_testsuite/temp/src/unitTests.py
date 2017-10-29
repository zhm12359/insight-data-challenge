import unittest
from Helper import process_line, median
from Entity import Entity

class HelperTestCase(unittest.TestCase):
    """Tests for `Helper.py` methods."""

    def test_process_line(self):
        """test_can_process_line."""
        line = "C00629618|N|TER|P|201701230300133512|15C|IND|PEREZ, JOHN A|LOS ANGELES|CA|90017|PRINCIPAL|DOUBLE NICKEL ADVISORS|01032017|40|H6CA34245|SA01251735122|1141239|||2012520171368850783"
        ret = process_line(line)
        self.assertEqual("C00629618", ret["cmte_id"])
        self.assertEqual("90017", ret["zip_code"])
        self.assertEqual("01032017", ret["transaction_date"])
        self.assertEqual("40", ret["transaction_amount"])
        self.assertEqual("H6CA34245", ret["other_id"])

    def test_median(self):
        """test_median."""
        self.assertEqual(median([1, 1, 2, 4]), 2)
        self.assertEqual(median([0, 0, 0, 0, 4, 4, 6, 8]), 2)
        self.assertEqual(median([0, 2, 5, 6, 8, 9, 9]), 6)
        self.assertEqual(median([1]), 1)

class EntityTestCase(unittest.TestCase):
    """Tests for `process_line`."""

    def test_validate_to_be_true(self):
        """test_validate_other_id_be_true."""
        ret = Entity("C00177436","300047357","01312017","384", "")
        self.assertTrue(ret.validate())

    def test_validate_to_be_false(self):
        """test_validate_other_id_be_false."""
        ret = Entity("C00177436","300047357","01312017","384", "H6CA34245")
        self.assertFalse(ret.validate())
        ret = Entity("C00177436","300047357","01312017","", "")
        self.assertFalse(ret.validate())
        ret = Entity("","300047357","01312017","384", "")
        self.assertFalse(ret.validate())

    def test_validate_zip_code_to_be_true(self):
        """test_zip_code_is_5_digits."""
        ret = Entity("C00177436","300047357","01312017","384", "")
        self.assertTrue(ret.validate_zip_code())

    def test_validate_zip_code_to_be_false(self):
        """test_zip_code_is_5_digits."""
        ret = Entity("C00177436","300","01312017","384", "")
        self.assertFalse(ret.validate_zip_code())

    def test_validate_date_to_be_true(self):
        """test_date_is_convertable."""
        ret = Entity("C00177436","300","01312017","384", "")
        self.assertTrue(ret.validate_date())

    def test_validate_date_to_be_false(self):
        """test_date_is_convertable."""
        ret = Entity("C00177436","300","01312","384", "")
        self.assertFalse(ret.validate_date())

if __name__ == '__main__':
    unittest.main()
