from pathlib import Path
from crewai_tools import FileReadTool

SPECIFICATION_FILE = Path("estate/tasks/perfect_home.md")

specification_read_tool = FileReadTool(
    file_path=SPECIFICATION_FILE,
    description="A tool to read perfect home example file.",
)
