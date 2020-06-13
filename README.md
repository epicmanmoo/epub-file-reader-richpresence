# epub-file-reader-discrichpresence 
## Yet another Discord related thing I made.

### This 'plugin' (not hosted on any server) allows you to show off what you're reading with epub file reader on Discord. This works on Windows (probably does not on other operating systems). Of course, you must have epubfilereader installed which you can get here: http://www.epubfilereader.com/. Next, place the epubfilereader.exe under `C:\Users\yourname\` This allows for easier lookup for connecting to the epubfilereader while it is active on your desktop. With that out of the way, you can pip install the necessary libraries such as discoIPC, psuitl, pywinauto (I used pywinauto==0.5.4), and win32gui. Next, you must create your own Discord application. The steps are not too complicated.
  1. Make a discord account if you do not already have one at https://discord.com/
  2. Once you are logged in, go to https://discord.com/developers/applications/
  3. Press New Application and give it a name
  4. On the left hand side, click Rich Presence
  5. Scroll down to Rich Presence Assets
  6. Add an image if you'd like and remember to give it a unique name. As you will see in the code, there is an area called 'large_image':      'book', you can simply replace that with the name of the image you chose (or it could be the same)
  7. Using the left hand side, go back to General Information 
  8. You will see Client ID which you can simply copy by pressing the button
  9. Place this in the config.ini file where it is noted with NO quotes and you are done
### Once the above steps are completed, simply run the script in python and open epubfilereader. If you've used this application before, you know how to open epub files. If not, well that's not too complicated. Download a book in .epub format and inside EPUB file reader click 'File' -> 'Open' and choose the .epub book you just downloaded. Now watch as your rich presence changes! Your friends can now see what you're reading ;)
