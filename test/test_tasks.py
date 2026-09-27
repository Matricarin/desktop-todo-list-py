from src.app.tasks import load_tasks, save_tasks, get_next_task_id
import pytest
import json
import pathlib

class TestLoadTasks:
    
    def test_load_not_existent_file(self, tmp_path):
        file = tmp_path / "missing.json"
        assert load_tasks(file) == []