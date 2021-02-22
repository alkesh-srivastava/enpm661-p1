## How to run this program?
To run the program you will need to make sure that your *python interpretor* supports the following packages :
* numpy	1.20.1	
* pip	21.0.1	
 
You need to run *program.py* file in the terminal. The program will ask you to input the puzzle in sequential order. Please enter the initial state of your test case to number by number, i.e. if your initial state is of the form :

#########
00 02 03 04
01 05 07 08
09 06 11 12
13 10 14 15
#########
Then you should input as :
0,2,3,4,1,5,7,8,9,6,11,12,13,10,14,15
i.e. separated by commas and sequentially. Press ENTER when done.
![Sequential Input](https://github.com/alkesh-umd/enpm661-p1/blob/main/img/1.PNG)

The program will then ask you to give name to the file where you want the solution to be stored. Remember - DO NOT ENTER THE EXTENSION OF THE FILE. The file will be saved as a .txt file in the root folder.
i.e if you enter *trial_1*, the output will saved in the root folder as *trial_1.txt*.
![Entering name of the file](https://github.com/alkesh-umd/enpm661-p1/blob/main/img/1.PNG)

The output will then be stored.




![Output](https://github.com/alkesh-umd/enpm661-p1/blob/main/img/3.PNG)

***

The virtual environment in which the program successfully ran had the following packages:

* JsonForm	0.0.2	
* JsonSir	0.0.2	
* PyYAML	5.4.1	
* Python-EasyConfig	
* Resource	0.2.1	
* attrs	20.3.0	
* jsonschema	3.2.0	
* numpy	1.20.1	
* pip	21.0.1	
* pyrsistent	0.17.3	
* setuptools	53.0.0	
* six	1.15.0	

If the program somehows fails to run on your computer, then try to adjust the virtual environment accordingly.
