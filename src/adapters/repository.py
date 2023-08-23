from abc import ABC, abstractmethod

from sqlalchemy.orm.session import Session

from domain import models


class AbstractRepository(ABC):
    session: Session

    def __init__(self) -> None:
        self.seen: set[models.Task] = set()

    def add(self, task: models.Task):
        self._add(task)

    def get(self, id: int) -> models.Task:
        task = self._get(id)
        return task

    @abstractmethod
    def _add(self, task: models.Task):
        raise NotImplementedError

    @abstractmethod
    def _get(self, id: int) -> models.Task:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
        super().__init__()

    def _add(self, task: models.Task):
        self.session.add(task)

    def _get(self, id: int) -> models.Task | None:
        return self.session.query(models.Task).filter_by(id=id).first()
