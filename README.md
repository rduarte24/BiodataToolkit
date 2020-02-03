# BioDataToolkit

BioDataToolkit it's a bioinformatic tool to clasify DNA and protein sequences from the GenBank at NCBI. To run this tool you need to download the package and run Main.py file.

#### Requirements
These are the required packages for BioDataToolkit to run. The command lines to install the packages are bellow each package.
* [Python 3](https://www.python.org/downloads/) - Programming language to compile. Make sure to install tkinter library, otherwise GUI is not going to work.
For Unix/Linux/MacOSX based systems
```sh
$sudo apt-get update
$sudo apt-get install python3
```
For Windows based systems go to the website.

* [Tkinter](https://docs.python.org/3.7/library/tkinter.html) - Window drawer and manager, usually included with Python installers, just check the box during the installation.
For Unix/Linux/MacOSX based systems
```sh
$sudo apt-get update
$sudo apt-get install python3-tk
```
For windows users check the box TK/TCL during installation
* [BioPython](https://biopython.org/) - Python library to manage sequences files.
For Unix/Linux/MacOSX based systems
```sh
$sudo apt-get update
$sudo python3 -m pip install biopython
```
For Windows users, refer to the link for futher instructions, you cana download the package and manually install it using PIP, or you can set an evironment variable python3 or find the python 3 installation path and run from terminal this command:
```sh
python3 -m pip install biopython
```
* [xlsxwriter](https://xlsxwriter.readthedocs.io/) - Python extension library to write Excel datasheets.
For Unix/Linux/MacOSX based systems
```sh
$sudo apt-get update
$sudo python3 -m pip install xlsxwriter
```
For Windows users, refer to the link for futher instructions, you cana download the package and manually install it using PIP, or you can set an evironment variable python3 or find the python 3 installation path and run from terminal this command:
```sh
python3 -m pip install xlxswriter
```

# Usage
The background in the main windows shows the usage steps in spanish, futhermore, we include this manual to guide the user and to explain terminal mode usage implementation.

#### User interface usage.
  - Afeter checking that all the requeriments are installed, run main.py file.
  - Load the input file clicking File>Open, that contains all the results of the query on the GenBank, select all the sequences in the top right corner of the results and create the file to download in "Genbank Full" format.
  - In the propmt windows, wirte down the output file name
  - Click run on the main window and wait for the "Runtime" message on the terminal as sign that the process has been completed.
  - Check the run directory for the outputfile.
  - To copy the Fasta column from the outputfile, copy first the column to a word document and the copy to your favorite text editor, because, the xlxswriter library adds quotes on each sequence in Fasta format, so to make te sequences able to run in another tool, you need to remove then doing the previous process.

#### Terminal implementation usage
BioDataToolkit is able to be implemented in your proyects as an extension library, just need to copy "Biodatatoolkit.py" file to your project then, you can import the file to your proyect and use it as described here:
```python
import BiodataToolkit as bdtk
```
Then you can call the parser method.
```python
parser(inputFilename,outputFilename)
```
Passing the input file name full route as inputFilename parameter and the output file name as outputFilename parameter, then the output file will be in the same directory as the Biodatatoolkit.py file.

# About
This is the thesis proyect for a barchelor degree in systems engineering.

- Author: Ruben O. Duarte B.
- Director: Lola X. Bautista R.
- Coodirector: Francisco J. Martínez P.


Universidad Industrial de Santander
Bucaramanga - Colombia.