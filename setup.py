
import os
from setuptools import setup, find_namespace_packages

def get_version():
    try:
        import ivpm
        return ivpm.get_pkg_version(__file__)
    except:
        return "0.0.0"


setup(
  name = "pybfms-tilelink",
  packages=find_namespace_packages(where='src'),
  package_dir = {'' : 'src'},
  version=get_version(),
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("Tilelink BFMs provides a Python Tilelink agent."),
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "BFMs"],
  url = "https://github.com/pybfms/tilelink_bfms",
  setup_requires=[
    'setuptools_scm',
    'ivpm'
  ],
  install_requires=[
    'pybfms',
  ],
)

