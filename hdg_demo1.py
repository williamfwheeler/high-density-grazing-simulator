from high_density_grazing import Herd,Plot,Paddock
from optimizations import *
import inspect

# Plot Characteristics
total_acreage = 200     #in acres
forage_height = 15      #in inches
regrowth_period = 90    #in days
dry_matter_per_inch_acre = 200  #in lbs

# Herd Characteristics
avg_head_weight = 1200  #in lbs
body_weight_eaten_daily = 0.025  # as % of body weight

# Behavioral Targets
target_utilization = 0.50 #as % of forage height eaten
target_herd_density = 25000 # as herd_lb per acre


# Load plot acreage into Plot
plot1 = Plot(total_acreage)

# Load plot characteristics to proxy paddock
proxy_paddock = Paddock(1,forage_height,regrowth_period,dry_matter_per_inch_acre)

# Load herd characteristics to proxy herd
proxy_herd = Herd(200,avg_head_weight,body_weight_eaten_daily)


# Determine max herd capable of being sustained on land
max_herd = max_herd_weight(plot1,proxy_herd,proxy_paddock,target_herd_density,target_utilization)

optimized_herd = Herd(max_herd,avg_head_weight,body_weight_eaten_daily)

# Determine optimal paddock structure using max_herd
result = optimize_paddock_structure(plot1,optimized_herd,proxy_paddock,target_herd_density,target_utilization)

paddock_list, paddocks_needed, paddock_size, length_of_stay, total_acres_needed, cycle_time = result

