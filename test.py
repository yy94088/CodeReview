import unittest
import sys
from unittest.mock import patch
from io import StringIO


class TestSimpleUtilsVariables(unittest.TestCase):
    """Test suite for variable assignments in simple_utils module."""
    
    def test_variable_a_value(self):
        """Test that variable 'a' is assigned the correct value."""
        # We need to test without executing the division
        with patch('builtins.print'):
            import simple_utils
            self.assertEqual(simple_utils.a, 10)
    
    def test_variable_b_value(self):
        """Test that variable 'b' is assigned the correct value."""
        with patch('builtins.print'):
            import simple_utils
            self.assertEqual(simple_utils.b, 0)
    
    def test_variable_types(self):
        """Test that variables have the expected types."""
        with patch('builtins.print'):
            import simple_utils
            self.assertIsInstance(simple_utils.a, int)
            self.assertIsInstance(simple_utils.b, int)


class TestSimpleUtilsDivisionOperation(unittest.TestCase):
    """Test suite for the division operation in simple_utils module."""
    
    def test_division_raises_zero_division_error(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        a = 10
        b = 0
        with self.assertRaises(ZeroDivisionError):
            result = a / b
    
    def test_division_error_message(self):
        """Test the error message when dividing by zero."""
        a = 10
        b = 0
        try:
            result = a / b
            self.fail("Expected ZeroDivisionError was not raised")
        except ZeroDivisionError as e:
            # ZeroDivisionError message is typically "division by zero"
            self.assertIn("division", str(e).lower())
    
    def test_division_with_non_zero_divisor(self):
        """Test that division works correctly with non-zero divisor."""
        a = 10
        b = 2
        result = a / b
        self.assertEqual(result, 5.0)
    
    def test_division_with_negative_divisor(self):
        """Test division with negative divisor."""
        a = 10
        b = -2
        result = a / b
        self.assertEqual(result, -5.0)
    
    def test_division_result_type(self):
        """Test that division returns a float."""
        a = 10
        b = 3
        result = a / b
        self.assertIsInstance(result, float)
    
    def test_division_with_float_dividend(self):
        """Test division when dividend is a float."""
        a = 10.5
        b = 2
        result = a / b
        self.assertEqual(result, 5.25)
    
    def test_division_precision(self):
        """Test division precision with specific values."""
        a = 10
        b = 3
        result = a / b
        self.assertAlmostEqual(result, 3.333333, places=5)


class TestSimpleUtilsModuleImport(unittest.TestCase):
    """Test suite for importing and executing the simple_utils module."""
    
    @patch('builtins.print')
    def test_module_import_does_not_raise(self, mock_print):
        """Test that the module can be imported when print is mocked."""
        # Since print is mocked, the division won't be attempted to print
        try:
            import simple_utils
        except ZeroDivisionError:
            self.fail("Module import raised ZeroDivisionError even with mocked print")
    
    def test_module_execution_raises_zero_division_error(self):
        """Test that executing the module raises ZeroDivisionError."""
        # When the module is imported without mocking, it should raise an error
        with self.assertRaises(ZeroDivisionError):
            # Force reimport to trigger the division
            if 'simple_utils' in sys.modules:
                del sys.modules['simple_utils']
            import simple_utils


class TestSimpleUtilsEdgeCases(unittest.TestCase):
    """Test suite for edge cases related to the operations in simple_utils."""
    
    def test_division_by_very_small_number(self):
        """Test division by a very small but non-zero number."""
        a = 10
        b = 0.0000001
        result = a / b
        self.assertGreater(result, 1000000)
    
    def test_division_of_zero(self):
        """Test division when dividend is zero."""
        a = 0
        b = 10
        result = a / b
        self.assertEqual(result, 0.0)
    
    def test_division_with_large_numbers(self):
        """Test division with large numbers."""
        a = 10000000
        b = 2
        result = a / b
        self.assertEqual(result, 5000000.0)
    
    def test_integer_division_vs_float_division(self):
        """Test the difference between integer and float division."""
        a = 10
        b = 3
        float_result = a / b
        int_result = a // b
        self.assertNotEqual(float_result, int_result)
        self.assertEqual(int_result, 3)
        self.assertAlmostEqual(float_result, 3.333333, places=5)
    
    def test_modulo_operation_with_zero_divisor(self):
        """Test modulo operation raises error with zero divisor."""
        a = 10
        b = 0
        with self.assertRaises(ZeroDivisionError):
            result = a % b
    
    def test_floor_division_with_zero_divisor(self):
        """Test floor division raises error with zero divisor."""
        a = 10
        b = 0
        with self.assertRaises(ZeroDivisionError):
            result = a // b


class TestSimpleUtilsAlternativeImplementations(unittest.TestCase):
    """Test suite for alternative safe implementations."""
    
    def test_safe_division_with_try_except(self):
        """Test a safe division implementation using try-except."""
        def safe_divide(a, b):
            try:
                return a / b
            except ZeroDivisionError:
                return None
        
        self.assertIsNone(safe_divide(10, 0))
        self.assertEqual(safe_divide(10, 2), 5.0)
    
    def test_safe_division_with_conditional(self):
        """Test a safe division implementation using conditional check."""
        def safe_divide_conditional(a, b):
            if b == 0:
                return float('inf') if a > 0 else float('-inf') if a < 0 else 0
            return a / b
        
        result = safe_divide_conditional(10, 0)
        self.assertEqual(result, float('inf'))
        self.assertEqual(safe_divide_conditional(10, 2), 5.0)
    
    def test_safe_division_with_default_value(self):
        """Test a safe division implementation with default return value."""
        def safe_divide_default(a, b, default=0):
            try:
                return a / b
            except ZeroDivisionError:
                return default
        
        self.assertEqual(safe_divide_default(10, 0), 0)
        self.assertEqual(safe_divide_default(10, 0, default=-1), -1)
        self.assertEqual(safe_divide_default(10, 2), 5.0)


class TestSimpleUtilsNumericBoundaries(unittest.TestCase):
    """Test suite for numeric boundaries and special values."""
    
    def test_division_with_max_int(self):
        """Test division with maximum integer value."""
        a = sys.maxsize
        b = 2
        result = a / b
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
    
    def test_division_with_negative_zero(self):
        """Test division with negative zero (Python treats -0.0 == 0.0)."""
        a = 10
        b = -0.0
        with self.assertRaises(ZeroDivisionError):
            result = a / b
    
    def test_division_result_infinity(self):
        """Test that division by very small number approaches infinity."""
        a = 10
        b = 1e-308  # Very small number close to zero
        result = a / b
        self.assertIsInstance(result, float)
        self.assertGreater(result, 1e307)


if __name__ == '__main__':
    unittest.main()
