
import inspect
import logging

class CustLog():

    def log_details(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        logger.setLevel(logging.INFO)
        fh = logging.FileHandler("..\\Logs\\apps.log")
        formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s/', datefmt = '%m/%d/%Y %I:%M:%S %p')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
    '''def log_details(self):
        logging.basicConfig(
            filename="apps.log",
            level=logging.INFO,
            format= '%(asctime)s -  %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        return logging.getLogger()'''


