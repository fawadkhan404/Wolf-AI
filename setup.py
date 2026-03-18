from setuptools import setup, find_packages

setup(
    name='wolf-ai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'flask',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'wolf = main:main',
        ],
    },
)