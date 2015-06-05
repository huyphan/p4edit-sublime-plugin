# p4edit-sublime-plugin
A simple Perforce plugin that automatically checkouts the file as you save it. 

## Installation

This plugin will be available on [Sublime Package Manger](https://packagecontrol.io/) soon (hopefully). While waiting for it to be approved, you can try the manual steps first:
* Open your Packages directory via Sublime menu at `Preferences -> Browse Packages`
* Create folder `P4Edit`.
* Clone or download this github repository and copy the content to the newly created folder.


## Let the plugin know about your Perforce views

This plugin relies on a predefined mapping between your workspaces and their root directory. The mapping can be updated manually by clicking on `Preferences -> Package Settings -> P4Edit -> Settings`.

You can generate a initial mapping of all your Perforce workspaces by the following bash command:

``` bash
printf "{\n\t\"perforce_views\": {\n" && p4 clients -u $P4USER | awk -F' ' '{print "\t\t\"" $2 "\":\"" $5 "\","}' && printf "\n\t}\n}\n"
```

## License

[WTFPL](http://www.wtfpl.net/)
