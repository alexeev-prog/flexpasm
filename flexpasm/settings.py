from dataclasses import dataclass


@dataclass
class Settings:
    title: str
    author: str
    filename: str
    executable: bool = True
    mode: str = "64"
    start_entry: str = "start"
    indentation: str = "	"
    backup_directory: str = ".backups"
