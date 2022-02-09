import docker

client = docker.from_env()

def create_container(container_name, unique_id):
    try:
        client.containers.run(container_name, name=f"{container_name}_{unique_id}", detach=True)
        return True
    except Exception as e:
        return False

def kill_container(container_name, unique_id):
    try:
        container = client.containers.get(f"{container_name}_{unique_id}")
        container.remove(force=True)
    except Exception as e:
        return False

def container_exists(container_name, unique_id):
    try:
        container = client.containers.get(f"{container_name}_{unique_id}")
        return True
    except docker.errors.NotFound as e:
        return False

if __name__ == "__main__":
    if not container_exists("demodocker", "rushi"):
        print("Creating container")
        create_container("demodocker", "rushi")
    else:
        print("Killing container")
        kill_container("demodocker", "rushi")