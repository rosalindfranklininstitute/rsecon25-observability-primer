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
#
# Note: .T transposes the pandas dataframe,
# making it easier to read on the terminal
print(bench.get_results().T)
