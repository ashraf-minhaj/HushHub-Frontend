<div align="center">

# Hush Hub
*Share thoughts wihtout letting them know who you are*
![banner](docs/banner.png)

![](https://img.shields.io/badge/License-MIT%20License-red?style=plastic&logo=mit)&nbsp;
![](https://img.shields.io/badge/NodeJs-18-yellow?style=plastic&logo=javascript)&nbsp;
![](https://img.shields.io/badge/EJS--yellow?style=plastic&logo=javascript)&nbsp;
</div>

### Environment variable file
The file should be named as `.env`, devs will get the dev env from the lead. no env specific things should reside on the repository.

### Refactoring
- If gitignore is not taking changes, reason is Git's cache hasn't been refreshed to reflect the changes in Gitignore.

    ```bash
    git rm -r --cached
    git add . .
    ```

> ashraf minhaj