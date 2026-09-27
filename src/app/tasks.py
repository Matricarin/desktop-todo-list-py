import json
import pathlib
import logging

def load_tasks(file_path):
    file = pathlib.Path(file_path)
    if not file.exists():
        return []
    with open(file=file_path, mode="r", encoding="urf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            logging.error("Json decode error")
            return []
        except Exception:
            logging.error("Unknown error")
            return []
    
def save_tasks(file_path, tasks):
    file = pathlib.Path(file_path)
    file.parent.mkdir(parents=True, exist_ok=True)
    if not file.exists():
        file.touch()
    with open(file=file_path, mode="w", encoding="utf-8") as f:
        try:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        except json.JSONDecodeError:
            logging.error("Json decode error")
        except Exception:
            logging.error("Unknown error")
        
    
def get_next_task_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1