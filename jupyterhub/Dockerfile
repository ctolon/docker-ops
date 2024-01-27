ARG JUPYTERHUB_TAG
FROM jupyterhub/jupyterhub:4.0.1

# Install postgres dependencies
RUN apt-get update 
RUN apt-get install -y libpq-dev python3-dev build-essential


# Install Pip Requirements
RUN pip install --upgrade pip
COPY config/requirements.txt .
RUN pip install -r requirements.txt

# Copy TLS certificate and key
#ENV SSL_CERT /srv/jupyterhub/secrets/jupyterhub.crt
#ENV SSL_KEY /srv/jupyterhub/secrets/jupyterhub.key
#COPY ./secrets/*.crt $SSL_CERT
#COPY ./secrets/*.key $SSL_KEY
#RUN chmod 700 /srv/jupyterhub/secrets && \
#    chmod 600 /srv/jupyterhub/secrets/*