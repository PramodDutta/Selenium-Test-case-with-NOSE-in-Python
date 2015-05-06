# Selenium-Test-case-with-NOSE-in-Python
Demo of Selenium Test cases with NOSE in Python

Creating a Selenium Test Cases for Nose:

Test 1 – Registration of the user in the http://demoaut.com/mercuryregister.php.

Test 2 – Login of the user to the http://demoaut.com/mercurysignon.php

using Selenium framework and With Results of the Test cases are managed by NOSE framework.

![Alt text](http://imagizer.imageshack.us/a/img538/8130/Q6CPVo.png "Optional title")

- Run all Test Cases in the Folder based on the Low or High priority. You can mention the priority of the test function by importing attr from nose.plugins.attrib
  "from nose.plugins.attrib import attr"
  Adding the attr annotations above Test Function.
  "@attr(priority="low")"
  Command line
  ">nosetests --verbosity=3"

![Alt text](http://imagizer.imageshack.us/a/img910/2479/5fEGRU.png "Optional title")
