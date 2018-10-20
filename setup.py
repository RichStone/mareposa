"""
la maREPOsa allows you to go through all the initiation process of new git/GitHub projects with just a single terminal command.
"""
from setuptools import find_packages, setup

dependencies = ['click']

setup(
    name='mareposa',
    version='1.0.2',
    url='https://github.com/RichStone/mareposa',
    license='MIT',
    author='Richard Rich Steinmetz',
    author_email='richard.had@hotmail.de',
    description='la maREPOsa automates creation of your remote GitHub & local git repositories, gitignore and README.md in one single line of code.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'mareposa = mareposa.cli:mareposa',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
