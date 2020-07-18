#! /bin/bash -e
image_name='cppad_py.img'
container_name='cppad_py.con'
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
    echo $*
    eval $*
}
command="$1"
if [ "$1" != 'image' ] && \
    [ "$1" != 'start' ] && \
    [ "$1" != 'continue' ] && \
    [ "$1" != 'copy' ]
then
    echo 'usage: ./dock_cpapd_py.sh (image|start|continue|copy)'
    exit 1
fi
if [ "$command" == 'copy' ]
then
    read -p 'name of file to copy: ' file_name
    read -p 'copy From or To the container [F/T]: ' direction
    if [ "$direction" == 'F' ]
    then
        echo_eval docker cp $container_name:$file_name $file_name
    elif [ "$direction" == 'T' ]
    then
        echo_eval docker cp $file_name $container_name:$file_name 
    else
        echo 'direction is not F (from) or T (to)'
        exit 1
    fi
    echo 'dock_cppad_py.sh copy: OK'
    exit 0
fi
if [ "$command" == 'continue' ]
then
    count=$(docker ps -a | grep " $container_name\$" | wc -l)
    if [ $count != '1' ]
    then
        docker ps -a 
        echo "There should be one and only one $container_name container"
        exit 1
    fi
    # enter the container
    echo "docker exec -it $container_name bash"
    if ! docker exec -it $container_name bash
    then
        echo "dock_cppad_py.sh: container $container_name exits code non zero"
        echo "Perhaps you need to start it with the command"
        echo "docker start $container_name"
        exit 1
    fi
    #
    echo 'dock_cppad_py.sh continue: OK'
    exit 0
fi
if [ "$command" == 'start' ]
then
    # check that the previous dismod_at container has been deleted
    if docker ps -a | grep " $container_name\$" 
    then
        echo 'dock_dismod_at.sh Error'
        echo "Must first remove the old $container_name container:"
        echo "	docker stop $container_name"
        echo "	docker rm $container_name"
        exit 1
    fi
    # create a new dismod_at container
    echo "echo 'exit 0' | docker run -i --name $container_name $image_name bash"
    echo 'exit 0' | docker run -i --name $container_name $image_name bash
    #
    # start up the container
    echo "docker start $container_name"
    docker start $container_name
    #
    # enter the container
    echo "docker exec -it $container_name bash"
    docker exec -it $container_name bash
    #
    echo 'dock_cppad_py.sh start: OK'
    exit 0
fi
# ---------------------------------------------------------------------------

if [ "$command" != 'image' ]
then
    echo 'dock_cppad_py.sh: Program error'
    exit 0
fi
if [ -e 'Dockerfile' ]
then
    echo 'dock_cppad_py.sh image: Must first remove ./Dockerfile'
    exit 1
fi
if docker ps -a | grep "$image_name" > /dev/null
then
    echo 'dock_cppad_py.sh Error'
    echo 'Must first remove following docker containers:'
    docker ps -a | head -1
    docker ps -a | grep "$image_name"
    echo 'Use the following command:'
    echo "docker rm $container_name"
    exit 1
fi
if docker images | grep "^$image_name " > /dev/null
then
    echo 'dock_cppad_py.sh Error'
    echo 'Must first remove following docker images:'
    docker images | head -1
    docker images | grep "^$image_name "
    echo 'Use the following command for each image above:'
    echo "docker rmi $image_name"
    exit 1
fi
echo 'Creating Dockerfile'
cat << EOF > Dockerfile
# -----------------------------------------------------------------------------
# Ubuntu 19.10 with cppad_py requirements 
# -----------------------------------------------------------------------------
FROM ubuntu:latest
RUN  apt-get update
RUN  DEBIAN_FRONTEND=noninteractive apt-get install -y  \
cmake \
git \
python3 \
python3-pip \
vim \
swig
#
RUN pip3 install numpy 
EOF
echo "Creating $image_name"
docker build --tag $image_name .
#
echo "dock_cppad_py.sh $command: OK"
exit 0
# ----------------------------------------------------------------------------
echo 'dock_cppad_py.sh image: OK'
exit 0
