from setuptools import setup, find_packages

setup(
    name="ana",
    version="0.0.1",
    description='A short description of your package',
    author='Ana Keita',
    author_email='keita.kukukhan@gmail.com',    
    packages=["conda"],
    install_requires=[
        'pandas',
        'sqlalchemy'
    ],
    python_requires='>=3.6'
)
