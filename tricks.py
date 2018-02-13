GENERAL
-------

- Parallel: dask
- Automated ML: TPOT
- EDA: pandas_profiling
- Plot ML: Yellowbrick
- ELI 5 (PermutationImportance) (show_prediction)
- LIME


Use Jupyter notebooks with parallel computing
pip3 install ipyparallel
ipcluster nbextension enable

Towards interpretable reliable models (PyWarsaw 2k17)
Debugging ML

Github: Data_science_delivered

Update your libraries every so often:
 pip3 install pandas --upgrade


 >> Tommi Jaakkola from MIT works towards interpretable machine learning models


Tricks

"""
    Add the current repo to the path
"""

from mlToolbox import *
from utils import *


AWS Sagemaker
-------------

# Read a pickle file from S3 (there's only one file in that bucket)

import boto3

bucket         = 'amazon-sagemaker-poc'

region         = boto3.Session().region_name
s3Client       = boto3.client('s3');
bucketList     = s3Client.list_objects_v2(Bucket=bucket);
bucketContents = [currentKey['Key'] for currentKey in bucketList['Contents']];
print(bucketContents)

obj = s3Client.get_object(Bucket=bucket, Key='tpsPurchases.pickle')
response = obj['Body'].read()

dfFromPickle = pickle.loads(response)
print(dfFromPickle.shape)


# Mutiprocessing. use MP with a function that accepts several arguments, being the 1st one
# the ONLY one that changes
	import multiprocessing as mp
	from functools import partial

	def worker(a,b,c,d):
		"""thread worker function"""
		print('A -> {},B -> {},C -> {},D -> {}'.format(a,b,c,d))
		return a-100

	cores      = mp.cpu_count()
	maxCores   = cores-1
	pool       = mp.Pool(maxCores)
	# use partial to fix the arguments that don't change
	worker_a = partial(worker, b='b',c='c',d='d')
	dataChunks = range(10000)
	results = pool.map(worker_a, dataChunks)
	pool.close()
	pool.join()


# Mutiprocessing with DATAFRAMES
	def parallelSum(df,b,c,d):
		a   = df.TEST.sum()
		dfA = pd.DataFrame(data=[{'results': a}])
		print('A -> {},B -> {},C -> {},D -> {}'.format(a,b,c,d))
		return dfA

	df = pd.DataFrame(np.random.random_sample((50000,1)), columns=['TEST'])
	df_split = np.array_split(df, 100)

	cores      = mp.cpu_count()
	maxCores   = cores-1
	pool       = mp.Pool(maxCores)
	# use partial to fix the arguments that don't change
	worker_a = partial(parallelSum, b='b',c='c',d='d')
	results = pool.map(worker_a, df_split)
	pool.close()
	pool.join()
	# The results are a list of dataframes
	extResults  = pd.DataFrame();
	for thisDF in results:
		extResults  = extResults.append(thisDF, ignore_index=True);





Exceptions:
    # Couldn't love PANDAS more...
    try:
        dfAdform = pd.read_csv(adformPath, delimiter='\t', compression='gzip');
    except Exception as e:
        dfAdform = pd.DataFrame()
        print('Cannot read {}'.format(adformPath))


Find values in a list:
	# try out the value 'covergirl' in' operator
	covergirlValues = [s for s in fNames if re.search('covergirl', s)];# with regEx
	covergirlValues = [s for s in fNames if 'covergirl' in s];# no regex


Types. perform differenct actions based on the datatype:

    if isinstance(filterValue, list):
        idxFilter = dfAdform[filterName].isin(filterValue);
    elif isinstance(filterValue, int):
        idxFilter = dfAdform[filterName] == filterValue;
		else:
			...


















































PANDAS/DATAFRAMES
----------------------------

Create a pivot table with Pandas:
	dfPurchasesFiltPerDay = pd.pivot_table(dfPurchasesFilt, values='productCount',
		index=['productName'], columns=['hour'], aggfunc=np.mean)


Homemade aggregations (get stats for a column):
	dfPurchasesFiltStats = dfPurchasesFilt.groupby(['productName']).agg({'productCount': ['min', 'max', 'mean', 'std', 'sum']});
	dfPurchasesFiltStats = dfPurchasesFiltStats['productCount'].sort_values('sum', ascending=[0]);



[Added to the cookbook]
Time operations. Get hour and month from timestamp

df = pd.DataFrame([{'Timestamp': pd.tslib.Timestamp.now()}]);
df['month']       = df.Timestamp.dt.month;
df['hour']        = df.Timestamp.dt.hour;
df['day']         = df.Timestamp.dt.day;
df['day_of_week'] = df.Timestamp.dt.dayofweek;




Indexing a value in a DF (same result):
	idx = 0;
	dfTPminimal.CookieID.iloc[idx]
	dfTPminimal.iloc[idx].CookieID
	dfTPminimal.CookieID[idx]


Memory footprint of a DF:
	df.info();

To visualise dataframes a bit better:
	pd.set_option('expand_frame_repr', False)


Equal size DF:
	df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10,11], columns=['TEST'])
	df_split = np.array_split(df, 3)
	Gives a list with the chunked DF

Skip rows when reading a dataframe:
train = pd.read_csv('../input/train.csv', usecols=[1,2,3,4], dtype=dtypes, parse_dates=['date'],
                    skiprows=range(1, 86672217) )

