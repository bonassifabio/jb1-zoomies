from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='jb1-zoomies',
    version='0.2',
    description='A Sphinx extension to integrate Viewer.js for image zooming.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Fabio Bonassi',
    author_email='fabio.bonassi@polimi.it',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['sphinx>=4.0'],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
