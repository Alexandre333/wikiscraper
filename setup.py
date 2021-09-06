from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'Easy scraper that extracts data from Wikipedia articles thanks to its URL slug'

# Setting up
setup(
    name="easywiki",
    version=VERSION,
    author="Alexandre Meyer",
    author_email="contact@alexandremeyer.fr",
    description=DESCRIPTION,
    url='https://github.com/Alexandre333/easy_wiki',
    long_description=file: README.md,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
    keywords=['python', 'web scraping', 'wikipedia', 'slug'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)