import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from scheduler import run_for_n_seconds

def test_schedule_run_for_n_seconds():
    t1 = run_for_n_seconds(2)
    t2 = run_for_n_seconds(3)
    print(t1)
    print(t2)
    assert t1 > 1
    assert t2 > 2