Save a DF compressed:
dfTest[['id','unit_sales']].to_csv('ma8dwof.csv.gz', index=False, float_format='%.3f', compression='gzip')

Read a gz file into a DF:
	import gzip
    # Couldn't love PANDAS more...
    with gzip.open(impressionsPath, 'rb') as fId:
        dfImpressions = pd.read_csv(fId, delimiter='\t');

	*This option is even better:
	dfImpressions = pd.read_csv(impressionsPath, delimiter='\t', compression='gzip');

Get a percentage in one go:
	cookieRatio = dfCookies.value_counts()/dfCookies.count();

Find and replace backslashes:
(Backslashes use backslash so if we are dealing with functions that can accept a regex as input, let's make sure
we explicitily pass the object as a regex one)
	b = r'\\'
	a = df.PublisherURL.str.contains(b)
	df.PublisherURL.str.replace(b, '', case=False);


Drop/Remove nulls from a dataset (based on a column):
	df = df[~df['Market'].isnull()]


Select rows and cols based on some condition:
	validColNames = ['Market', 'Year'];
	idxValid = ~df['Market'].isnull();
	df = df.ix[idxValid, validColNames];

Multiple indexing - must be a better way:
	listOfVars = ['numAggregations', 'numAggregations_imp', 'numAggregations_tp'];
	idxVals    = dfCITemp[listOfVars] > 0;
	for idx in [0,1,2]:
		dfCITemp.ix[idxVals.ix[:, idx], listOfVars[idx]] = 1.0;

Read csv data:
	fileName      = imprName
	csvFile       = os.path.join(dataRoot, fileName);
	df            = pd.read_csv(csvFile, delimiter='\t')
	colsToReplace = {'BannerId-AdGroupId': 'BannerId', 'PlacementId-ActivityId': 'PlacementId'}
	df.rename(columns=colsToReplace, inplace=True)

Read csv data from the web:
	import pandas as pd
	urlSource = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
	df = pd.read_csv(urlSource, delimiter=';')
	df.head()

Filter a dataframe by a list of values (all the unique ones):
	uniqueBPNS     = dfTest['item_nbr'].unique();
	idxItemsInList = dfTest['item_nbr'].isin(uniqueBPNS);


Drop some rows of a DF (must be another way):
	dfPurchasesExt.drop(['customvars'], axis = 1, inplace = True)

idxList = list(range(1,60));
df.drop(df.index[idxList], inplace=True)

DropNaN's:
	df2.dropna(axis=1, how='any', inplace=True)

isnan:
	np.isnan(a)

To iterate through all the rows:
>> iterrows returns a Series for each row, it does not preserve dtypes across the rows
for index, row in df.iterrows():
	print(row['name'], row['score'])


One Hot encoding (OHE will be superseeded soon. Keep an eye)
	pd.get_dummies(obj_df, columns=["body_style", "drive_wheels"], prefix=["body", "drive"]).head()


Iterate through datatypes
	for iVar, iType in df.dtypes.iteritems():
		print(iType)

Also, a list with the selected dtype:
	objTypes = df.select_dtypes(include=['object']).keys().tolist()


SORT OUT A DF
	grpDF.sort_values(['total'], ascending=[0], inplace = True)

Get a row: df.ix[0]
	.iloc is primarily integer position based
	.ix supports mixed integer and label based access

Indexing a column:
	idxPresentCVars  = ~df['customvars'].isnull();
	dfCustomVarsTemp = df.customvars.ix[idxPresentCVars]

Make a percentage count based on an index:
	# How many customvars are not null
	idxPresentCVars   = ~df['customvars'].isnull();
	print(idxPresentCVars.value_counts()/idxPresentCVars.count())

Convert the row of a DF into a list:
	avgValues     = df.ix[0].values.tolist();

Reshuffle a DF (avoid time/reading effects):
	import numpy as np
	np.random.seed(0)
	df = df.reindex(np.random.permutation(df.index))

Apply a function to a DF column:
	p = lambda x: x*2
	df['newVar'] = df['sentiment'].apply(p)

Apply a function to a DF:
	cl1 = lambda x: str.replace(x, "___","_none_none_" )
	cl2 = lambda x: str.replace(x, "__","_none_" )
	df.applymap(cl1)
	df.applymap(cl2)
	# same idea but inline
	df['age_segment'] = df['age'].apply(lambda age: get_age_segment(age))


Toy DFs:

	df = pd.DataFrame([{'A': 'foo', 'B': 'green', 'C': 11}, \
					{'A':'bar', 'B':'blue', 'C': 20}, \
					{'A':'foo', 'B':'blue', 'C': 20}])

	df2 = pd.DataFrame({ 'A' : 1.,
	....:                      'B' : pd.Timestamp('20130102'),
	....:                      'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
	....:                      'D' : np.array([3] * 4,dtype='int32'),
	....:                      'E' : pd.Categorical(["test","train","test","train"]),
	....:                      'F' : 'foo' })


	d = [{'col1': 12, 'col2': 17}, {'col1': 2, 'col2': 1}]
	df = pd.DataFrame(data=d)


