import docker
import random
import yaml

client = docker.from_env()

def create_container(container_name, unique_id, exposed_port):
    try:
        ports = {
            exposed_port: random.randrange(1025, 65534)
        }

        client.containers.run(
            container_name, 
            name=f"{container_name}_{unique_id}", 
            detach=True,
            ports=ports
        )

        return ports[exposed_port]
    except Exception as e:
        print(str(e))
        return -1

def kill_container(container_name, unique_id):
    try:
        container = client.containers.get(f"{container_name}_{unique_id}")
        container.remove(force=True)
        return True
    except Exception as e:
        return False

def container_exists(container_name, unique_id):
    try:
        container = client.containers.get(f"{container_name}_{unique_id}")

        port_bindings = container.attrs["HostConfig"]["PortBindings"]
        keys = list(port_bindings.keys())

        return port_bindings[keys[0]][0]["HostPort"]
    except docker.errors.NotFound as e:
        return -1