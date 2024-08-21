import os
import fnmatch

def delete_files_by_pattern(directory, pattern, interactive=False):
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            
            if fnmatch.fnmatch(file, pattern):
                file_path = os.path.join(root, file)
                try:
                    if interactive:
                        prompt = f"Delete? y/s/q : {file_path} \t : "
                        confirmation = input(prompt)
                        
                        while confirmation not in ['y', 's', 'q']:
                            confirmation = input(prompt)
                        if confirmation == 'y':
                            os.remove(file_path)
                        elif confirmation == 'q':
                            exit()
                        elif confirmation =='s':
                            continue
                        else:
                            print("Invalid confirmation:")
                    else:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
                    
if __name__ == "__main__":
     
    directory_to_search = "/Users/vd/Desktop/Github/vdanepalli_notes/"
    
    delete_files_by_pattern(directory_to_search, "*.class")