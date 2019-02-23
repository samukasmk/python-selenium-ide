

def test_module_import():
    import sys
    cached_modules = [k for k in sys.modules.keys() if k.startswith('selenium_ide')]

    for selenium_module in cached_modules:
        del sys.modules[selenium_module]

    from selenium_ide.runner import SeleniumIDE  # noqa

