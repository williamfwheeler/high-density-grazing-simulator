from high_density_grazing import Plot, Paddock, Herd
from math import ceil

class Optimizations:

    '''ADD DESCRIPTIONS AND COMMENTARY'''

    def potential_herd_weight(self,plot,no_of_paddocks,proxy_herd,proxy_paddock,target_utilization):
    
        plotlengthneeded = proxy_paddock.regrowth_period/(no_of_paddocks-1)
        
        forage_per_paddock = (proxy_paddock.forage_height*proxy_paddock.dry_matter_per_inch_acre*target_utilization)*(plot.total_acreage/
                                                                                            no_of_paddocks)
        
        daily_forage_available = forage_per_paddock / plotlengthneeded
        
        potential_herd_weight = daily_forage_available/proxy_herd.body_weight_eaten
        
        return round(potential_herd_weight,0) #,plotlengthneeded


    
    def acres_needed(self,herd,no_of_paddocks,proxy_paddock,target_utilization):
    
        plotlengthneeded = proxy_paddock.regrowth_period/(no_of_paddocks-1)
        
        herd90dayneed = herd.herd_forage_need*plotlengthneeded
        
        acres_needed_per_paddock = herd90dayneed/(proxy_paddock.forage_height*
                                            proxy_paddock.dry_matter_per_inch_acre*target_utilization)
        
        acres_needed = acres_needed_per_paddock * no_of_paddocks
        
        return round(acres_needed,2) #, no_of_paddocks, acres_needed_per_paddock

    

    # determine optimal paddock structure given plot and herd characteristics
    def optimize_paddock_structure(self,plot,herd,proxy_paddock,target_density,target_utilization):
        
        '''Need to account for excess room in plot OR too little room
            if too much, provide potential capacity given
            if too little, provide error or excess feed required (changing density doesn't change the math
            that there's too little feed)'''
        
    #     optimal paddock size given density
        paddock_size = herd.herd_weight / target_density
        
        test = Paddock(paddock_size,proxy_paddock.forage_height)
        
        length_of_stay = test.graze_target_util(herd,target_utilization)
        
        paddocks_needed = ceil(proxy_paddock.regrowth_period/length_of_stay)
        
        total_acres_needed = paddocks_needed * paddock_size
        
        cycle_time = paddocks_needed*length_of_stay
        
    #     generate paddock list for ideal paddock distribution
        paddock_list = [Paddock(paddock_size,proxy_paddock.forage_height,proxy_paddock.regrowth_period,
                                proxy_paddock.dry_matter_per_inch_acre) for x in range(paddocks_needed)]
        

        
        return paddock_list, paddocks_needed, paddock_size, length_of_stay, total_acres_needed, cycle_time

    
    # determine max herd_weight given plot
    def max_herd_weight(self,plot,herd,proxy_paddock,target_density,target_utilization):
    
        potential_herd_weight = self.potential_herd_weight(plot,4,herd,proxy_paddock,target_utilization)
        
        test_herd = Herd(potential_herd_weight,herd.avg_head_weight,herd.body_weight_eaten)
        
        new_paddock_ct = self.optimize_paddock_structure(plot,test_herd,proxy_paddock,target_density,target_utilization)[1]
        
        max_herd_weight = potential_herd_weight(plot,new_paddock_ct,herd,proxy_paddock,target_utilization)
    
        return int(max_herd_weight)