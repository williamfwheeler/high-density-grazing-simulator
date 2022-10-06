# high-density-grazing-simulator
This script simulates the potential benefit of utilizing the technique High Density Grazing.

## High Density Grazing
High Density Grazing is a tehchnique that ultimately seeks to improve the fertility of the pastures by using a denser, combined herd. The combined manure and trampling of this denser, single herd, moved regularly from paddock to paddock (where suitable recovery time is allowed) leads to greater plant density on regrowth. More plant material per acre can then support more cattle/sheep/bison/shaak.

## Model Intent
The intent of this model is to provide the max herd size that can sustainably be kept on a given plot. Optimize_paddock_structre returs how many subdivided pastures/paddocks will be necessary and how long teh combined herd can stay on each paddock. 

By inputting today's Plot forage characteristics and runnign density we have a baseline for improvement. The key variable that we are seeking to affect is plant density (in terms of lb_per_inch_acre). 

As you assume the benefits of high density grazing to plant density, you can run the implied NEW max herd for the same plot of land. The difference between this and the baseline is your implied benefit.

## Key Variables
```python
# Determine max herd capable of being sustained on land
max_herd = max_herd_weight(plot1,proxy_herd,proxy_paddock,target_herd_density,target_utilization)

optimized_herd = Herd(max_herd,avg_head_weight,body_weight_eaten_daily)

# Determine optimal paddock structure using max_herd
result = optimize_paddock_structure(plot1,optimized_herd,proxy_paddock,target_herd_density,target_utilization)
```

<p align="center">
  <img src="./images/plant_density_illustration.png" width="620px">
</p>

## Demo Walkthrough


## Disclaimers


## Future Improvements


## References & Resources
I sourced most of key assumptions from this USDA document.

[USDA PDF explaining HDG](https://www.nrcs.usda.gov/wps/PA_NRCSConsumption/download?cid=nrcseprd1630415&ext=pdf)

[Noble Research Institute](https://www.noble.org/news/publications/ag-news-and-views/2019/april/what-is-high-stock-density-grazing/#:~:text=High%20stock%20density%20grazing%20begins,forages%20and%20ultimately%20livestock%20production.)