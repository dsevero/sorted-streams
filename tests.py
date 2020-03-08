from main import MergedOrderedStream

s1 = [{'timestamp': 0, 'value': 0},
      {'timestamp': 2, 'value': 1}]
s2 = [{'timestamp': 1, 'value': 2},
      {'timestamp': 3, 'value': 3}]

stream = MergedOrderedStream(s1, s2)

assert stream.peek() == {'timestamp': 0, 'value': 0}
assert stream.peek() == {'timestamp': 0, 'value': 0}

assert stream.next() == {'timestamp': 0, 'value': 0}

assert stream.peek() == {'timestamp': 1, 'value': 2}
assert stream.peek() == {'timestamp': 1, 'value': 2}

assert stream.next() == {'timestamp': 1, 'value': 2}
assert stream.next() == {'timestamp': 2, 'value': 1}
assert stream.next() == {'timestamp': 3, 'value': 3}

assert stream.peek() is None
assert stream.next() is None
assert stream.peek() is None
assert stream.next() is None
