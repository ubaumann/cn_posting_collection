FROM python:3.12

WORKDIR /data
ADD . .
RUN pip install --root-user-action=ignore textual-web &&\
    pip install --root-user-action=ignore posting tree-sitter==0.24.0 &&\
    pip install --root-user-action=ignore cryptography
RUN chmod u=rx,g=r,o=r entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "python", "run.py" ]
