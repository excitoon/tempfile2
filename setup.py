import setuptools


setuptools.setup(
    name = 'tempfile2',
    version = '0.1.1',
    description = '`tempfile` wrapper',
    long_description = '`tempfile` wrapper with slightly more convenient interface.',
    url = 'https://github.com/excitoon/tempfile2',
    author = 'Vladimir Chebotarev',
    author_email = 'vladimir.chebotarev@gmail.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords = 'tempfile',
    packages = ['tempfile2'],
    install_requires = [],
    extras_require = { 'dev' : [], 'test' : [] },
    package_data = {},
    data_files = [],
    entry_points = { 'console_scripts' : [] },
    project_urls = {
        'Bug Reports' : 'https://github.com/excitoon/tempfile2/issues',
        'Documentation' : 'https://github.com/excitoon/tempfile2/blob/master/README.md',
        'Source' : 'https://github.com/excitoon/tempfile2'
    }
)
