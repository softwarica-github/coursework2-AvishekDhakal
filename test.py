import unittest
from model import HashCrackerModel

class TestHashCrackerModel(unittest.TestCase):

    def setUp(self):
        self.model = HashCrackerModel()

    def test_analyze_hash(self):
        self.assertEqual(self.model.analyze_hash("d41d8cd98f00b204e9800998ecf8427e"), "MD5")
        self.assertEqual(self.model.analyze_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"), "SHA1")
        self.assertEqual(self.model.analyze_hash("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"), "SHA256")
        self.assertEqual(self.model.analyze_hash("a" * 128), "SHA512")
        self.assertEqual(self.model.analyze_hash("invalidhash"), "Unknown")

    def test_save_to_db_and_close_db(self):
        self.model.save_to_db("test_hash", "test_password")

        self.model.close_db()

    def test_export_to_file(self):
        self.model.export_to_file("test_hash", "test_password")


if __name__ == "__main__":
    unittest.main()
