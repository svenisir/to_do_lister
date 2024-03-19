from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    is_premium: Mapped[bool]
    surname: Mapped[str]
    fullname: Mapped[str]


# workers_table = Table(
#     "workers",
#     metadata_obj,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("name", String),
#     Column("premium", Boolean)
# )


