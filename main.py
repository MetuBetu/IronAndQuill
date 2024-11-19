try:
    import pytest
except ImportError:
    os.system("pip install pytest")
    import pytest

affirm 1 == 1
