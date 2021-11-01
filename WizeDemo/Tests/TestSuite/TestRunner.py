import sys, os
import testtools as testtools
import HtmlTestRunner
sys.path.insert(1, '../../')

from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Scripts.test_Purchase import Swang_Purchase
from Tests.Scripts.test_MultipleItems import Swang_MultItems
from Tests.Scripts.test_LoginPage import Swang_LoginPage
from Tests.Scripts.test_NavigateHome import Swang_Navigate
from Tests.Scripts.test_InvalidLogin import Swang_InvalinLogin

if __name__ == "__main__":
 
    html_report_dir = ("../../Reports") 
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Swang_LoginPage),
        test_loader.loadTestsFromTestCase(Swang_Navigate),
        test_loader.loadTestsFromTestCase(Swang_InvalinLogin),
        test_loader.loadTestsFromTestCase(Swang_Purchase),
        test_loader.loadTestsFromTestCase(Swang_MultItems),
        ))
 
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    test_runner.run(test_suite)