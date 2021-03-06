Solution
========

The solution is done in pure Python (version 3.6 or superior).

I opted to use a min-heap datastructure in [`heapq`](https://docs.python.org/3.0/library/heapq.html) to take advantage of `O(log <heap size>)` insertion. 

A simpler solution would be to use peekable-iterators from [`more-itertools`](https://pypi.org/project/more-itertools/), but the challenge explicitly said to create a class.

In `02_output.txt` the final printed average had no decimal places (`22` instead of `22.0`), so I manually added the zero. I also added additional tests in `tests/{03,04}_*` and `tests.py`.

Overall, it took a bit over 30 minutes to complete.

Exercise summary
================

Combine multiple multiple ordered streams into a single ordered stream.

You may use any resources, programming languages, platforms, or frameworks to fulfill the exercise. Put all the code into a single git repository. The exercise should not take more than an hour or so, so scope the level of effort to that amount of time. We will use the code as the basis of a technical discussion later.

Exercise detail
===============

Assume you have n stream instances which have the following methods available:

- `peek()` returns the next available record or null/undefined/None if the stream is empty, but does not remove that record from the underlying queue. This method is idempotent.
- `next()` returns the next available record and removes it from the underlying queue. This method is not idempotent.

The records returned by these stream instances are JSON objects (or their equivalent in whatever language you choose) with the following fields:

- `timestamp` an non-negative integer
- `value` some arbitrary integer

Within each stream instance, `timestamp` is monotonically increasing. The `timestamp` value will always be equal to or greater than the `timestamp` value of the previous record emitted by a call to `next()`. Once a stream is empty, it's done and will never produce any further records.

Create a class that implements `peek()` and `next()` as described above; it must accept an arbitrary number of streams when instantiated.

Finally, create a method that will read from the given streams and will:
- print the values of the `timestamp` and `value` fields from the input streams in timestamp-order
- every 5 records, print the count, sum, and average value of all the records consumed so far
- if/when the streams are all exhausted, print the final count, sum, and average values of all the records consumed.

For example, if there are 2 input streams which contain data  `[{timestamp: 0, value: 10}, {timestamp: 2, value: 12}]` and `[{timestamp: 1, value:11}, {timestamp: 2, value: 13}]`, the output would be:

    timestamp: 0, value: 10
    timestamp: 1, value: 11
    timestamp: 2, value: 12
    timestamp: 2, value: 13
    count: 4, sum: 46, avg: 11.5

Testing
=======

For convenience, a very simple test harness is set up via `make test`. Input "stream" values are provided in JSON files, an array of array where each inner array is the contents of one particular stream, and expected output is provided in a text file. Note that multiple orders are valid because order is on the timestamp field and not on value field, so the test harness should be considered a helpful tool but not the only definition of correctness.

Edit `launcher.sh` to run your application as needed if you find it helpful.

