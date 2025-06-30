from src.utils.screen_interactor import ScreenInteractor

class ESLLogin:
    def __init__(self, 
            screen_interactor: ScreenInteractor, 
            esl_email: str,
            esl_password: str) -> None:
        self.screen_interactor = screen_interactor
        self.esl_email = esl_email
        self.esl_password = esl_password
    
    def run(self) -> None:
        self.screen_interactor.wait_until_visible('assets/login/email.png')
        self.screen_interactor.click_and_type('assets/login/email.png', self.esl_email)
        self.screen_interactor.click_and_type('assets/login/password.png', self.esl_password)
        self.screen_interactor.click('assets/login/login-btn.png')
        self.screen_interactor.wait_and_click('assets/login/login-successful.png')
        self.screen_interactor.wait_and_click('assets/login/never-btn.png')
