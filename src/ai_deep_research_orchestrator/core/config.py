from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL : str

    ACCESS_TOKEN_SECRET_KEY : str
    ACCESS_TOKEN_EXPIRY_IN_MINUTES : int
    REFRESH_TOKEN_EXPIRY_IN_DAYS : int
    ACCESS_TOKEN_ALGORITH : str

    GOOGLE_API_KEY : str


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )



settings = Settings()