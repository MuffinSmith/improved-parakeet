### Guided Practice: Wireshark Tips and Tricks

- In this activity, you will work on customizing your Wireshark setup to be even more useful.

- As you customize Wireshark, keep in mind the types of questions you want to be able to answer:
    - What is the source and destination of traffic?
    - What are the source and destination ports?
    - What website is the http request coming from?

#### Setup

- For this activity, use the pcap file located [HERE](https://wiki.wireshark.org/SampleCaptures?action=AttachFile&do=get&target=Obsolete_Packets.cap)

- This is just a sample pcap so you have data in Wireshark while you make configurations. If you already have a pcap loaded in Wireshark, you can use that.


#### Instructions

- Let's start by taking a look at the different column options!
    - Did you know you can remove columns just by right clicking on them and un-checking or removing them?
    - Take out some of the columns that you see that don't interest you.
    - Some recommended columns to remove might be:
        - `No.` or `Length`
![](../../Images/RemoveColumns.jpg)
- Now create some new columns that might be more helpful!
    - Go to `Edit > Preferences` and choose Columns under Appearance on the left side.
    - If you're using a Macintosh, it will be `Wireshark > Preferences`
    - Here there are many different options that can be added or removed.
![](../../Images/ColumnsRemove.jpg)

- Let's start by changing the time to be more readable.
    - Change the display of the time column to a more readable format.
    - Click on `Time (format as specified)` and change it to `UTC date, as YYYY-MM-DD, and time`
![](../../Images/ChangeTime.jpg)
![](../../Images/ChangeTime2.jpg)
- How about a column that shows you the name of a website?
    - Use the `+` sign at the bottom to add a custom column.
    - Change `New Column` to `Host` and in the drop down, choose `Custom`
    - Double click on the `Fields` column and enter `http.host`
![](../../Images/Host.jpg)
![](../../Images/Host2.jpg)
- Would it be nice to see source or destination ports?
    - Use the `+` sign at the bottom to add a custom column.
    - Change `New Column` to `Src Port` and in the drop down, choose `Source Port`
![](../../Images/Port.jpg)
- Explore other options you might add and take some time to customize your columns exactly to your preference.

- When you are finished with your custom columns, go to the `Font and Colors` option.
    - Customize the colors to your liking.
![](../../Images/Colors.jpg)
    - Remember that you can turn colors off altogether with the color toggle button on the toolbar.
![](../../Images/ColorsOff.jpg)
- Move on to the Layout option and try a few different layouts to see which ones you might like.
    - Definitely try the side by side option.
    - When your finished, close the Preferences pane.
![](../../Images/Layout.jpg)
- That's it! Don't be afraid to explore the Wireshark interface to make it more usable.
