import setuptools

with open("README.md",'r',encoding='utf-8')as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="Text-Summarization-NLP"
AUTHOR_NAME="prasantpoudel"
SRC_REPO="Text-Summarization"
AUTHOR_EMAIL="prasantpoudel33@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=" TEXT summarization project using NLP",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_url={
        "bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"","src"},
    packages=setuptools.find_packages(where="src"),
)