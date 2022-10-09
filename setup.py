from setuptools import setup
from setuptools import find_packages

setup(
	name="probtest",
	version="0.0.1",
	description="A Simple Competitive Programming Judge",
	author="Andrei S.",
	author_email="andreisva2023@gmail.com",
	packages=["probtest", "probtest/langs"],
	license="MIT",
	scripts=["scripts/probtest"]
)
