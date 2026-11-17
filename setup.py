"""Setup script for Timestamp Random Generator Library."""
from setuptools import setup

setup(
    name="randomgen",
    version="0.1.0",
    # Note: This package was developed using Cline + Ollama + Qwen3.5:9b
    author="AI Assistant (Cline)",
    author_email="",
    description="A Python library for generating pseudo-random numbers using system timestamps and CPU clock cycles.",
    long_description=None,
    url="https://github.com/yukata13/rand-gen",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    # Package structure: randomgen/ directory at root level with submodules
    packages=["randomgen", "randomgen.generators", "randomgen.utils", "randomgen.tests"],
    install_requires=[],
    license="MIT",
)