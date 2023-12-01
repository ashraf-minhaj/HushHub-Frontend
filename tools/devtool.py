""" ********** DevTool ***************
******** for HushHub Frontend ********

    author: ashraf minhaj
    mail: ashraf_minhaj@yahoo.com
    
    date: 02-12-2023
"""

import sys
import docker 

client = docker.from_env()

def build_image(image_name):
    """ build docker image by given command. """
    pass

def run_container(conatiner_tag, to_detach=True):
    print(f"Runing Container {conatiner_tag}")
    client.containers.run(f"{conatiner_tag}", detach=to_detach)

def get_list_of_images():
    print("List of all images")
    images = client.images.list()
    print(images)

if __name__ == "__main__":
    print("Thanks for using the tool, let us know if you face any bugs.")
    try:
        # get user command
        coammand = sys.argv[1]

        if coammand == "help":
            print("""
                  dev tool to enhance developer experience.

                  run - 
                  $ sudo python3 devtool.py <arg> <value>
                  list of args -
                    arg          -   value
                    help            
                    list_images 
                    run_app         image_tag    
                  """)
        if coammand == "run_app":
            print(type(sys.argv[2]))
            run_container(conatiner_tag=f"{sys.argv[2]}")
        if coammand == "list_images":
            get_list_of_images()
        else:
            print("Please pass a valid command, type 'sudo python3 devtool.py help'")
        # get_list_of_images()
    except Exception as e:
        print("error! report to your devops team")
        print(e)