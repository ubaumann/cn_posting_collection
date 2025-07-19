FROM python:3.12

WORKDIR /data
ADD . .
RUN pip install --root-user-action=ignore textual-web &&\
    pip install --root-user-action=ignore posting
RUN chmod u=rx,g=r,o=r entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
CMD [ "python", "run.py" ]
