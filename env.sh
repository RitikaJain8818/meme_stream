PWD=`pwd`
/usr/local/bin/virtualenv --python=python3 myprojectenv
echo $PWD
activate () {
    . $PWD/myprojectenv/bin/activate
}

activate