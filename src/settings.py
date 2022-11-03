from pydantic import BaseSettings


class Settings(BaseSettings):
    sqlite_name: str
    postgres_db_name: str
    postgres_db_host: str
    postgres_db_port: str
    postgres_db_username: str
    postgres_db_password: str

    @property
    def postgres(self):
        return f"postgresql+psycopg2://{self.postgres_db_username}:{self.postgres_db_password}" \
               f"@{self.postgres_db_host}:{self.postgres_db_port}/{self.postgres_db_name}"

    class Config:
        env_file = './venv_ubuntu/.env'


settings = Settings()
