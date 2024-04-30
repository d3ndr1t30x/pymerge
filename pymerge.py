import os
import glob

def cat_and_sort(files, output_file):
    # Function to concatenate content of multiple files and sort them uniquely
    
    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through each input file
        for file in files:
            # Open each input file in read mode
            with open(file, 'r') as infile:
                # Read content of input file and write it to output file
                outfile.write(infile.read())
    
    # Read the contents of the output file
    with open(output_file, 'r') as f:
        lines = f.readlines()
    
    # Sort and remove duplicates
    lines = sorted(set(lines))
    
    # Write the sorted and unique lines back to the output file
    with open(output_file, 'w') as f:
        f.writelines(lines)

def display_banner():
    # Display banner art
    print("""
                                                  
______ ___.__. _____   ___________  ____   ____  
\____ <   |  |/     \_/ __ \_  __ \/ ___\_/ __ \ 
|  |_> >___  |  Y Y  \  ___/|  | \/ /_/  >  ___/ 
|   __// ____|__|_|  /\___  >__|  \___  / \___  >
|__|   \/          \/     \/     /_____/      \/ 
    """)

def display_help():
    # Display help menu
    print("""
Usage: python script.py

Description:
This script allows you to concatenate the content of multiple text files and perform a sort -u style operation on the merged text files.

Options:
-h, --help      Display this help menu
    """)

def main():
    display_banner()
    
    import sys
    
    if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        display_help()
        return
    
    # Ask the user for input files
    input_files = input("Enter the paths of the text files to concatenate (separated by spaces), or use * to merge all txt files in the current directory: ").split()
    
    # If * is used, replace it with all txt files in the current directory
    if '*' in input_files:
        input_files.remove('*')
        input_files.extend(glob.glob('*.txt'))
    
    # Filter out non-txt files
    input_files = [file for file in input_files if file.endswith('.txt')]
    
    if not input_files:
        print("No valid txt files found.")
        return
    
    # Ask the user for the output file name
    output_file = input("Enter the name of the output file: ")
    
    # Call the function
    cat_and_sort(input_files, output_file)
    
    print("Files concatenated and sorted uniquely!")

if __name__ == "__main__":
    main()
