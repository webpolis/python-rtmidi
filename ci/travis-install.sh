#!/bin/bash
#
# travis-install.sh - Install build dependencies in Travis CI environment
#

set -ev

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    # Install macOS / OS X build dependencies (i.e. Python) via official
    # installers from python.org
    wget -O python.pkg "$PYTHON_INSTALLER_URL"
    test "$(md5 -q python.pkg)" = $PYTHON_INSTALLER_MD5
    sudo installer -pkg python.pkg -target /
elif [[ $TRAVIS_OS_NAME == 'linux' ]]; then
    # Install Linux build dependencies via package manager
    sudo apt-get -y install build-essential libasound2-dev libjack-jackd2-dev
else
    echo "Unsupported build OS environment $TRAVIS_OS_NAME. Aborting." > /dev/stderr
    exit 1
fi

$PYTHON --version
# Update packaging tools
$PYTHON -m pip --disable-pip-version-check install --user -U pip setuptools wheel
# Install Python build and deployment dependencies
$PYTHON -m pip install --user -U Cython twine
# Show installed Python packages
$PYTHON -m pip freeze --all
