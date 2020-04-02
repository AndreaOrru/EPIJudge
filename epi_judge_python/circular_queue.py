from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self.array = [None] * capacity
        self.head = self.tail = self.n_elements = 0

    def enqueue(self, x: int) -> None:
        self._resize()

        self.array[self.tail] = x
        self.tail = (self.tail + 1) % len(self.array)
        self.n_elements += 1

    def dequeue(self) -> int:
        if self.n_elements == 0:
            raise Exception('No more elements')

        x = self.array[self.head]
        self.head = (self.head + 1) % len(self.array)
        self.n_elements -= 1
        return x

    def size(self) -> int:
        return self.n_elements

    def _resize(self) -> None:
        if self.n_elements < len(self.array):
            return

        self.array = self.array[self.head:] + self.array[:self.head]
        self.array += [None] * ((len(self.array) * self.SCALE_FACTOR) -
                                 len(self.array))
        self.head, self.tail = 0, self.n_elements


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
