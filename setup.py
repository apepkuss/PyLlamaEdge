from setuptools import find_packages, setup

# Add these lines at the top
with open("requirements.txt") as f:
    requirements = [
        line.strip() for line in f if line.strip() and not line.startswith("#")
    ]

setup(
    name="llamaedge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Liu Xin",
    author_email="xin.sam.liu@hotmail.com",
    description="Python library for LlamaEdge",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/apepkuss/PyLlamaEdge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
