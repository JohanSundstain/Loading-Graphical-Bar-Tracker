from setuptools import setup, find_packages

setup(
    name="lgbt",  # Уникальное имя пакета
    version="1.0.1",  # Версия
    packages=find_packages(),  # Автоматический поиск модулей
    install_requires=[],  # Сюда можно добавить зависимости
    author="Johan Sundstain",
    author_email="johansundstainx@gmail.com",
    description="Rainbow tqdm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[ 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)