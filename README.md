README

Using Visual Studio Code or simply bask

Pre-requisites:
 - XQuartz Server on MacOS https://www.xquartz.org
 - Docker
 - Visual Code (optional)

Using existing image:

1. open project /working directory
2. start up xquarts
3. Start docker (note IP is dynamic): `docker run -it -e DISPLAY=10.0.1.20:0 -p 8888:8888 -p 6006:6006 -v $(pwd)/notebooks:/notebooks --privileged --name tf5 amaksimov/python_data_science`
3. SSH into docker container: `docker exec -it tf5 bash`
4. enter:
<pre>
apt-get update
apt-get install -y python3-tk
cd notebooks
python3 house_price_prediction.py
</pre>


Using docker-compose:
TODO
2. spin up docker engine: `docker-compose up`
3. in another terminal run: `docker exec -it tf4 bash`
apt-get update
apt-get install -y python3-tk
cd notebooks
export HOSTNAME=`hostname`
4. Start
brew install socat
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"


Links:
https://dev-ops-notes.com/docker/howto-run-jupiter-keras-tensorflow-pandas-sklearn-and-matplotlib-docker-container/
https://dzone.com/articles/docker-x11-client-via-ssh
https://github.com/jessfraz/dockerfiles/issues/169