class Config(object):
    """Add docstrings."""

    def __init__(self, file_path=None):
        if not file_path:
            self.dir_path = DEFAULT_DATA_DIR + '/run/conf'
            self.file_name = 'nude-man'
            self.file_ext = 'conf'
            self.file_path = Path(
                self.dir_path + f'/{self.file_name}.{self.file_ext}')
        else:
            self.file_path = Path(file_path)
            full_file_name = self.file_path
