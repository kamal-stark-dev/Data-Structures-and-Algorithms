# Usage: pytest test_contains_duplicate.py 
# Requirements: pytest (pip-installable)

import pytest 
from contains_duplicate import Solution

solution = Solution()

# def test_duplicates_exist():
#     assert solution.contains_duplicate([1, 2, 3, 1])
#
# def test_no_duplicates():
#     assert not solution.contains_duplicate([1, 2, 3, 4])
#
# def test_empty():
#     assert not solution.contains_duplicate([])
#
# def test_single():
#     assert not solution.contains_duplicate([5])

# instead of creating function for each test case pytest let's you do this
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1], False),
        ([], False),
        ([1, 1, 1, 3, 3, 4, 3, 2], True)
    ],
)
def test_contains_duplicate(nums, expected):
    assert solution.contains_duplicate(nums) == expected
