# AwfulMint's PyCfgParser

### About
---
This parser will work in every file who follows the key=value standard, also support (maybe?) comments.

Comments are identified by '#'. Lines started with it will be ignored, if '#' is part of a key, a error will be raised,
if '#' is in the value then the parser will only consider the string until its index.

### How to use
---
There're few functions in this module they are:
* read_conf
* new_conf
* remove_conf
* edit_conf
* save_conf

And a single 'Config' class.

#### read_conf
This function is called at the Config class '\_\_init__' function and loads the file specified by 'filename' variable,
that said make sure at least the file already exists on your system.

The loaded data will be stored in the 'data' variable which is a dictionary.

The parse is done in this function.

#### new_conf
This function creates a new entry in the 'data' variable __if__ there's no key with the same identifier (name).

It have a default parameter called 'saveonchange' which trigger the 'save_conf' function to be called when set to True.

#### remove_conf
This function removes an entry in the 'data' variable __if__ the key exists.

It have a default parameter called 'saveonchange' which trigger the 'save_conf' function to be called when set to True.

#### edit_conf
This function edit an entry with the given key and replace the content to the given value.

It have a default parameter called 'saveonchange' which trigger the 'save_conf' function to be called when set to True.

#### save_conf
This function deletes the original file of the system and then create a new one with the data in 'data' variable.

### Examples

* With 'saveonchange' set to True.
```python
cfg = Config("config_filename.cfg")
cfg.new_conf('key1', 'hello', True) # This will create and save.
cfg.new_conf('key1', 'hello again?', True) # This will do nothing, but expect an error message.
cfg.new_conf('key2', ', or not!', True)
cfg.edit_conf('key2', ', world!', True)
cfg.remove_conf('key2', True)

print(cfg.data)
```

The output will be something like this:
```text
key key1 already exists.
use: edit_conf instead.
{'key1': 'hello'}
```

* Without 'saveonchage' set to True.
```python
cfg = Config("config_filename.cfg")
cfg.new_conf('key1', 'hello') # This will  just create.
cfg.new_conf('key1', 'hello again?') # This will do nothing, but expect an error message.
cfg.new_conf('key2', ', or not!')
cfg.edit_conf('key2', ', world!')
cfg.remove_conf('key2')
cfg.save_conf()

print(cfg.data)
```
The output will be exactly the same as before. This method is for the speed and CPU's sake. The first method should be
used only if you are going to write __only one__ statement in a loop (or the entire program execution) and the second one
is better when dealing with loops since you can do all the changes you need and call 'save_conf' in the end of the loop.