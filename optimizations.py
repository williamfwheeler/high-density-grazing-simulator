from high_density_grazing import Plot, Paddock, Herd

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