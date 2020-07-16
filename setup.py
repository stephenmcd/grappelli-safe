
from setuptools import setup, find_packages

setup(
    name="grappelli_safe",
    version="0.5.2",
    description="A snapshot of the grappelli_2 branch of django-grappelli, "
                "packaged as a dependency for the Mezzanine CMS for Django.",
    long_description=open("README.rst").read(),
    license="BSD 3-clause",
    author="Patrick Kranzlmueller, Axel Swoboda (vonautomatisch)",
    author_email="werkstaetten@vonautomatisch.at",
    maintainer="Stephen McDonald",
    maintainer_email="stephen.mc@gmail.com",
    url="http://github.com/stephenmcd/grappelli-safe/",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.8",
    ],
)
