from pydantic import BaseSettings,EmailStr

class Setting(BaseSettings):
    SMTP_EMAIL : str
    SMTP_PASSWORD : str

    class config:
        env_file = ".env"

settings = Setting()        