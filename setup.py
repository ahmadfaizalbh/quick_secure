from setuptools import setup

setup(
    name='quick_secure',
    version='0.2.1.1',
    py_modules=['quick_secure'],
    author="Ahmad Faizal B H",
    author_email="ahmadfaizalbh726@gmail.com",
    url="https://github.com/ahmadfaizalbh/quick_secure",
    data_files=[],
    long_description=open('README.rst').read(),
    packages=['quick_secure'],
    license='MIT',
    keywords='Quick secure is for encryption and decryption of string',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir={'quick_secure': 'quick_secure'},
)
