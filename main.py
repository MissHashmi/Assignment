"""Runs all the test: $ python main.py"""

# Standard library
import pytest

# Third-party
import HTMLTestRunner

# First-party
from testCases.login_testcases import TestLogin
from testCases.PIM_testcases import Test_PIM


def test_suite():
    """
    Function to create Test Suite from Unit-Tests
    :return:
    """
    test1 = pytest.TestReport.loadTestsFromTestCase(TestLogin)
    test2 = pytest.TestLoader().loadTestsFromTestCase(Test_PIM)
    suite = pytest.TestSuite([test1, test2])
    runner = HTMLTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output="outfile.html",
        title="Test report",
        report_name="report",
        open_in_browser=True,
        description="HTMLTestReport",
    )
    runner.run(suite)


if __name__ == "__main__":
    test_suite()
