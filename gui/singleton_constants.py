class SingleConstantsHolder:
    _instance = None

    def __init__(self):
        if SingleConstantsHolder._instance is not None:
            raise ValueError("An instance of SingleConstantsHolder already exists.")
        SingleConstantsHolder._instance = self

        self.github_repo_url = ""
        self.project_name = ""
        self.local_file_folder_path = ""

    @staticmethod
    def get_instance():
        if SingleConstantsHolder._instance is None:
            SingleConstantsHolder()
        return SingleConstantsHolder._instance
