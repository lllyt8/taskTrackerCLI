import os
import sys
import json
from datetime import datetime

TASK_FILE="tasks.json"

def load_task():
    """Load tasks data, if file not found return empty list"""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []
