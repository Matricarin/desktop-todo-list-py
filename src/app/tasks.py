import json
import os
import tempfile
import pathlib
import logging

def load_tasks(file_path):
    file = pathlib.Path(file_path)
    if not file.exists():
        return []
    with open(file_path, mode="r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Json decode error: {e}")
            return []
        except Exception:
            logging.error(f"Unknown error: {e}", exc_info=True)
            return []
    
def save_tasks(file_path, tasks):
    file = pathlib.Path(file_path)
    file.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        json_str = json.dump(tasks, ensure_ascii=False, indent=2)
    except Exception as e:
        logging.error(f"Serialize error: {e}", exc_info=True)
        return False
    
    try:
        fd, temp_path = tempfile.mkstemp(dir=file.parent, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(json_str)
        os.replace(temp_path, file_path)
        return True
    except Exception as e:
        logging.error(f"Writing error: {e}", exc_info=True)
        if 'temp_path' in locals() and pathlib.Path(temp_path).exists():
            os.remove(temp_path)
        return False
    
def get_next_task_id(tasks):
    if not tasks:
        return 1
    ids = [task.get("id", 0) for task in tasks if isinstance(task.get("id"), int)]
    return max(ids) + 1 if ids else 1