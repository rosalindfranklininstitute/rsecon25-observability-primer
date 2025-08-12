## Observability for batch workloads

### Planning

What logs, metrics, tools do you need to capture relevant metadata and outputs?

### Tools

- A logging library/framework for your code
    - [Python's logging module](https://docs.python.org/3/library/logging.html)
    - [Go's log module](https://gobyexample.com/logging)
    - [Java's java.util.logging](https://blog.sentry.io/a-guide-to-logging-and-debugging-in-java/)
    - JavaScript's `console.log` or [one of node.js's logging frameworks](https://engineering.deptagency.com/in-praise-of-logging-a-node-js-javascript-logging-guide)
    - [C++'s spdlog](https://github.com/gabime/spdlog)

- Metrics


- Traces
    - In simple cases, dumping tracebacks into logs may be sufficient
    - For multi-user systems like web apps, a monitoring system like [Sentry](https://sentry.io/welcome/) can provide a simple overview of logs and tracebacks, if your main concern is error handling
    - For complex cases like complex distributed computational/data pipelines, a full distributed tracing system like [Jaeger](https://www.jaegertracing.io/) can be used
