class ReadmeTemplate:
    def __init__(self):
        self.sections = []

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

        return readme

    def generate_badges(self):
        return "[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)\n"

    def generate_authors(self):
        return "\n## Authors \n "

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
        return "\n## License\n\n \n"
