# Project1 @ Metis: MTA Data Analysis
Published On January 22, 2018

## A Short and Productive Week:

I started my first week of this intense yet exciting 12-week Data Science Bootcamp with my first project in Metis. Right away, we were divided into groups of 2 to start working on this Data Exploratory project which was due in next 3 days. I could feel the intense pressure I was going through......Thanks to all who wrote those uplifted quotes on the wall in Metis premisis :smile:.
The objective of the project was to make recommendation to a hypothetical client “Women Tech, Women Yes” on how they should allocate their volunteers for their upcoming fund raising event, the WTWY Gala, so that they could optimize collection of signatures and gala attendance.


## Approach:

With the objective of gaining support for WTWY’s cause, our team sought to target the demographics which we believed would be most sympathetic to the organization’s goals. With that in mind, we target subway stops which had the following factors in common:

** High overall traffic level **
** Located in an area with the highest concentration of tech companies **
** Located in an area with the highest rates of funding for tech companies **

## Methods & Analysis

With the idea of the gala would take place in early summer, it seemed ideal to look at the most recent trends in the months leading up to the event.So, we scrape and clean data which spanned 90 days from March-May of 2017. Then, to get a broad perspective of subway traffic trends we were able to group entries by station and look at the aggregate entries for each station during the full 90 day span of the data.

From the aggregate data, we wanted to look at the most trafficked stations only. Figure 1 demonstrates our results for the top 15 stations with the most entries. Most of these stations are concentrated in the Midtown area of Manhattan, with a smaller cluster in lower Manhattan near the financial district and a few others anomalies which are much farther north, though still in Manhattan. As we compared these preliminary results with our data from Build in NYC, it was clear that there was a good deal of overlap between heavily trafficked subway stops and clusters of tech companies. In fact, most of our top 15 stops were located within the 4.5 mile region cited as having the highest concentration of tech companies. (INSERT FIGURE WITH MAP) When we zoom in to individual zip codes and look at those with the highest funding for tech ventures, we again see significant overlap. Because these areas overlap to a large extent with our areas of high tech company density, we also see a few station names crop up on both lists. Our team took note of such stations and decided to zoom in on a single stop for further analysis.

Grand Central Station is undoubtedly a consistently heavily trafficked area. It is also conveniently located within our 4.5 mile region previously mentioned. Additionally it is located just blocks from 10016 and 10018 in midtown, two areas on the top 10 list for highest tech funded zip codes. For these reasons, we wanted to use Grand Central as a test case for further analysis. One further point of consideration for our team was that different stations might have varying levels of traffic by day of the week or hours of the day (with the latter being more likely). In Grand Central, March-May of 2017 in particular, weekdays dominated over weekends, with relatively consistent levels through the week and a peak on Thursdays. When we examine traffic on an hourly basis it seems that late evenings are most trafficked in Grand Central Station, with noticeable peaks in early morning and early evening hours being more consistent with rush hours in the city.

## Conclusions

In the end my team came up with the following list of recommended stations:

** 34th St-Penn **
** 23rd St **
** 42nd St Grand Central **
** 42nd St Times Sq **
** Fulton St **
** Canal St **

Overall , this week was not less than roller coaster ride. And no doubt there was so much to learn . Looking forward to learn more with the support of instructors, the TAs, and the rest of the class. 
