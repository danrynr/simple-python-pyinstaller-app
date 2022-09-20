from setuptools import setup

setup(
    name='simple-python-pyinstaller-app',
    version='1.0.0',
    author='Daniel Reynard Kurniawan',
    python_requires='>=2.7',
    install_requires=[
        'pyinstaller',
        'gunicorn',
    ],
    package_dir={'': 'sources'},
    py_modules=[
        'add2vals',
        'calc',
        'main',
    ],
    html=[
        'templates/index.html',
        'templates/result.html',
    ],
    entry_points={
        'console_scripts': [
            'simple-python-pyinstaller-app = simple_python_pyinstaller_app.__main__:main',
        ],
    },
)