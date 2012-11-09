#! /usr/bin/env python

import re, os, sys, stat

def main():

	'Check if there are enough arguments supplied.'
	if check_args():

            'Keep the current directory.'
            curr_dir = os.getcwd()
            
            'Walk the directories, find matches and rename them'
            for root, dirs, files in os.walk(curr_dir):
		
                for name in files:
			path = os.path.join(root, name)
			
			if(os.path.isfile(path)):
				if(os.path.getsize(path) == 0):
					print(path + " found.")
            
    
def check_args():
    '''Checks if there are enough arguments to go on.'''

    arg_num = len(sys.argv)
    if arg_num < 1:
        'Print out a pretty usage statement.'
        print()
        print("Usage:")
        print("python empty_file_finder.py")
        
        return False
    else:
        return True
        

if __name__ == "__main__": main()
