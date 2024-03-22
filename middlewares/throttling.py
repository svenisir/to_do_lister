from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import User, TelegramObject
from aiogram.fsm.storage.redis import Redis


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, redis: Redis):
        self.redis = redis

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ):
        if self.redis:
            user: User = data.get('event_from_user')

            flag = await self.redis.get(f'{user.id}')
            if flag:
                return

            await self.redis.append(f'{user.id}', 1)
            await self.redis.expire(f'{user.id}', 5)

        return await handler(event, data)
