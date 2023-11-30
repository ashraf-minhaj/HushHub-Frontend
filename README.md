# Hush Hub
Share thoughts wihtout letting them know who you are

### Refactoring
- If gitignore is not taking changes, reason is Git's cache hasn't been refreshed to reflect the changes in Gitignore.

    ```bash
    git rm -r --cached
    git add . .
    ```

> ashraf minhaj