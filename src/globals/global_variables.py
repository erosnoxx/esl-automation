import os
from dotenv import load_dotenv


class GlobalVariables:
    def __init__(self):
        load_dotenv()
        self.chrome_path = os.getenv('CHROME_PATH')
        self.esl_email = os.getenv("ESL_EMAIL")
        self.esl_pwd = os.getenv("ESL_PASSWORD")
        self.esl_base_url = os.getenv("ESL_BASE_URL")
