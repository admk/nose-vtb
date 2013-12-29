from setuptools import setup


setup(
    name='nose-vtb',
    version='0.1',
    url='https://github.com/admk/nose-vtb',
    author='Xitong Gao',
    author_email='@'.join(['gxtfmx', 'gmail.com']),
    install_requires=['nose', 'ipython'],
    description=(
        'Nose plugin to format tracebacks with colors and debug details '
        'using IPython.core.ultratb'
    ),
    long_description=open('README.rst').read(),
    keywords=' '.join([
        'test', 'unittest', 'nose', 'nosetests ', 'plugin', 'debug',
        'traceback', 'ipython', 'verbose']),
    py_modules=['vtb'],
    entry_points={'nose.plugins.0.10': ['vtb = vtb:NoseVTB']}
)
