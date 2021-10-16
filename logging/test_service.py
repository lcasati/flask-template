from flask import current_app

def ciao():
    current_app.logger.info("Hello")