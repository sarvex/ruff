import logging
import logging as foo

logging.info('Hello World!')
logging.log(logging.INFO, 'Hello World!')
foo.info('Hello World!')
logging.log(logging.INFO, msg='Hello World!')
logging.log(level=logging.INFO, msg='Hello World!')
logging.log(msg='Hello World!', level=logging.INFO)
