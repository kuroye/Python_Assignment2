# Python_Assignment2

This is Assignment2 for advanced programming in python course, this program can scrap realted informations from Coinmarketcap.com

## Installation

Make sure that you have installed beautifulsoup4 and requests libraries

```
pip install beautifulsoup4

pip install requests
```

## Usage

import Package and Class to your python file
```
from Assignment2 import Scrapper
```
create an object 
```
scrapper = Scrapper()

```

## Example

call the method and set parameter to scrap informations related to bitcoin
```
scrapper.my_scrapper("bitcoin")
```
output
```
[<td>$55,103.63</td>,
 <td><span>$195.27</span><div><span class="sc-15yy2pl-0 kAXKAX" style="font-size:12px;font-weight:600"><span class="icon-Caret-up"></span>0.36<!-- -->%</span></div></td>,
 <td><div>$54,264.26<!-- --> /</div><div>$56,006.37</div></td>,
 <td><span>$35,434,144,220.51</span><div><span class="sc-15yy2pl-0 kAXKAX" style="font-size:12px;font-weight:600"><span class="icon-Caret-up"></span>11.60<!-- -->%</span></div></td>,
 <td>0.03413</td>,
 ......
```
