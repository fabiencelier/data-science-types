from . import ndarray

def assert_allclose(
    actual: ndarray, desired: ndarray, rtol: float = 1e-7, atol: float = 0
) -> None: ...
def assert_array_equal(actual: ndarray, desired: ndarray) -> None: ...
