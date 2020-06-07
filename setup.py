import setuptools

setuptools.setup(name="osmapy",
                 author="Philipp Rigoll",
                 version="0.0.1.5",
                 author_email="philipp@rigoll.de",
                 url="https://github.com/PhilippRigoll/osmapy",
                 packages=setuptools.find_packages(),
                 include_package_data=True,
                 install_requires=[
                     "numpy",
                     "Pillow",
                     "PyYAML",
                     "PySide2",
                     "easydict",
                     "lxml",
                     "requests",
                     "gpxpy",
                     "dataclasses;python_version<'3.7'"
                 ],
                 python_requires=">=3.6",
                 entry_points={
                     "console_scripts": ["osmapy=osmapy.main:main"]
                 })
