import setuptools

with open('README.rst', 'r', encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(name='xuzhao-markdown-editor',
                 version='1.0',
                 description='xuzhao markdown editor',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author='xuzhao',
                 author_email='markdown@felinae.net',
                 url='https://markdown.felinae.net',
                 keywords='django markdown editor editormd',
                 packages=setuptools.find_packages(),
                 zip_safe=False,
                 include_package_data=True,
                 classifiers=(
                     "Programming Language :: Python",
                     "Development Status :: 4 - Beta",
                     "Operating System :: OS Independent",
                     "License :: OSI Approved :: Apache Software License",
                     "Framework :: Django"
                 ))
