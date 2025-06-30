from src.globals.global_services import GlobalServices
from src.globals.global_usecases import GlobalUsecases
from src.globals.global_variables import GlobalVariables


class App:
    def __init__(self):
        self.variables = GlobalVariables()
        self.services = GlobalServices(self.variables)
        self.usecases = GlobalUsecases(self.variables, self.services)
    
    def run(self):
       self.usecases.esl_report_panel.run()

app = App()
app.run()
