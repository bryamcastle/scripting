import logging

log_file = 'avantica.log'

class ConnInfo:
    def __getitem__(self, name):
        from random import choice
        if name == "state":
           result = choice(["open","closed"])
        elif name == "Rx":
            result = choice(range(1,100))
        elif name == "Tx":
            result = choice(range(1,100))
        else:
            result = self.__dict__.get(name, "?")
        return result

    def __iter__(self):
        keys = ["state", "Rx", "Tx"]
        keys.extend(self.__dict__.keys())
        return keys.__iter__()

from random import choice
levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)

logging.basicConfig(filename=log_file,
                    level=logging.DEBUG,
                    format="%(asctime)s, %(levelname)s, %(message)s state: %(state)s, Tx: %(Tx)s, Rx: %(Rx)s")

record = logging.LoggerAdapter(logging.getLogger("bryam"), ConnInfo())
for i in range(86400):
    lv1 = choice(levels)
#    logging.debug('conn_id: %d,' % i)
    record.log(lv1,'conn_id: %d,' % i)
"""
logging.debug('This is a debug')
logging.info('This is an info')
logging.error('This is an error')
logging.fatal('This is a fatal')

"""
