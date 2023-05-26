class GitignoreGenerator:
    def generate(self, ides, frameworks, custom_lines=None):
        ignore_content = self._get_common_ignore_content()
        ignore_content += self._get_ide_specific_ignore_content(ides)
        ignore_content += self._get_framework_specific_ignore_content(frameworks)
        if custom_lines:
            ignore_content += "\n# Custom ignore rules\n\n"
            ignore_content += "\n".join(custom_lines)
        return ignore_content

    def _get_common_ignore_content(self):
        return "# Common ignore rules\n\n"

    def _get_ide_specific_ignore_content(self, ide):
        ignore_content = "# IDE specific ignore rules\n\n"
        if ide == "vscode":
            ignore_content += ".vscode/\n"
        elif ide == "intellij":
            ignore_content += ".idea/\n"
        elif ide == "vim":
            ignore_content += ".vim/\n"
        return ignore_content

    def _get_framework_specific_ignore_content(self, framework):
        ignore_content = "# Framework specific ignore rules\n\n"
        if framework == "nodejs":
            ignore_content += "node_modules/\n"
        elif framework == "express":
            ignore_content += "node_modules/\n"
            ignore_content += "public/\n"
        elif framework == "golang":
            ignore_content += "*.exe\n"
        elif framework == "python":
            ignore_content += "__pycache__/\n"
        elif framework == "java":
            ignore_content += "*.class\n"
        return ignore_content
