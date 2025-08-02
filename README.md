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

You can run the container with various options supported by `run.py`:

```bash
docker run --rm -it \
  -e DEVICE="sw01-pod-1.network.garden" \
  -e DEVICE_USER="ins" \
  -e DEVICE_PASSWORD="REPLACE_WITH_PASSWORD" \
  -e API_SERVER="10.255.255.254:8080" \
  -e APP_NAME=sw01 \
  ghcr.io/ubaumann/cn_posting_collection:main \
  python run.py
```

### Common options for `run.py`:

Example getting encrypted keys using http:

```bash
docker run --rm -it \
  -e DEVICE="sw01-pod-1.network.garden" \
  -e DEVICE_USER="ins" \
  -e DEVICE_PASSWORD="REPLACE_WITH_PASSWORD" \
  -e API_SERVER="10.255.255.254:8080" \
  -e APP_NAME=sw01 \
  -e APP_ACCOUNT="pod-1" \
  -e KEY_LOCATION="http://10.255.255.254:8000" \
  -e DECRYPTION_KEY="yJ3RNNOyeGc2NRVzR4PbwKf79_D9fQtlvCL7cIcXJKQ=" \
  ghcr.io/ubaumann/cn_posting_collection:main \
  python run.py
```

When the environment variable `APP_ACCOUNT` is set, the run.py script tries to get the key from `KEY_LOCATION/account`.  
- `KEY_LOCATION` defaults to a local directory (e.g., `.keys/`).  
- If `KEY_LOCATION` starts with `http`, the key is fetched via HTTP GET.  
- If `DECRYPTION_KEY` is set, the key is decrypted using the Fernet algorithm.
