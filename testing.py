# Testing Companion code file for 'testme.py'

# Testing - Individual units of source code are checked to see if they work properly
# A test in python is just another code file that accompanies the main code
# For example, If you develop 100 python modules (.py files that are importable), you will have 100 test files 
# corresponding to each module
# The test code is run before releasing a module to production to make sure it works properly
# Customers will never see the testing files


# SIMPLE MISTAKES AND STYLING ISSUES CHECK
# pylint
# pyflakes
# AutoPEP8 - style guide check

# TESTING IS A HIGHER LEVEL UP TO THESE TESTS

# Python has the 'unittest' built-in module to test code
import unittest

# Import the file/module to be tested or a particular set of functions from the file/module
import testme

# create a class inheriting 'unittest.TestCase' class as parent
# CODE READABILITY IS MORE IMPORTANT THAN REPETITION OF CODE IN TESTS
# TEST METHOD NAMES MUST BE UNIQUE WITHIN THE CLASS
class TestMain(unittest.TestCase):
    # built-in method from unittest
    def setUp(self):
        # The code there is run before each of the individual test methods are invoked
        # Hence, this setup can be used to set-up some default variables and other pre-test setup
        print('about to run a test!')
    # method to test - will be successful
    def test_do_stuff(self):
        # Docstring
        '''
        HIIII!!!!!
        '''
        test_param = 10
        result = testme.do_stuff(test_param)
        # method specific to the 'unittest.TestCase' class
        self.assertEqual(result, 15)
    # Your source code should be able to gracefull handle errors to prevent errors in testing
    # We want errors in source code to trigger the AssertionError from this test file rather than triggering
    # its own errors from the source file and propagating it to the test.
    def test_error(self): # Improve our function by Breaking it!
        test_param = 'wqefa'
        result = testme.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError)) # Check if the argument is True
        self.assertIsInstance(result, ValueError) # Check if the result is an object of class 'ValueError'
        # Errors raised by the source code will be instances of the corresponding error Classes and not equal
        # the Error Class themselves.
    # def test_failure(self):
    #     test_param = 11
    #     result = testme.do_stuff(test_param)
    #     self.assertEqual(result, 15) # This test fails
    def test_do_stuff_none(self):
        test_param = None
        result = testme.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    def test_do_stuff_empty(self):
        test_param = ''
        result = testme.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    # Another built-in method from unittest that is used for clean-up post testing methods
    def tearDown(self):
        print('cleaning up!')


if __name__ == '__main__': # Run the tests only when this file is the main file being run.
    # We don't want to import any code from this test file into a source file or other test files.
    # Test files should be treated as individual files for each module.
    #######################################################################################################################
   # HOWEVER, YOU CAN RUN ALL TEST FILES IN CURRENT DIRECTORY SIMULTANEOUSLY USING 'python -m unittest' FROM COMMAND LINE  #
    #######################################################################################################################
    unittest.main() # This statement is used to invoke all tests declared within this file when this script is run
    # Run this entire test file using 'python testing.py' from command-line

# USE 'python -m unittest' FROM COMMAND-LINE TO RUN BOTH THIS CLONE AND THE ORIGINAL TEST FILE
# USE 'python -m unittest -v' FROM COMMAND-LINE FOR MORE INFO WHEN RUNNING TESTS INCLUDING PRINTING OF DOCSTRINGS
# FROM THE TESTS