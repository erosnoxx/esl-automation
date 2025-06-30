from src.esl.data_export.esl_report_panel import ESLReportPanel
from src.globals.global_services import GlobalServices
from src.globals.global_variables import GlobalVariables


class GlobalUsecases:
    def __init__(self, 
            variables: GlobalVariables,
            services: GlobalServices):
        self.esl_report_panel = ESLReportPanel(
            variables.esl_base_url,
            services.screen_interactor,
            services.chrome_manager,
            services.logger)
