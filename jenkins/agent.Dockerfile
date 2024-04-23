FROM jenkins/ssh-agent:jdk17

# Create jenkins home directories
RUN mkdir /var/log/jenkins
RUN mkdir /var/cache/jenkins
RUN chown -R  jenkins:jenkins /var/log/jenkins
RUN chown -R  jenkins:jenkins /var/cache/jenkins

# set timezone
ARG timezone="Europe/Istanbul"
ENV TZ=$timezone

# Install dependencies
RUN apt-get update && apt-get install -qy \
    apt-utils \
    libyaml-dev \
    build-essential \
    libxml2-dev \
    libxslt-dev \
    libffi-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    #python-mysqldb \
    #python-pip3 \
    libjpeg-dev \
    zlib1g-dev \
    libblas-dev\
    liblapack-dev \
    libatlas-base-dev \
    apt-transport-https \
    ca-certificates \
    wget \
    software-properties-common \
    zip \
    unzip \
    git \
    nano \
    vim \
    gfortran \
    jq \
    tzdata \
    curl \
    openrc \
    openntpd \
    python3-pip \
    python3-setuptools \
    python3-dev

# Install docker
# Add Docker's official GPG key:
    RUN apt-get install ca-certificates curl \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc \
    && chmod a+r /etc/apt/keyrings/docker.asc
    
# Add the repository to Apt sources:
RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update -y

# Install Docker CE
RUN apt-get install -qy docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
#ENV VERSION_STRING=5:25.0.3-1~debian.12~bookworm
#RUN apt-get install -y docker-ce=$VERSION_STRING
#RUN apt-get install -y --allow-downgrades docker-ce-cli=$VERSION_STRING
#RUN apt-get install -y containerd.io docker-buildx-plugin docker-compose-plugin

# Clean up
RUN rm -rf /var/lib/apt/lists/*

# add the jenkins user to the docker group so that sudo is not required to run docker commands
#RUN groupmod -g 999 docker && gpasswd -a jenkins docker
RUN gpasswd -a jenkins docker

# Set the docker group id to the same as the host
ENV DOCKER_USER_GID=${DOCKER_USER_GID:-999}
RUN usermod -aG ${DOCKER_USER_GID} jenkins

USER jenkins