import numpy as np
import pandas as pd
import homework3
import unittest

class testhw3(unittest.TestCase):
	
	#Test if column names are video_id, category_id and Language
	def test_col_names(self):
		df=homework3.create_dataframe('class.db')
		cols=set(df.columns)
		t=set(['video_id','category_id','Language'])
		self.assertTrue(t.intersection(cols) == t)
	
	#Test if number of rows is greater than 10
	def test_num_rows(self):
		df=homework3.create_dataframe('class.db')
		self.assertTrue(df.shape[0]>10)
	
	#Check if video_id and Language is a key
	def test_key(self):
		df = homework3.create_dataframe("class.db")
		self.assertTrue(len(df) == df.groupby(['video_id', 'Language']).ngroups)
		
	
	#Check for correct exception when invalid path is given
	def test_invalid_path(self):
		self.assertRaises(ValueError, homework3.create_dataframe, "example.db")
		 
if __name__ == '__main__':
    unittest.main()