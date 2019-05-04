# Exploring Snort
In this exercise, you'll explore a Snort installation to:
- Familiarize yourself with Snort's directory structure
- Inspect the Snort configuration file
- Examine Snort community rules

---

## Instructions
### The Snort Configuration File
Begin by moving into `/etc/snort`. Then, answer the questions below.
- List the four directories in `/etc/snort`, and explain what each is for.
  > **Solution**
  >   - `/etc/`: Contains Snort's core configuration files.
  >   - `preproc_rules`: Contains preprocessor rules.
  >   - `rules`: Contains rules files.
  >   - `so_rules`: Contains Shared Object rules.

- Run: `grep -in step snort.conf`. 
  - How many steps are there to configuring Snort?
  > **Solution**: There are 7 steps; see below.

  ```bash
  root@4f489d942436:/etc/snort/etc# grep -in step snort.conf
  27:# You should take the following steps to create your own custom configuration:
  41:# Step #1: Set the network variables.  For more information, see README.variables
  113:# Step #2: Configure the decoder.  For more information, see README.decode
  186:# Step #3: Configure the base detection engine.  For more information, see  README.decode
  238:# Step #4: Configure dynamic loaded libraries.
  252:# Step #5: Configure preprocessors
  510:# Step #6: Configure output plugins
  534:# Step #7: Customize your rule set
  663:# Step #8: Customize your preprocessor and decoder alerts
  673:# Step #9: Customize your Shared Object Snort Rules
  ```

- Open `snort.conf` in nano. Scroll down to Step 1.
  - What kind of information do you configure in Step 1?
  - How would you configure Snort to protect the home network `192.168.1.0/24`? 
  > **Solution**: Run `nano +41 snort.conf`. You'd protect the home network by setting `ipvar HOME_NET 192.168.1.0/24`

- Scroll down to Step 7.
  - How do you add rules to Snort?
  - Which rules are included by default?
  - Edit the file to include `local.rules`.
  > **Solution**
  >   - You add rules to Snort by adding a path to a directory containing a rules file in Step 7. 
  >   - This configuration includes `sql.rules` and `community.rules` by default. 
  >  - Include `local.rules` by uncommenting Line 545, so it reads: `include $RULE_PATH/local.rules`.

### Inspecting Rules
- Navigate to `/etc/snort/rules`.
  - How many lines are in the files `local.rules`, `community.rules`, and `sql.rules`?

  > **Solution**
  > ```bash
  > root@4f489d942436:/etc/snort/rules# wc -l {community,local,sql}.rules
  > 3773 community.rules
  >   27 local.rules
  >  107 sql.rules
  > 3907 total
  > ```

- Run the following command to print the last rule in each file:
  - `tail -n 1 {local,sql,community}.rules`

- For each rule you see, identify the following:
  - What **action** does snort take when it matches this rule's pattern?
  - Which **protocol** does each rule watch for?
  - What are the source/destination addresses the rule monitors?
  - What kind of activity does each rule monitor for (e.g., command and control messages in the packet? embedded viruses? etc.)

  - Note the `content` keyword in all three words. Refer to the documentation at: <http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node32.html#SECTION00451000000000000000>
    - What does the `content` keyword allow you to do?
    - What does the `content` keyword in the last rule in `local.rules` do?
