from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='AICreatorPack',
    version='0.0.4',
    description='AI Creator Package By - oren',
    long_description=open('README.txt').read(),
    url='',
    author='oren',
    author_email='orennadle@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='ai',
    packages=["AICreatorPack","AICreatorPack/functions","AICreatorPack/functions/ini"],
    install_requires=['requests']
)
