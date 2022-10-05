import subprocess
try:
    output_check = subprocess.check_output(['whoami'])# Run command. Format as ['cmd','arg1','arg2',.....] 
    print(output_check)
except Exception as e:
    print("Error occurred while running")