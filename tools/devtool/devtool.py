""" ********** DevTool ***************
******** for HushHub Frontend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 25-12-2023

a docker wrapper tool for local development env.
"""


from subprocess import Popen, PIPE, STDOUT
import typer

local_compose_file = "docker-compose-dev.yml"

app = typer.Typer()

def run_command(job, command):
    """ runs command and ret err code """
    print(f"Executing command: {command}")
    command_response = Popen(f"({command})", stderr=PIPE, stdout=PIPE, shell=True, executable="/bin/bash")
    output, errors = command_response.communicate()

    print(output.decode("utf-8"))
    if command_response.returncode != 0:
        print(f"{job} went wrong!")
        print(errors.decode("utf-8"))
    # if command_response.returncode == 0:
    #     print(f"{job} success")

    return output, command_response.returncode

def run_with_stream(command):
    print(f"Executing command: {command}")
    with Popen(f"({command})", stdout=PIPE, stderr=STDOUT, shell=True, executable="/bin/bash") as process:
        for line in process.stdout:
            print(line.decode('utf8'))

# def build_image(image_tag):
#     """ build docker image by given command. """
#     command = f"cd ../app; docker build -t {image_tag} -f {local_docker_file} ."
#     # command = f"cd ../app; ls"
#     # _, err = run_command(job=f"building {image_tag}", command=command)
#     # if err != 0:
#     #     print("error, notify devops team")
#     run_with_stream(command)

@app.command()
def run_app(detach: bool = False):
    """ run the application. """
    print(f"Runing app")
    if detach:
        command = f"cd ../app; docker compose -f {local_compose_file} up --build -d"
    else:
        command = f"cd ../app; docker compose -f {local_compose_file} up --build"
        run_with_stream(command)
        return
    _, err = run_command(job=f"Running app", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def stop():
    """ stop the running application. """
    print(f"stopping app")
    command = f"cd ../app; docker compose -f {local_compose_file} down"

    _, err = run_command(job=f"Stopping local env", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def get_logs(image_tag: str = "app-frontend"):
    """ get application logs."""
    command = f"docker logs $(docker ps -a -q --filter ancestor={image_tag})"
    _, err = run_command(job=f"Getting logs for {image_tag}", command=command)
    if err != 0:
        print("error, notify devops team")

@app.command()
def get_errors(image_tag: str = "app-frontend"):
    """ get application errors."""
    command = f"docker logs $(docker ps -a -q --filter ancestor={image_tag}) | grep error"
    _, err = run_command(job=f"Getting logs for {image_tag}", command=command)
    if err != 0:
        print("Probably no error found, if you are sure otherwise - notify devops team")

@app.command()
def list_images():
    """ get list of images. """
    command = f"docker images"
    _, err = run_command(job=f"getting images", command=command)
    if err != 0:
        print("error, notify devops team")

if __name__ == "__main__":
    print("Thanks for using the tool, let us know if you face any bugs.")
    app()