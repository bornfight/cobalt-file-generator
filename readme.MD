Python script for generating files with different extensions. 

Requirements:
- Python >= 3.6.5
- pip3 (package manager for python)

Steps:
1. In terminal navigate to the directory where the main python script is located.
2. `pip3 install python-docx`
3. `python cobaltFileGenerator.py`
4. Test files will be generated in the directory called 'generated-test-files'.

Optional paramteres:
If you wish, you can provide extenstion names which you would like to generate when running the script. Otherwise, it will generate the files from the default extensions pack ('jpg', 'jpeg', 'pdf', 'png', 'docx', 'gif', 'doc').

Example:
`python cobaltFileGenerator.py png jpg`