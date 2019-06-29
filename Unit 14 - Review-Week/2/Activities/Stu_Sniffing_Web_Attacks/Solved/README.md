## Sniffing Web Attacks

### Solutions:

- Open the pcap in [http_dvwa_sqlinjection.pcapng](http_dvwa_sqlinjection.pcapng).

- Find the packets containing the SQLi payloads and record the three payloads you found. 

  > **Solution**: Filter for `http`. You'll find thre GET requests, with the following payloads.
  >   - `%' or '0'='0`
  >   - `%' or 0=0 union select null, version()`
  >   - `%' or '0'='0' union select null, version()`

- Were the attacks successful? Support your conclusion with evidence.
  > **Solutions**
  >  - Yes. To confirm, click: **File** -> **Export Objects** -> **HTTP**. Then, save the last file (filename `%25%27+or+%270%27%3D%270`) as `dump1.html`. Note that this HTML contains the name of all users in the database.
  >  - No. To confirm, click: **File** -> **Export Objects** -> **HTTP**. Then, save the last file (filename `%25%27+or+0%3D0+union+select+null%2C+version%28%29`) as `dump2.html`. Note that the response indicates an error in the SQL. This is because the OR condition has `0=0` instead of `'0'='0'`.
  >  - Yes. To confirm, click: **File** -> **Export Objects** -> **HTTP**. Then, save the last file (filename `%3fid=%25%27+or+0%3D0+union+select+null%2C+version%28%29+%23&Submit=Submit`) as `dump.html`. Open this with a web browser, and note that the injection dumped the names of all the users in the database, as well as the operating system version.


