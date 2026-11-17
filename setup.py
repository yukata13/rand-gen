"""Setup script for Timestamp Random Generator Library."""
from setuptools import setup

setup(
    name="randomgen",
    version="0.1.0",
    author="Yukata13",
    author_email="yukata13@example.com",
    description="A Python library for generating pseudo-random numbers using system timestamps and CPU clock cycles.",
    long_description=None,
    url="https://github.com/yukata13/randomgen",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    # Explicitly define packages at root level as namespace submodules
    packages=["generators", "utils", "tests"],
    install_requires=[],
    license="MIT",
)