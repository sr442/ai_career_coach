import logging

def setup_logger():
    logging.basicConfig(filename="chatbot.log", level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

def log_error(msg):
    logging.error(msg)
