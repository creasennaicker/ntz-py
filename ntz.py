# add your code in this file
import os
import yaml
import click

def read_file():
  try:
    stream = open('foobar.yaml', 'r')
    dictionary = (yaml.safe_load(stream))
    for key, value in dictionary.items():
      print(f'{key} : {value}')
  except yaml.YAMLError as exc:
    return exc

read_file()

#READ FILE WORKS!!!!!!


def write_file(note):

  notepad = read_file()

  try:
    if note not in notepad:
      notepad.append(note)
    else:
      click.echo('NO DUPLICATES ALLOWED')
  except KeyError:
    notepad = [note]




# main function
def cli():
  pass
  
def get_args():
  return os.sys.argv
  
# run the main function

def yaml_to_read():
  try:
    with open('foobar.yaml', 'r') as note_file:
      return yaml.load(note_file)
  except FileNotFoundError:
    with open('foobar.yaml', 'w+'):
      ...
      yaml_to_read()

def yamel_to_write(notepad):
  with open('foobar.yaml', 'w') as notefile:
    yaml.dump(notepad, notefile, indent=4, flow_style=False)




if __name__ == '__main__':
  cli()


