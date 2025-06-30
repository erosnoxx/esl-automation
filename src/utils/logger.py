import logging, inspect

class Logger:
    def __init__(self, level=logging.INFO):
        logging.basicConfig(
            format='[%(asctime)s] [%(message)s]',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=level
        )
        self.logger = logging.getLogger(__name__)

    def log(self, message):
        stack = inspect.stack()
        frame = stack[1]
        func = frame.function
        cls = frame.frame.f_locals.get('self', None)
        cls_name = cls.__class__.__name__ if cls else None
        module = f"{cls_name}.{func}" if cls_name else func

        self.logger.info(f"{module} | {message}")
