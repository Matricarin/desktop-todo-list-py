import logging
import pathlib


def setup_logging(app_name="Todo App"):
    log_dir = pathlib.Path.home() / f".{app_name}" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "app.log"
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=2*1024*1024, backupCount=5, encoding="utf-8"
    )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)