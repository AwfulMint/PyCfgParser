"""
This module can be used to deal with configuration files.

This parser only recognize the key=value pattern, of course you can
leave spaces between then like "mykey = myvalue" if you wish to do
so. Also, '#' chars are recognized as comments but they are not
supported by now, so when editing, removing or creating properties
with this module all comments will be lost.

Try not use the functions of the Config class in loops if you set
'saveonchange' to True when calling the function. Setting 'saveonchange'
to True will call 'save_conf' function which delete the original file
and replaces it by a brand new one, this can be CPU consuming.
"""

from os import remove
from os import getcwd as cwd


class Config:
    """
    The Config class have two variables: 'filename' and 'data'.

    The 'data' variable store the configurations specified in 'filename' variable,
    when a new instanced is created the file will load automatically.
    """

    def __init__(self, filename='{0}/config.cfg'.format(cwd())):
        self.filename = filename
        self.data = {}

        self.data = self.read_conf()

    def read_conf(self):
        """
        Open the file specified in the 'filename' variable, parse it and load it
        to the 'data' variable.

        :return: A dictionary with the configurations founded.
        """
        with open(self.filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    continue

                newline = line.strip().replace(" ", "")
                splited = newline.split("=")

                key = splited[0]
                value = splited[1]

                if key.count('#') > 0:
                    print('invalid char at:', key)
                    print('char at pos', key.find('#'), "is invalid here.")
                    continue

                if value.count('#') > 0:
                    index = value.find('#')
                    self.data[key] = value[:index]
                else:
                    self.data[key] = value

        return self.data

    def new_conf(self, key, value, saveonchange=False):
        """
        Create a new configuration, if 'saveonchange' is set to True then
        'save_conf' will be called.

        If the 'key' already exists then an error message will be printed.

        :param key: Configuration key
        :param value: Configuration value
        :param saveonchange: Save it
        :return:
        """
        if key in self.data:
            print('key', key, 'already exists.')
            print('use: edit_conf instead.')
        else:
            self.data[key] = value
            if saveonchange:
                self.save_conf()

    def remove_conf(self, key, saveonchange=False):
        """
        Remove a configuration, if 'saveonchange' is set to True then
        'save_conf' will be called.

        If the 'key' isnt present in 'data' then an error message will
        be printed.

        :param key: Configuration key.
        :param saveonchange: Save it
        :return:
        """
        if key not in self.data:
            print('unable to remove the key', key, 'it doesnt exist!')
            print('use: new_config to create the key=value pair first.')
        else:
            del self.data[key]
            if saveonchange:
                self.save_conf()

    def edit_conf(self, key, value, saveonchange=False):
        """
        Edit the configuration specified by 'key' and replace its
        contents by 'value'.

        If doesn't exists then an error message will be printed.

        :param key: Configuration key
        :param value: The new value
        :param saveonchange: Save it
        :return:
        """
        if key not in self.data:
            print('unable to edit the key', key, 'it doesnt exist!')
            print('use: new_config to create the key=value pair first.')
        else:
            self.data[key] = value
            if saveonchange:
                self.save_conf()

    def save_conf(self):
        """
        Save the configuration to the file specifies in 'filename', this
        function will delete the original file and rewrite it with the 'data'
        content. Comments will be lost.
        :return:
        """
        remove(self.filename)
        with open(self.filename, 'x') as f:
            for key in self.data:
                f.write('{0} = {1}\n'.format(key, self.data[key]))