Create vars on-the-fly
 for i in range(1,hm_days+1):
        df['{}_{}d'.format(ticker,i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]


Concatenate columns of a DF into a new one:

	dfTrainWithItems['base_product_number_std'] = \
		dfTrainWithItems['item_nbr'].astype(str) + \
		'_' + dfTrainWithItems['store_nbr'].astype(str);


Get the column names of a DF:
	Either 'keys()' or tickers = df.columns.values.tolist() to get them on a list

Add columns in a DF where we want to keep the date index.In this case,
we read every 'df' and add it to main_df keeping the dates as an index. The gaps will be filled with Nan
Replace the Nan's with zeroes
	df.fillna(0, inplace=True)

Add cols to dataframe:

	dfClicksCI['iNodeID'] = [ 'c' + str(idx) for idx in range(0, numClicks)]

Size of a dataframe: DataFrame.shape
nR, nC = df.shape

Set up PANDAS options at the beginning of the code
	import pandas as pd
	pd.options.display.max_rows = 10
	pd.options.display.float_format = '{:.1f}'.format

Group values bigger than zero and group them:
	a = data['A']>0
	b = data['B']>0
	data.groupby([a,b]).count()


Filter by timestamp:
idxValidTimes = (dfTPoints['Timestamp'] > '2017-12-12 14:00') & (dfTPoints['Timestamp'] < '2017-12-12 17:00')


GROUP
----

A primer to groupings:
	groupedDF = df.groupby(df['campaign_id'])
	for name, group in groupedDF:
		groupClientName = group['clientsname'].iloc[0]
		print('Current campaign {} id {} got {} clicks'.format(groupClientName, name, group['totalclicks'].sum()))
	# Also, you can extract into a dictionary and index v b y the key value
	v = dict(list(groupedDF))

A bit more on grouping:

	df = pd.DataFrame([{'A': 'foo', 'B': 'green', 'C': 11, 'D': 's1'}, \
					{'A':'bar', 'B':'blue', 'C': 20, 'D': 's2'}, \
					{'A':'foo', 'B':'blue', 'C': 20, 'D': 's3'}])
	# group by one of the fields (this one is a bit confussing as I rather group by a variable: df.groupby(['A', 'B']);)
	groupedDF = df.groupby(df['A']);
	# get the list of groups
	groupNames = list(groupedDF.groups.keys());
	# access one of the groups
	thisGroup = groupedDF.get_group(groupNames[0])



Access the index when iterating:
	for idx,ai in enumerate(a):


Inner joins with Pandas:
# Code this SQL query using Pandas
sqlQuery = '''select
    A.ID, A.Site,A.Value2,A.Random,
    C.minSD,C.maxSD,
    sum(A.Value)     as totalValue
    from df as A
    inner join (select B.ID,
                min(B.StartDate) as minSD,
                max(B.EndDate)   as maxSD
                from df as B
                group by 1) as C
        on A.ID = C.ID
    group by 1,2,3,4,5,6
    '''
# Same with pandas (more on groupby)
varA      = 'ID';
dfGrouped = df.groupby(varA, as_index=False).agg({'StartDate': 'min', 'EndDate': 'max'}).copy();

varsToKeep = ['ID', 'Value', 'Site', 'Value2', 'Random', 'StartDate_grp', 'EndDate_grp'];
dfTemp = pd.merge(df, dfGrouped, how='inner', on='ID', suffixes=(' ', '_grp'), copy=True)[varsToKeep];

dfBreakDown = dfTemp.groupby(['ID', 'Site', 'Value2', 'Random', 'StartDate_grp',
       'EndDate_grp']).sum()


Aggregations (sql-like):

	df = pd.DataFrame([{'A': 'foo', 'B': 'green', 'C': 11, 'D': 's1'}, \
					{'A':'bar', 'B':'blue', 'C': 20, 'D': 's2'}, \
					{'A':'foo', 'B':'blue', 'C': 20, 'D': 's3'}])

	aggregations  = {'C': 'sum', 'B': 'count'}
	dfGrouped     = df.groupby(['A','D'], as_index=False).agg(aggregations).copy();

To use count-distinct:
dfGrouped = dfPurchasesExt.groupby(varA, as_index=False).agg({'yyyymmdd_str': pd.Series.nunique}).copy();

Read and filter a csv file with PD:

	# Read the csv file and get the valid dates
	dfTrain = pd.read_csv(csvPath,
			parse_dates=['date'],
			low_memory=False,
			dtype={'id':np.uint32, 'store_nbr':np.uint8, 'item_nbr': np.uint32,
			'onpromotion': np.bool, 'unit_sales': np.float32});

	idxTrain = dfTrain.date >= minDate;
	dfTrain = dfTrain.ix[idxTrain];


Access the rows of a DF (not the columns) and use them to normalise

# save the stats
dfStats = mainDF.describe();
minVals = dfStats.ix['min'];
maxVals = dfStats.ix['max'];

# stats for dates
dfStats = dfTrainPeriodA.date.describe();
minVals = dfStats.ix['first'];
maxVals = dfStats.ix['last'];
print('min date {} and max date {}'.format(minVals, maxVals));


Max of all values and max of each column:
	maxValue = df.values.max();
	xMax, yMax, zMax = df.max()

mainDFNorm = (mainDF - minVals)/(maxVals-minVals);


Bin a variable in pandas:
	def get_quantile_based_buckets(df, feature_name, num_buckets):
		boundaries = np.arange(1.0, num_buckets) / num_buckets;
		quantiles = df[feature_name].quantile(boundaries);
		[quantiles[q] for q in quantiles.keys()];
		bucketVar = 'bucket_' +  feature_name;
		df[bucketVar] = pd.cut(df[feature_name], quantiles, retbins=False, labels=False);
		return df;


Convert Pandas series to a list:
	[quantiles[q] for q in quantiles.keys()];
	Actually... quantiles.tolist()

Change from integer to float:
	# clean the item_price column and transform it in a float
	prices = [float(value[1 : -1]) for value in chipo.item_price]
	# reassign the column with the cleaned prices
	chipo.item_price = prices

Change from integer to categorical:
	char_cabin = titanic_train["Cabin"].astype(str)    # Convert cabin to str
	new_Cabin = np.array([cabin[0] for cabin in char_cabin]) # Take first letter
	titanic_train["Cabin"] = pd.Categorical(new_Cabin)  # Save the new cabin var


# ...or cast after reading
df["age"] = df["age"].astype(np.int16)

# Cast from float to string removing the decimals
dfTPminimal['orderID_str'] = dfTPminimal['orderID'].astype(int).astype(str)


Categorical/Nominal variables:
# (opt A)
# cast a string into numbers and ignore the nulls
# Using Apply
df['bionic_campaign_id'] = df['bionic_campaign_id'].apply(pd.to_numeric, errors='coerce')
#  Directly with 'to_numeric' and downcasting to integer
df['bionic_campaign_id'] = pd.to_numeric(df['bionic_campaign_id'], downcast='integer', errors='coerce')
# (opt B)
for feature in combined_set.columns: # Loop through all columns in the dataframe
    if combined_set[feature].dtype == 'object': # Only apply for columns with categorical strings
        combined_set[feature] = pd.Categorical(combined_set[feature]).codes # Replace strings with an integer


# create a column of percentages
df['percCity'] = 100*df['numtimes']/df['numtimes'].sum();

Set one column as index:
	browserMeta = browserMeta.set_index(['id'])

Quick count and return as DF:
	my_tab = pd.crosstab(index=titanic_train["Survived"],  # Make a crosstab
								columns="count")      # Name the count column


Filter a dataframe based on two conditions:
	world = world[(world.pop_est>0) & (world.continent=="Europe")]

Rename columns:
	bannersMeta.rename(columns={'id': 'BannerId', 'name': 'BannerName'}, inplace=True);

Select by dates:
	minDate    = datetime(2016, 7, 1);
	maxDate    = datetime(2016, 9, 1);
	rangeDates = pd.date_range(minDate, maxDate);
	idxPeriodA = dfTrain['date'].isin(rangeDates);
	# directly...
	dfA = dfTrain[rangeDates]

JSON: Python, Pandas and Flask

Df to json:
df_clean.to_json(orient='records')

Read from a html flask web a json string:

	var geojson = L.geoJson({{ geojsonData|tojson|safe }}, {
		pointToLayer: function (feature, latlng) {
			return L.circleMarker(latlng, myStyle);
		}


Pandas timestamps as strings:
#timestamp
df['thisTimeStamp'] = df['yyyy_mm_dd'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'));
Strings to Pandas timestamp:
pd.to_datetime(thisCookieID_Clicks['Timestamp'], format='%Y-%m-%d %H:%M:%S')


Get a PD col as numpy array:
	# My usual....
	a_returns['JPM Returns'].as_matrix()
	# This other approach:
	a_returns.values.T[0]


Time differences with Pandas:
Pandas series less than a minute
	timeDiffBetweenCookies < np.timedelta64(1, 'm')

Date differences in Pandas. Get a column with the date of a lagged day:

df = pd.DataFrame({ 'A' : 1., 'date' : pd.Timestamp('20130102') }, index=[0])
currentLag = 1;
df['dayLagged_{}'.format(currentLag)] = df.date - timedelta(days=currentLag);


Append dataframes with different nuymber of columns:

	df = pd.DataFrame([{'A': 'foo', 'B': 'green', 'C': 11}, \
					{'A':'bar', 'B':'blue', 'C': 20}])
	df2 = pd.DataFrame([{'A': 'foo', 'B': 'green', 'C': 11, 'D': 'cojones'}])
	df = df.append(df2, ignore_index=True);



# Partial indexing
	# let's read this file, set these 3 variables as Indexes
	df_test = pd.read_csv(
		"/Users/carlos.aguilar/Documents/Kaggle Competition/Grocery Sales Forecasting/test.csv", usecols=[0, 1, 2, 3, 4],
		dtype={'onpromotion': bool},
		parse_dates=["date"]  # , date_parser=parser
	).set_index(['store_nbr', 'item_nbr', 'date'])
	# get the index values so we can perform search, etc operations
	storeValues = df_test.index.get_level_values(0)
	itemValues = df_test.index.get_level_values(1)
	dateValues = df_test.index.get_level_values(2)
	# get the data for this particular item
	idxItem = itemValues == 310671;
	df_test = df_test[idxItem]



# Stack and unstack multindex files
	index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'), ('two', 'a'), ('two', 'b'), ('three', 'b')])
	s = pd.Series(np.arange(1.0, 6.0), index=index)
	s.head()
	# have a look to the 'labels' index
	s.keys()
	# unstack the by (1,b)
	s.unstack(level=-1)
	# unstack the by (one, two, three)
	s.unstack(level=0)
	# get the original back
	df = s.unstack(level=0)
	df.unstack()

#..........................

import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta


df = pd.DataFrame([{'unit_sales' :1, 'date' : pd.Timestamp('20130103'), 'store_nbr' : 2, 'onpromo': True },
				  {'unit_sales' : 7, 'date' : pd.Timestamp('20130106'), 'store_nbr' : 2, 'onpromo': False },
				  {'unit_sales' : 2, 'date' : pd.Timestamp('20130102'), 'store_nbr' : 1, 'onpromo': True  }])

varsToKeep = ['unit_sales', 'date', 'store_nbr', 'onpromo'];
leftKeys   = ['date', 'store_nbr']

for currentLag in range(1,28+1):
	currentLagVar     = 'dLag_{}'.format(currentLag);
	df[currentLagVar] = df.date - timedelta(days=currentLag);
	varsToKeepRightDF = [x + '_' + currentLagVar for x in ['unit_sales', 'onpromo']]
	allVarsToKeep     = varsToKeep
	for iVar in varsToKeepRightDF:
		allVarsToKeep.append(iVar)
	# Set the current rightKeys
	rightKeys = [currentLagVar, 'store_nbr'];
	dfTemp    = pd.merge(df, df, how='left', left_on=leftKeys, right_on=rightKeys,  suffixes=('', '_' + currentLagVar), copy=True);
	# Update the DF
	df = dfTemp[allVarsToKeep].copy();
	varsToKeep = allVarsToKeep

df.fillna(0)

#..........................




# Read files and apply functions and filters
df_train = pd.read_csv(
    '/Users/carlos.aguilar/Documents/Kaggle Competition/Grocery Sales Forecasting/train.csv', usecols=[1, 2, 3, 4, 5],
    dtype={'onpromotion': bool},
    converters={'unit_sales': lambda u: np.log1p(
        float(u)) if float(u) > 0 else 0},
    parse_dates=["date"],
    skiprows=range(1, 66458909)  # 2016-01-01
)



# Reindexing
# Reindex arranges the data according to the new index, introducing missing values if any index values are not present
promo_2017_test = promo_2017_test.reindex(promo_2017_train.index).fillna(False)


Boosting Pandas
------------------
# It is designed to work in Jupyter
import pandas as pd
import pandas_profiling
df = pd.DataFrame([{'A': 'foo', 'B': 'green', 'C': 11}, \
				   {'A':'bar', 'B':'blue', 'C': 20}])
profile = pandas_profiling.ProfileReport(df)
# but we can output the file and read it from a browser
profile.to_file(outputfile="//Users/carlos.aguilar/Downloads/myoutputfile.html")



DATES
-----------------------------

Dates differences:
from dateutil.relativedelta import relativedelta
endDT   = dt.datetime.today();
startDT = endDT - relativedelta(years=1);

From timestamp to string:
	 stocks.index[-1].strftime('%Y-%m-%d')

From timestamp to string:
	dateAsStr = dfTest['date'].dt.strftime('%d_%m_%Y');

From string to date:
pd.to_datetime(thisCookieID_Clicks['Timestamp'], format='%Y-%m-%d %H:%M:%S')

a bit more complex. Dates to string in a required format and then unique and to a list:
	idxValid = dfCITemp['retrieveRow'] > 0
	listOfDates = dfCITemp['date'].ix[idxValid].dt.strftime('%Y_%m_%d').unique().tolist()

Convert from standard date format to simple numbers in a dataframe
	import matplotlib.dates   as mdates
	df['Date'] = df['Date'].map(mdates.date2num);

# get the following 16 days...
t2017 = date(2017, 5, 31)
pd.date_range(t2017, periods=16)


EXCEL
-----------------------------

Save DF to Excel:
	fName     = 'winequality-red.xlsx';
	xlsRoot   = '/Users/carlosAguilar/Documents/PythonDev/Coding/data for testing';
	xlsFile   = os.path.join(dataRoot, fName)
	xlsWriter = pd.ExcelWriter(xlsFile)
	df.to_excel(xlsWriter, 'Red')
	xlsWriter.save();

Read DF from excel: df.read_excel();

From list of lists to a simple list:
	from itertools import chain
	listOfTickers = [['AAPL', 'MSFT', 'TSCO.L', 'SBRY', 'BP', 'REP.MC']]
	categories = list(chain.from_iterable(listOfTickers));



Use a progress bar in python:

	totalNumber = 1000
	pbar = pyprind.ProgBar(totalNumber)
	for i in range(0, totalNumber):
	    pbar.update()





dir() – will display the defined symbols. Eg: >>>dir(str) – will only display the defined symbols.
Built-in functions such as max(), min(), filter(), map(), etc is not apparent immediately as they are
available as part of standard module. dir(__builtins ) to view them.

zip() function- it will take multiple lists say list1, list2, etc and transform them into a single list of
tuples by taking the corresponding elements of the lists that are passed as parameters.

Every object holds unique id and it can be obtained by using id() method. Eg: id(obj-name) will return unique id of the given object.

File-related modules in Python:
	os and os.path – modules include functions for accessing the filesystem
	shutil – module enables you to copy and delete the files.
	 “with” statement makes the exception handling simpler by providing cleanup activities.




Version control for the modules:
	from distutils.version import LooseVersion
	import sklearn as sk
	if LooseVersion(sk.__version__) < '0.18':
	    from sklearn.grid_search import GridSearchCV
	else:
	    from sklearn.model_selection import GridSearchCV

sklearn version:
	import sklearn as sk
	sk.__version__

Pandas version:
	import pandas as pd
	pd.__version__

Bokeh version:
	import bokeh as bk
	bk.__version__


RegEx remainder:
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
. = Any character except a new line

RegEx: remove one or more blanks by just one blank
latexString = re.sub(' +', ' ', latexString)





PyMongo:
(http://ec2-54-218-106-48.us-west-2.compute.amazonaws.com/moschetti.org/rants/mongopandas.html)

To Create a collection
db = client['yahooStocks']
stocksCollection = db['stocksCollection']

To delete all the records
db = client['yahooStocks']
stocksCollection.remove()


Logical not of an index:
idxTest   = oneBPNS['promoToFrc']>0;
idxTrain  = np.logical_not(idxTest);

Get the count in a for loop: for idx,item in enumerate(list): do stuff



from mpl_toolkits.mplot3d import axes3d
	# Get the test data
	X, Y, Z = axes3d.get_test_data(0.05)
	numR, numC = X.shape

Python: local and global scopes

def test1(currentDF, bannersMeta):
    lc = locals()
    print(lc.keys())

def test2(currentDF, bannersMeta):
    gb = globals()
    print(gb.keys())


_ has 3 main conventional uses in Python:

	To hold the result of the last executed statement in an interactive interpreter session. This precedent was set by the standard CPython interpreter, and other interpreters have followed suit
	For translation lookup in i18n (see the gettext documentation for example), as in code like: raise forms.ValidationError(_("Please enter a correct username"))

	As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored, as in code like: label, has_label, _ = text.partition(':')

	The latter two purposes can conflict, so it is necessary to avoid using _ as a throwaway variable in any code block that also uses it for i18n translation (many folks prefer a double-underscore, __, as their throwaway variable for exactly this reason).



TIMERS
-----------------------------
import time

start = time.time()
end = time.time()
elapsed_time = end - start
print ('completed staging insert loops in {:.2f} sec!'.format(elapsed_time))

From the command line...
python3 -m timeit '"-".join(str(n) for n in range(100))'


NUMPY
-----------------------------

Get an array as a column-one

>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> print(np.ravel(x))
[1 2 3 4 5 6]

Random integers
np.random.randint(2, high=10, size=10)


myBID        = np.array([1.76197, 1.73945]);
numberStocks = np.array([20, 1980]);
totalShares  = np.sum(numberStocks);
grossBook    = np.dot(numberStocks, myBID);

Numerical encoding:
	# Create a label encoder and fit it
	from sklearn.preprocessing import LabelEncoder
	le_sex = LabelEncoder()
	le_sex.fit(df["sex"].unique())
	le_sex.classes_  # The fit results in two classes - M and F


# From Srbastian Raschka
df = pd.DataFrame([['green', 'M', 10.1, 'class1'],
				['red', 'L', 13.5, 'class2'],
				['blue', 'XL', 15.3, 'class1']])

df.columns = ['color', 'size', 'price', 'classlabel']
from sklearn.preprocessing import LabelEncoder
class_le = LabelEncoder()
y = class_le.fit_transform(df['classlabel'].values)
# Invert the transform
class_le.inverse_transform(y)





Manually...
	# make it numerical
	uniqueType = stores2.type.unique()
	uniqueTypeDict = dict(zip(uniqueType, range(len(uniqueType))))
	stores2['type'] = stores2['type'].replace(uniqueTypeDict)

# Remove a value from a NP array
	a = np.array([3,7,2])
	b = 7
	c = a[a != b]



To do OHE: just go to PANDAS and oheTarget = pd.get_dummies(df1['target'])


Save numpy data:

	import numpy as np
	np.save('filename', npVarName)

Get the indices after sorting an array:
	np.argsort
	Descending order...
	idxSorted = np.argsort(classProb)[0][::-1]


PLOTTING
-----------------------------


Use seaborn to plot a heat map

import seaborn as sns
dfPurchasesFiltPerDay = pd.pivot_table(dfPurchasesFilt, values='productCount',
    index=['productName'], columns=['hour'], aggfunc=np.mean)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(dfPurchasesFiltPerDay, annot=True, linewidths=.5, ax=ax)
plt.show()





Colorbar depending on the current data:

    data1 = df_corr.values
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    heatmap1 = ax1.pcolor(data1, cmap=plt.cm.RdYlGn)
    fig1.colorbar(heatmap1)

Scatterplot colouring by a third variable

	plt.figure(figsize=(13, 8))

	ax = plt.subplot(1, 2, 1)
	ax.set_title("Validation Data")

	ax.set_autoscaley_on(False)
	ax.set_ylim([32, 43])
	ax.set_autoscalex_on(False)
	ax.set_xlim([-126, -112])
	# set the colour depending on 'median_house_value'
	plt.scatter(validation_examples["longitude"],
	            validation_examples["latitude"],
	            cmap="coolwarm",
	            c=validation_targets["median_house_value"] / validation_targets["median_house_value"].max())

	ax = plt.subplot(1,2,2)
	ax.set_title("Training Data")

	ax.set_autoscaley_on(False)
	ax.set_ylim([32, 43])
	ax.set_autoscalex_on(False)
	ax.set_xlim([-126, -112])
	plt.scatter(training_examples["longitude"],
	            training_examples["latitude"],
	            cmap="coolwarm",
	            c=training_targets["median_house_value"] / training_targets["median_house_value"].max())

	# drop the axis by using _
	_ = plt.plot()


Get the axes of a figure:

fig = plt.gcf()
ax1 = fig.get_axes();


IMAGE PROCESSING IN Python

import cv2                 # working with, mainly resizing, images


SQL with sqlAlchemy
------------------
Avoid problems with special/escape characters by simply using the text helper from sqlAlchemy

from sqlalchemy import text
sqlQueryB = text(sqlQueryB)
df = rs.query2DF(sqlQueryB)


RegEx
------

Get all the fields between brackets in a string and replace them

sqlCreateTable = cu.dataFrameToCreateTableSQL(bionicData);

# Use a regular expression to find any parts within quotes
for quoted_part in re.findall(r'\"(.+?)\"', sqlCreateTable):
    print(quoted_part)
    sqlCreateTable = sqlCreateTable.replace(quoted_part, quoted_part.replace(" ", "_"))

print(sqlCreateTable)


Parse a list of regular expressions (use filter):
	import re
	thisRegEx = 'manolo-\\d{1}'
	regEx  = re.compile(thisRegEx);
	listIDs = ['manolo-12', 'manolo-8']
	parsedList = list(filter(regEx.match, listIDs))


# Apply a regex to a DF
	#dfPrices.Price will contain rows such as >> '[{'date': '2017-11-29', 'price': '£26.99'}]'
	price = dfPrices.Price.astype(str).apply(lambda x: re.match(r'\[(.+?)\]', x)[1])


sklearn
-------
from sklearn.feature_extraction.text import CountVectorizer
plainText = df['Campaign Name'].tolist()
vect = CountVectorizer(min_df=0., max_df=1.0)
X = vect.fit_transform(plainText)




FILESYSTEM
-----------------------------



To use a temporary directory:
from tempfile import TemporaryDirectory
    with TemporaryDirectory() as local_target_location:
		# do stuff

Find files with certain extension:

	path2PDFs = '/Users/carlosAguilar/Google Drive/order/Machine Learning Part/Papers/papers';
	pdfExt    = 'pdf'
	folderContents = listdir(path2PDFs);
	pdfFiles  = [f for f in folderContents if isfile(join(path2PDFs, f)) and f.endswith(pdfExt)]



# Where is Python installed? Bin path to Python
which python3

# Do this trick to add the new Beamly functionality
import sys
[print(iP) for iP in sys.path]
pythonModsRoot = '/Users/carlos.aguilar/Google Drive/PythonDev/Coding/BeamlyPython'
if pythonModsRoot not in sys.path:
    sys.path.append(pythonModsRoot)


Implicitly, by opening files with the with statement. The close() method will be c
alled when the end of the with block is reached, even in the event of
abnormal termination (from an exception).
	with open("data.txt") as in_file:
		data = in_file.read()

Write file:
	with open(fileToRun, 'w+') as in_file:
    for thisFile in missingBackUp:
        srcPath = '''"s3://beamly-metrics-data-stage/''' + folderNameBMetrics[0] + '/' + thisFile + '"'
        thisCmd = cmdPrefix + srcPath + cmdPostFix + ';'
        in_file.write(thisCmd);


Check the end of a string:
	filename.endswith(".json")

Find text in string:
	filename.find("_analysis_")



The path module already has join, split, dirname, and basename functions

os.path.join(os.path.abspath('.'), 'utils')

Join a path:
	jsonPath = os.path.join(metaRoot, jsonFile);

To get the parts (Matlab filepart):
	[fPath,fName] = os.path.split('/Volumes/Impressions/Impression_86132_Summary.pickle')



Delete all the files with a particular extension within a folder:
	rmCommand = '''find "{}" -name "{}"'''.format(metaTempFolder, '*.xml');
	os.system(rmCommand)

Split path into chunks:
import ntpath
thisFolder, thisFile = ntpath.split(subString)


Uswe split to get parts of filenames:
fName = 'A.B.C'
partA = fName.split('.')[-3]

Create a vector from 0 to the lenght of a variable
np.arange(0, len(variables))

import sys
fid = sys.stderr
print("fatal error", file=fid)
but also:

fid = open('test.txt','w')
print("fatal error", file=fid)
fid.fclose()

Make a folder if it doesn't exist:
            dataFolder = 'xlsTickers';
            if not os.path.exists(dataFolder):
                os.makedirs(dataFolder)



Interaction with Viscosity:
import utils.carlosUtils as cu

# Set up connections to Viscosity
vpnNameAWS = 'Beamly AWS VPN';
cu.viscosityConnect(vpnNameAWS);

vpnName = 'AWS Platform - eu-central-1 (Frankfurt)';
cu.viscosityConnect(vpnName);




From Simon:
___________

class Animal:
    def __init__(self,name,life_span):
        self.name = name
        self.life_span = life_span

    def say_hi():
        print('Hi Carlos')


    def __str__(self):
        return self.name

    def __repr__(self):
        return u'<\N{WHITE SMILING FACE} AnimalClass {0} >'.format(self.name)



Animals = []


Human = Animal('Homosapean',80)
Animals.append(Human)
Dog = Animal('Dog', 20)
Animals.append(Dog)
Mouse = Animal('Mouse',2)
Animals.append(Mouse)

print(Animals)
Animals.pop(1)
print(Animals)


Stupid tricks to save time...
-------
idx = 0
idx = idx + 1;
print('Here...{}'.format(idx))
idx = idx + 1;
print('Here...{}'.format(idx))



JUPYTER
-------
jupyter nbconvert --to script 'my-notebook.ipynb'


Import nbformat as nbf
---------------------
import nbformat as nbf

nb = nbf.v4.new_notebook()
text = """\
# My first automatic Jupyter Notebook
This is an auto-generated notebook."""


with open('analyseDataForJoopAndTPS.py') as f:
	pythonCode = f.read()

nb['cells'] = [nbf.v4.new_markdown_cell(text),
               nbf.v4.new_code_cell(pythonCode)]
fname = 'test.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)




KAGGLE lessons
--------------

# create a DF with the indexes "store_nbr", "item_nbr", "date" and
# unstack the dates so the columns are the combination "onpromotion", "date"
promo_2017_train = df_2017.set_index(
    ["store_nbr", "item_nbr", "date"])[["onpromotion"]].unstack(
        level=-1).fillna(False)
# Then, remove the "onpromotion" from the columns to just have the "dates"
promo_2017_train.columns = promo_2017_train.columns.get_level_values(1)

# Same idea applied to the test set
promo_2017_test = df_test[["onpromotion"]].unstack(level=-1).fillna(False)
promo_2017_test.columns = promo_2017_test.columns.get_level_values(1)
# Not sure...but I think by doing this i we kind of left join on the training set
# and set the products not present in the test set to false
promo_2017_test = promo_2017_test.reindex(promo_2017_train.index).fillna(False)

promo_2017 = pd.concat([promo_2017_train, promo_2017_test], axis=1)
del promo_2017_test, promo_2017_train

# Set the date as columns and if the sales are not found, set them to zero
df_2017 = df_2017.set_index(
    ["store_nbr", "item_nbr", "date"])[["unit_sales"]].unstack(
        level=-1).fillna(0)
df_2017.columns = df_2017.columns.get_level_values(1)

# Reindex the items as in the training set
items = items.reindex(df_2017.index.get_level_values(1))












######################
Mastering Python


Help on a module
help(moduleName)

PIP (Python Package Index)

Pip normalyy installs in the systems package folder, to tell PIP to install in the personal user folder, simply add the modifier
pip3 install --user PACKAGENAME
Also, we can run PIP from Python as
python -m pip3 install --user PACKAGENAME

List of the installed packages:

pip3 list

pip3 unistall PACKAGENAME

Upgrade a package:
pip3 install PACKAGENAME --Upgrade

pip3 help

search package:

pip3 search PACKAGENAME

------------------------------
Section 2: Creating a Package
------------------------------

Creating the package folder
Creating the __init__.py file
emacs PACKAGENAME/__init__.py
Inside of the __init__.py, type the name of the modules (to avoid issues with cases, etc)
__all__ = ['mod1', 'mod2']
Importing the new package

To get the list of folder that Python uses to find packages, do
import sys
print(sys.path)

Conventions for modules: should not start with numbers or capitals.

To add a package to the list of Python packages,
sys.append(folderName)


Folders that don't contain an __init__.py file are 'namespace packages'. Namespace packages can be useful
for a large collection of loosely-related packages
(such as a large corpus of client libraries for multiple products from a single company). Each sub-package can now be separately installed, used, and versioned.


Relative import of a package with the trick:
import .localModule

Absolute imports:
import utils.adformUtils as adform

If two modules import each other:
- move some of the code to a third module
- import one of the modules at the bottom of the other

To read the data files from a package:

from pkgutil import get_data
currentData = get_data(packagename, datafileName)
# if the data contains text:
currentData = get_data(packagename, datafileName).decode('utf8')

------------------------------
Section 3: Basic Best Practices
------------------------------
PEP 8 (Python Enhancement Proposals) and Writing Readable Code

Objects names according to how they are used, not to what they are.
Classes: CamelCase
Functions/Methods: Lowercase with underscore. Internal variables should be preceded by underscore.
Constants: capitals

Don't use tab characters for indentation, use 4 spaces.

3.2 Using Version Control

git init
git add fileName.py
git commit -a

Review the commits:
git log

In case we want to revert to a previous commit, find the id and reverts as
git checkout IDpreviousOne

Create branches:
git branch -t branchName
git checkout branchName

Merge into the master branch
git merge branchName
If overlapping changes:
git mergetool

My usual:

git add -A
git commit -m "this is the message"
git push origin master

To include code from other repositories, use git pull

More on GIT: https://devguide.python.org/gitbootcamp/


3.3 Using venv to Create a Stable and Isolated Work Area

venv allows us to install a package without interfering with the current installation.

i - Create:
python3 -m venv venvExample
ii - Activate it so we can work on it:
source bin/activate
iii - Run any command. Install some private packages using pip:
pip install pillow

iv - to deactivate, simply type 'deactivate'

Getting the Most Out of docstrings Part 1 – PEP 257 and Sphinx:

Basic rules for docstrings:
- use triple quotes
- 1st line is a short description
- Blank-line and then a more detailed description

Using reStructuredText. Follow https://devguide.python.org/

Sphinx:
sphinx-quickstart
It will ask for a root folder ('docs'). make sure the autodoc plugin is enabled.
sphinx-apidoc -o docs example
(sphinx-apidoc -o docs pandas -f)

emacs conf.py
In the conf.py file add
	import os
	import sys
	sys.path.append(os.path.abspath('..'))
make html

From the Sphix-doc web:
sphinx-quickstart
sphinx-build -b html sourcedir builddir

Getting the Most Out of docstrings Part 2 – doctest
To enable doctest to run python code, we actually write the test as if we were in the python shell, ie:
"""Doctest example
>>> for idx in range(5):
...		print(idx)
0
1
2
3
4

"""

python3 -m doctest -v fileName.py




