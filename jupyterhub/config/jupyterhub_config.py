import os
from dockerspawner import DockerSpawner
import docker
from jinja2 import Template

c = get_config()  # noqa: F821

c.JupyterHub.allow_named_servers = True
c.JupyterHub.cleanup_servers = False
c.JupyterHub.log_level = 10

# Get docker images as hardcoded list
# c.DockerSpawner.image_whitelist = {
#    "minimal"     : "jupyter/minimal-notebook:latest",
#    "all-spark"   : "jupyter/all-spark-notebook:latest",
#    "single-user" : "jupyterhub/singleuser:1.2",
#    "test": "test"
# }

c.DockerSpawner.cmd = "start-singleuser.sh"

# Define a custom spawner class that inherits from DockerSpawner and Gets all docker images from baremetal host
class CustomDockerSpawner(DockerSpawner):
    async def options_form(self, spawner):
        # Get the list of available Docker images
        client = docker.from_env()
        all_images = client.images.list()

        # Build the list of image choices, only including images with tags
        image_choices = []
        for image in all_images:
            tags = image.tags
            if tags:
                image_choices.append((tags[0], tags[0]))

        # Generate the form to select Docker images
        form_template_str = """
        <label for="select-image">Select a Docker image:</label>
        <select class="form-control" name="image" required>
            {% for image in image_choices %}
                <option value="{{ image[0] }}">{{ image[1] }}</option>
            {% endfor %}
        </select>
        """
        template = Template(form_template_str)
        return template.render(image_choices=image_choices)

    def options_from_form(self, formdata):
        # Retrieve the selected Docker image from the submitted form
        options = {}
        options['image'] = formdata.get('image', [''])[0]
        return options

c.JupyterHub.spawner_class = CustomDockerSpawner
# c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"

# Set Timeout
c.DockerSpawner.start_timeout = 300
# c.DockerSpawner.http_timeout = 120


# Network name for the containers to connect to
network_name = "jupyterhub-net"
c.DockerSpawner.network_name = network_name #  project name + jupyterhub-net


# Proxy Settings
c.DockerSpawner.use_internal_ip = True
c.JupyterHub.hub_ip = "0.0.0.0" # 0.0.0.0
c.JupyterHub.hub_port = 8899 # Container Port
c.JupyterHub.hub_connect_ip = "nm-jupyterhub" # Container Hostname/IP of container # 172.13.0.3

# Hub Network Settings
# Hub Host IP address/RP and Container Port and IP/Host of container
c.JupyterHub.ip = "0.0.0.0" 
c.JupyterHub.port = 8199
c.NotebookApp.allow_origin = '*' #allow all origins
c.NotebookApp.allow_remote_access = True

# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 
    'network_mode': network_name,
    "volume_driver": "local", 
}


# User Authentication Section
# c.PAMAuthenticator.admin_groups = {'jupyterhub-admins'}
c.Authenticator.allowed_users = allowed = set()
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()
c.JupyterHub.admin_access = True
pwd = os.path.dirname(__file__)
with open(os.path.join(pwd, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        whitelist.add(name)
        allowed.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)

# Allow users to create their own users
c.LocalAuthenticator.create_system_users = True

# Authenticate users with Native Authenticator
c.JupyterHub.authenticator_class = "native"

#  Setting to an empty string disables authentication altogether, which is NOT RECOMMENDED.
c.NotebookApp.token = ''

# Allow anyone to sign-up without approval
c.NativeAuthenticator.open_signup = True

# TLS config Section
c.ConfigurableHTTPProxy.should_start = False
c.ConfigurableHTTPProxy.api_url = 'https://jupyterhub-proxy:8030'
c.JupyterHub.internal_ssl = True
c.JupyterHub.internal_certs_location = os.environ['INTERNAL_SSL_PATH']
c.JupyterHub.trusted_alt_names = ["DNS:nm-jupyterhub", "DNS:jupyterhub-proxy"]
#c.JupyterHub.port = 443
#c.JupyterHub.ssl_key = os.environ['SSL_KEY']
#c.JupyterHub.ssl_cert = os.environ['SSL_CERT']

#c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
#    'jupyterhub_cookie_secret')

c.DockerSpawner.extra_create_kwargs = {'user': 'root'}
#c.DockerSpawner.extra_host_config = {'runtime': 'nvidia'}

# DB Connection String
c.JupyterHub.db_url = 'postgresql://postgres:{password}@{host}:{port}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    port=os.environ['POSTGRES_PORT'],
    password=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB'],
)


# Notebook directory (For docker spawner is / and for normal spawner is ~/notebooks)
c.DockerSpawner.notebook_dir = "/"
c.Spawner.notebook_dir = '~/notebooks'

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container

#c.DockerSpawner.volumes = {
#          'jupyterhub-user-{username}': '/',
#          'jupyterhub-shared': '',
#          'jupyterhub-data': '/home/jovyan/work/data'
#}

# Remove containers once they are stopped
c.DockerSpawner.remove_containers = True

# Default URL for JupyterHub
c.DockerSpawner.default_url = '/lab'
c.Spawner.default_url = '/lab'


# Collab accounts
c.JupyterHub.load_roles = []
c.JupyterHub.load_groups = {
    # collaborative accounts get added to this group
    # so it's easy to see which accounts are collaboration accounts
    "collaborative": [],
}

