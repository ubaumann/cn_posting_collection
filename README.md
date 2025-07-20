# Posting collection for Cisco 9300 Switch - RESTconf


## Start Posting for sw01-pod-1.network.garden

```bash
posting --collection . --env sw01-pod-1.env
```

### Docker

```bash
docker run --rm -it -e DEVICE="sw01-pod-1.network.garden" -e DEVICE_USER="ins" -e DEVICE_PASSWORD="REPLACE_WITH_PASSWORD" ghcr.io/ubaumann/cn_posting_collection:main posting --collection . --env .env
```

## Using in the terminal

### Copy

Mark the text and press "c".

### Paste

Press "Shift" + "INS"


## Run container and connect to ganglion

```bash
docker run --rm -it -e DEVICE="sw01-pod-1.network.garden" -e DEVICE_USER="ins" -e DEVICE_PASSWORD="REPLACE_WITH_PASSWORD" -e API_SERVER="10.255.255.254:8080" ghcr.io/ubaumann/cn_posting_collection:main
```
