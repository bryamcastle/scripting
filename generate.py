import logging
from random import choice
import time

start_time = time.time()
log_file = 'avantica.log'
levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)


class ConnInfo:
    def __getitem__(self, name):
        from random import choice
        if name == "state":
           result = choice(["open","closed"])
        elif name == "Rx":
            result = choice(range(1,10000))
        elif name == "Tx":
            result = choice(range(1,10000))
        else:
            result = self.__dict__.get(name, "?")
        return result

    def __iter__(self):
        keys = ["state", "Rx", "Tx"]
        keys.extend(self.__dict__.keys())
        return keys.__iter__()


def generatelogs():
    logging.basicConfig(filename=log_file,
                        level=logging.DEBUG,
                        format='{"ts": "%(asctime)s", "level": "%(levelname)s", %(message)s "state": "%(state)s", "Tx": %(Tx)s, "Rx": %(Rx)s}')
    record = logging.LoggerAdapter(logging.getLogger("user"), ConnInfo())
    for i in range(86400):
        lv1 = choice(levels)
        record.log(lv1, '"conn_id": %d,' % i)


if __name__ == '__main__':
    generatelogs()
    print "Execution time:", (time.time() - start_time)
