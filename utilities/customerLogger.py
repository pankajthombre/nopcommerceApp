#Utilities to generate logs file for TC

import logging

class LogGen():

    @staticmethod
    def loggen(self):
        logging.basicConfig(filename=".\\Logs\\automation.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S')


        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
