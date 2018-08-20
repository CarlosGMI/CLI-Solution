from setuptools import setup

setup(
    name = 'CLISolution',
    version = '0.1',
    py_modules = ['CLISolution'],
    install_requires = ['Click','eyed3'],
    entry_points = '''
        [console_scripts]
        cliS=CLISolution:main
    '''
)