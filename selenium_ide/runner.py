import os
import json
from selenium_ide.exceptions import SideFileNotExists, TestCaseNotFound


class SeleniumIDE():
    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.file_encoding = encoding
        self.file_source = None

        self.id = None
        self.name = None
        self.test_cases = []

        self.load_file()

    def load_file(self):
        if not os.path.exists(self.file_path):
            raise SideFileNotExists()

        with open(self.file_path, 'r', encoding=self.file_encoding) as side_file:
            self.file_source = side_file.read()

        json_content = json.loads(self.file_source)
        self.id = json_content.get('id')
        self.name = json_content.get('name')
        self.test_cases = json_content.get('tests')

    def find_test_case(self, name):
        return [t for t in self.test_cases if t.get('name') == name]

    def run(self, test_case):
        pass

    def run_test_case(self, name):
        found_tests = self.find_test_case(name)
        if not found_tests:
            raise TestCaseNotFound('Not found test cases with name ({name}) in file ({self.file_path})')

        for test_case in found_tests:
            self.run(test_case)

    def run_all_test_cases(self):
        ...
