from setuptools import setup


setup(
    name='pre-commit-format-sql',
    description='a pre-commit hook for formatting sql',
    version='0.0.2',
    license='BSD',
    author='tchoedak',
    install_requires=[
        'format-sql'
    ],
    entry_points={
        'console_scripts': ['format=format:main']
    }
)
