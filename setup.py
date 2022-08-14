from setuptools import setup, find_packages

setup(
    name="msgraph-azure",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Click",
        "Click-plugins",
        "msgraph-core",
        "azure-identity",
    ],
    entry_points={
        "console_scripts": [
            "msgraph-azure = msgraph_azure.cli:azure",
        ],
    },
    extras_require={
        "development": ["mypy", "black[d]", "flake8", "pytest", "devtools"]
    },
)
