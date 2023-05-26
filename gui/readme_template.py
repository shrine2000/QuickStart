import os
import fnmatch

class ReadmeTemplate:
    def __init__(self, root_path):
        self.sections = []
        self.root_path = root_path

    def add_section(self, section):
        self.sections.append(section)

    def generate_readme(self):
        readme = "# Project Title\n\n Description\n\n"

        for section in self.sections:
            if section == "Badges":
                readme += self.generate_badges()
            elif section == "Authors":
                readme += self.generate_authors()
            elif section == "Usage/Examples":
                readme += self.generate_usage_examples()
            elif section == "Run Locally":
                readme += self.generate_run_locally()
            elif section == "Running Tests":
                readme += self.generate_running_tests()
            elif section == "Demo":
                readme += self.generate_demo()
            elif section == "Screenshots":
                readme += self.generate_screenshots()
            elif section == "Roadmap":
                readme += self.generate_roadmap()
            elif section == "License":
                readme += self.generate_license()
            elif section == "Project Structure":
                readme += self.generate_project_structure()

        return readme

    def generate_badges(self):
        return "[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)\n"

    def generate_authors(self):
        return "\n## Authors \n"

    def generate_usage_examples(self):
        return "\n## Usage/Examples \n"

    def generate_run_locally(self):
        return "\n## Run Locally \n"

    def generate_running_tests(self):
        return "\n## Running Tests "

    def generate_demo(self):
        return "\n## Demo "

    def generate_screenshots(self):
        return "\n## Screenshots \n"

    def generate_roadmap(self):
        return "\n## Roadmap \n"

    def generate_license(self):
        return "\n## License\n\n"

    def generate_project_structure(self):
        tree = ""
        indent = " "

        # Read the patterns from .gitignore
        gitignore_path = os.path.join(self.root_path, ".gitignore")
        ignore_patterns = self.read_gitignore_patterns(gitignore_path)

        # Walk through the files and directories
        for root, dirs, files in os.walk(self.root_path):
            # Remove ignored files
            files = [f for f in files if not self.is_ignored(os.path.join(root, f), ignore_patterns)]
            dirs[:] = [d for d in dirs if not self.is_ignored(os.path.join(root, d), ignore_patterns)]

            # Add directories to the project structure
            for dir in dirs:
                tree += f"{indent}|- {dir}\n"

            # Add files to the project structure
            for file in files:
                tree += f"{indent}|- {file}\n"

        return tree

    def read_gitignore_patterns(self, gitignore_path):
        patterns = []
        if os.path.isfile(gitignore_path):
            with open(gitignore_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        patterns.append(line)
        return patterns

    def is_ignored(self, path, patterns):
        for pattern in patterns:
            if fnmatch.fnmatch(path, pattern):
                return True
        return False
