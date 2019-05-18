# Day 3 Cheat Sheet — Configuring a LAMP Server

## Key Terms

- **Linux**: a family of freely distributed, open-source software based on the Linux-kernel operating system.
  > **Example**: Ubuntu, Mint, Kali Linux are a few examples.
  
- **Apache**: most widely used web server software
  > **Example**: Many web servers running a Linux operating system are using Apache as the web service on that particular server
    
- **MySQL**: a freely available open source Relational Database Management System (RDBMS) that uses Structured Query Language (SQL).
  > **Example**: MySQL is used to add, access, and manage content in a database
    
- **PHP**: server scripting language, and a powerful tool for making dynamic and interactive Web pages.
  > **Example**: PHP (front end) and MySQL (backend) are a common combination for many web sites out today
    
- **Ubuntu**: open source Debian-based Linux distribution
  > **Example**: just one of the many distributions (flavors) of Linux available primarly used for personal computers 
    
- **VM**: or virtual machine, is an operating system environment installed on software which acts like dedicated hardware.
  > **Example**: it is possible to have Windows, Linux, and Mac VM's
    
- **VirtualBox**: lightweight application that allows you to run virtual machines (VMs) on a variety of host operating systems.
  > **Example**: VirtualBox is used as a tool to run multiple VMs of operating systems.
    
- **Personal Package Archives**: also known as PPAs, are collections of software not included in Ubuntu by default 
  > **Example**: PPAs provide updates for your favorite software at a much quicker rate than Ubuntu itself.
    
- **Nano**: a simple terminal-based text editor.
  > **Example**: ideal for making small changes to existing configuration files or for writing short plain text files
    
- **Microsoft IIS**: a web server software package designed for Microsoft Windows.
  > **Example**: Web sites that are hosted on Windows servers use Micorsoft IIS
  
- **Nginx**: a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server
  > **Example**: accelerates content and application delivery, improves security, facilitates availability and scalability for the busiest web sites on the Internet.
    
- **Directive**: a setting/option that can be configured
  > **Example**: Apache config file has sections where different directives are configurable 
  
- **Iptables**: an application that allows users to configure specific rules that will be enforced by the kernel's netfilter framework
  > **Example**: simply defined as the software firewall on Linux
      
- **UFW**: default firewall configuration tool for Ubuntu, hence the name Uncomplicated Firewall (ufw)
  > **Example**: developed to provide an easier firewall solution than iptables, ufw acts a frontend for iptables
      
- **Python**: a general purpose and high level programming language

- **Ruby**: a dynamic, interpreted, reflective, object-oriented, general-purpose programming language
  > **Example**: Rails is written in Ruby, the programming language which is also used alongside Rails
      
- **Database**: an electronic filing system, organized by fields, records, and files
  > **Example**: Microsoft Excel spreadsheet or Microsoft Access are good examples of desktop database programs
      
- **SQL Injections**: uses malicious code to manipulate your database into revealing information.
  > **Example**: In 2017, SQL Injection attacks were the number one application security risk based on the [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project).
      
- **Vulnerability**: a weakness which can be exploited by a Threat Actor, such as an attacker, to perform unauthorized actions within a computer system.
  > **Example**: Computer systems that aren't patched contain vulnerabilities that can be exploited by attackers.
  
- **Exploit**: unintended and unpatched flaw in software code that exposes it to potential exploitation by hackers or malicious software code.
  > **Example**: malicious code like viruses, worms, Trojan horses and other forms of malware.
        
- **Single Host**:  runs both the web server and the database
  > **Example**: Doesn't scale; insecure (compromising a single host compromises the whole application); single point of failure (if the host goes down, the entire app does too)
        
- **Dual Host**:  one host runs a web server, and another runs a database. The web server makes requests to the database server when it needs data.
  > **Example**: more secure than a single host, but still doesn't scale well; still insecure (compromising the HTTP server compromises most of the application); still has a single point of failure (if either the HTTP server or database goes down, the application does, too)
        
- **Web Farm without Database Cluster**: requests go through a load balancer, then to one of many web servers. The web servers then make requests to the database. Note that each of these many web servers is the same
  > **Example**: each one would send the same response to any given request. The point of having many is to be able to serve large numbers of users at a time.
        
- **Web Farm with Database Cluster**: Same as a web farm, but with multiple databases instead of just one
  > **Example**: This setup might be more secure, because different pieces of sensitive data can be stored in completely separate databases.
        
- **Web Farm with Application Servers**: requests go through a load balancer; then to a Web Server, which handles HTTP requests; and then from the Web Server to an Application Server, which is another server that figures out how to fulfill the HTTP requests
        
- **Web Farm with Load-Balanced Application Servers**: Same as the previous architecture, but with a load balancer in front of the application servers.
                              

## Key Commands

### Apt

APT (Advanced Package Tool) is the more friendly command line tool to interact with the packaging system where you can use it to find and install new packages, upgrade packages, remove the packages etc.

```bash
# Launch a bash shell 
sudo apt update
```
This command makes sure everything is up-to-date and requires root privileges

```bash
# Install package 
sudo apt install <packagename>
```
This command installs a package.

```bash
# Installs fortune
sudo apt install fortune fortunes-bofh-excuses
```
This installs a program called fortune, which prints 	a "fortune cookie" to the command line.

```bash
# View installed packages 
apt list
```
This command sees which packages are installed

```bash
# Search packages 
apt search <searchterm>
```
This command looks for specific packages

```bash
# Remove packages 
apt remove --purge <package>
```
This command uninstalls packages

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>remove</code> uninstalls a package
    <li><code>--purge</code> deletes its configuration files
  </ul>
</details>

###

```bash
# Remove dependencies 
apt autoremove
```
This removes any dependencies installed along with <package>, as long as they're not used by any other packages on the system.

### Nano

Nano is a simple terminal-based text editor ideal for making small changes to existing configuration files or for writing short plain text files.

```bash
# Create and open file
nano -u Notes.txt
```
Creates and open a file called Notes.txt

<details>
  <summary>Expand for Explanations of Flags</summary>
  <ul>
    <li><code>-u</code> enables undo/redo
  </ul>
</details>

### Apache

```bash
# Verify Apache config file 
apache2ctl configtest
```
This command verifies apache config files

```bash
# View Apache config file 
less /etc/apache2/apache2.conf
```
This command views apache config file which basic configuration settings for Apache

### MySQL

```bash
# MySQL Install
mysql_secure_installation
```
This command launches a series of prompts that help the user configure strong passwords, reset default credentials, etc.

### PHP

```bash
# Installs various PHP Packages
php libapache2-mod-php php-mysql
```
This command installs packages for PHP
