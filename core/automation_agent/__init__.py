"""
Automation Agent Module
Handles workflow automation and script execution
"""

from .automation import AutomationAgent
from .script_executor import ScriptExecutor
from .workflow import WorkflowEngine

__all__ = [
    "AutomationAgent",
    "ScriptExecutor",
    "WorkflowEngine",
]