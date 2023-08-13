from typing import Protocol


class AbstractUnitOfWork(Protocol):
    def __enter__(self):
        return self
