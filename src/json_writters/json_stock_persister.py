from src.common.persister import Persister

class JsonStockPersister(Persister):
    def __init__(self, item_list, file_path) -> None:
        super().__init__(item_list)
    
    def load(self):
        pass

    def persist(self):
        pass