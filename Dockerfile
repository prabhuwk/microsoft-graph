FROM python:slim-bullseye
COPY . /opt/msgraph_azure/
RUN pip install --upgrade pip && \
    pip install -e /opt/msgraph_azure/
USER msgraph_azure
WORKDIR /opt/msgraph_azure
ENTRYPOINT ["/bin/bash"]
