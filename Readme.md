**One-way synchronization of directories**

The program synchronizes two directories: the source directory and the replica directory:

     1. Synchronization is one-sided.
     2. Synchronization is running with a specified period.
     3. Operations of creating / copying / deleting objects are logged to a file and output to the console.
     4. Paths to directories, synchronization interval and path to the log file are set by command line parameters when starting the program.

To run this:
- `pip3 install -r requirements.txt`

To use it:  
- Read help `synchronization_of_directories.py -h`
- Example of running `synchronization_of_directories.py --source_dir C:\Temp\source_dir 
  --replicated_dir C:\Temp\replicated_dir --log_file C:\Temp\Log.txt  --time 10`
- To finish the process `Press Enter`  