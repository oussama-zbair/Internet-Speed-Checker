# Internet Speed Checker

<a href="https://ibb.co/yFRvfZH"><img src="https://i.ibb.co/pjPV0MY/Internet-Speed-Checker.png" alt="Internet-Speed-Checker" border="0"></a>

### Prerequisites: 
- [ Python Programming Language](https://www.python.org/ " Python Programming Language")
## Section 1: Installation

### Installing the required library:
You will need to install an additional library speedtest-cli.
<a href="https://ibb.co/9GT0768"><img src="https://i.ibb.co/9GT0768/carbon.png" alt="carbon" border="0"></a>
Now that it’s installed, let’s go ahead and import it:

```python
import speedtest
```

After installing the above package one can check if the package is installed correctly or not by doing the version check. The version of the package can be checked using the following command

<a href="https://ibb.co/hWhgy6f"><img src="https://i.ibb.co/hWhgy6f/carbon-1.png" alt="carbon-1" border="0"></a> 
[![](https://media.geeksforgeeks.org/wp-content/uploads/20200213185821/speedtest-cli-version1.png)](https://media.geeksforgeeks.org/wp-content/uploads/20200213185821/speedtest-cli-version1.png)

------------
### Description of methods
First we will need to create an instance of **Speedtest()** class and then inspect the methods it has and discuss each of them.
```python
s = speedtest.Speedtest()
```
Using the inspect library (prebuilt in Python), let’s take a look at what methods the  object has:
```python
import inspect

for method in inspect.getmembers(s, predicate=inspect.ismethod):
    print(method)

```
We should get the following list as the output:

- download
- upload
- get_best_server
- get_closest_servers
- get_servers
- set_mini_server
- get_config
**.download()**
this method will test the download speed of your current connection (in bytes)
```python
print('My download speed is:', s.download())
```
`>>>  231857662.477676, which is equivalent to 231 Mbps`


**.upload()**
This method is similar to the previous one, but tests the upload speed of your current connection (in bytes). 

**.get_best_server()**
This method allows us to identify the best server that we will be testing the connection from. In general, this tends to find the best testing server that is within your region (city).

In terms of formatting, it will return a dictionary with the details of that server. Let’s take a look:

<a href="https://ibb.co/HhzQZLm"><img src="https://i.ibb.co/PDh8ksB/R52449543340d69ecffb69923076ab146.png" alt="R52449543340d69ecffb69923076ab146" border="0"></a>
In my case, since I live in Morocco

**.get_closest_servers()**
This method allows us to a set of servers that are close to our location and we can use these after to do speed tests from different servers/regions.

Similarly to the previous method, we will get back a dictionary, but not instead of one server with details it will be much more.

Here we create store the entire dictionary, but for display purposes only print out the details of the first item in the dictionary:

<a href="https://ibb.co/K7wc6nz"><img src="https://i.ibb.co/vmYC19v/Capture.png" alt="Capture" border="0"></a>

------------


## the special way that i I prefer
using this python script 
And we get the following as the output:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/ZxrLPpq/Capture2.png" alt="Capture2" border="0"></a>

