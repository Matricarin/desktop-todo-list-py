from src.app.tasks import load_tasks, save_tasks, get_next_task_id
import pytest
import json
import pathlib

class TestLoadTasks:
    
    def test_load_not_existent_file(self, tmp_path):
        file = tmp_path / "missing.json"
        assert load_tasks(file) == []
        
    def test_load_tasks_success(self):
        file = "test/data/load_tasks_success.json"
        tasks = load_tasks(file)
        assert len(tasks) == 2            
        
    def test_load_tasks_decode_error(self):
        file = "test/data/decode_error.json"
        try:
            load_tasks(file)
        except Exception as e:
            assert type(e) == type(json.JSONDecodeError)        
        
class TestSaveTasks:
    
    def test_save_with_serialization_error(self):
        ...
        
    def test_save_success(self):
        ...
        
class TestGetNextTask:
    
    def test_return_one(self):
        tasks = []
        id = get_next_task_id(tasks)
        assert id == 1
        
    def test_return_valid_id(self):
        tasks = [{"id": 1, "title": "Task 1"}, {"id": 2, "title" : "Task2"}]
        id = get_next_task_id(tasks)
        assert id == 3