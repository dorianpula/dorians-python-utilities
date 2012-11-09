#! /usr/bin/env python
'''A recursive, removal utility that focuses on files with a target extension.'''

import re, os, sys

def main():
	print("Search by Extension Tool")
	print("-------------------------------")
	print("Code: Dorian 'deepwave' Pula")

	'Check if there are enough arguments supplied.'
	if check_args():
            'Grab the arguments.'
            trg_ext = sys.argv[1]

            'Keep the current directory.'
            curr_dir = os.getcwd()

            'Set up the regex matching.'
            matcher = re.compile("^.+\." + trg_ext + "$")
            
            'Walk the directories, find matches and rename them'
            for root, dirs, files in os.walk(curr_dir):
                print("Searching in: " + root)

                for name in files:
                    if matcher.match(name):
                        path = os.path.join(root, name)
                        print(path + " found.")
            
    
def check_args():
    '''Checks if there are enough arguments to go on.'''

    arg_num = len(sys.argv)
    if arg_num < 2:
        'Print out a pretty usage statement.'
        print()
        print("Usage:")
        print("python search_by_ext.py <extension>")
        print("     <extension>: Find files with this extension.")
        print("NOTE: DO NOT INCLUDE THE . IN THE EXTENSIONS!")
        
        return False
    else:
        return True
        

if __name__ == "__main__": main()
