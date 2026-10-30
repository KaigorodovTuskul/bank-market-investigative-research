import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from funding_economics import calculate

class EconomicsTest(unittest.TestCase):
    def setUp(self):
        self.data={"principal_rub":"500000000","average_balance_rub":"500000000","days":90,
                   "day_count":365,"direct_rate":"0.145","agent_rate":"0.14",
                   "upfront_fee_rate":"0.001","other_costs_rub":"100000"}
    def test_base(self):
        result=calculate(self.data)
        self.assertEqual(result['agent_fee_rub'],'500000.00')
        self.assertEqual(result['gross_saving_rub'],'616438.36')
        self.assertEqual(result['net_before_other_costs_rub'],'16438.36')
        self.assertEqual(result['breakeven_days'],'87.60')
    def test_partial_balance(self):
        self.data['average_balance_rub']='350000000'
        result=calculate(self.data)
        self.assertEqual(result['net_before_other_costs_rub'],'-168493.15')
    def test_nonpositive_spread_no_break_even(self):
        self.data['agent_rate']='0.15'
        self.assertIsNone(calculate(self.data)['breakeven_days'])
    def test_bad_basis(self):
        self.data['day_count']=0
        with self.assertRaises(ValueError):calculate(self.data)
if __name__=='__main__':unittest.main()
