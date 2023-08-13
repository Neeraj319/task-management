from abc import ABC


class AbstractUnitOfWork(ABC):
    def __enter__(self):
        return self
