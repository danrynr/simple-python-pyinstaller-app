from setuptools import setup

setup(
    name='simple-python-pyinstaller-app',
    version='1.0.0',
    author='Daniel Reynard Kurniawan',
    python_requires='>=2.7',
    install_requires=[
        'pyinstaller',
        'gunicorn',
        'flask',
    ],
    package_dir={'': 'sources'},
    py_modules=[
        'add2vals',
        'calc',
        'main',
    ],
    entry_points={
        'console_scripts': [
            'simple-python-pyinstaller-app = main:main',
        ],
    },
)