#Homework 3
import sqlite3
import pandas as pd
import os
def create_dataframe(path):
	if not os.path.exists(path):
		raise ValueError('Path doesn\'t exist')
	else:
		conn=sqlite3.connect(path)
		dataframe=pd.read_sql_query("SELECT video_id, category_id, 'US' as Language FROM USvideos UNION SELECT video_id, category_id, 'GB' as Language FROM GBvideos UNION SELECT video_id, category_id, 'FR' as Language FROM FRvideos UNION SELECT video_id, category_id, 'DE' as Language FROM DEvideos UNION SELECT video_id, category_id, 'CA' as Language FROM CAvideos;", conn)
		return dataframe