# **Cloud designed**
## Introduction
> 3 layers cloud computing, First, we use vargrant to enable three virtual machines as front-end, back-end, and data base.

${\Large\color{orange}Front}$
1. Front : Simple user portal for calling back-end designed web pages

${\Large\color{orange}Backend \ \ (web server)}$

WebServer :
1. design the web interface with `css, html`.
2. Using `JS` to implement dynamic webpage interactive functions 
3. Bridging Databases with `Flask`

Cloud :

4. Request front-end web data (e.g., images, .js , .html) from the cloud (`minio`).

${\Large\color{orange}Database}$

1. Create a database using `Mysql` and connect to the backend to transfer the necessary stored data.

## Feature

### how to use?
1.  vagrant up 3 vms (mysql, back, front)
2.  Open chrome and link url : “ http://192.168.56.5:5000/ (front end)
![alt text](https://github.com/TapiocaQAQ/cloud-computing/blob/main/assets/start.png?raw=true)
![alt text](https://github.com/TapiocaQAQ/cloud-computing/blob/main/assets/end.png?raw=true)

3.	Game time: 
    -	Click 開始遊戲 to start game.
    -   Press ‘Blank key’ to jump.
    -   If finish : insert ‘user name’ and click 確認.
    -   Click ‘重新開始’ to reload web.
    -   If want to clean DB, please click ‘清除’.

![alt text](https://github.com/TapiocaQAQ/cloud-computing/blob/main/assets/flowchart.png?raw=true)

<p style='color:red'>This is some red text.</p>
