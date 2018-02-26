from task_4 import selectionsort
from task_4 import selectionsort


def test_selectionsort():
    assert selectionsort([2, -1, 0, 5, 3, -1, 2]) == [ -1, -1, 0, 2, 2, 3, 5], "Test failed should be [0, -1, -1, 2, 2, 3, 5]"
    assert selectionsort([0, -1, 3, 5, -1, -1, 2]) == [ -1, -1, -1, 0 , 2, 3, 5], "Test failed should be 0, -1, -1, -1, 2, 3, 5]"
    return


if __name__ == '__main__':
    test_selectionsort()
    print("All tests passing ... ")
