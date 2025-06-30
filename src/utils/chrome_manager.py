import os, psutil, subprocess, tempfile, time, shutil
from src.esl.esl_login import ESLLogin


class ChromeManager:
    def __init__(self, 
            chrome_path: str=None,
            esl_login: ESLLogin=None):
        self.chrome_path = chrome_path or self._default_chrome_path()
        self.timestamp = None
        self.temp_profile_dir = None
        self.esl_login = esl_login

    def _default_chrome_path(self):
        return 

    def open(self, url: str):
        if not os.path.exists(self.chrome_path):
            raise FileNotFoundError("Caminho do Chrome inválido.")

        self.timestamp = time.time()

        self.temp_profile_dir = tempfile.mkdtemp(prefix="chrome_profile_")

        subprocess.Popen([
            self.chrome_path,
            "--new-window", url,
            f"--user-data-dir={self.temp_profile_dir}",
            "--no-first-run",
            "--no-default-browser-check",
            "--start-maximized"
        ])

        time.sleep(5)
        if self.esl_login.screen_interactor.find('assets/login/email.png') != None:
            self.esl_login.run()

    def close(self):
        if not self.timestamp:
            return

        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                if 'chrome' in proc.info['name'].lower() and proc.info['create_time'] >= self.timestamp:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        if self.temp_profile_dir and os.path.exists(self.temp_profile_dir):
            shutil.rmtree(self.temp_profile_dir, ignore_errors=True)
        self.temp_profile_dir = None
        self.timestamp = None
