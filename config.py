import os
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_KEY")
DATABASE_ID = os.getenv("NOTION_PAGE_ID")