# Dotfiles

## Usage

- Clone the repo in the home dir:

    ```shell
    git clone https://github.com/Piagrammist/dotfiles "$HOME"
    ```
- Install the packages:

    ```shell
    sudo pacman -S - < ~/pacman-ls
    ```

- Run Nitrogen to set the wallpaper:

    ```shell
    nitrogen
    ```

## Git Credential Manager

```shell
git-credential-manager configure
git config --global credential.credentialStore gpg
gpg --gen-key
# get <gpg-id> from above command
pass init <gpg-id>
```
