"""Simple test to verify imports work"""

def test_imports():
    """Test that required libraries can be imported"""
    try:
        import pandas
        import numpy
        import matplotlib
        import sklearn
        print("All imports successful!")
        return True
    except ImportError as e:
        print(f"Import failed: {e}")
        return False


if __name__ == "__main__":
    test_imports()