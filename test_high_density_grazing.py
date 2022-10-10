import unittest
import high_density_grazing as hdg

class test_high_density_grazing(unittest.TestCase):

    def test_Plot(self):
        test = hdg.Plot(200)

        # default value of paddock_count
        a = test.paddock_count
        self.assertEqual(a,0)

        # add_paddock working
        test.add_paddock('name1')
        test.add_paddock('name2')
        self.assertEqual(test.paddock_count,2)

        # paddock_list working
        self.assertEqual(test.paddock_list,['name1','name2'])
        
        # remove_paddock working
        test.remove_paddock('name1')
        self.assertEqual(test.paddock_count,1)
        self.assertEqual(test.paddock_list,['name2'])


    def test_Herd(self):
        test = hdg.Herd(30000)
        # confirm variable setup
        self.assertEqual(test.avg_head_weight,1200)
        self.assertEqual(test.body_weight_eaten,0.025)
        self.assertEqual(test.body_weight_eaten_lb,30)
        self.assertEqual(test.herd_forage_need,750.0)

        test = hdg.Herd(30000,1400,0.4)
        # confirm variable setup
        self.assertEqual(test.avg_head_weight,1400)
        self.assertEqual(test.body_weight_eaten,0.4)
        self.assertEqual(test.body_weight_eaten_lb,560)
        self.assertEqual(test.herd_forage_need,12000)

    def test_Paddock_graze_target(self):
        test = hdg.Paddock(200,20)
        herd = hdg.Herd(200)
        self.assertEqual(test.dry_matter_available,800000)

        # confirm grazing spills down to other persistent variables
        test.graze_target_util(herd,0.7)
        self.assertEqual(test.forage_height,14)
        self.assertEqual(test.utilization,0.7)
        self.assertEqual(test.dry_matter_available,560000)

        # confirm no additional grazing days available after graze
        self.assertEqual(test.graze_target_util(herd,0.7),0)

    def test_regrow(self):
        test = hdg.Paddock(100,10)
        herd = hdg.Herd(200)
        self.assertEqual(test.utilization,1)
        self.assertEqual(test.forage_height,10)
        self.assertEqual(test.max_forage_height,10)

        test.graze_target_util(herd,0.7)
        test.regrow()
        self.assertEqual(test.utilization,1)
        self.assertEqual(test.forage_height,10)
        self.assertEqual(test.max_forage_height,10)

        

if __name__=='__main__':
    unittest.main()