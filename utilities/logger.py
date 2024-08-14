import logging

# Set the encoding for logging
logging.basicConfig(encoding='utf-8')


class LogGen:

    logger = None

    @staticmethod
    def loggen():

        if LogGen.logger is None:
            log_file_path = 'Logs/actionLogs.log'
            LogGen.logger = logging.getLogger("pytest_logger")
            LogGen.logger.setLevel(logging.INFO)

            # Create a file handler and set the level to DEBUG
            fh = logging.FileHandler(log_file_path)
            fh.setLevel(logging.INFO)

            # Create a formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)

            # Add the handlers to the logger
            LogGen.logger.addHandler(fh)

        return LogGen.logger
