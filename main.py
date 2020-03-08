import json
import heapq
import sys
from itertools import chain


def to_dict(el: tuple) -> dict:
    return {'timestamp': el[0],
            'value': el[1]}

def to_tuple(el: dict) -> tuple:
    return (el['timestamp'], el['value'])


class MergedOrderedStream:
    def __init__(self, *streams):
        tuple_streams = [map(to_tuple, s) for s in streams]
        self.stream = chain(heapq.merge(*tuple_streams), [None])
        self.head = next(self.stream)

    @classmethod
    def init_from_json(cls, filepath: str):
        ''' Constructs the merged stream from a json filepath'''
        with open(filepath, 'r') as f:
            streams = json.load(f)
            return cls(*streams)

    def peek(self):
        if self.is_not_empty():
            return to_dict(self.head)
    
    def next(self):
        if self.is_not_empty():
            current_head = self.head
            self.head = next(self.stream)
            return to_dict(current_head)

    def is_not_empty(self):
        return self.head is not None

    def consume(self):
        if self.is_not_empty():
            sum_ = 0
            count = 0
            while self.is_not_empty():
                el = self.next()
                value = el['value']
                sum_ += value
                count += 1
                print(f"timestamp: {el['timestamp']}, value: {value}")
                if count % 5 == 0:
                    print(f'count: {count}, sum: {sum_}, average: {sum_/count}')
            print(f'sum: {sum_}, count: {count}, average: {sum_/count}')


if __name__ == '__main__':
    input_filepath = sys.argv[-1]
    stream = MergedOrderedStream.init_from_json(input_filepath)
    stream.consume()
    
