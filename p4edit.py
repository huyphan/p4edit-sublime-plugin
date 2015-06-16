import sublime, sublime_plugin
import os, stat
import subprocess

def is_readonly(filename):
    if not filename or len(filename) <= 0:
        return False

    return not os.access(filename, os.W_OK)

def is_subdir(path, directory):
    path = os.path.realpath(path)
    directory = os.path.realpath(directory)

    relative = os.path.relpath(path, directory)

    if relative.startswith(os.pardir + os.sep):
        return False
    else:
        return True

class P4EditCommand(sublime_plugin.EventListener):
    
    def get_setting(self, view, setting):
        settings = sublime.load_settings('P4Edit.sublime-settings')
        return settings.get(setting)

    def on_pre_save(self, view):
        file_path = view.file_name()
        if file_path is None:
            return

        if not is_readonly(file_path):
            return

        perforce_views = self.get_setting(view, 'perforce_views')
        dir = os.path.dirname(view.file_name())
        for client, root_dir in perforce_views.items():
            if is_subdir(dir, root_dir):
                command = ["p4", "edit", file_path]
                message = "Marking %s as being edited under workspace %s" % (file_path, client)
                sublime.status_message(message)
                p4_user = self.get_setting(view, 'perforce_user')
                p4_port = self.get_setting(view, 'perforce_server')
                p = subprocess.Popen(command, env=dict(os.environ, P4CLIENT=client, P4PORT=p4_port, P4USER=p4_user), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = p.communicate()
                if len(err) > 0:
                    err = err.decode('utf-8').strip()
                    if "Perforce password (P4PASSWD) invalid or unset" in err:
                        message = "P4Edit was unable to checkout the file because you hadn't logged in. Please run 'p4 login' on your console first."
                    else:
                        message = "P4Edit was unable to checkout the file due to the following reason: \"%s\"" % err
                    sublime.message_dialog(message)
