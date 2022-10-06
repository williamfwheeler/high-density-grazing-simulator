class Herd:
    
    ''' this holds all herd charactistics where size is primarily
    calculated in poundage (herd weight) rather than headcount (per HDG documentation standards)
    
    This dictates appetite and forage required (body_weight_eaten)
    
    Herd weight will also be the ultimate measure of success
    
    Herd Variables: herd_weight, avg_head_weight, body_weight_eaten, body_weight_eaten_lb, herd_forage_needed'''
    
    def __init__(self, herd_weight, avg_head_weight=1200, body_weight_eaten=0.025):
#         self.herd_size = herd_size
        self.herd_weight = herd_weight
        self.avg_head_weight = avg_head_weight
        self.body_weight_eaten = body_weight_eaten
        
        self.body_weight_eaten_lb = body_weight_eaten * avg_head_weight
        self.herd_forage_need = herd_weight * body_weight_eaten
        
#     LATER factor in herd selectivity of forage, not sure what that would look like as a metric



class Plot:
    
    '''Plot encompasses the entire property and is primarily of use
    to hold the Paddock class. The plot is intended to be divided into
    optimal paddocks
    
    Plot Variables: total_acreage, paddock_list
    
    Plot Methods: add_paddock, remove_paddock'''
    
    def __init__(self,total_acreage,paddock_count=0):
        self.total_acreage = total_acreage
        self.paddock_count = paddock_count
        self.paddock_list = []
        
    def add_paddock(self,paddock):
        self.paddock_list.append(paddock)
        self.paddock_count+=1
    
    def remove_paddock(self,paddock_name):
        for x in range(len(self.paddock_list)):
            if self.paddock_list[x] == paddock_name:
                self.paddock_list.pop(x)
                self.paddock_count-=1
                break



class Paddock:
    
    '''Paddock class is the primary functional unit and counterpart to the herd.
    
    The paddock holds all information on available feed, time for proper regrowth
    and ultimately plant density (the key target variable we're trying to improve.)
    
    Paddock Variables: acreage, forage_height, regrowth_period, dry_matter_per_inch_acre, utilization,
    dry_matter_available
    
    Paddock Methods: graze_target_util, graze_days, regrow '''
    
    def __init__(self, acreage, forage_height, regrowth_period=90, dry_matter_per_inch_acre=200, utilization = 1.00):
        self.acreage = acreage
        self.forage_height = forage_height
        self.regrowth_period = regrowth_period
        self.dry_matter_per_inch_acre = dry_matter_per_inch_acre
        self.utilization = utilization
        self.dry_matter_available = dry_matter_per_inch_acre * forage_height * acreage
        self.max_dry_matter = self.dry_matter_available / utilization


    
    def graze_target_util(self,herd,utilization_target):
#     graze till target utilization reached
    
        if utilization_target < 0 or utilization_target > 1:
            raise Exception("Utilization out of bounds 0.0 - 1.0")
        else:
            incremental_utilization = (self.utilization - utilization_target)

            feed_till_target_available = self.dry_matter_available * incremental_utilization

            days_on_paddock = feed_till_target_available / herd.herd_forage_need

    #         reset persistent forage availability variables (utilization, forage_height, dry_matter_available)

            self.utilization = utilization_target

            self.forage_height = self.forage_height - (self.forage_height*incremental_utilization)

            self.dry_matter_available = self.dry_matter_per_inch_acre * self.forage_height * self.acreage

            return days_on_paddock
        
        
    
    def graze_days(self,herd, graze_days):
#         graze for a set number of days
        
        implied_forage_needed = herd.herd_forage_need * graze_days
        
        if implied_forage_needed > self.dry_matter_available:
            days_on_paddock = self.dry_matter_available / herd.herd_forage_need
#             raise Exception('ERROR: more feed required than is available')
            raise Exception("Max of {0} days on paddock to graze to 0 utilization".format(days_on_paddock))
        else:
#             adjust persistent forage availability variables 
            self.dry_matter_available = self.dry_matter_available - implied_forage_needed
            self.forage_height = self.max_dry_matter / self.acreage / self.dry_matter_per_inch_acre
            self.utilization = self.dry_matter_available / self.max_dry_matter


            
    def regrow(self):
#         regrow plot command to be signalled after recovery period

    #             adjust persistent forage availability variables 
        self.dry_matter_available = self.max_dry_matter
        self.forage_height = self.max_dry_matter / self.dry_matter_per_inch_acre
        self.utilization = 1.0
