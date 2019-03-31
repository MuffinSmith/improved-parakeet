# Day 3 Cheat Sheet - Unit-Terminal

## Key Terms

- **Shell**: The shell is the program used to interpret and manage commands. It is the operating system command line interface (CLI) and provides a way to create and execute scripts.  
  - **Example**: The *bash* shell which stands for Bourne Again Shell is included in most Unix distributions.

- **Shell Script**: A shell script is a text file consisting of commands that are stored and run.  Shell scripting is a powerful tool to use because it allows IT and security professionals to prescript repeatable processes for future use. Shell scripts have the extension *.sh*
  - **Example**: `script.sh`
  
 ```bash 
    # Create a folder called Summary
    mkdir Summary

    # Combine all files in the Files folder into a single file called MySummary.txt
    cat Files/*.txt > MySummary.txt

    # Move the MySummary.txt file into the Summary folder.
    mv MySummary.txt Summary

    # Preview the contents
head Summary/MySummary.txt
```

- **Docker**: Docker makes it easy to create a network of machines. Docker packages software into units called *containers*. 
  - **Example**: Docker was installed as part of the lesson activity.

- **Container**: Containers or "machines" have all the software needed to run including libraries, system tools, code, and runtime within a small footprint. They provide a way to package and distribute software and are designed to be able to interact with one another.
  - **Example**: List containers using `docker ps`.

- **Virtual Machine**: A virtual machine (VM) runs one operating system (e.g., Windows, Linux). VMs come with considerable overhead such as large files and complex networking.
  - **Example**: Virtual Box. 

- **ssh**: *ssh* stands for **secure shell** and allows a user to connect their local machines to remote machines.
  - **Example**: `ssh root@evr_ssh_sshd_1`

## Key Commands

### Docker Commands        

#### Check that installation was successful

```bash 
`docker --version`
`docker run library/hello-world`
```

#### Download and launch a machine

```bash 
`docker-compose up -d`
```

#### List running machines (containers)

```bash 
`docker ps`
```

#### Log into a machine

```bash 
`docker exec -it <Name> bash`
```

#### Print out machine name

```bash 
`uname`
```

#### Stop machines

```bash 
`docker rm -vf $(docker ps -a -q)`
```

-------

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
