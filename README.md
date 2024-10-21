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

- Manually install `paru`, and then:

    ```shell
    paru -S - < ~/aur-ls
    ```

- Set your wallpaper using:

    ```shell
    wall-set "path/to/pic.jpg"
    ```

- Correct your home path in picom config:

    ```
    log-level = "warn";
    log-file = "/home/rz/.local/share/picom/picom.log"; <----
    ```

## Git Credential Manager

```shell
git-credential-manager configure
git config --global credential.credentialStore gpg
gpg --gen-key
# get <gpg-id> from above command
pass init <gpg-id>
```
