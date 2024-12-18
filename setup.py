from setuptools import find_packages, setup

setup(
    name="play-mobile",
    version="1.0.0",
    license="MIT",
    download_url="https://github.com/Omni-Libraries/play-mobile.git",
    changelog="https://play-mobile.mukhsin.space/installation",
    documentation="https://play-mobile.mukhsin.space",
    bug="https://github.com/Omni-Libraries/play-mobile.git/issues",
    description="A Python library for SMS authentication using Play Mobile API",
    long_description=open("docs/index.md").read(),
    long_description_content_type="text/markdown",
    author="Mukhsin Mukhtorov",
    author_email="mukhsinmukhtorov@arizona.edu",
    maintainer="Mukhsin Mukhtorov",
    maintainer_email="mukhsinmukhtorov@arizona.edu",
    url="https://github.com/Omni-Libraries/play-mobile.git",
    keywords="sms-authentication, otp, sms-verification, sms-auth, play-mobile-api, python-sms, sms-workflows, uzbekistan-sms, otp-python, two-factor-authentication, 2fa",
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests",
        "python-dotenv>=1.0.1"
    ],
    extras_require={
        'django':['Django>=4.2'],
        'drf':['djangorestframework>=3.12.3'],
        'flask':['Flask>=3.0.0'],
        'fastapi':['fastapi>=0.115.0'],
    },
    project_urls = {
        "Documentation":"https://play-mobile.mukhsin.space",
        "Source":"https://github.com/Omni-Libraries/play-mobile.git",
        "Tracker":"https://github.com/Omni-Libraries/play-mobile.git/issues",
    },
)
