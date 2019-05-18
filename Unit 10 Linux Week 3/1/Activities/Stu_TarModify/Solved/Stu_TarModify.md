## Sysadmin Essentials: Archiving Data using tar

--------

## Solutions for How to Modify an Archive

-------


In this activity you will modify the contents of an archive by `appending`, `updating` and `deleting` files.

* Open a terminal window on the Virtual Machine.

* Change to the `Projects` directory.

    * `cd Projects`

* **Exercise 1:**  

* Copy `sample.tar` `update.tar`

    * `cp sample.tar update.tar`

* List the contents of `update.tar`.    

    * `tar tf update.tar`

* Create two files `test1.txt` and `test2.txt`. 

    * `touch test1.txt test2.txt`

* Append them to `update.tar`.    

    * `tar -rvf update.tar test1.txt test2.txt`

* List the contents of `update.tar`.

    * `tar tf update.tar`

* **Exercise 2:**    

* Update `update.tar` with latest copy of `test2.txt`.

    * `touch test2.txt`

    * `tar -uvf update.tar test2.txt`

* List the contents of `update.tar`.

    * `tar -tvf update.tar`

* **Exercise 3:**

* Delete `test1.txt` from `update.tar`.

    * `tar -f update.tar --delete test1.txt`

* List the contents of the `update.txt`.

    * `tar -tf update.tar`