import os
import dotenv

dotenv.load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
PROVIDER_TOKEN = os.getenv('PROVIDER_TOKEN') 