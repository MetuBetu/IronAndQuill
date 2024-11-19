try:
    import pytest
except ImportError:
    os.system("pip install pytest")
    import pytest

assert 1 == 1
