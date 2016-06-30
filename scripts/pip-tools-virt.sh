#!/bin/sh
#
# Hack: pip-tools doesn't yet support pip 8.1.2
#
# ./virt_piptools/bin/pip-compile --header --index --annotate -o rdrf/runtime-requirements.txt rdrf/runtime-requirements.in
#
virtualenv virt_piptools
. virt_piptools/bin/activate
pip --version
pip install pip==8.1.1 --upgrade
pip --version
pip install pip-tools
