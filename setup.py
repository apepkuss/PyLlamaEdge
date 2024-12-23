from setuptools import find_packages, setup

setup(
    name="llamaedge",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 在这里添加依赖
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="一个示例Python库",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
