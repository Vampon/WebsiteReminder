# WebsiteReminder
Website information reminder tool based on simple crawler knowledge

Function
-------
If there is data update in the information part of the crawling website, the updated data will be saved in the record file, and the e-mail will remind you to update the information

Setup
-------
###Dependencies
* Numpy
* smtplib
* BeautifulSoup
* json
* os
* CentOS


Usage
-------
You need to edit the following files with root privileges

```
sudo vim /etc/crontab
```

Add the following command at the end of the file


```
* /2 * * * root /usr/bin/python3 /home/WebsiteReminder/spider.py > /home/WebsiteReminder/spider.log
```

The script will be executed at a rate of two hours


###Crontab writing explanation


```
* * * * * user command represents
*Minute* *Hour* *Day* *Month* *Week* *user* *command*
```

Contact
-------
If you have any questions, please contact me（403500543@qq.com）
[My Blog](http://vampon.club "VAM")