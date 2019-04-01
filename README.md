# TCP_Video_Transmission
One-way and two-way TCP based video streaming over a local network. Submitted as Compuer Networks project at PESU.

Introduction:
Our application enables video transmission over a local area network without the requirement of an internet connection between 2 users. A user will be able to enter a video conference through a Graphical User Interface.
The GUI gives a user the ability to send, receive or enter a two-way conference through video transmission.
The GUI also provides the user with an option of applying a filter on the video being streamed.
We were able to implement this using Transfer Control Protocol. TCP is a connection-oriented, end-to-end reliable protocol which supports multi-network applications. TCP is able to operate above a wide spectrum of communication systems ranging from hard-wired connections to packet-switched or circuit-switched networks. Because TCP was designed with a series of requests and responses to verify file transfers, it is ideal for our applications that needs guaranteed delivery.


About the Software:
For the programming of our application, Python has been used. Using Python, socket programming is implemented in our project. Sockets allow us to communicate between a client and server by specifying the port numbers and respective IP addresses. The Graphical User Interface has also been coded using Python and the various libraries in it.
For the purpose of image processing and video transmission, a library in Python called OpenCV is used. OpenCV (Open source computer vision) is a library of programming functions mainly aimed at real-time computer vision. Being a BSD-licensed product, OpenCV makes it easy for applications to utilize and modify the code.
Wireshark is an open source tool for packet analysis.We have used Wireshark to capture the data packet transfer and analyze the communication protocol being used in our application i.e. TCP.


NOTE: The paths to the image and file resources have been hardcoded. Please change the paths to your respective code file location.
