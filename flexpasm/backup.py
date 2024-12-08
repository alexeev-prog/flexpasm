import json
import os
from datetime import datetime

from rich import print

from flexpasm.settings import Settings


class BackupManager:
	def __init__(self, settings: Settings):
		self.settings = settings
		self.backups_limit = 5
		self._backups_files = []

		os.makedirs(self.settings.backup_directory, exist_ok=True)

	def _save_to_json(self):
		data = self._load_from_json()

		if data:
			for file in data["files"]:
				if file not in self._backups_files:
					self._backups_files.append(file)

		backups = {
			"limit": self.backups_limit,
			"filename": self.settings.filename,
			"files": self._backups_files[::-1],
		}

		with open(".flexpasm_backups.json", "w") as write_file:
			json.dump(backups, write_file)

	def _resave_file(self, filename: str):
		with open(os.path.join(self.settings.backup_directory, filename), "r") as file:
			with open(self.settings.filename, "w") as file2:
				file2.write(file.read())

	def _load_from_json(self):
		try:
			with open(".flexpasm_backups.json", "r") as read_file:
				data = json.load(read_file)
		except (FileNotFoundError, OSError):
			return False

		return data

	def create_backup(self, content: str):
		date = datetime.now().strftime("%Y%m%d_%H-%M-%S")

		filename = f"{date}_{self.settings.filename}"

		with open(os.path.join(self.settings.backup_directory, filename), "w") as file:
			file.write(content)

		self._backups_files.append(filename)

		if len(self._backups_files) > self.backups_limit:
			self._backups_files = self._backups_files[::-1][: self.backups_limit - 1]

		self._save_to_json()

	def restore(self, backup_num: int = None):
		backups = self._load_from_json()

		if backup_num is None:
			for num, filename in enumerate(backups["files"]):
				if num == 0:
					continue
				try:
					self._resave_file(filename)
				except Exception as ex:
					print(f"[yellow]WARNING {ex}[/yellow]")
					continue
				else:
					print(f"SUCCESS Restore Backup_{num}: {filename}")
					return

		print(f"Failed to restore file {self.settings.filename}")

		return False
