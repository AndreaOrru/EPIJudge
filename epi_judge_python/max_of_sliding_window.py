import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


from collections import deque


class QueueMax:
    def __init__(self):
        self.queue = deque()
        self.maximums = deque()

    def enqueue(self, item):
        self.queue.append(item)
        while self.maximums and self.maximums[-1] < item:
            self.maximums.pop()
        self.maximums.append(item)

    def dequeue(self):
        item = self.queue.popleft()
        if self.maximums[0] == item:
            self.maximums.popleft()
        return item

    def head(self):
        return self.queue[0]

    def max(self):
        return self.maximums[0]


class TrafficElement:
    def __init__(self, time: int, volume: float) -> None:
        self.time = time
        self.volume = volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __eq__(self, other):
        return (self.time, self.volume) == (other.time, other.volume)


def calculate_traffic_volumes(A: List[TrafficElement],
                              w: int) -> List[TrafficElement]:
    A.sort(key=lambda t: t.time)
    sliding_window = QueueMax()
    maximum_volumes = []

    for traffic in A:
        sliding_window.enqueue(traffic)
        while traffic.time - sliding_window.head().time > w:
            sliding_window.dequeue()
        maximum_volumes.append(TrafficElement(traffic.time, sliding_window.max().volume))

    return maximum_volumes




###################################################################


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_of_sliding_window.py',
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
