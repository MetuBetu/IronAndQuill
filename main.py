import os
try:
    import pytest
except ImportError:
    os.system("pip install pytest")
    import pytest

def testofthetesting():
    assert 1 == 1
