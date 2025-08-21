from microbench import MicroBench
import time

bench = MicroBench()

@bench
def slow_function(x):
    time.sleep(x)
    return x

slow_function(2)

# Dump the results - in a real example,
# we'd save the results to a file or Redis
# and retrieve them later
print(bench.get_results())
