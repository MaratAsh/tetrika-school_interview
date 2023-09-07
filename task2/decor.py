from typing import Callable
import logging
import tempfile
import hashlib
from os import makedirs, path


def file_buffering(decored_func: Callable) -> Callable:
	temp_path = [tempfile.gettempdir(), 'MaratAshPythonBuff']
	if temp_path[-1] != '':
		temp_path.append('')
	temp_path = path.sep.join(temp_path)
	makedirs(temp_path, exist_ok=True)
	
	def func(url: str) -> str:
		_hash = hashlib.md5(url.encode())
		file_path = '{path}{name}.html'.format(path=temp_path, name=_hash.hexdigest())
		
		content = None
		if (path.exists(file_path) == True):
			logging.info('buffered file \'{0}\' exists.'.format(file_path))
			with open(file_path, 'r', encoding="utf-8") as f:
				logging.info('reading \'{0}\' file.'.format(file_path))
				content = f.read()
			return content
		content = decored_func(url)
		if not content:
			return None
		logging.info('saving downloaded page into \'{0}\' file.'.format(file_path))
		with open(file_path, 'w', encoding="utf-8") as f:
			f.write(content)
		return content
	return func
