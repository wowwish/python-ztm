# A SECOND TEST FILE THAT IS A CLONE
# USE 'python -m unittest' FROM COMMAND-LINE TO RUN BOTH THIS CLONE AND THE ORIGINAL TEST FILE
# USE 'python -m unittest -v' FROM COMMAND-LINE FOR MORE INFO WHEN RUNNING TESTS INCLUDING PRINTING OF DOCSTRINGS
# FROM THE TESTS


from multiprocessing.sharedctypes import Value
import unittest

# Import the file/module to be tested or a particular set of functions from the file/module
import testme

# create a class inheriting 'unittest.TestCase' class as parent
# CODE READABILITY IS MORE IMPORTANT THAN REPETITION OF CODE IN TESTS
# TEST METHOD NAMES MUST BE UNIQUE WITHIN THE CLASS
class TestMain(unittest.TestCase):
    # method to test - will be successful
    def test_do_stuff(self):
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


if __name__ == '__main__': # Run the tests only when this file is the main file being run.
    # We don't want to import any code from this test file into a source file or other test files.
    # Test files should be treated as individual files for each module.
    #######################################################################################################################
   # HOWEVER, YOU CAN RUN ALL TEST FILES IN CURRENT DIRECTORY SIMULTANEOUSLY USING 'python -m unittest' FROM COMMAND LINE  #
    #######################################################################################################################
    unittest.main() # This statement is used to invoke all tests declared within this file when this script is run
    # Run this entire test file using 'python testing.py' from command-line