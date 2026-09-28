from src.app.tasks import load_tasks, save_tasks, get_next_task_id
import pytest
import json
import pathlib

class TestLoadTasks:
    
    def test_load_not_existent_file(self, tmp_path):
        file = tmp_path / "missing.json"
        assert load_tasks(file) == []
        
    def test_load_tasks_success(self):
        ...
        
    def test_load_tasks_decode_error(self):
        ...
        
        
class TestSaveTasks:
    
    def test_save_with_serialization_error(self):
        ...
        
    def test_save_success(self):
        ...
        
class TestGetNextTask:
    
    def test_return_one(self):
        ...
        
    def test_return_valid_id(self):
        ...