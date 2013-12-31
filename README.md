sg-snowprofile
==============

Welcome to the SnowGeek Snow Profile creation tool. The purpose of this tool
is to easily generate an image that represents the hardness profile of
a snowpit using a simple text file as input.

Below is an example of a sample snowpit.
#Sample Profile
![Snow Profile](/example.png "Sample Snow Profile")

The input file is formatted with two columns. It is assumed that 0 is at the
surface. Below are the allowed hardnesses:

F-, F, 4F-, 4F, 1F-, 1F, P-, P, K-, K

Here is an example of a valid input file:
```
0	F
10	1F
35	4F
45	P
47	F-
50	P
52	F-
53	K
55	4F-
65	K
70	4F
100	4F
```
The first entry should be the starting depth, then the next should be the hardness. On the newline, enter what depth that layer extends to. NOTE: The last hardness should not matter, but it is still required by the program to be there.

#Installation
1. Visit the releases tab, which can be found [here](https://github.com/EntilZha/sg-snowprofile/releases/tag/v1.0).
2. Choose the correct option for Mac (.app), Windows (.exe), or Linux (run from command line).
3. Run the application, a file chooser should appear, select the input file, then the plot with the option to save should appear.
