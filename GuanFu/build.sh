
sudo docker build -t dettrace:guanfu .

###--env HTTPS_PROXY=$https_proxy
sudo docker run -it -v $(pwd)/mount:/home/rebuild/mount --env HTTPS_PROXY=$https_proxy  --network host  --rm --privileged dettrace:guanfu  /bin/bash   /home/rebuild/start.sh