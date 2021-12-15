from src.common.persister import Persister

class LoadingList:
    def __init__(self, persister: Persister) -> None:
        self.persister = persister

    def __enter__(self):
        self.persister.load()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.persister.persist()