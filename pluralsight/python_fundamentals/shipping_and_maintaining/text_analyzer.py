__author__ = 'ralph'

import os
import unittest


def analyze_text(filename):
    """Calculate the number of lines and characters in a file.

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If ``filename`` does not exist or cant't be read.

    Returns: The number of lines in the file.
    """
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

class TextAnalysisTests(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        """Fixture that creates a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great ware.\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:  # Assumes that any failure is acceptable becuase just trying to remove file
            pass

    def test_function_runs(self):  # simple start with test_ as these are auto discovered
        """Basic smoke test: does the function run."""
        # Will fail if it throws any exceptions
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that the line count is correct."""
        self.assertEqual(analyze_text(self.filename), 4)

    def test_character_count(self):
        """Check that the character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1], 131)

if __name__ == '__main__':
    unittest.main()