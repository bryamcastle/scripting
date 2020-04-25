from prometheus_client import start_http_server, Histogram, CollectorRegistry, write_to_textfile
import json
import time


start_time = time.time()
_INF = float("inf")
file_log = 'avantica.log'


class JsonData(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def process_request():
    registry = CollectorRegistry()
    graphs = {}
    graphs['h1'] = Histogram('Tx', 'Numbers of Tx.', buckets=(500, 1000, 5000, 9000, _INF), registry=registry)
    graphs['h2'] = Histogram('Rx', 'Number of Rx.', buckets=(500, 1000, 5000, 9000, _INF), registry=registry)
    with open(file_log, 'r') as f:
        for i in f:
            line = JsonData(i)
            tx = line.Tx
            rx = line.Rx
            graphs['h1'].observe(tx)
            graphs['h2'].observe(rx)
    write_to_textfile('histogram.prom', registry)


if __name__ == '__main__':
    process_request()
    print "Execution time:", (time.time() - start_time)
