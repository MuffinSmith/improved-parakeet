
## Start gAWK-ing Activity Review

**Setup**: For this activity, move into the Stu_Awk directory and locate the `17-18-Breaches.txt` file.

### Solutions

Using the `17-18-Breaches.txt` file, create various AWK commands that accomplish the following:

- Print only the first field of the 17-18-Breaches.txt.
  - **Solution**: `awk -F"\t" '{print $1}' 17-18-Breaches.txt`

    ```bash
      COMPANY NAME
      AerServ (subsidiary of InMobi)
      Bethesda Game Studios
      BlankMediaGames
      BMO and Simplii
      British Airways
      Cathay Pacific Airways
      Centers for Medicare & Medicaid Services
      Defense Integrated Data Center (South Korea)
      Deloitte
      Equifax
      Erie County Medical Center
      Facebook
      Google Plus
      Grozio Chirurgija
      Heathrow Airport
      Marriott International
      MyHeritage
      Orbitz
      Popsugar
      Quora
      Reddit
      SingHealth
      Taringa!
      Ticketfly (subsidiary of Eventbrite)
      Typeform
      Uber
      Under Armour
      Wordpress
    ````

- Print only the breaches from 'web' companies.
  - **Solution**: `awk '/web/' 17-18-Breaches.txt`

    ```bash
      Orbitz	2018	880,000	web	hacked
      Reddit	2018	unknown	web	hacked
      Taringa!	2017	28,722,877	web	hacked
    ````

- Out of the web companies that were breached, print only the company name.
  -  **Solution**: `awk -F"\t" '/web/{print $1}' 17-18-Breaches.txt`

      ```bash
        Orbitz
        Reddit
        Taringa!
      ````

- Print all the breaches from 2017.
  - **Solution**: `awk '/2017/' 17-18-Breaches.txt`
  
    ```bash
      Defense Integrated Data Center (South Korea)	2017	235 GB	military	hacked
      Deloitte	2017		consulting, accounting	poor security
      Equifax	2017	143,000,000	financial, credit reporting	poor security
      Erie County Medical Center	2017	unknown	healthcare	poor security
      Grozio Chirurgija	2017	25,000	healthcare	hacked
      Heathrow Airport	2017	2.5GB	transport	lost / stolen media
      Taringa!	2017	28,722,877	web	hacked
      Uber	2017	57,000,000	transport	hacked
    ````

- For the companies that had breaches in 2017, print only the company name and the number of records lost.
  - **Solution**: `awk -F"\t" '/2017/{print $1, $3}' 17-18-Breaches.txt`

    ```bash
      Defense Integrated Data Center (South Korea) 235 GB
      Deloitte 
      Equifax 143,000,000
      Erie County Medical Center unknown
      Grozio Chirurgija 25,000
      Heathrow Airport 2.5GB
      Taringa! 28,722,877
      Uber 57,000,000
    ````

- For the companies that had breaches in 2018, save the company name, company type and number of breaches to a new file named 2018Breaches.txt

  - **Solution**: `awk -F"\t" '/2018/{print $1, $4, $3}' 17-18-Breaches.txt > 2018Breaches.txt`
  - Run `ls` afterwards to see the new file created.
