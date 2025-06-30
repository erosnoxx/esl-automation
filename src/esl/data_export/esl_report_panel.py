import time
from src.utils.logger import Logger
from src.utils.chrome_manager import ChromeManager
from src.utils.screen_interactor import ScreenInteractor, pyautogui


class ESLReportPanel:
    def __init__(self,
            base_url: str,
            screen_interactor: ScreenInteractor,
            chrome_manager: ChromeManager,
            logger: Logger) -> None:
        self.base_url = base_url
        self.path = "companies/5461826/edit"
        self.url = f"{self.base_url}{self.path}"
        self.screen_interactor = screen_interactor
        self.chrome_manager = chrome_manager
        self.logger = logger
    
    def run(self) -> None:
        self.logger.log('Starting execution')
        self.chrome_manager.open(self.url)
        self.logger.log('Chrome opened - Login successfully')
        self.logger.log(f'Current page: {self.path}')
        self.screen_interactor.wait_and_click('assets/menu/edi/config.png')
        self.screen_interactor.wait_and_click('assets/menu/edi/edi.png')
        
        if self.screen_interactor.is_image_on_screen('assets/menu/edi/select-proceda.png'):
            self.logger.log('Pattern Found: PROCEDA 3.0')
            self.screen_interactor.click_and_type('assets/menu/edi/select-proceda.png', "TIVIT 5.0")
            self.logger.log('Pattern Changed: TIVIT 5.0')
            
        elif self.screen_interactor.is_image_on_screen('assets/menu/edi/select-tivit.png'):
            self.logger.log('Pattern Found: TIVIT 5.0')
            self.screen_interactor.click_and_type('assets/menu/edi/select-tivit.png', "PROCEDA 3.0")
            self.logger.log('Pattern Changed: PROCEDA 3.0')
        
        pyautogui.press('ENTER')
        time.sleep(0.8)
        pyautogui.scroll(-100)
        self.screen_interactor.wait_and_click('assets/menu/edi/save.png')
        pyautogui.press('ENTER')
        self.screen_interactor.click_and_type('assets/menu/edi/url-chrome.png', f'{self.base_url}edi/file/occurrences')
        pyautogui.press('ENTER')
        self.screen_interactor.wait_until_visible('assets/menu/edi/generate-edi.png')
        self.screen_interactor.click_and_type('assets/menu/edi/customer-selection.png', "43.643.857/0001-32")
        self.screen_interactor.wait_and_click('assets/menu/edi/monte-vergine.png')
        self.screen_interactor.wait_and_click('assets/menu/edi/search.png')
        
        self.logger.log('Searching for Monte Vergine Occurrences')
        
        if self.screen_interactor.is_image_on_screen('assets/menu/edi/no-pendencies.png', 2):
            self.logger.log('No Occurrences Found')
            return
            
        self.logger.log('Occurrences Found')
        
        while not self.screen_interactor.is_image_on_screen('assets/menu/edi/no-pendencies.png'):
            self.screen_interactor.wait_and_click('assets/menu/edi/generate.png')
            self.screen_interactor.wait_and_click('assets/menu/edi/yes.png')
            
        self.screen_interactor.wait_and_click('assets/menu/edi/generated-files.png')
        self.screen_interactor.click_and_type('assets/menu/edi/customer-selection.png', "43.643.857/0001-32")
        self.screen_interactor.wait_and_click('assets/menu/edi/monte-vergine.png')
        self.screen_interactor.wait_and_click('assets/menu/edi/search.png')
