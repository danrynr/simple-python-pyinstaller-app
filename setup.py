from setuptools import setup

setup(
    name='simple-python-pyinstaller-app',
    version='1.0.0',
    author='Daniel Reynard Kurniawan',
    python_requires='>=2.7',
    install_requires=[
        'pyinstaller',
    ],
    py_modules=[
        'add2vals',
    ],
    entry_points={
        'console_scripts': [
            'simple-python-pyinstaller-app = simple_python_pyinstaller_app.__main__:main',
        ],
    },
)