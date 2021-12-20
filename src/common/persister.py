class Persister:
    def __init__(self, item_list) -> None:
        self.item_list = item_list

    def __enter__(self):
        self.load()
        return self.item_list

    def __exit__(self,exc_type, exc_value, exc_traceback):
        if not exc_type:
            self.persist()

    def load(self):
        raise NotImplementedError()

    def persist(self):
        raise NotImplementedError()
