# Project1 @ Metis: MTA Data Analysis
Published On January 22, 2018

## A Short and Productive Week:

I started my first week of this intense yet exciting 12-week Data Science Bootcamp with my first project in Metis. Right away, we were divided into groups of 2 to start working on this Data Exploratory project which was due in next 3 days. I could feel the intense pressure I was going through......Thanks to all who wrote those uplifted quotes on the wall in Metis premisis :simple_smile:.

The objective of the project was to make recommendation to a hypothetical client “Women Tech, Women Yes” on how they should allocate their volunteers for their upcoming fund raising event, the WTWY Gala, so that they could optimize collection of signatures and gala attendance.And the week concluded with the presentation of our cohort's first project, Project Benson.


## Approach:

With the objective of gaining support for WTWY’s cause, our team sought to target the demographics which we believed would be most sympathetic to the organization’s goals. With that in mind, we target subway stops [MTA turnstile data](http://web.mta.info/developers/turnstile.html).  which had the following factors in common:

* High traffic 
* Area with the highest concentration of tech companies 
* Area with the highest rates of funding for tech companies 

## Methods & Analysis

With the idea of the gala would take place in early summer, it seemed ideal to look at the most recent trends in the months leading up to the event.So, we scrape and clean data which spanned for 3 months from March-May of 2017. Then, to get a broad perspective of subway traffic trends we were able to group entries by station and look at the aggregate entries for each station during the full period of the data.

![Fig 1](https://github.com/PinkyJ12/Johar_Metis/blob/master/Project%201/images/Entries_total.png)


From the aggregate data, we wanted to look at the most trafficked stations only. Fig 1. demonstrates our results for the top 15 stations with the most entries. Most of these stations are concentrated in the Midtown area of Manhattan, with a smaller cluster in lower Manhattan near the financial district and a few others anomalies which are much farther north, though still in Manhattan. As we compared these preliminary results with our data from Build in NYC, it was clear that there was a good deal of overlap between heavily trafficked subway stops and clusters of tech companies. In fact, most of our top 15 stops were located within the 4.5 mile region cited as having the highest concentration of tech companies.
<p>When we zoomed in to individual zip codes and look at those with the highest funding for tech ventures, we again see significant overlap. Because these areas overlap to a large extent with our areas of high tech company density, we also see a few station names crop up on both lists. Our team took note of such stations and decided to zoom in on a single stop for further analysis.

Grand Central Station is undoubtedly a consistently heavily traffic area which is located within our 4.5 mile region mentioned before. Additionally it is located just blocks from 10016 and 10018 in midtown, two areas on the top 10 list for highest tech funded zip codes. For these reasons, we decided to use Grand Central as a test case for further analysis. One further point of consideration for our team was that different stations might have varying levels of traffic by day of the week or hours of the day (with the latter being more likely). In Grand Central, March-May of 2017 in particular, weekdays dominated over weekends, with relatively consistent levels through the week and a peak on Thursdays.

![Fig 2](/images/GRND_CNTRL.png) 

After examining traffic on an hourly basis it was found that late evenings were most trafficked in Grand Central Station, with noticeable peaks in early morning and early evening hours being more consistent with rush hours in the city.
 
![fig 3](/images/GRND_CNTRL_hourly.png) 
![fig 4](/images/Line_chrt.png)

## Conclusions

In the end we came up with the following list of recommended stations:

* 34th St-Penn 
* 23rd St 
* 42nd St Grand Central 
* 42nd St Times Sq 
* Fulton St 
* Canal St 

Overall , this week was not less than roller coaster ride and now would love to have this ride again and again, knowing things are going to be better than yesterday  Looking forward to learn more with the support of instructors, the TAs, and the rest of the class. Your support in time to time is really commendable.
