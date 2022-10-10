import unittest
import high_density_grazing as hdg
import optimizations as opt

class test_optimizations(unittest.TestCase):

    def test_optimize_paddock_structure(self):
        plot1 = hdg.Plot(200)
        proxy_herd = hdg.Herd(30000)
        proxy_paddock = hdg.Paddock(200,15)
        target_utilization = 0.75
        target_density = 25000

        herd_possible = opt.max_herd_weight(plot1,proxy_herd,proxy_paddock,target_density,target_utilization)
        new_herd = hdg.Herd(herd_possible)

        test = opt.optimize_paddock_structure(new_herd,proxy_paddock,target_density,target_utilization)
        land_needed = test[4]

        # remove_paddock working
        self.assertEqual(land_needed,plot1.total_acreage)



if __name__=='__main__':
    unittest.main()