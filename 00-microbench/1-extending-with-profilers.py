from microbench import MicroBench, MBLineProfiler, MBHostInfo, MBPythonVersion

class MyBench(MicroBench, MBLineProfiler, MBHostInfo, MBPythonVersion):
    pass

bench = MyBench()

@bench
def compute(n):
    squares = [i**2 for i in range(n)]
    return sum(squares)

compute(1_000_000)

# Dump the results - in a real example,
# we'd save the results to a file or Redis
# and retrieve them later
results = bench.get_results()
print(results.iloc[0].T)

# Print the line profiler report
MBLineProfiler.print_line_profile(
    results['line_profiler'][0])
