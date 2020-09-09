# Home Assistant Add-on Devcontainer Template

### Summary

This is a templated to ease development of Home Assistant add-ons inside of a VS Code [devcontainer](https://code.visualstudio.com/docs/remote/containers).

### Usage

Simply copy the contents of this repository to the base directory of the add-on you are developing. Modify the files in the directory as needed.  

Your add-on will be appear in the `Local Add-ons` section of the Home Assistant "Add-on store" tab.

#### VS Code Tasks

The following tasks are included for your convenience.

- Start Home Assistant

This task will download and run a Home Assistant environment inside the container using the latest `dev` targets of Home Assistant and Home Assistant Core. It will be mapped to port 8123 (by default) on the host machine.

- Run Home Assistant CLI - _Requires a running Home Assistant instance_

This task will open a [Home Assistant CLI](https://github.com/home-assistant/cli) window inside VS Code.

- Cleanup stale Home Assistant environment

This task will nuke the data stored by Home Assistant (including the underlying Home Assistant Core). Can be used to revert to a pristine state before starting Home Assistant.

### FAQ

Q: How do I customize some-widget-or-another?

A: There is almost no "black magic" going on here. Make sure to read up on how devcontainers work from the [official website](https://code.visualstudio.com/docs/remote/containers).

Q: I read the docs. I still need help customizing some-widget-or-another!

A: Come ask on [Discord](https://discordapp.com/invite/2Uath3J) in channel #devs_addon or #devs_supervisor.

Q: How do I develop more than one add-on in the same Home Assistant instance?

A: See [this issue](https://github.com/issacg/hassio-addon-devcontainer/issues/1).

Q: Why are there 2 `Dockerfile`s?  

A: The `.devcontainer\Dockerfile` is for your development environment. The `Dockerfile` in the root directory is to build your add-on.

Q: I added `.devcontainer` to my `.dockerignore` and now things are broken.

A: Don't. The `.dockerignore` is shared by both Dockerfiles, and by adding `.devcontainer` to your `.dockerignore`, you will break things in the devcontainer. Instead, use other means to avoid copying `.devcontainer` (and `.vscode` for that matter) in your "production" `Dockerfile`.

Q: When installing my local add-on, I'm not seeing my latest changes. Instead, I see the functionality of the last published version of my add-on.

A: Make sure that you remove the `image` key from your `config.json`, else when "installing" the add-on, it will try to use the docker image, rather than building the add-on locally.
