{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": " <a href=\"https://www.bigdatauniversity.com\"><img src = \"https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png\" width = 300, align = \"center\"></a>\n\n<h1 align=center><font size = 5>Data Analysis with Python</font></h1>"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# House Sales in King County, USA"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015."
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<b>id</b> : A notation for a house\n\n<b> date</b>: Date house was sold\n\n\n<b>price</b>: Price is prediction target\n\n\n<b>bedrooms</b>: Number of bedrooms\n\n\n<b>bathrooms</b>: Number of bathrooms\n\n<b>sqft_living</b>: Square footage of the home\n\n<b>sqft_lot</b>: Square footage of the lot\n\n\n<b>floors</b> :Total floors (levels) in house\n\n\n<b>waterfront</b> :House which has a view to a waterfront\n\n\n<b>view</b>: Has been viewed\n\n\n<b>condition</b> :How good the condition is overall\n\n<b>grade</b>: overall grade given to the housing unit, based on King County grading system\n\n\n<b>sqft_above</b> : Square footage of house apart from basement\n\n\n<b>sqft_basement</b>: Square footage of the basement\n\n<b>yr_built</b> : Built Year\n\n\n<b>yr_renovated</b> : Year when house was renovated\n\n<b>zipcode</b>: Zip code\n\n\n<b>lat</b>: Latitude coordinate\n\n<b>long</b>: Longitude coordinate\n\n<b>sqft_living15</b> : Living room area in 2015(implies-- some renovations) This might or might not have affected the lotsize area\n\n\n<b>sqft_lot15</b> : LotSize area in 2015(implies-- some renovations)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "You will require the following libraries: "
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [],
            "source": "import pandas as pd\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport seaborn as sns\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler,PolynomialFeatures\nfrom sklearn.linear_model import LinearRegression\n%matplotlib inline"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# Module 1: Importing Data Sets "
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": " Load the csv:  "
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [],
            "source": "file_name='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/kc_house_data_NaN.csv'\ndf=pd.read_csv(file_name)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "\nWe use the method <code>head</code> to display the first 5 columns of the dataframe."
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>id</th>\n      <th>date</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>0</td>\n      <td>7129300520</td>\n      <td>20141013T000000</td>\n      <td>221900.0</td>\n      <td>3.0</td>\n      <td>1.00</td>\n      <td>1180</td>\n      <td>5650</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>7</td>\n      <td>1180</td>\n      <td>0</td>\n      <td>1955</td>\n      <td>0</td>\n      <td>98178</td>\n      <td>47.5112</td>\n      <td>-122.257</td>\n      <td>1340</td>\n      <td>5650</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>1</td>\n      <td>6414100192</td>\n      <td>20141209T000000</td>\n      <td>538000.0</td>\n      <td>3.0</td>\n      <td>2.25</td>\n      <td>2570</td>\n      <td>7242</td>\n      <td>2.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>7</td>\n      <td>2170</td>\n      <td>400</td>\n      <td>1951</td>\n      <td>1991</td>\n      <td>98125</td>\n      <td>47.7210</td>\n      <td>-122.319</td>\n      <td>1690</td>\n      <td>7639</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2</td>\n      <td>5631500400</td>\n      <td>20150225T000000</td>\n      <td>180000.0</td>\n      <td>2.0</td>\n      <td>1.00</td>\n      <td>770</td>\n      <td>10000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>6</td>\n      <td>770</td>\n      <td>0</td>\n      <td>1933</td>\n      <td>0</td>\n      <td>98028</td>\n      <td>47.7379</td>\n      <td>-122.233</td>\n      <td>2720</td>\n      <td>8062</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>3</td>\n      <td>2487200875</td>\n      <td>20141209T000000</td>\n      <td>604000.0</td>\n      <td>4.0</td>\n      <td>3.00</td>\n      <td>1960</td>\n      <td>5000</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>7</td>\n      <td>1050</td>\n      <td>910</td>\n      <td>1965</td>\n      <td>0</td>\n      <td>98136</td>\n      <td>47.5208</td>\n      <td>-122.393</td>\n      <td>1360</td>\n      <td>5000</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>4</td>\n      <td>1954400510</td>\n      <td>20150218T000000</td>\n      <td>510000.0</td>\n      <td>3.0</td>\n      <td>2.00</td>\n      <td>1680</td>\n      <td>8080</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>...</td>\n      <td>8</td>\n      <td>1680</td>\n      <td>0</td>\n      <td>1987</td>\n      <td>0</td>\n      <td>98074</td>\n      <td>47.6168</td>\n      <td>-122.045</td>\n      <td>1800</td>\n      <td>7503</td>\n    </tr>\n  </tbody>\n</table>\n<p>5 rows \u00d7 22 columns</p>\n</div>",
                        "text/plain": "   Unnamed: 0          id             date     price  bedrooms  bathrooms  \\\n0           0  7129300520  20141013T000000  221900.0       3.0       1.00   \n1           1  6414100192  20141209T000000  538000.0       3.0       2.25   \n2           2  5631500400  20150225T000000  180000.0       2.0       1.00   \n3           3  2487200875  20141209T000000  604000.0       4.0       3.00   \n4           4  1954400510  20150218T000000  510000.0       3.0       2.00   \n\n   sqft_living  sqft_lot  floors  waterfront  ...  grade  sqft_above  \\\n0         1180      5650     1.0           0  ...      7        1180   \n1         2570      7242     2.0           0  ...      7        2170   \n2          770     10000     1.0           0  ...      6         770   \n3         1960      5000     1.0           0  ...      7        1050   \n4         1680      8080     1.0           0  ...      8        1680   \n\n   sqft_basement  yr_built  yr_renovated  zipcode      lat     long  \\\n0              0      1955             0    98178  47.5112 -122.257   \n1            400      1951          1991    98125  47.7210 -122.319   \n2              0      1933             0    98028  47.7379 -122.233   \n3            910      1965             0    98136  47.5208 -122.393   \n4              0      1987             0    98074  47.6168 -122.045   \n\n   sqft_living15  sqft_lot15  \n0           1340        5650  \n1           1690        7639  \n2           2720        8062  \n3           1360        5000  \n4           1800        7503  \n\n[5 rows x 22 columns]"
                    },
                    "execution_count": 10,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.head()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 1 \nDisplay the data types of each column using the attribute dtype, then take a screenshot and submit it, include your code in the image. "
        },
        {
            "cell_type": "code",
            "execution_count": 11,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                },
                "scrolled": true
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "Unnamed: 0         int64\nid                 int64\ndate              object\nprice            float64\nbedrooms         float64\nbathrooms        float64\nsqft_living        int64\nsqft_lot           int64\nfloors           float64\nwaterfront         int64\nview               int64\ncondition          int64\ngrade              int64\nsqft_above         int64\nsqft_basement      int64\nyr_built           int64\nyr_renovated       int64\nzipcode            int64\nlat              float64\nlong             float64\nsqft_living15      int64\nsqft_lot15         int64\ndtype: object"
                    },
                    "execution_count": 11,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.dtypes"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We use the method describe to obtain a statistical summary of the dataframe."
        },
        {
            "cell_type": "code",
            "execution_count": 12,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>id</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>21613.00000</td>\n      <td>2.161300e+04</td>\n      <td>2.161300e+04</td>\n      <td>21600.000000</td>\n      <td>21603.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>...</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>10806.00000</td>\n      <td>4.580302e+09</td>\n      <td>5.400881e+05</td>\n      <td>3.372870</td>\n      <td>2.115736</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>...</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>6239.28002</td>\n      <td>2.876566e+09</td>\n      <td>3.671272e+05</td>\n      <td>0.926657</td>\n      <td>0.768996</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>...</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>0.00000</td>\n      <td>1.000102e+06</td>\n      <td>7.500000e+04</td>\n      <td>1.000000</td>\n      <td>0.500000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>5403.00000</td>\n      <td>2.123049e+09</td>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>10806.00000</td>\n      <td>3.904930e+09</td>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>16209.00000</td>\n      <td>7.308900e+09</td>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>21612.00000</td>\n      <td>9.900000e+09</td>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>...</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n<p>8 rows \u00d7 21 columns</p>\n</div>",
                        "text/plain": "        Unnamed: 0            id         price      bedrooms     bathrooms  \\\ncount  21613.00000  2.161300e+04  2.161300e+04  21600.000000  21603.000000   \nmean   10806.00000  4.580302e+09  5.400881e+05      3.372870      2.115736   \nstd     6239.28002  2.876566e+09  3.671272e+05      0.926657      0.768996   \nmin        0.00000  1.000102e+06  7.500000e+04      1.000000      0.500000   \n25%     5403.00000  2.123049e+09  3.219500e+05      3.000000      1.750000   \n50%    10806.00000  3.904930e+09  4.500000e+05      3.000000      2.250000   \n75%    16209.00000  7.308900e+09  6.450000e+05      4.000000      2.500000   \nmax    21612.00000  9.900000e+09  7.700000e+06     33.000000      8.000000   \n\n        sqft_living      sqft_lot        floors    waterfront          view  \\\ncount  21613.000000  2.161300e+04  21613.000000  21613.000000  21613.000000   \nmean    2079.899736  1.510697e+04      1.494309      0.007542      0.234303   \nstd      918.440897  4.142051e+04      0.539989      0.086517      0.766318   \nmin      290.000000  5.200000e+02      1.000000      0.000000      0.000000   \n25%     1427.000000  5.040000e+03      1.000000      0.000000      0.000000   \n50%     1910.000000  7.618000e+03      1.500000      0.000000      0.000000   \n75%     2550.000000  1.068800e+04      2.000000      0.000000      0.000000   \nmax    13540.000000  1.651359e+06      3.500000      1.000000      4.000000   \n\n       ...         grade    sqft_above  sqft_basement      yr_built  \\\ncount  ...  21613.000000  21613.000000   21613.000000  21613.000000   \nmean   ...      7.656873   1788.390691     291.509045   1971.005136   \nstd    ...      1.175459    828.090978     442.575043     29.373411   \nmin    ...      1.000000    290.000000       0.000000   1900.000000   \n25%    ...      7.000000   1190.000000       0.000000   1951.000000   \n50%    ...      7.000000   1560.000000       0.000000   1975.000000   \n75%    ...      8.000000   2210.000000     560.000000   1997.000000   \nmax    ...     13.000000   9410.000000    4820.000000   2015.000000   \n\n       yr_renovated       zipcode           lat          long  sqft_living15  \\\ncount  21613.000000  21613.000000  21613.000000  21613.000000   21613.000000   \nmean      84.402258  98077.939805     47.560053   -122.213896    1986.552492   \nstd      401.679240     53.505026      0.138564      0.140828     685.391304   \nmin        0.000000  98001.000000     47.155900   -122.519000     399.000000   \n25%        0.000000  98033.000000     47.471000   -122.328000    1490.000000   \n50%        0.000000  98065.000000     47.571800   -122.230000    1840.000000   \n75%        0.000000  98118.000000     47.678000   -122.125000    2360.000000   \nmax     2015.000000  98199.000000     47.777600   -121.315000    6210.000000   \n\n          sqft_lot15  \ncount   21613.000000  \nmean    12768.455652  \nstd     27304.179631  \nmin       651.000000  \n25%      5100.000000  \n50%      7620.000000  \n75%     10083.000000  \nmax    871200.000000  \n\n[8 rows x 21 columns]"
                    },
                    "execution_count": 12,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.describe()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# Module 2: Data Wrangling"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 2 \nDrop the columns <code>\"id\"</code>  and <code>\"Unnamed: 0\"</code> from axis 1 using the method <code>drop()</code>, then use the method <code>describe()</code> to obtain a statistical summary of the data. Take a screenshot and submit it, make sure the <code>inplace</code> parameter is set to <code>True</code>"
        },
        {
            "cell_type": "code",
            "execution_count": 14,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>condition</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>2.161300e+04</td>\n      <td>21600.000000</td>\n      <td>21603.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>5.400881e+05</td>\n      <td>3.372870</td>\n      <td>2.115736</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>3.409430</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>3.671272e+05</td>\n      <td>0.926657</td>\n      <td>0.768996</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>0.650743</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>7.500000e+04</td>\n      <td>1.000000</td>\n      <td>0.500000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>1.000000</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.000000</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.000000</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>4.000000</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>5.000000</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n</div>",
                        "text/plain": "              price      bedrooms     bathrooms   sqft_living      sqft_lot  \\\ncount  2.161300e+04  21600.000000  21603.000000  21613.000000  2.161300e+04   \nmean   5.400881e+05      3.372870      2.115736   2079.899736  1.510697e+04   \nstd    3.671272e+05      0.926657      0.768996    918.440897  4.142051e+04   \nmin    7.500000e+04      1.000000      0.500000    290.000000  5.200000e+02   \n25%    3.219500e+05      3.000000      1.750000   1427.000000  5.040000e+03   \n50%    4.500000e+05      3.000000      2.250000   1910.000000  7.618000e+03   \n75%    6.450000e+05      4.000000      2.500000   2550.000000  1.068800e+04   \nmax    7.700000e+06     33.000000      8.000000  13540.000000  1.651359e+06   \n\n             floors    waterfront          view     condition         grade  \\\ncount  21613.000000  21613.000000  21613.000000  21613.000000  21613.000000   \nmean       1.494309      0.007542      0.234303      3.409430      7.656873   \nstd        0.539989      0.086517      0.766318      0.650743      1.175459   \nmin        1.000000      0.000000      0.000000      1.000000      1.000000   \n25%        1.000000      0.000000      0.000000      3.000000      7.000000   \n50%        1.500000      0.000000      0.000000      3.000000      7.000000   \n75%        2.000000      0.000000      0.000000      4.000000      8.000000   \nmax        3.500000      1.000000      4.000000      5.000000     13.000000   \n\n         sqft_above  sqft_basement      yr_built  yr_renovated       zipcode  \\\ncount  21613.000000   21613.000000  21613.000000  21613.000000  21613.000000   \nmean    1788.390691     291.509045   1971.005136     84.402258  98077.939805   \nstd      828.090978     442.575043     29.373411    401.679240     53.505026   \nmin      290.000000       0.000000   1900.000000      0.000000  98001.000000   \n25%     1190.000000       0.000000   1951.000000      0.000000  98033.000000   \n50%     1560.000000       0.000000   1975.000000      0.000000  98065.000000   \n75%     2210.000000     560.000000   1997.000000      0.000000  98118.000000   \nmax     9410.000000    4820.000000   2015.000000   2015.000000  98199.000000   \n\n                lat          long  sqft_living15     sqft_lot15  \ncount  21613.000000  21613.000000   21613.000000   21613.000000  \nmean      47.560053   -122.213896    1986.552492   12768.455652  \nstd        0.138564      0.140828     685.391304   27304.179631  \nmin       47.155900   -122.519000     399.000000     651.000000  \n25%       47.471000   -122.328000    1490.000000    5100.000000  \n50%       47.571800   -122.230000    1840.000000    7620.000000  \n75%       47.678000   -122.125000    2360.000000   10083.000000  \nmax       47.777600   -121.315000    6210.000000  871200.000000  "
                    },
                    "execution_count": 14,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.drop([\"id\", \"Unnamed: 0\"], axis = 1, inplace = True)\ndf.describe()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We can see we have missing values for the columns <code> bedrooms</code>  and <code> bathrooms </code>"
        },
        {
            "cell_type": "code",
            "execution_count": 15,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "number of NaN values for the column bedrooms : 13\nnumber of NaN values for the column bathrooms : 10\n"
                }
            ],
            "source": "print(\"number of NaN values for the column bedrooms :\", df['bedrooms'].isnull().sum())\nprint(\"number of NaN values for the column bathrooms :\", df['bathrooms'].isnull().sum())\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "\nWe can replace the missing values of the column <code>'bedrooms'</code> with the mean of the column  <code>'bedrooms' </code> using the method <code>replace()</code>. Don't forget to set the <code>inplace</code> parameter to <code>True</code>"
        },
        {
            "cell_type": "code",
            "execution_count": 16,
            "metadata": {},
            "outputs": [],
            "source": "mean=df['bedrooms'].mean()\ndf['bedrooms'].replace(np.nan,mean, inplace=True)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "\nWe also replace the missing values of the column <code>'bathrooms'</code> with the mean of the column  <code>'bathrooms' </code> using the method <code>replace()</code>. Don't forget to set the <code> inplace </code>  parameter top <code> True </code>"
        },
        {
            "cell_type": "code",
            "execution_count": 17,
            "metadata": {},
            "outputs": [],
            "source": "mean=df['bathrooms'].mean()\ndf['bathrooms'].replace(np.nan,mean, inplace=True)"
        },
        {
            "cell_type": "code",
            "execution_count": 18,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "number of NaN values for the column bedrooms : 0\nnumber of NaN values for the column bathrooms : 0\n"
                }
            ],
            "source": "print(\"number of NaN values for the column bedrooms :\", df['bedrooms'].isnull().sum())\nprint(\"number of NaN values for the column bathrooms :\", df['bathrooms'].isnull().sum())"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# Module 3: Exploratory Data Analysis"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 3\nUse the method <code>value_counts</code> to count the number of houses with unique floor values, use the method <code>.to_frame()</code> to convert it to a dataframe.\n"
        },
        {
            "cell_type": "code",
            "execution_count": 22,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>floors</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1.0</th>\n      <td>10680</td>\n    </tr>\n    <tr>\n      <th>2.0</th>\n      <td>8241</td>\n    </tr>\n    <tr>\n      <th>1.5</th>\n      <td>1910</td>\n    </tr>\n    <tr>\n      <th>3.0</th>\n      <td>613</td>\n    </tr>\n    <tr>\n      <th>2.5</th>\n      <td>161</td>\n    </tr>\n    <tr>\n      <th>3.5</th>\n      <td>8</td>\n    </tr>\n  </tbody>\n</table>\n</div>",
                        "text/plain": "     floors\n1.0   10680\n2.0    8241\n1.5    1910\n3.0     613\n2.5     161\n3.5       8"
                    },
                    "execution_count": 22,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df['floors'].value_counts().to_frame()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 4\nUse the function <code>boxplot</code> in the seaborn library  to  determine whether houses with a waterfront view or without a waterfront view have more price outliers."
        },
        {
            "cell_type": "code",
            "execution_count": 24,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "<matplotlib.axes._subplots.AxesSubplot at 0x7f3cc52bfdd8>"
                    },
                    "execution_count": 24,
                    "metadata": {},
                    "output_type": "execute_result"
                },
                {
                    "data": {
                        "image/png": "iVBORw0KGgoAAAANSUhEUgAAAaEAAAEKCAYAAAC7c+rvAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAHnRJREFUeJzt3X2UXVWZ5/HvL4lAoiJQFCyoShvspFVaBOEKmbanGyGEwmkTZpa0pGdNbjtM1zQiRB27Bcc1GV8Xrp4lQ5iWNiMZKjMCRkaHwpWXqfDSvgGmEl5iiE5KDFAJDWUlRjAIJHnmj7sr3Cpu6s3cs6+5v89ad91znrPP2buyKnmy99lnH0UEZmZmOUzJ3QAzM2teTkJmZpaNk5CZmWXjJGRmZtk4CZmZWTZOQmZmlo2TkJmZZeMkZGZm2dQ1CUn6mKQtkn4s6XZJx0g6TdJDkrZJ+oako1LZo9N+Xzo+q+o616X4TyVdXBXvSLE+SddWxSdch5mZFU/1WjFBUhvwfeD0iHhR0ipgNfA+4FsRcYekfwAejYibJX0YeGdE/LWky4F/GREflHQ6cDtwLnAqsB74g1TN/wMuAvqBDcCiiHg81TXuOkb7OU488cSYNWvWYf2zMTM70m3cuPEXEdE6VrlpdW7HNGC6pFeAGcAzwAXAX6TjXcB/Bm4GFqZtgDuB/yZJKX5HRLwE/FxSH5WEBNAXEU8ASLoDWChp60TriFEy8axZs+jt7Z3kj29m1pwkPTmecnUbjouIHcB/AZ6iknz2ABuBX0bEvlSsH2hL223A0+ncfal8S3V8xDmHirdMoo5hJHVK6pXUOzAwMJkf38zMxqFuSUjS8VR6HqdRGUZ7PXBJjaJDvRAd4tjhio9Wx/BAxPKIKEVEqbV1zN6kmZlNUj0nJswDfh4RAxHxCvAt4I+A4yQNDQO2AzvTdj8wEyAdfxOwqzo+4pxDxX8xiTrMzCyDeiahp4C5kmakezsXAo8D9wEfSGXKwF1puzvtk47fm+7VdAOXp5ltpwFzgB9RmYgwJ82EOwq4HOhO50y0DjMzy6Ce94QeonLzfxOwOdW1HPgk8PE0waAFuCWdcgvQkuIfB65N19kCrKKSwNYCV0XE/nRP5yPAOmArsCqVZaJ1WDEGBwe55pprGBwczN0UM2sQdZuifaQolUrh2XGHx5e//GXuvvtuFixYwMc+9rHczTGzOpK0MSJKY5XziglWiMHBQdauXUtEsHbtWveGzAxwErKCdHV1ceDAAQD279/PypUrM7fIzBqBk5AVYv369ezbV3l0a9++ffT09GRukZk1AichK8S8efOYNq0ya37atGlcdNFFmVtkZo3AScgKUS6XmTKl8us2depUFi9enLlFZtYInISsEC0tLXR0dCCJjo4OWlpes1qSmTWhei9ganZQuVxm+/bt7gWZ2UFOQlaYlpYWli1blrsZZtZAPBxnZmbZOAmZmVk2TkJmZpaNk5CZmWXjJGRmZtk4CZmZWTZOQmZmlo2TkJk1Pb9wMR8nITNrel1dXWzevNmvGMmgbklI0lslPVL1+ZWkj0o6QVKPpG3p+/hUXpKWSeqT9Jiks6uuVU7lt0kqV8XPkbQ5nbNMklJ8wnWYWXPyCxfzqlsSioifRsRZEXEWcA6wF/g2cC1wT0TMAe5J+wCXAHPSpxO4GSoJBVgKnAecCywdSiqpTGfVeR0pPqE6zKx5+YWLeRU1HHch8LOIeBJYCHSleBdwadpeCKyMigeB4ySdAlwM9ETErojYDfQAHenYsRHxQEQEsHLEtSZShxXA4+7WiPzCxbyKSkKXA7en7ZMj4hmA9H1SircBT1ed059io8X7a8QnU8cwkjol9UrqHRgYmMCPaaPxuLs1Ir9wMa+6JyFJRwELgG+OVbRGLCYRn0wdwwMRyyOiFBGl1tbWMS5p4+Fxd2tUfuFiXkX0hC4BNkXEs2n/2aEhsPT9XIr3AzOrzmsHdo4Rb68Rn0wdVmced7dG5Rcu5lVEElrEq0NxAN3A0Ay3MnBXVXxxmsE2F9iThtLWAfMlHZ8mJMwH1qVjz0uam2bFLR5xrYnUYXXmcXdrZOVymTPOOMO9oAzqmoQkzQAuAr5VFb4euEjStnTs+hRfDTwB9AH/HfgwQETsAj4HbEifz6YYwJXA19I5PwPWTKYOqz+Pu1sjG3rhontBxVNlYpkdSqlUit7e3tzN+J03ODjIokWLePnllzn66KO57bbb/Bfe7AgmaWNElMYq5xUTrBAedzezWqblboA1j3K5zPbt2z3ubmYHOQlZYYbG3c3Mhng4zszMsnESMjOzbJyEzMwsGychMzPLxknIzMyycRIyM7NsnITMzCwbJyEzM8vGScjMzLJxEjIzs2ychMzMLBsnITMzy8ZJyMzMsnESMjOzbOr9eu/jJN0p6SeStkr6Z5JOkNQjaVv6Pj6VlaRlkvokPSbp7KrrlFP5bZLKVfFzJG1O5yyTpBSfcB1mZla8eveEbgTWRsTbgDOBrcC1wD0RMQe4J+0DXALMSZ9O4GaoJBRgKXAecC6wdCippDKdVed1pPiE6jAzszzqloQkHQv8CXALQES8HBG/BBYCXalYF3Bp2l4IrIyKB4HjJJ0CXAz0RMSuiNgN9AAd6dixEfFARASwcsS1JlKHmZllUM+e0FuAAeB/SHpY0tckvR44OSKeAUjfJ6XybcDTVef3p9ho8f4acSZRxzCSOiX1SuodGBiY2E9tZmbjVs8kNA04G7g5It4F/JpXh8VqUY1YTCI+mnGdExHLI6IUEaXW1tYxLmlmZpNVzyTUD/RHxENp/04qSenZoSGw9P1cVfmZVee3AzvHiLfXiDOJOszMLIO6JaGI+CfgaUlvTaELgceBbmBohlsZuCttdwOL0wy2ucCeNJS2Dpgv6fg0IWE+sC4de17S3DQrbvGIa02kDjMzy2Bana9/NfB1SUcBTwAfopL4Vkm6AngKuCyVXQ28D+gD9qayRMQuSZ8DNqRyn42IXWn7SuBWYDqwJn0Arp9IHWZmlocqE8vsUEqlUvT29uZuhpnZ7xRJGyOiNFY5r5hgZmbZOAlZYQYHB7nmmmsYHBzM3RQzaxBOQlaYrq4uNm/ezMqVK3M3xcwahJOQFWJwcJC1a9cSEaxdu9a9ITMDnISsIF1dXRw4cACA/fv3uzdkZoCTkBVk/fr17Nu3D4B9+/bR09OTuUVm1gichKwQ8+bNY9q0ymNp06ZN46KLLsrcIjNrBE5CVohyucyUKZVftylTprB48eLMLTKzRuAkZIVoaWnh1FNPBeDUU0+lpaUlc4vMXuXHB/JxErJCDA4OsmPHDgB27tzpv+zWUPz4QD5OQlaIrq4uhpaIOnDggP+yW8Pw4wN5OQlZITw7zhqVHx/Iy0nICuHZcdao/B+kvJyErBDVs+OmTp3q2XHWMPwfpLychKwQLS0tdHR0IImOjg7PjrOGUS6XDw7HHThwwP9BKli9X2pndlC5XGb79u3+S25mB7knZIVpaWlh2bJl7gVZQ+nq6kISAJI8MaFgdU1CkrZL2izpEUm9KXaCpB5J29L38SkuScsk9Ul6TNLZVdcpp/LbJJWr4uek6/elczXZOsysOa1fv579+/cDldlxnphQrCJ6Qu+NiLOqXvN6LXBPRMwB7kn7AJcAc9KnE7gZKgkFWAqcB5wLLB1KKqlMZ9V5HZOpw8yalycm5JVjOG4h0JW2u4BLq+Iro+JB4DhJpwAXAz0RsSsidgM9QEc6dmxEPBCVpyBXjrjWROowsyblmZt51TsJBfB/JW2U1JliJ0fEMwDp+6QUbwOerjq3P8VGi/fXiE+mjmEkdUrqldQ7MDAwgR/XzH7XeOZmXvWeHfeeiNgp6SSgR9JPRimrGrGYRHw04zonIpYDywFKpdJY1zSz33GeuZlPXXtCEbEzfT8HfJvKPZ1nh4bA0vdzqXg/MLPq9HZg5xjx9hpxJlGHmTUxz9zMp25JSNLrJb1xaBuYD/wY6AaGZriVgbvSdjewOM1gmwvsSUNp64D5ko5PExLmA+vSseclzU2z4haPuNZE6jAzswzqORx3MvDtNGt6GnBbRKyVtAFYJekK4CngslR+NfA+oA/YC3wIICJ2SfocsCGV+2xE7ErbVwK3AtOBNekDcP1E6jAzszw0tLy+1VYqlaK3tzd3M8ysjgYHB/nMZz7D0qVLPSR3mEjaWPVoziF5xQQza3p+qV0+TkJm1tT8Uru8nITMrKn5pXZ5OQlZYQYHB7nmmmv8P01rKH6pXV5OQlYYj7tbI5o3b96wVbS9dlyxnISsEB53t0a1YMEChmYJRwTvf//7M7eouTgJWSE87m6Nqru7e1hP6O67787coubiJGSF8Li7Nar169cP6wn5d7NYTkJWCL+zxRqVfzfzchKyQvidLdao/LuZl5OQFcLvbLFG5d/NvJyErDALFixgxowZnn1kDadcLnPGGWe4F5SBk5AVpru7m71793r2kTUcv08on3EnIUlvljQvbU8feleQ2Xj4OSEzq2VcSUjSXwF3Al9NoXbg/9SrUXbk8XNCZlbLeHtCVwHvAX4FEBHbgJPq1Sg78vg5ITOrZbxJ6KWIeHloR9I0wG/Ds3HzsxhmVst4k9A/SvoUMF3SRcA3gXHdXZY0VdLDkr6T9k+T9JCkbZK+IemoFD867fel47OqrnFdiv9U0sVV8Y4U65N0bVV8wnVYfZXL5YPDcQcOHPAsJDMDxp+ErgUGgM3AvwdWA58e57lLgK1V+18CboiIOcBu4IoUvwLYHRGzgRtSOSSdDlwO/CHQAXwlJbapwN8DlwCnA4tS2QnXYWZmeYw3CU0HVkTEZRHxAWBFio1KUjvwL4CvpX0BF1CZ5ADQBVyathemfdLxC1P5hcAdEfFSRPwc6APOTZ++iHgiDRXeASycZB1WZ11dXcMWifTEBDOD8SehexiedKYD68dx3n8F/hY4kPZbgF9GxL603w+0pe024GmAdHxPKn8wPuKcQ8UnU8cwkjol9UrqHRgYGMePaWNZv349+/fvByqz4zwxwcxg/EnomIh4YWgnbc8Y7QRJfwY8FxEbq8M1isYYxw5XfKz6Xw1ELI+IUkSUWltba5xiEzVv3ryD63NNmTLFExPMDBh/Evq1pLOHdiSdA7w4xjnvARZI2k5lqOwCKj2j49LsOqg8b7QzbfcDM9P1pwFvAnZVx0ecc6j4LyZRh9WZJyaYWS3Txi4CwEeBb0oa+sf8FOCDo50QEdcB1wFIOh/4RET8a0nfBD5AJTGVgbvSKd1p/4F0/N6ICEndwG2SvgycCswBfkSlVzNH0mnADiqTF/4inXPfROoY55+B/RZ27979mn0vkWIAN910E319fVnbsGPHDgDa2trGKFl/s2fP5uqrr87djMKMqycUERuAtwFXAh8G3j5imG0iPgl8XFIflfsxt6T4LUBLin+cyow8ImILsAp4HFgLXBUR+9M9nY8A66jMvluVyk64Dqu/z3/+86Pum+X04osv8uKLYw3uWD1otI6ApAsi4l5J/6rW8Yj4Vt1a1iBKpVL09vbmbsbvvPPPP/81sfvvv7/wdpjVsmTJEgBuvPHGzC05ckjaGBGlscqNNRz3p8C9QK219wM44pOQHR7t7e309/cf3J85c+Yopc2sWYyahCJiqaQpwJqIWFVQm+wINHPmzGFJqL29PWNrzKxRjHlPKCIOULn3YjZpDz300Kj7ZtacxjtFu0fSJyTNlHTC0KeuLbMjysh7j56UaGYw/ina/5bKPaAPj4i/5fA2x45UU6ZMObhiwtC+mdl4/yU4ncpioY8CjwA3UVlQ1Gxc5s2bN+q+mTWn8SahLuDtwDIqCejtvLoQqNmYOjs7R903s+Y03uG4t0bEmVX790l6tB4NMjOz5jHentDDkuYO7Ug6D/hBfZpkR6KvfvWrw/aXL1+eqSVm1kjGm4TOA34oaXtakPQB4E8lbZb0WN1aZ0eM9euHv/nDr3IwMxj/cFxHXVthR7yhFbQPtW9mzWlcSSginqx3Q8zMrPn4YQ0zM8vGScgKccIJJ4y6b2bNyUnICrFnz55R982sOTkJWSGql+yptW9mzaluSUjSMZJ+JOlRSVskfSbFT5P0kKRtkr4h6agUPzrt96Xjs6qudV2K/1TSxVXxjhTrk3RtVXzCdZiZWfHq2RN6CbggrbRwFtCRHnj9EnBDRMwBdgNXpPJXALsjYjZwQyqHpNOBy6msVdcBfEXSVElTqaxndwmVte0WpbJMtA4zM8ujbkkoKl5Iu69LnwAuAO5M8S7g0rS9kFfXo7sTuFCSUvyOiHgpIn4O9AHnpk9fRDwRES8DdwAL0zkTrcPMzDKo6z2h1GN5BHgO6AF+BvwyIvalIv1AW9puA54GSMf3AC3V8RHnHCreMok6zMwsg7omoYjYHxFnAe1Uei5vr1UsfdfqkcRhjI9WxzCSOiX1SuodGBiocYqZmR0OhcyOi4hfAvcDc4HjJA2t1NAO7Ezb/cBMgHT8TcCu6viIcw4V/8Uk6hjZ3uURUYqIUmtr6+R+aDMzG1M9Z8e1SjoubU8H5gFbgfuAD6RiZeCutN2d9knH743KO6C7gcvTzLbTgDnAj4ANwJw0E+4oKpMXutM5E63DzMwyGO8CppNxCtCVZrFNAVZFxHckPQ7cIenzwMPALan8LcD/lNRHpXdyOUBEbJG0Cngc2AdcFRH7ASR9BFgHTAVWRMSWdK1PTqQOMzPLo25JKCIeA95VI/4ElftDI+O/AS47xLW+AHyhRnw1sPpw1GFmZsXziglmZpaNk5CZmWXjJGRmZtk4CZmZWTZOQmZmlo2TkJmZZeMkZGZm2TgJmZlZNk5CZmaWjZOQmZll4yRkZmbZOAmZmVk2TkJmZpaNk5CZmWVTz/cJmVkDu+mmm+jr68vdjIYw9OewZMmSzC1pDLNnz+bqq68upC4nIbMm1dfXx7YtD/N7b9ifuynZHfVKZVDopSd7M7ckv6demFpofU5CZk3s996wn0+d/avczbAG8sVNxxZaX93uCUmaKek+SVslbZG0JMVPkNQjaVv6Pj7FJWmZpD5Jj0k6u+pa5VR+m6RyVfwcSZvTOcskabJ1mJlZ8eo5MWEf8B8i4u3AXOAqSacD1wL3RMQc4J60D3AJMCd9OoGboZJQgKXAeVRe2b10KKmkMp1V53Wk+ITqMDOzPOqWhCLimYjYlLafB7YCbcBCoCsV6wIuTdsLgZVR8SBwnKRTgIuBnojYFRG7gR6gIx07NiIeiIgAVo641kTqMDOzDAqZoi1pFvAu4CHg5Ih4BiqJCjgpFWsDnq46rT/FRov314gziTrMzCyDuichSW8A/jfw0YgY7Q6oasRiEvFRmzOecyR1SuqV1DswMDDGJc3MbLLqmoQkvY5KAvp6RHwrhZ8dGgJL38+leD8ws+r0dmDnGPH2GvHJ1DFMRCyPiFJElFpbW8f/A5uZ2YTUc3acgFuArRHx5apD3cDQDLcycFdVfHGawTYX2JOG0tYB8yUdnyYkzAfWpWPPS5qb6lo84loTqcPMzDKo53NC7wH+DbBZ0iMp9ingemCVpCuAp4DL0rHVwPuAPmAv8CGAiNgl6XPAhlTusxGxK21fCdwKTAfWpA8TrcPMzPKoWxKKiO9T+x4MwIU1ygdw1SGutQJYUSPeC7yjRnxwonWYmVnxvICpmZll4yRkZmbZOAmZmVk2TkJmZpaNk5CZmWXjJGRmZtk4CZmZWTZOQmZmlo2TkJmZZeMkZGZm2dRz7Tgza2A7duzg189P5Yubjs3dFGsgTz4/ldfv2FFYfe4JmZlZNu4JmTWptrY2Xtr3DJ86e7R3TVqz+eKmYzm6rbgXTrsnZGZm2TgJmZlZNk5CZmaWjZOQmZllU7eJCZJWAH8GPBcR70ixE4BvALOA7cCfR8RuSQJupPLq7b3AX0bEpnROGfh0uuznI6Irxc/h1Vd7rwaWRERMpo4j3U033URfX1/uZrzGkiVLstQ7e/Zsrr766ix1m9lw9ewJ3Qp0jIhdC9wTEXOAe9I+wCXAnPTpBG6Gg0lrKXAecC6wVNLx6ZybU9mh8zomU4eZmeVTt55QRHxX0qwR4YXA+Wm7C7gf+GSKr4yIAB6UdJykU1LZnojYBSCpB+iQdD9wbEQ8kOIrgUuBNROtIyKeOZw/dyNqhP/1n3/++a+J3XjjjcU3xMwaStH3hE4e+kc/fZ+U4m3A01Xl+lNstHh/jfhk6rACHHPMMcP2p0+fnqklZtZIGmVigmrEYhLxydTx2oJSp6ReSb0DAwNjXNbGY+3atcP216xZk6klZtZIik5Cz6ZhNtL3cyneD8ysKtcO7Bwj3l4jPpk6XiMilkdEKSJKra2tE/oBbWzuBZnZkKKTUDdQTttl4K6q+GJVzAX2pKG0dcB8ScenCQnzgXXp2POS5qZZb4tHXGsidVhBzjzzTM4880z3gszsoHpO0b6dygSBEyX1U5nldj2wStIVwFPAZan4aipTp/uoTJ/+EEBE7JL0OWBDKvfZoUkKwJW8OkV7Tfow0TrMzCyfes6OW3SIQxfWKBvAVYe4zgpgRY14L/COGvHBidZhZmZ5eBVtsyb21At+nxDAs3srdyZOnnEgc0vye+qFqcwpsD4nIbMmNXv27NxNaBgvpxVFjn6z/0zmUOzvhpOQWZNqhIeYG8XQElJ+gLp4TkJ11qjrtuUw9OeQa824RuM17MychOqur6+PR368lf0zTsjdlOymvFx5NnjjE89mbkl+U/fuGruQWRNwEirA/hkn8OLb3pe7GdZApv9kde4mmDWERlm2x8zMmpCTkJmZZePhuDrbsWMHU/fu8fCLDTN17yA7duzL3Qyz7NwTMjOzbNwTqrO2tjb+6aVpnphgw0z/yWra2k7O3Qyz7NwTMjOzbNwTKsDUvbt8TwiY8ptfAXDgGK9VVnlOyD0haIwHuhvpQepme4jZSajOvD7Xq/r6ngdg9lv8jy+c7N+NBuIXLeajyhsO7FBKpVL09vbmbsYRwetzmTUPSRsjojRWOd8TMjOzbJyEzMwsm6ZLQpI6JP1UUp+ka3O3x8ysmTXVxARJU4G/By4C+oENkroj4vG8LauvRph9BI0zA6nZZh+ZNbJm6wmdC/RFxBMR8TJwB7Awc5uaxvTp0z0LycyGaaqeENAGPF213w+cl6kthfH/+s2sUTVbT0g1Yq+Zoy6pU1KvpN6BgYECmmVm1pyaLQn1AzOr9tuBnSMLRcTyiChFRKm1tbWwxpmZNZtmS0IbgDmSTpN0FHA50J25TWZmTaup7glFxD5JHwHWAVOBFRGxJXOzzMyaVlMlIYCIWA14NVEzswbQbMNxZmbWQJyEzMwsGychMzPLxq9yGIOkAeDJ3O04gpwI/CJ3I8xq8O/m4fXmiBjzGRcnISuUpN7xvGPErGj+3czDw3FmZpaNk5CZmWXjJGRFW567AWaH4N/NDHxPyMzMsnFPyMzMsnESskL4terWqCStkPScpB/nbkszchKyuqt6rfolwOnAIkmn522V2UG3Ah25G9GsnISsCH6tujWsiPgusCt3O5qVk5AVodZr1dsytcXMGoiTkBVhXK9VN7Pm4yRkRRjXa9XNrPk4CVkR/Fp1M6vJScjqLiL2AUOvVd8KrPJr1a1RSLodeAB4q6R+SVfkblMz8YoJZmaWjXtCZmaWjZOQmZll4yRkZmbZOAmZmVk2TkJmZpaNk5BZA5H0UUkzJnHe2yQ9IulhSb9/GNpxqReZtSI4CZk1lo8CE0pCaZXyS4G7IuJdEfGzqmOSNJm/55dSWfHcrK6chMzqQNLfSrombd8g6d60faGk/yXpZkm9krZI+kw6dg1wKnCfpPtSbL6kByRtkvRNSW9I8e2S/pOk7wMfpJK8/p2k+yTNkrRV0leATcBMSYskbZb0Y0lfqmrnC5K+IOlRSQ9KOlnSHwELgL9LvavfumdldihOQmb18V3gn6ftEvAGSa8D/hj4HvAfI6IEvBP4U0nvjIhlVNbUe29EvFfSicCngXkRcTbQC3y8qo7fRMQfR8RtwD8AN0TEe9OxtwIrI+JdwCvAl4ALgLOAd0u6NJV7PfBgRJyZ2vxXEfFDKssq/U1EnFXdszI73JyEzOpjI3COpDcCL1FZFqZEJTF9D/hzSZuAh4E/pPbQ19wU/4GkR4Ay8Oaq498Ypf4nI+LBtP1u4P6IGEhLKH0d+JN07GXgO1VtnjWRH9LstzUtdwPMjkQR8Yqk7cCHgB8CjwHvBX4feBH4BPDuiNgt6VbgmBqXEdATEYsOUc2vR2lC9bFar9IY8kq8unbXfvxvghXMPSGz+vkulWTzXSq9n78GHgGOpZIk9kg6mcprz4c8D7wxbT8IvEfSbABJMyT9wSTa8RCVIb8T0ySGRcA/jnFOdTvM6sZJyKx+vgecAjwQEc8CvwG+FxGPUhmG2wKsAH5Qdc5yYI2k+yJiAPhL4HZJj1FJSm+baCMi4hngOuA+4FFgU0TcNcZpdwB/c7imfJsdilfRNjOzbNwTMjOzbJyEzMwsGychMzPLxknIzMyycRIyM7NsnITMzCwbJyEzM8vGScjMzLL5/7PzJ25ACb4KAAAAAElFTkSuQmCC\n",
                        "text/plain": "<Figure size 432x288 with 1 Axes>"
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": "sns.boxplot(x=\"waterfront\", y=\"price\", data=df)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 5\nUse the function <code>regplot</code>  in the seaborn library  to  determine if the feature <code>sqft_above</code> is negatively or positively correlated with price."
        },
        {
            "cell_type": "code",
            "execution_count": 27,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "<matplotlib.axes._subplots.AxesSubplot at 0x7f3cc4ed0a58>"
                    },
                    "execution_count": 27,
                    "metadata": {},
                    "output_type": "execute_result"
                },
                {
                    "data": {
                        "image/png": "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\n",
                        "text/plain": "<Figure size 432x288 with 1 Axes>"
                    },
                    "metadata": {
                        "needs_background": "light"
                    },
                    "output_type": "display_data"
                }
            ],
            "source": "sns.regplot(x=\"sqft_above\", y=\"price\", data=df, ci = None)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "\nWe can use the Pandas method <code>corr()</code>  to find the feature other than price that is most correlated with price."
        },
        {
            "cell_type": "code",
            "execution_count": 28,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "zipcode         -0.053203\nlong             0.021626\ncondition        0.036362\nyr_built         0.054012\nsqft_lot15       0.082447\nsqft_lot         0.089661\nyr_renovated     0.126434\nfloors           0.256794\nwaterfront       0.266369\nlat              0.307003\nbedrooms         0.308797\nsqft_basement    0.323816\nview             0.397293\nbathrooms        0.525738\nsqft_living15    0.585379\nsqft_above       0.605567\ngrade            0.667434\nsqft_living      0.702035\nprice            1.000000\nName: price, dtype: float64"
                    },
                    "execution_count": 28,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.corr()['price'].sort_values()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# Module 4: Model Development"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "\nWe can Fit a linear regression model using the  longitude feature <code>'long'</code> and  caculate the R^2."
        },
        {
            "cell_type": "code",
            "execution_count": 29,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "0.00046769430149007363"
                    },
                    "execution_count": 29,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "X = df[['long']]\nY = df['price']\nlm = LinearRegression()\nlm.fit(X,Y)\nlm.score(X, Y)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question  6\nFit a linear regression model to predict the <code>'price'</code> using the feature <code>'sqft_living'</code> then calculate the R^2. Take a screenshot of your code and the value of the R^2."
        },
        {
            "cell_type": "code",
            "execution_count": 31,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "0.49285321790379316"
                    },
                    "execution_count": 31,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "X1 = df[['sqft_living']]\nY1 = df['price']\nlm = LinearRegression()\nlm.fit(X1,Y1)\nlm.score(X1, Y1)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 7\nFit a linear regression model to predict the <code>'price'</code> using the list of features:"
        },
        {
            "cell_type": "code",
            "execution_count": 32,
            "metadata": {},
            "outputs": [],
            "source": "features =[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]     "
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Then calculate the R^2. Take a screenshot of your code."
        },
        {
            "cell_type": "code",
            "execution_count": 34,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "0.657679183672129"
                    },
                    "execution_count": 34,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "X2 = df[features]\nY2 = df['price']\nlm.fit(X2,Y2)\nlm.score(X2,Y2)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### This will help with Question 8\n\nCreate a list of tuples, the first element in the tuple contains the name of the estimator:\n\n<code>'scale'</code>\n\n<code>'polynomial'</code>\n\n<code>'model'</code>\n\nThe second element in the tuple  contains the model constructor \n\n<code>StandardScaler()</code>\n\n<code>PolynomialFeatures(include_bias=False)</code>\n\n<code>LinearRegression()</code>\n"
        },
        {
            "cell_type": "code",
            "execution_count": 35,
            "metadata": {},
            "outputs": [],
            "source": "Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 8\nUse the list to create a pipeline object to predict the 'price', fit the object using the features in the list <code>features</code>, and calculate the R^2."
        },
        {
            "cell_type": "code",
            "execution_count": 37,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "Pipeline(memory=None,\n     steps=[('scale', StandardScaler(copy=True, with_mean=True, with_std=True)), ('polynomial', PolynomialFeatures(degree=2, include_bias=False, interaction_only=False)), ('model', LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,\n         normalize=False))])"
                    },
                    "execution_count": 37,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "pipe=Pipeline(Input)\npipe"
        },
        {
            "cell_type": "code",
            "execution_count": 39,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "0.0033607985166381744"
                    },
                    "execution_count": 39,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "pipe.fit(X,Y)\npipe.score(X,Y)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# Module 5: Model Evaluation and Refinement"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Import the necessary modules:"
        },
        {
            "cell_type": "code",
            "execution_count": 40,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "done\n"
                }
            ],
            "source": "from sklearn.model_selection import cross_val_score\nfrom sklearn.model_selection import train_test_split\nprint(\"done\")"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We will split the data into training and testing sets:"
        },
        {
            "cell_type": "code",
            "execution_count": 41,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "number of test samples: 3242\nnumber of training samples: 18371\n"
                }
            ],
            "source": "features =[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]    \nX = df[features]\nY = df['price']\n\nx_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)\n\n\nprint(\"number of test samples:\", x_test.shape[0])\nprint(\"number of training samples:\",x_train.shape[0])"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 9\nCreate and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data. \n"
        },
        {
            "cell_type": "code",
            "execution_count": 42,
            "metadata": {},
            "outputs": [],
            "source": "from sklearn.linear_model import Ridge"
        },
        {
            "cell_type": "code",
            "execution_count": 45,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "0.6478759163939121"
                    },
                    "execution_count": 45,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "RigeModel = Ridge(alpha=0.1) \nRigeModel.fit(x_train, y_train)\nRigeModel.score(x_test, y_test)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Question 10\nPerform a second order polynomial transform on both the training data and testing data. Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided. Take a screenshot of your code and the R^2."
        },
        {
            "cell_type": "code",
            "execution_count": 49,
            "metadata": {
                "jupyter": {
                    "outputs_hidden": false
                }
            },
            "outputs": [
                {
                    "data": {
                        "text/plain": "0.7002744279699229"
                    },
                    "execution_count": 49,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "pr=PolynomialFeatures(degree=2)\nx_train_pr=pr.fit_transform(x_train[features])\nx_test_pr=pr.fit_transform(x_test[features])\n\nRigeModel = Ridge(alpha=0.1) \nRigeModel.fit(x_train_pr, y_train)\nRigeModel.score(x_test_pr, y_test)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<p>Once you complete your notebook you will have to share it. Select the icon on the top right a marked in red in the image below, a dialogue box should open, and select the option all&nbsp;content excluding sensitive code cells.</p>\n        <p><img width=\"600\" src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/save_notebook.png\" alt=\"share notebook\"  style=\"display: block; margin-left: auto; margin-right: auto;\"/></p>\n        <p></p>\n        <p>You can then share the notebook&nbsp; via a&nbsp; URL by scrolling down as shown in the following image:</p>\n        <p style=\"text-align: center;\"><img width=\"600\"  src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/url_notebook.png\" alt=\"HTML\" style=\"display: block; margin-left: auto; margin-right: auto;\" /></p>\n        <p>&nbsp;</p>"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<h2>About the Authors:</h2> \n\n<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD."
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Other contributors: <a href=\"https://www.linkedin.com/in/michelleccarey/\">Michelle Carey</a>, <a href=\"www.linkedin.com/in/jiahui-mavis-zhou-a4537814a\">Mavis Zhou</a> "
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": ""
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3.6",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.6.9"
        },
        "widgets": {
            "state": {},
            "version": "1.1.2"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}