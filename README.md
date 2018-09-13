# Topographic Influences on Snowmelt in a Warmer World 
### With Airborne Snow Observatory (ASO) Lidar Data
### Geohackweek 2018

Slack channel: [#snowmelt](https://geohackweek2018.slack.com/messages/CCQT0KTHC)

---

### Collaborators:
* Nicoleta Cristea (cristn@u.washington.edu) (Data Science Lead)
* Cassie Lumbrazo (lumbraca@uw.edu) (Project Lead)
* Steven Pestana (spestana@uw.edu)
* 

---

### The Problem:
* ASO lidar can provide snapshots of snowdepth across a watershed
* Previous geohackweek projects have developed tools for the spatial analysis of this data
* We want to expand these tools to investigate temporal changes in snow depth (melt) as a function of topgraphic variables

---

### Broader Impacts: 
* The Tuolumne River Basin (TRB) is a major water supply for human use in California
* It is expected that with climate change, more future years will resemble the 2015 water year 
* Winter snowpack in the TRB is a natural form of water storage, that may change due to climate change
* We can test the hypothesis suggested by previous work - that snowmelt will be slower in warmer temperatures


---

### Application Example:
* Incorporating streamflow, the results could help improve modeling and water resources prediction
* Results could be compared against model outputs to evaluate a model's performance
* Future investigations: snow accumulation/snow change in depressions (current models may not capture this well)

---

### Data:
https://drive.google.com/drive/folders/1uhxMHkf9YgU2qVDntqTGSbzZlJY0v94X
* Snow depth (30m, ASO lidar-derived) 2014 - 2016
* DEM (30m, ASO lidar-derived)

---

### Specific Questions:
* How does the change in snow depth (melt and accumulation) behave as a function of topography (slope, aspect, elevation) in the Tuolumne River watershed?
* How does the change in snow depth (melt and accumulation) behave as a function of forest cover (forested versus not forested) in the Tuolumne River watershed?
* How do these behaviors compare between relatively “normal” snowpack years (2014, 2016) and a year with much lower snowpack (2015 - representative of future conditions due to climate change)? 
* Can we conclude that there is “slower snowmelt in a warmer world” (Musselman et al. 2017)?

---

### Existing Methods/Tools:
* https://github.com/NCristea/NCristeaGEE 

---

### Proposed Methods/Tools:
* Raster/array math

---

### Background Reading:
* NASA JPL - [Airborne Snow Observatory](https://aso.jpl.nasa.gov/)
* Musselman, Keith N., et al. "Slower snowmelt in a warmer world." Nature Climate Change 7.3 (2017): 214. doi: 10.1038/nclimate3225  https://www.nature.com/articles/nclimate3225.pdf 
* Painter, T. H., Berisford, D. F., Boardman, J. W., Bormann, K. J., Deems, J. S., Gehrke, F., ... & Mattmann, C. (2016). The Airborne Snow Observatory: Fusion of scanning lidar, imaging spectrometer, and physically-based modeling for mapping snow water equivalent and snow albedo. Remote Sensing of Environment, 184, 139-152.
