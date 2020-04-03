import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    E = []
    for event in A:
        E.append(Endpoint(event.start, True))
        E.append(Endpoint(event.finish, False))
    E.sort(key=lambda e: (e.time, not e.is_start))

    curr_simul = max_simul = 0
    for e in E:
        curr_simul += 1 if e.is_start else -1
        max_simul = max(max_simul, curr_simul)

    return max_simul


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
