import os, easyocr, pyautogui, time, cv2, numpy as np


class ScreenInteractor:
    def __init__(self, confidence: float = 0.8):
        self.confidence = confidence
        
    def _is_image_path(self, path: str) -> bool:
        return path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))

    def _load_template(self, path: str) -> np.ndarray:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Template não encontrado: \n{path}")

        image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError(f"Erro ao carregar o template: \n{path}")

        return image

    def _capture_screen(self) -> np.ndarray:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    def find(self, template_path: str) -> tuple[int, int] | None:
        template = self._load_template(template_path)
        screen = self._capture_screen()

        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        match_locations = np.where(result >= self.confidence)

        if not match_locations[0].size:
            return None

        x, y = match_locations[1][0], match_locations[0][0]
        w, h = template.shape[::-1]
        return x + w // 2, y + h // 2

    def click(self, target: str, offset_x: int = 0, offset_y: int = 0) -> None:
        position = None

        if self._is_image_path(target):
            position = self.find(target)

        if position is None:
            raise ValueError(f"Nenhuma imagem ou texto encontrado: '{target}'")

        x, y = position[0] + offset_x, position[1] + offset_y
        pyautogui.click(x, y)

    def click_and_type(self, template_path: str, text: str, offset_x: int = 0, offset_y: int = 0) -> None:
        self.click(template_path, offset_x, offset_y)
        pyautogui.write(text)

    def wait_until_visible(self, template_path: str, timeout: int = 30) -> None:
        start_time = time.time()

        while time.time() - start_time < timeout:
            if self.find(template_path):
                return
            time.sleep(1)

        raise TimeoutError(f"Imagem não apareceu dentro do tempo limite: \n{template_path}")

    def wait_and_click(self, wait_for_path: str, click_path: str='', timeout: int=30) -> None:
        if click_path == '':
            click_path = wait_for_path
        self.wait_until_visible(wait_for_path, timeout)
        self.click(click_path)

    def is_image_on_screen(self, template_path: str, timeout: int = 10) -> bool:
        start_time = time.time()

        while time.time() - start_time < timeout:
            if self.find(template_path):
                return True
            time.sleep(0.5)

        return False
