import pytest
from selenium_ide.runner import SeleniumIDE
from selenium_ide.exceptions import SideFileNotExists,  TestCaseNotFound


def test_instantiating_runner_with_existing_file():
    SeleniumIDE('test_cases/GoogleSearch.side')


def test_instantiating_runner_with_non_existing_file():
    with pytest.raises(SideFileNotExists):
        SeleniumIDE('/non/existing/file')


def test_runner_google_search_load_side_file():
    runner = SeleniumIDE('test_cases/GoogleSearch.side')

    assert runner.file_path != None
    assert runner.file_encoding == 'utf-8'
    assert isinstance(runner.file_source, str)
    assert runner.id == "10147271-c6c2-4431-8739-77c1ec334968"
    assert runner.name == "Test"
    assert len(runner.test_cases) == 2
    assert any(runner.find_test_case('Google Search'))
    assert any(runner.find_test_case('Selenium Site'))


def test_runner_run_non_existing_test_case_by_name():
    runner = SeleniumIDE('test_cases/GoogleSearch.side')

    with pytest.raises(TestCaseNotFound):
        runner.run_test_case('Non existing test case')


def test_runner_run_test_cases_google_search_by_name():
    runner = SeleniumIDE('test_cases/GoogleSearch.side')

    runner.run_test_case('Google Search')