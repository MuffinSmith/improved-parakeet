## Docker Setup
Docker makes it easy for us to create a network of machines, which we can use to practice technical activities in a virtualized environment.

Recal that typical virtual machine (VM) environments come with considerable overhead:
- Large files
- Complex networking (involving port forwards, choosing the correct adapters, etc.)
- Difficult to launch and interact with multiple VMs
  
- Docker mitigates these problems for some use cases through the use of a technology called containers.

- Containers provide a way to package and distribute software, such as:
  - Simple tools like nmap
  - Network services, like an Apache web server
  - Entire operating systems (!), such as Ubuntu Linux
  
- For the purpose of this class, we can then think of containers as "machines." 

- Docker also lets us create multiple containers - or machines-  on a single host.
  - These machines are also designed to be able to interact with one another.
  - This is very important because our ssh activity requires that we have two machines set up that can interact with one another. 

### Installing Docker
The first step is to install Docker. Docker will require different installations for Mac computers and Windows computers. 
    
To get started with Docker, download and run the installer:
  - Mac: https://docs.docker.com/v17.12/docker-for-mac/install/
  - Windows (regardless of the Windows version): https://docs.docker.com/toolbox/toolbox_install_windows/
 
    
- Installation should take between 5-10 minutes. 

### Checking Installation

- Check that your installation was successful by opening up Terminal (on Mac) or Docker Quickstart Terminal (on Windows—_**not**_ Git Bash!) and running:
  - `docker --version`
  - `docker run library/hello-world`
  - The latter command should simply print a "help" message—boring, but functional! 
  
- The next step is to download the machine required for the activities that we will do in class.

### Downloading the Machine for the Day's Activity

- For the day's activity, we will need to download the machines that we'll be using. This download will take considerable time. 

- Mac users will open Terminal
- Windows uses will open Docker Quickstart Terminal

- Next run: `docker pull rastasheep/ubuntu-sshd`
- When done, it will print "Download complete" in your terminal. 

## Important Note for Windows Users

- This will become relevant in class when Windows students are running labs. You can ignore this now when it comes to installation. We will cover this thoroughly in class. 

- Be aware that Windows students may have errors launching lab environments with `docker-compose`. This is because Docker Compose expects `docker-compose.yml` and Dockerfiles to have Unix-style line endings, but Windows automatically changes the line-ending format of files slacked out to students.

- If Windows students encounter issues in the lab environments, try the steps below.

  ```bash
  # Move into the directory containing the student exercise, e.g.: 
  cd Stu_Example_Activity
  # Convert everything to Unix-style line-endings by running: 
  dos2unix **/*
  # Rebuild the containers: 
  docker-compose build --no-cache
  # Start the lab: 
  docker-compose up -d
  ```

### Summary

Discomfort with new technologies like Docker is normal, but that this is important practice—technical security professionals constantly need to learn new tools on the fly, and Docker is our first major example of such a new tool.

We're using Docker as a convenient way to simulate machines and virtual networks—it's commonly used in security, but is not necessarily a "security tool".
