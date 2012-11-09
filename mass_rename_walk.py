#! /usr/bin/env python
'''A recursive, and mass rename utility.  Especially useful for changing
extensions on files.'''

import re, os, sys

global old_ext, new_ext

def main():
	print("Massive Extension Renaming Tool")
	print("-------------------------------")
	print("Code: Dorian Pula")

	'Check if there are enough arguments supplied.'
	if check_args():
            'Grab the arguments.'
            old_ext = sys.argv[1]
            new_ext = sys.argv[2]

            'Keep the current directory.'
            curr_dir = os.getcwd()

            'Set up the regex matching.'
            matcher = re.compile("^.+\." + old_ext + "$")
            
            'Walk the directories, find matches and rename them'
            for root, dirs, files in os.walk(curr_dir):
                print("Root dir: " + root)

                for name in files:
                    if matcher.match(name):
                        path, ext = os.path.splitext(os.path.join(root, name))
                        new_path = path + "." + new_ext
                        os.rename(os.path.join(root, name), new_path)
                        print(os.path.join(root, name) + " to " + new_path)
            
    
def check_args():
    '''Checks if there are enough arguments to go on.'''

    arg_num = len(sys.argv)
    if arg_num < 3:
        'Print out a pretty usage statement.'
        print()
        print("Usage:")
        print("python mass_rename_walk.py <old-ext> <new-ext>")
        print("     <old-ext>: Rename files with this extension.")
        print("     <new-ext>: Rename files to this extension.")
        print("NOTE: DO NOT INCLUDE THE . IN THE EXTENSIONS!")
        
        return False
    else:
        return True
        

if __name__ == "__main__": main()
