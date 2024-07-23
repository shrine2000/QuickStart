import os
import subprocess

class ProjectInitializer:
    def __init__(self, project_name: str, folder: str):
        self.project_name = project_name
        self.folder = folder
        self.project_path = os.path.join(folder, project_name)

    def create_project(self):
        os.makedirs(self.project_path, exist_ok=True)
        self._initialize_git()
        self._create_readme()
        self._create_gitignore()
        self._open_vscode()

    def _initialize_git(self):
        subprocess.run(["git", "init"], cwd=self.project_path, check=True)
        print(f"Initialized empty Git repository in {self.project_path}")

    def _create_readme(self):
        readme_path = os.path.join(self.project_path, "README.md")
        with open(readme_path, "w") as file:
            file.write(f"# {self.project_name}\n")
        print(f"Created README.md with project title in {self.project_path}")

    def _create_gitignore(self):
        gitignore_content = "*.pyc\n__pycache__/\n"
        gitignore_path = os.path.join(self.project_path, ".gitignore")
        with open(gitignore_path, "w") as file:
            file.write(gitignore_content)
        print(f"Created .gitignore in {self.project_path}")

    def _open_vscode(self):
        subprocess.run(["code", self.project_path], check=True)
        print(f"Opened VS Code in {self.project_path}")
