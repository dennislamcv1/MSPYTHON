# CODE SHOULD NOT BE MODIFIED

import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Set app in testing mode
    with app.test_client() as client:
        yield client

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Add a section to the terminal summary reporting passing tests.
    """
    try:
        import pytest_mock  # Try importing pytest-mock
    except ImportError:
        terminalreporter.write_line("WARNING: pytest-mock is not installed. "
                                   "Please install it using `pip install pytest-mock` "
                                   "to enable all test functionality.",
                                   red=True, bold=True)

    terminalreporter.write_sep("=", "PASSING TESTS")
    for rep in terminalreporter.stats.get('passed', []):
        terminalreporter.write_line(f"{rep.nodeid} {rep.when}")