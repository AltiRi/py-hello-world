from setuptools import setup

setup(
    name="py-hello-world",
    version="0.0.1",
    entry_points={
        "console_scripts": [
            "py-hello-world = main:say_hi",
        ]
    }
)
