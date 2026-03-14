
import pytest

class TestInBuiltAssertionDemo:

    # 1. AssertEqual, AssertDictEqual, AssertListEqual
    # In pytest, we use the standard '==' for all of these.
    def test_equality_assertions(self):
        # Basic Equality
        assert 10 == 10
        
        # List Equality (pytest shows index-by-index diff on failure)
        assert [1, 2, 3] == [1, 2, 3]
        
        # Dictionary Equality (pytest shows key/value diff on failure)
        expected_user = {"name": "Gemini", "role": "AI"}
        actual_user = {"name": "Gemini", "role": "AI"}
        assert actual_user == expected_user

    # 2. Test Raise Exception Catch
    def test_exception_handling(self):
        def divide_by_zero():
            return 1 / 0

        # Ensures the block raises ZeroDivisionError
        with pytest.raises(ZeroDivisionError) as exc_info:
            divide_by_zero()
        
        # You can also verify the error message
        assert "division by zero" in str(exc_info.value)

    # 3. Parameterized Test
    # This runs the same test function 3 times with different inputs
    @pytest.mark.parametrize("num, den", [
        (10, 0),      # Test case 1
        (5, 1),     # Test case 2
        (10, 20),    # Test case 3
    ])
    def test_exception_handling_pameterized(self, num, den):

        def divide_by_zero(num, den):
            return num / den

        # Ensures the block raises ZeroDivisionError
        with pytest.raises(ZeroDivisionError) as exc_info:
            divide_by_zero(num, den)
        
        # You can also verify the error message
        assert "division by zero" in str(exc_info.value)


