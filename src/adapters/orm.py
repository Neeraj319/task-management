import enum

from sqlalchemy import Column, DateTime, Enum, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.mapper import Mapper

from src.domain.modles import Task

Base = declarative_base()


class TasksStatusEnum(enum.Enum):
    TODO = "TODO"
    DOING = "DOING"
    DONE = "DONE"


tasks = Table(
    "tasks",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column(
        "status",
        Enum(TasksStatusEnum),
        default=TasksStatusEnum.TODO,
    ),
    Column("created_at", DateTime()),
    Column("updated_at", DateTime()),
)


def start_mapper():
    Mapper(Task, tasks)
