import logging


def test():
    logging.info('test start')
    print(9 / 0)
    logging.info('test end')


print(test())
