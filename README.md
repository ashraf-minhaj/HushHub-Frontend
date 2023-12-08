<div align="center">

# Hush Hub
*Share thoughts wihtout letting them know who you are*
![banner](docs/banner.png)

![](https://img.shields.io/badge/License-MIT%20License-red?style=plastic&logo=mit)&nbsp;
![](https://img.shields.io/badge/NodeJs-18-yellow?style=plastic&logo=javascript)&nbsp;
![](https://img.shields.io/badge/EJS--yellow?style=plastic&logo=javascript)&nbsp;
</div>

### setup local development envionment 
- Install latest version of docker in your system
- Install python3 on your system (should come with your distro BTW)

- go to the `tools` dir and run tool - 
  You just need to remember the `image_tag`, the tool handles the rest.
    ```
        $ sudo python3 devtool.py <arg> <value>
    ```

- list of args -
    ``` 
        arg          -   value
        help       
        build           image_tag 
        list_images 
        run             image_tag 
        stop            image_tag or all
        logs            image_tag
        errors          image_tag (todo)
    ```

### Environment variable file
The file should be named as `.env`, devs will get the dev env from the lead. no env specific things should reside on the repository.

### Refactoring
- If gitignore is not taking changes, reason is Git's cache hasn't been refreshed to reflect the changes in Gitignore.

    ```bash
    git rm -r --cached
    git add . .
    ```

- if you are a mac OSX user and facing permission issue please change setting on your docker-desktop application - 

    ```
    In Preferences > General there is an option "Use gRPC FUSE for file sharing" which is by default checked. Uncheck that option Apply and restart.
    ```

> ashraf minhaj