""" ********** DevTool ***************
******** for HushHub Frontend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 02-12-2023
"""

import sys
from subprocess import Popen, PIPE

def run_command(job, command):
    """ runs command and ret err code """
    print(command)
    command_response = Popen(f"({command})", stderr=PIPE, stdout=PIPE, shell=True)
    output, errors = command_response.communicate()

    print(output.decode("utf-8"))
    if command_response.returncode != 0:
        print(f"{job} went wrong!")
        print(errors.decode("utf-8"))
    # if command_response.returncode == 0:
    #     print(f"{job} success")

    return output, command_response.returncode

def build_image(image_name):
    """ build docker image by given command. """
    pass

def run_container(conatiner_tag, to_detach=True):
    print(f"Runing Container {conatiner_tag}")
    pass

def get_list_of_images():
    print("List of all images")
    pass

if __name__ == "__main__":
    print("Thanks for using the tool, let us know if you face any bugs.")
    try:
        # get user command
        coammand = sys.argv[1]

        if coammand == "help":
            print("""
                  dev tool to enhance developer experience.

                  run tool - 
                  $ sudo python3 devtool.py <arg> <value>
                  list of args -
                    arg          -   value
                    help       
                    build_app     
                    list_images 
                    run_app         image_tag    
                    logs            image_tag
                    errors          image_tag
                    
                  """)
        if coammand == "build_app":
            print(type(sys.argv[2]))
        if coammand == "run_app":
            print(type(sys.argv[2]))
            run_container(conatiner_tag=f"{sys.argv[2]}")
        if coammand == "list_images":
            get_list_of_images()
        if coammand == "logs":
            pass
        if coammand == "errors":
            pass
        else:
            print("Please pass a valid command, type 'sudo python3 devtool.py help'")
        # get_list_of_images()
    except Exception as e:
        print("error! report to your devops team")
        print(e)