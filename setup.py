from setuptools import setup, find_packages


def install_requirements():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f.readlines() if line != '' ]


setup(
    name="preplay",
    version="0.0.1",
    packages=find_packages(".", include=["pre_play", "flow"]),
    requires=install_requirements()
)



