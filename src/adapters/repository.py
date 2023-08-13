from abc import ABC, abstractmethod

from domain import models
from sqlalchemy.orm.session import Session


class AbstractRepository(ABC):
    session: Session

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


class SqlAlchemyRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def _add(self, task: models.Task):
        self.session.add(task)

    def _get(self, id: int) -> models.Task | None:
        return self.session.query(models.Task).filter_by(id=id).first()
