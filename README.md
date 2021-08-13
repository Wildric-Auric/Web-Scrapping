# Web-Scraping
The script instagram scraping was originally created to download all pictures from an Instagram account. 
It's works like Selenium, which means that a real user is simulated. I didn't want to use selenium because of the fact 
that it limits it's use on a special web tab where it communicates that your computer is using an automated tool to
the website. With the tool I'm creating, it's impossible for the website to know if a program is running.
The first function I created was the one downloading the profile pic of someone. You have to get the source code
of the page and get the URL following "profile_pic_url_hd". There is a tutorial in GeeksForGeeks about this but their 
use of requests librairy is not good when you are managing to create instagram bots since Instagram policy is a constraint;
(see [this blog](https://blog.hubspot.com/marketing/bots-vs-humans-instagram#:~:text=The%20answer%20%2D%2D%20according%20to,large%20number%20of%20bot%20accounts.&text=If%20you%20really%20wanted%20to,news%2C%20don't%20be.))
Requests coming from an adress are highly restrained and it even bans the agent when a big amount of requests come from it 
which results in HTTP 429 error (see [this topic](https://stackoverflow.com/questions/56758333/error-429-with-simple-query-on-google-with-requests-python/56758488)). 
So, you get the error on  your first request! Requests would do the job faster, but it's use is limited in other extents,
Using a method of scraping different from Selenium made me face another issue: to get all images from instagram page, you should get the source 
code of the page, iterate over all "srcset" keyword, test if it's valid and download picture with highest resolution as it is like:
```html
srcset= "
    https://instagram.frak2-1.fna.fbcdn.net/v/t51.2885-15/e35/s150x150/235776336_3886225414816365_2529639022446482933_n.jpg?
    _nc_ht=instagram.frak2-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=xUSyygulaRwAX9hvv-_&tn=SG9EeeZ3-
    rAHjxXI&edm=ABfd0MgBAAAA&ccb=7-4&oh=2c7c2d1ec64633d05545e5f4726a217a&oe=611CA38C&_nc_sid=7bff83 150w,

    https://instagram.frak2-1.fna.fbcdn.net/v/t51.2885-15/e35/s240x240/235776336_3886225414816365_2529639022446482933_n.jpg?
    _nc_ht=instagram.frak2-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=xUSyygulaRwAX9hvv-_&tn=SG9EeeZ3-rAHjxXI&edm=ABfd0MgBAAAA&ccb=7-
    4&oh=155ee2ac27fc47309fed8a1187c1469c&oe=611D36C4&_nc_sid=7bff83 240w,

    https://instagram.frak2-1.fna.fbcdn.net/v/t51.2885-15/e35/s320x320/235776336_3886225414816365_2529639022446482933_n.jpg?
    _nc_ht=instagram.frak2-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=xUSyygulaRwAX9hvv-_&tn=SG9EeeZ3-rAHjxXI&edm=ABfd0MgBAAAA&ccb=7-
    4&oh=071eb8b296d7d96d4fc56dc26eb79f44&oe=611D8BDD&_nc_sid=7bff83 320w,

    https://instagram.frak2-1.fna.fbcdn.net/v/t51.2885-15/e35/s480x480/235776336_3886225414816365_2529639022446482933_n.jpg?
    _nc_ht=instagram.frak2-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=xUSyygulaRwAX9hvv-_&tn=SG9EeeZ3-rAHjxXI&edm=ABfd0MgBAAAA&ccb=7
    -4&oh=0515797596a7551e5b44e9e826701329&oe=611CCADF&_nc_sid=7bff83 480w,

    https://instagram.frak2-1.fna.fbcdn.net/v/t51.2885-15/e35/235776336_3886225414816365_2529639022446482933_n.jpg?
    _nc_ht=instagram.frak2-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=xUSyygulaRwAX9hvv-_&tn=SG9EeeZ3-rAHjxXI&edm=ABfd0MgBAAAA&ccb=7-
    4&oh=a94e9f75eedb6c31af32584c0c0eee5e&oe=611D1328&_nc_sid=7bff83 640w
"
```
We should pick the last url as it contains an image of size 640x640 px (always the last, it is sorted)
The issue is that the original source code does not contain all pictures, Instagram load them in shunks while user is scrolling
down and delete top pictures. Instagram is dynamic because of it based a lot on JavaScript, meanwhile the shortcut "ctrl+u" open a page
of the original source code.
To get the current source code, you can get get it by inspecting the page, showing it as one string is only possible if you master JavaScript.
Fortunately, I found a google extension made by [Thomas Greiner](https://github.com/ThomasGreiner) which is [view-current-source](https://chrome.google.com/webstore/detail/view-current-source/bloebkffnmchginelkmdcemamcdeamei)
it allows you to see the current source code. However there is no shortcut for it, so I just controlled the mouse using Pynput to access it:







![Extension](https://github.com/Wildric-Auric/Web-Scrapping/blob/89d3d1121144557ef10f9377379d0c9f1d79e5eb/Capture%20d%E2%80%99%C3%A9cran%202021-08-13%20153959.png)
