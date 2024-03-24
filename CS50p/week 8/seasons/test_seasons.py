from datetime import datetime
from io import StringIO
import sys
from unittest.mock import patch
import pytest
from seasons import main

@pytest.mark.parametrize("input_date, expected_output", [
    ("2000-01-01", "Two million, one hundred eighty-nine thousand, six hundred minutes"),
    # Add more test cases as needed
])
def test_main(input_date, expected_output):
    with patch("builtins.input", return_value=input_date), patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        actual_output = mock_stdout.getvalue().strip()
        assert actual_output == f"{expected_output.capitalize()} minutes"

if __name__ == "__main__":
    pytest.main()
