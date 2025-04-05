from setuptools import setup, Extension, find_packages

memtool_ext = Extension(
    'memtool.core',
    sources=['memtool/core.c'],
)

setup(
    name='memtool',
    version='0.1.2',
    description='Memory management and manual allocation library for Python using C',
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author='S7n5c4n',
    author_email='cr.hachim2.0@egmail.com',
    url='https://github.com/s7n5c4n/memtool',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: C",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    packages=find_packages(),
    ext_modules=[memtool_ext],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
