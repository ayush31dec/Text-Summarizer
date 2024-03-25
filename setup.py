import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHER_USER_NAME = "ayush31dec"
SRC_REPO_NAME = "textSummarizer"
AUTHOR_EMAIL = "ayugupt2506@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHER_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)