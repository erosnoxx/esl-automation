from src.utils.logger import Logger
from src.esl.esl_login import ESLLogin
from src.globals.global_variables import GlobalVariables
from src.utils.chrome_manager import ChromeManager
from src.utils.screen_interactor import ScreenInteractor


class GlobalServices:
    def __init__(self, variables: GlobalVariables):
        self.screen_interactor = ScreenInteractor()
        self.esl_login = ESLLogin(
            self.screen_interactor,
            variables.esl_email,
            variables.esl_pwd)
        self.chrome_manager = ChromeManager(variables.chrome_path, self.esl_login)
        self.logger = Logger()
