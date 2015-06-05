# p4edit-sublime-plugin
A simple Perforce plugin that automatically checkouts the file as you save it. 

## Installation

This plugin will be available on [Sublime Package Manger](https://packagecontrol.io/) soon (hopefully). While waiting for it to be approved, you can try the manual steps first:
* Open your Packages directory via Sublime menu at `Preferences -> Browse Packages`
* Create folder `P4Edit`.
* Clone or download this github repository and copy the content to the newly created folder.

Please make sure that `p4` is available under your `$PATH`, `P4PORT` and `P4USER` environment variables are set properly. 

## Let the plugin know about your Perforce views

This plugin relies on a predefined mapping between your workspaces and their root directory. The mapping can be updated manually by clicking on `Preferences -> Package Settings -> P4Edit -> Settings`.

Linux and Mac users can generate an initial mapping of all your Perforce workspaces by the following bash command:

``` bash
printf "{\n\t\"perforce_views\": {\n" && p4 clients -u $P4USER | awk -F' ' '{print "\t\t\"" $2 "\":\"" $5 "\","}' && printf "\n\t}\n}\n"
```

Note that the command output also contains the workspaces **not** on your current machine so you might want to remove them from the mapping list.

## License

[WTFPL](http://www.wtfpl.net/)
