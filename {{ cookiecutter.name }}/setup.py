from setuptools import setup
from {{ cookiecutter.package }} import NAME


with open("README.rst") as fo:
    README = fo.read()

setup(
    name=NAME,
    description=README.split("\n")[0],
    long_description=README,
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.url }}",
    packages=["{{ cookiecutter.package }}"],
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.package }}={{ cookiecutter.package }}.cli:main",
        ]
    }
)
