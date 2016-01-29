def test_import():
    from {{ cookiecutter.package }} import NAME
    NAME
    
if __name__ == "__main__":
    test_import()
