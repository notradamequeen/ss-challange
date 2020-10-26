
class Transaction:
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, exception_type, exception_value, traceback):
        self.session.rollback()
