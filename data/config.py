from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati


DB_USER = env.str("POSTGRES_USER")
DB_PASS = env.str("POSTGRES_PASSWORD")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
