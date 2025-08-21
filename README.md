# Observability: A Practical Primer for RSEs

A walkthrough at [RSECon25](https://rsecon25.society-rse.org/), a conference on [Research Software Engineering](https://society-rse.org/about/).

## Learning objectives

By the end of this walkthrough, participants should understand what observability is, where it can and should be used, and how to implement it within their own code for simple problems.

## Audience and scope

This walkthrough is designed as an initial primer rather than to be fully comprehensive. It's targetted as research software engineers (RSEs), and therefore is more tailored to research computing workloads (e.g. batch and cloud) rather than large enterprise use cases, although hopefully the introductory nature of the material is beneficial for a general audience.

## What is observability?

Observability refers to the ability to understand the internal state of software and computer systems via event-driven outputs such as logs, metrics and traces.

Use cases include:

- Troubleshooting - detecting and diagnosing issues with software and digital infrastructure
- Performance monitoring - identifying speed issues such as high latency or memory usage spikes, which can help with optimisation and capacity planning
- Security - detecting unusual usage patterns, and allowing audit after a cybersecurity event
- Analytics - understanding how software/digital resources are used to focus future development efforts

## What factors affect the cost/benefit of observability?

Most computational workloads can benefit from at least a basic level of observability, and you can always start with a simple approach as we'll soon see. However, the benefits of observability increase when any of the following factors apply:

- Complexity - in general, more complex systems have more ways they can go wrong, and are harder and more costly (time and/or financial cost) to debug when they do
- Remote workloads - i.e. software running on remote servers, cloud, high-performance compute (HPC) clusters or distributed systems, since these workloads are often running for a long time, can have differences from development environments, and may encounter issues that are difficult to reproduce without sufficient context
- High reliability/assurance environments - if there's a need for high uptime, security, or (in scientific contexts) reproducibility, being able to both spot potential issues early, and have audit capabilities when things go wrong, is valuable

## What types of workload can benefit from observability?

In line with the factors discussed above, this walkthrough will focus on two of the most prominent use cases for observability:

- Batch/HPC - software which runs as jobs or pipelines, including workload managers like [SLURM](https://slurm.schedmd.com/) or jobs run on workflow managers such as [Apache Airflow](https://airflow.apache.org/), [Argo Workflows](https://argoproj.github.io/workflows/) or field-specific tools such as [Snakemake](https://snakemake.readthedocs.io/en/stable/) or [Nextflow](https://www.nextflow.io/) in Bioinformatics. See the [separate README](Observability-for-batch-workloads.md) for this use case.
- Cloud - network-accessible software, such as web sites/apps, [REST APIs](https://www.ibm.com/think/topics/rest-apis), or server software.

There are often different considerations and tooling for observability in these two environments, which we'll cover as we move along.

## What types of outputs are used for observability?

### Logs

Logs are records of notable events within a system, which are usually timestamped and often have a severity level attached, such as "warning" or "error". They may have other context such as the active user in the case of multi-user software.

### Metrics

Metrics are readouts of a system's state, which are often (but not always) numerical values. These are usually continually varying, such as memory usage throughout a program's lifetime or the availability (uptime) of a network service, but for batch workloads, terminal values are often captured as well, such as number of files processed, or job runtime.

### Traces

Traces show the path taken by a request or a single run of a piece of software. For a standalone piece of software, this will usually consist of a set of function calls. For example, when a Python program crashes, you'll see a [traceback](https://www.pythonmorsels.com/reading-tracebacks-in-python/). For networked software, traces show how each pieces of software invokes another, which might be a REST API call or a remote procedure call. This is particularly valuable where lots of smaller networked services interact, as is the case with [microservices](https://en.wikipedia.org/wiki/Microservices).

## Tools

For batch workloads, see [Observability for batch workloads](Observability-for-batch-workloads.md).

For cloud and other workloads, see [awesome-observability](https://github.com/adriannovegil/awesome-observability) for best practices and a list of tools.
