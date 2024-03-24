from datetime import date
from typing import Annotated

from sqlalchemy import ForeignKey, BigInteger, String
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
str_32 = Annotated[str, mapped_column(String(32))]


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(BigInteger)
    text: Mapped[str_32]
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete='SET NULL'), nullable=True)
    date_task: Mapped[date]
    # date_complete: Mapped[date]
    # time: Mapped[int]
    # repeat: Mapped[bool]
    # days_repeat_id: Mapped[int]
    # reminder: Mapped[bool]
    # time_id: Mapped[int]
    # notes_id: Mapped[int]


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[intpk]
    user_id: Mapped[int]
    category_name: Mapped[str]


class Subtasks(Base):
    __tablename__ = 'subtasks'

    id: Mapped[intpk]
    task_id: Mapped[int] = mapped_column(ForeignKey('tasks.id', ondelete='CASCADE'))
    text: Mapped[str_32]
    complete: Mapped[bool]

# workers_table = Table(
#     "workers",
#     metadata_obj,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("name", String),
#     Column("premium", Boolean)
# )


