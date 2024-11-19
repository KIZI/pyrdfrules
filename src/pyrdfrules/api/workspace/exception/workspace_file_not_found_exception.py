class WorkspaceFileNotFoundException(Exception):
    def __init__(self, file_path: str):
        super().__init__(f"File not found: {file_path}")
        self.file_path = file_path