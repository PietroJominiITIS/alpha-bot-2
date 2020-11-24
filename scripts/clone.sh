#!/bin/sh
# Alphabotbot dowload script
# Pietro Jomini

REPO="https://github.com/PietroJominiITIS/alphabotbot"
FNAME="alphabotbot"

if [ ! "$2" = "" ]
then
    FNAME=$2
fi

prepare() {
    git clone               \
        --depth 1           \
        --filter=blob:none  \
        --no-checkout       \
        "$REPO" "$FNAME"
    cd "$FNAME"
}

checkout_common() {
    git checkout master --  \
        '__init__.py'       \
        'src/*.py'          \
        'src/protocol/*'
}

conclude() {
    rm -rf '.git'
    exit 0
}

if [ "$1" = "server" ]
then
    echo "Downloading alphabotbot server..."
    prepare
    checkout_common
    git checkout master --  \
        'server.py'         \
        'src/server/*'
    conclude
elif [ "$1" = "client" ]
then
    echo "Downloading alphabotbot client..."
    prepare
    checkout_common
    git checkout master --  \
        'client.py'         \
        'src/client/*'
    conclude
else
    echo "ERROR :: \$1 should be \`client\` or \`server\`"
    exit 1
fi
