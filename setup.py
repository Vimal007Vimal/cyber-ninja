from setuptools import setup, find_packages

setup(
    name="cyberninja",
    version="0.1",
    description="A tool for hunting down social media accounts by username across networks.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Vimal",
    author_email="2004.vimald@gmail.com",
    url="https://github.com/vimal007/cyberninja",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4',
        'bs4',
        'certifi',
        'colorama',
        'lxml',
        'PySocks',
        'requests',
        'requests-futures',
        'soupsieve',
        'stem',
        'torrequest'
    ],
)
