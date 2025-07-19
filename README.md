# Posting collection for Cisco 9300 Switch - RESTconf


## Start Posting for sw01-pod-1.network.garden

```bash
posting --collection . --env sw01-pod-1.env
```

### Docker

```bash
docker run --rm -it -e DEVICE="sw01-pod-1.network.garden" -e DEVICE_USER="ins" -e DEVICE_PASSWORD="ins@lab" ghcr.io/ubaumann/cn_posting_collection posting --collection . --env .env
```

## Using in the terminal

### Copy

Mark the text and press "c".

### Paste

Press "Shift" + "INS"
