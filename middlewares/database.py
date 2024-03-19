from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update
from sqlalchemy.ext.asyncio import async_sessionmaker


class Database(BaseMiddleware):
    def __init__(self, sm: async_sessionmaker) -> None:
        self.Session = sm

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any],
    ) -> Any:
        data['session'] = self.Session 
        return await handler(event, data)

