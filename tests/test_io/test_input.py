import unittest
import os
import pandas as pd
from app.io.input import read_from_file,read_from_file_with_pandas


class TestInputFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with test data for testing
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, 'w') as file:
            file.write("Test data\nfor\nfile\nreading")

        # Create a temporary CSV file with test data for pandas testing
        self.test_csv_file_path = "test_csv_file.csv"
        with open(self.test_csv_file_path, 'w') as file:
            file.write("Name,Age,Gender\nJohn,25,Male\nAlice,30,Female\nBob,28,Male\nEmma,35,Female")

    def tearDown(self):
        # Clean up temporary files after each test
        os.remove(self.test_file_path)
        os.remove(self.test_csv_file_path)

    def test_read_from_file_existing_file(self):
        # Test reading from an existing text file
        expected_output = "Test data\nfor\nfile\nreading"
        self.assertEqual(read_from_file(self.test_file_path), expected_output)

    def test_read_from_file_empty_file(self):
        # Test reading from an empty text file
        empty_file_path = "empty_file.txt"
        with open(empty_file_path, 'w') as file:
            pass
        self.assertEqual(read_from_file(empty_file_path), "")

    def test_read_from_file_nonexistent_file(self):
        # Test reading from a non-existent text file
        non_existent_file_path = "non_existent_file.txt"
        with self.assertRaises(FileNotFoundError):
            read_from_file(non_existent_file_path)

    def test_read_from_file_with_pandas_existing_file(self):
        # Test reading from an existing CSV file using pandas
        expected_output = pd.DataFrame({
            "Name": ["John", "Alice", "Bob", "Emma"],
            "Age": [25, 30, 28, 35],
            "Gender": ["Male", "Female", "Male", "Female"]
        })
        pd.testing.assert_frame_equal(read_from_file_with_pandas(self.test_csv_file_path), expected_output)

    def test_read_from_file_with_pandas_empty_file(self):
        # Test reading from an empty CSV file using pandas
        empty_csv_file_path = "empty_csv_file.csv"
        # Create an empty CSV file with headers
        with open(empty_csv_file_path, 'w') as file:
            file.write("Name,Age,Gender\n")
        # Create an empty DataFrame
        expected_output = pd.DataFrame(columns=["Name", "Age", "Gender"])
        # Call the function and compare the result with the expected output
        pd.testing.assert_frame_equal(read_from_file_with_pandas(empty_csv_file_path), expected_output)

    def test_read_from_file_with_pandas_nonexistent_file(self):
        # Test reading from a non-existent CSV file using pandas
        non_existent_csv_file_path = "non_existent_csv_file.csv"
        with self.assertRaises(FileNotFoundError):
            read_from_file_with_pandas(non_existent_csv_file_path)


if __name__ == '__main__':
    unittest.main()
