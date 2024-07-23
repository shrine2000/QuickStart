import typer
from quickstart.project_initializer import ProjectInitializer

app = typer.Typer()

@app.command()
def init(project_name: str, folder: str):
    """
    Initialize a new project with the given name in the specified folder.
    """
    initializer = ProjectInitializer(project_name, folder)
    initializer.create_project()
    print(f"Project {project_name} initialized in {folder}")

if __name__ == "__main__":
    app()
