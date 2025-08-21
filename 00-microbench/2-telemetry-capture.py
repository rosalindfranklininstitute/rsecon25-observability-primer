from microbench import MicroBench

class TelemetryBench(MicroBench):
    telemetry_interval = 1  # Every second

    @staticmethod
    def telemetry(process):
        # For values you can capture from "process",
        # see https://psutil.readthedocs.io/en/latest/#psutil.Process
        return {'cpu_percent': process.cpu_percent()}

bench = TelemetryBench()

@bench
def busy_work():
    for _ in range(5_000_000):
        _ = 123**456

busy_work()

# Dump the results - in a real example,
# we'd save the results to a file or Redis
# and retrieve them later
results = bench.get_results()
print(results.iloc[0].T)
print(results.iloc[0].loc['telemetry'])
