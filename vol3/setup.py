# -*- coding:utf-8 -*-
import os
from setuptools import setup, find_packages


curdir = os.path.abspath(os.path.dirname(__file__))
local_uri = "file://{directory}/extra_eggs/{module}"
dependency_links = [
    local_uri.format(directory=curdir, module=x)
    for x in [
        #"bpmappers-0.6dev-py2.7.egg#egg=bpmappers-0.6dev",
    ]
]


requirements = [
    "Django==1.4",
    #"python-dateutil==1.5",
]


development_requirements = [
]


tests_require = [
]


entry_points = {
    "console_scripts": [
        #"runtest=vol3.commands.runtest:main",
    ],
}


def main():
    setup(
        name="vol3",
        install_requires=requirements,
        tests_require=tests_require,
        extras_require={
            "testing": tests_require,
            "dev": development_requirements,
        },
        packages=find_packages("src"),
        package_dir={"": "src"},
        entry_points=entry_points,
        dependency_links=dependency_links,
    )


if __name__ == "__main__":
    main()
