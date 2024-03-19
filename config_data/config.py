from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    db_name: str  # Название базы данных
    db_port: int  # Порт для подключения к бд
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_pass: str  # Пароль к базе данных

    @property
    def DATABASE_URL_asyncpg(self):
        return f'postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'

    @property
    def DATABASE_URL_psycopg(self):
        return f'postgresql+psycopg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'


class TgBot(BaseSettings):
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота
    use_redis: bool       # Флаг для включения Redis хранилища


class SettingsExtractor(BaseSettings):
    # tg_bot
    TG_BOT_TOKEN: str
    TG_BOT_ADMIN_IDS: list[int]
    TG_BOT_USE_REDIS: bool

    # db
    DB_NAME: str
    DB_PORT: int
    DB_HOST: str
    DB_USER: str
    DB_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env")


class Settings(BaseSettings):
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(env_file=".env") -> Settings:
    # Создаем экземпляр класса Config и наполняем его данными из переменных окружения
    settings = SettingsExtractor()

    return Settings(
        tg_bot=TgBot(
            token=settings.TG_BOT_TOKEN,
            admin_ids=settings.TG_BOT_ADMIN_IDS,
            use_redis=settings.TG_BOT_USE_REDIS
        ),
        db=DatabaseConfig(
            db_name=settings.DB_NAME,
            db_host=settings.DB_HOST,
            db_port=settings.DB_PORT,
            db_user=settings.DB_USER,
            db_pass=settings.DB_PASSWORD
        )
    )
