from datetime import date

from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int]
    text: Mapped[str] = mapped_column(Text)
    # category_id: Mapped[int]
    # date_complete: Mapped[date]
    # time: Mapped[int]
    # repeat: Mapped[bool]
    # days_repeat_id: Mapped[int]
    # reminder: Mapped[bool]
    # time_id: Mapped[int]
    # notes_id: Mapped[int]


class Category(Base):
    __tablename__ = 'category'



# workers_table = Table(
#     "workers",
#     metadata_obj,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("name", String),
#     Column("premium", Boolean)
# )


