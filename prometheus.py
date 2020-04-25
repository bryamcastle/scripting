from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

_INF = float("inf")

graphs = {}
graphs['h1'] = Histogram('Tx', 'Total of number of Tx.', buckets=(500, 1000, 5000, 9000, _INF))
graphs['h2'] = Histogram('Rx', 'Total of number of Rx.', buckets=(500, 1000, 5000, 9000, _INF))

open('C:/Users/bryam/PycharmProjects/Tutorial/venv/avantica.log','r')

