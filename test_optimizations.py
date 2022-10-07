import unittest
import high_density_grazing as hdg
import optimizations as opt

class test_optimizations(unittest.TestCase):

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


        

if __name__=='__main__':
    unittest.main()