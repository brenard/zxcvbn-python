from setuptools import setup
import os, subprocess

with open('README.rst') as file:
    long_description = file.read()

if not os.path.exists('.currently_generating_catalog'):
    open('.currently_generating_catalog', 'ab').close()
    subprocess.call('python setup.py compile_catalog', shell=True)
    os.remove('.currently_generating_catalog')

def create_mo_files():

    data_files = []
    localedir = 'zxcvbn/locale'
    po_dirs = [localedir + '/' + l + '/LC_MESSAGES/'
               for l in next(os.walk(localedir))[1]]
    for d in po_dirs:
        mo_files = []
        po_files = [f for f in next(os.walk(d))[2]
                      if os.path.splitext(f)[1] == '.po']
        for po_file in po_files:
            filename, extension = os.path.splitext(po_file)
            mo_file = filename + '.mo'
#            msgfmt_cmd = 'msgfmt {} -o {}'.format(d + po_file, d + mo_file)
#            subprocess.call(msgfmt_cmd, shell=True)
            mo_files.append(d + mo_file)

        # install in $PREFIX/share/locale/
        distdir = os.path.join('share', '/'.join(d.split('/')[1:]))
        data_files.append((distdir, mo_files))
    return data_files

setup(
    name='zxcvbn',
    version='4.4.28',
    packages=['zxcvbn'],
    url='https://github.com/dwolfhub/zxcvbn-python',
    download_url='https://github.com/dwolfhub/zxcvbn-python/tarball/v4.4.28',
    license='MIT',
    author='Daniel Wolf',
    author_email='danielrwolf5@gmail.com',
    long_description=long_description,
    keywords=['zxcvbn', 'password', 'security'],
    entry_points={
        'console_scripts': [
            'zxcvbn = zxcvbn.__main__:cli'
         ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    message_extractors={'zxcvbn': [
        ('**.py', 'python', None),
    ]},
    data_files = create_mo_files(),
)
