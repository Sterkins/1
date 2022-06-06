{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "cb0142a4",
   "metadata": {},
   "source": [
    "# Сессия 1\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "25bef6f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# импорт библиотек\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt \n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f083253",
   "metadata": {},
   "source": [
    "### 1.1 Подготовка данных"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "bf6f0106",
   "metadata": {},
   "source": [
    "Необходимо выполнить подготовку данных для дальнейшего  анализа и построения прогнозных моделей. Следует выполнить загрузку всех необходимых данных по пассажирским перевозкам. Требуется выполнить объединение двух частей набора данных по перевозкам."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f75b8c72",
   "metadata": {},
   "outputs": [],
   "source": [
    "first_part = pd.read_excel(\"train_first_part.xlsx\")\n",
    "second_part = pd.read_json(\"train_second_part.json\")\n",
    "weather = pd.read_csv(\"weather.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "9dffecd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>vendor_id</th>\n",
       "      <th>pickup_datetime</th>\n",
       "      <th>dropoff_datetime</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>trip_duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>id2875421</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-14 17:24:55</td>\n",
       "      <td>2016-03-14 17:32:30</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.982155</td>\n",
       "      <td>40.767937</td>\n",
       "      <td>-73.964630</td>\n",
       "      <td>40.765602</td>\n",
       "      <td>N</td>\n",
       "      <td>455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>id2377394</td>\n",
       "      <td>1</td>\n",
       "      <td>2016-06-12 00:43:35</td>\n",
       "      <td>2016-06-12 00:54:38</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.980415</td>\n",
       "      <td>40.738564</td>\n",
       "      <td>-73.999481</td>\n",
       "      <td>40.731152</td>\n",
       "      <td>N</td>\n",
       "      <td>663</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>id3858529</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-01-19 11:35:24</td>\n",
       "      <td>2016-01-19 12:10:48</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.979027</td>\n",
       "      <td>40.763939</td>\n",
       "      <td>-74.005333</td>\n",
       "      <td>40.710087</td>\n",
       "      <td>N</td>\n",
       "      <td>2124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>id3504673</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-04-06 19:32:31</td>\n",
       "      <td>2016-04-06 19:39:40</td>\n",
       "      <td>1</td>\n",
       "      <td>-74.010040</td>\n",
       "      <td>40.719971</td>\n",
       "      <td>-74.012268</td>\n",
       "      <td>40.706718</td>\n",
       "      <td>N</td>\n",
       "      <td>429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>id2181028</td>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-26 13:30:55</td>\n",
       "      <td>2016-03-26 13:38:10</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.973053</td>\n",
       "      <td>40.793209</td>\n",
       "      <td>-73.972923</td>\n",
       "      <td>40.782520</td>\n",
       "      <td>N</td>\n",
       "      <td>435</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  vendor_id     pickup_datetime    dropoff_datetime  \\\n",
       "0  id2875421          2 2016-03-14 17:24:55 2016-03-14 17:32:30   \n",
       "1  id2377394          1 2016-06-12 00:43:35 2016-06-12 00:54:38   \n",
       "2  id3858529          2 2016-01-19 11:35:24 2016-01-19 12:10:48   \n",
       "3  id3504673          2 2016-04-06 19:32:31 2016-04-06 19:39:40   \n",
       "4  id2181028          2 2016-03-26 13:30:55 2016-03-26 13:38:10   \n",
       "\n",
       "   passenger_count  pickup_longitude  pickup_latitude  dropoff_longitude  \\\n",
       "0                1        -73.982155        40.767937         -73.964630   \n",
       "1                1        -73.980415        40.738564         -73.999481   \n",
       "2                1        -73.979027        40.763939         -74.005333   \n",
       "3                1        -74.010040        40.719971         -74.012268   \n",
       "4                1        -73.973053        40.793209         -73.972923   \n",
       "\n",
       "   dropoff_latitude store_and_fwd_flag  trip_duration  \n",
       "0         40.765602                  N            455  \n",
       "1         40.731152                  N            663  \n",
       "2         40.710087                  N           2124  \n",
       "3         40.706718                  N            429  \n",
       "4         40.782520                  N            435  "
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "first_part.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "e2c1e6b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>vendor_id</th>\n",
       "      <th>pickup_datetime</th>\n",
       "      <th>dropoff_datetime</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>trip_duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>id3758523</td>\n",
       "      <td>2</td>\n",
       "      <td>6/2/16 2:30</td>\n",
       "      <td>6/2/16 2:50</td>\n",
       "      <td>6</td>\n",
       "      <td>-73.991272</td>\n",
       "      <td>40.697350</td>\n",
       "      <td>-73.989700</td>\n",
       "      <td>40.767689</td>\n",
       "      <td>N</td>\n",
       "      <td>1210</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>id1849264</td>\n",
       "      <td>2</td>\n",
       "      <td>1/6/16 18:12</td>\n",
       "      <td>1/6/16 18:30</td>\n",
       "      <td>5</td>\n",
       "      <td>-73.988281</td>\n",
       "      <td>40.723385</td>\n",
       "      <td>-74.005089</td>\n",
       "      <td>40.749908</td>\n",
       "      <td>N</td>\n",
       "      <td>1077</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>id3457947</td>\n",
       "      <td>1</td>\n",
       "      <td>2/28/16 12:09</td>\n",
       "      <td>2/28/16 12:11</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.968872</td>\n",
       "      <td>40.767120</td>\n",
       "      <td>-73.962051</td>\n",
       "      <td>40.776581</td>\n",
       "      <td>N</td>\n",
       "      <td>135</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>id2181863</td>\n",
       "      <td>2</td>\n",
       "      <td>6/26/16 16:22</td>\n",
       "      <td>6/26/16 16:29</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.982330</td>\n",
       "      <td>40.775517</td>\n",
       "      <td>-73.965622</td>\n",
       "      <td>40.804626</td>\n",
       "      <td>N</td>\n",
       "      <td>415</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>id1445143</td>\n",
       "      <td>1</td>\n",
       "      <td>5/12/16 22:43</td>\n",
       "      <td>5/12/16 22:57</td>\n",
       "      <td>2</td>\n",
       "      <td>-73.966698</td>\n",
       "      <td>40.764000</td>\n",
       "      <td>-73.938751</td>\n",
       "      <td>40.766308</td>\n",
       "      <td>N</td>\n",
       "      <td>810</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  vendor_id pickup_datetime dropoff_datetime  passenger_count  \\\n",
       "0  id3758523          2     6/2/16 2:30      6/2/16 2:50                6   \n",
       "1  id1849264          2    1/6/16 18:12     1/6/16 18:30                5   \n",
       "2  id3457947          1   2/28/16 12:09    2/28/16 12:11                1   \n",
       "3  id2181863          2   6/26/16 16:22    6/26/16 16:29                1   \n",
       "4  id1445143          1   5/12/16 22:43    5/12/16 22:57                2   \n",
       "\n",
       "   pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  \\\n",
       "0        -73.991272        40.697350         -73.989700         40.767689   \n",
       "1        -73.988281        40.723385         -74.005089         40.749908   \n",
       "2        -73.968872        40.767120         -73.962051         40.776581   \n",
       "3        -73.982330        40.775517         -73.965622         40.804626   \n",
       "4        -73.966698        40.764000         -73.938751         40.766308   \n",
       "\n",
       "  store_and_fwd_flag  trip_duration  \n",
       "0                  N           1210  \n",
       "1                  N           1077  \n",
       "2                  N            135  \n",
       "3                  N            415  \n",
       "4                  N            810  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "second_part.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2383c73",
   "metadata": {},
   "source": [
    "Объединяем выборки"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "36e88425",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.concat([first_part, second_part]).drop_duplicates(\"id\").drop(\"id\", axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f7559226",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>vendor_id</th>\n",
       "      <th>pickup_datetime</th>\n",
       "      <th>dropoff_datetime</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>trip_duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-14 17:24:55</td>\n",
       "      <td>2016-03-14 17:32:30</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.982155</td>\n",
       "      <td>40.767937</td>\n",
       "      <td>-73.964630</td>\n",
       "      <td>40.765602</td>\n",
       "      <td>N</td>\n",
       "      <td>455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2016-06-12 00:43:35</td>\n",
       "      <td>2016-06-12 00:54:38</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.980415</td>\n",
       "      <td>40.738564</td>\n",
       "      <td>-73.999481</td>\n",
       "      <td>40.731152</td>\n",
       "      <td>N</td>\n",
       "      <td>663</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-01-19 11:35:24</td>\n",
       "      <td>2016-01-19 12:10:48</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.979027</td>\n",
       "      <td>40.763939</td>\n",
       "      <td>-74.005333</td>\n",
       "      <td>40.710087</td>\n",
       "      <td>N</td>\n",
       "      <td>2124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-04-06 19:32:31</td>\n",
       "      <td>2016-04-06 19:39:40</td>\n",
       "      <td>1</td>\n",
       "      <td>-74.010040</td>\n",
       "      <td>40.719971</td>\n",
       "      <td>-74.012268</td>\n",
       "      <td>40.706718</td>\n",
       "      <td>N</td>\n",
       "      <td>429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-26 13:30:55</td>\n",
       "      <td>2016-03-26 13:38:10</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.973053</td>\n",
       "      <td>40.793209</td>\n",
       "      <td>-73.972923</td>\n",
       "      <td>40.782520</td>\n",
       "      <td>N</td>\n",
       "      <td>435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8582</th>\n",
       "      <td>1</td>\n",
       "      <td>4/6/16 14:16</td>\n",
       "      <td>4/6/16 14:20</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.973015</td>\n",
       "      <td>40.760948</td>\n",
       "      <td>-73.976387</td>\n",
       "      <td>40.755604</td>\n",
       "      <td>N</td>\n",
       "      <td>207</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8583</th>\n",
       "      <td>2</td>\n",
       "      <td>3/24/16 1:26</td>\n",
       "      <td>3/24/16 1:38</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.985550</td>\n",
       "      <td>40.727257</td>\n",
       "      <td>-73.957039</td>\n",
       "      <td>40.712387</td>\n",
       "      <td>N</td>\n",
       "      <td>740</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8584</th>\n",
       "      <td>1</td>\n",
       "      <td>2/23/16 16:38</td>\n",
       "      <td>2/23/16 16:48</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.972038</td>\n",
       "      <td>40.750202</td>\n",
       "      <td>-73.998360</td>\n",
       "      <td>40.733360</td>\n",
       "      <td>N</td>\n",
       "      <td>605</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8585</th>\n",
       "      <td>1</td>\n",
       "      <td>5/24/16 7:20</td>\n",
       "      <td>5/24/16 7:25</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.993332</td>\n",
       "      <td>40.724342</td>\n",
       "      <td>-74.004250</td>\n",
       "      <td>40.707470</td>\n",
       "      <td>N</td>\n",
       "      <td>287</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8586</th>\n",
       "      <td>2</td>\n",
       "      <td>3/15/16 22:00</td>\n",
       "      <td>3/15/16 22:19</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.988060</td>\n",
       "      <td>40.759548</td>\n",
       "      <td>-74.005585</td>\n",
       "      <td>40.711521</td>\n",
       "      <td>N</td>\n",
       "      <td>1169</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1048575 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      vendor_id      pickup_datetime     dropoff_datetime  passenger_count  \\\n",
       "0             2  2016-03-14 17:24:55  2016-03-14 17:32:30                1   \n",
       "1             1  2016-06-12 00:43:35  2016-06-12 00:54:38                1   \n",
       "2             2  2016-01-19 11:35:24  2016-01-19 12:10:48                1   \n",
       "3             2  2016-04-06 19:32:31  2016-04-06 19:39:40                1   \n",
       "4             2  2016-03-26 13:30:55  2016-03-26 13:38:10                1   \n",
       "...         ...                  ...                  ...              ...   \n",
       "8582          1         4/6/16 14:16         4/6/16 14:20                1   \n",
       "8583          2         3/24/16 1:26         3/24/16 1:38                1   \n",
       "8584          1        2/23/16 16:38        2/23/16 16:48                1   \n",
       "8585          1         5/24/16 7:20         5/24/16 7:25                1   \n",
       "8586          2        3/15/16 22:00        3/15/16 22:19                1   \n",
       "\n",
       "      pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  \\\n",
       "0           -73.982155        40.767937         -73.964630         40.765602   \n",
       "1           -73.980415        40.738564         -73.999481         40.731152   \n",
       "2           -73.979027        40.763939         -74.005333         40.710087   \n",
       "3           -74.010040        40.719971         -74.012268         40.706718   \n",
       "4           -73.973053        40.793209         -73.972923         40.782520   \n",
       "...                ...              ...                ...               ...   \n",
       "8582        -73.973015        40.760948         -73.976387         40.755604   \n",
       "8583        -73.985550        40.727257         -73.957039         40.712387   \n",
       "8584        -73.972038        40.750202         -73.998360         40.733360   \n",
       "8585        -73.993332        40.724342         -74.004250         40.707470   \n",
       "8586        -73.988060        40.759548         -74.005585         40.711521   \n",
       "\n",
       "     store_and_fwd_flag  trip_duration  \n",
       "0                     N            455  \n",
       "1                     N            663  \n",
       "2                     N           2124  \n",
       "3                     N            429  \n",
       "4                     N            435  \n",
       "...                 ...            ...  \n",
       "8582                  N            207  \n",
       "8583                  N            740  \n",
       "8584                  N            605  \n",
       "8585                  N            287  \n",
       "8586                  N           1169  \n",
       "\n",
       "[1048575 rows x 10 columns]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "93fc88de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1048575 entries, 0 to 8586\n",
      "Data columns (total 10 columns):\n",
      " #   Column              Non-Null Count    Dtype  \n",
      "---  ------              --------------    -----  \n",
      " 0   vendor_id           1048575 non-null  int64  \n",
      " 1   pickup_datetime     1048575 non-null  object \n",
      " 2   dropoff_datetime    1048575 non-null  object \n",
      " 3   passenger_count     1048575 non-null  int64  \n",
      " 4   pickup_longitude    1048575 non-null  float64\n",
      " 5   pickup_latitude     1048575 non-null  float64\n",
      " 6   dropoff_longitude   1048575 non-null  float64\n",
      " 7   dropoff_latitude    1048575 non-null  float64\n",
      " 8   store_and_fwd_flag  1048575 non-null  object \n",
      " 9   trip_duration       1048575 non-null  int64  \n",
      "dtypes: float64(4), int64(3), object(3)\n",
      "memory usage: 88.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c7b1f759",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1048575 entries, 0 to 8586\n",
      "Data columns (total 10 columns):\n",
      " #   Column              Non-Null Count    Dtype         \n",
      "---  ------              --------------    -----         \n",
      " 0   vendor_id           1048575 non-null  int64         \n",
      " 1   pickup_datetime     1048575 non-null  datetime64[ns]\n",
      " 2   dropoff_datetime    1048575 non-null  datetime64[ns]\n",
      " 3   passenger_count     1048575 non-null  int64         \n",
      " 4   pickup_longitude    1048575 non-null  float64       \n",
      " 5   pickup_latitude     1048575 non-null  float64       \n",
      " 6   dropoff_longitude   1048575 non-null  float64       \n",
      " 7   dropoff_latitude    1048575 non-null  float64       \n",
      " 8   store_and_fwd_flag  1048575 non-null  object        \n",
      " 9   trip_duration       1048575 non-null  int64         \n",
      "dtypes: datetime64[ns](2), float64(4), int64(3), object(1)\n",
      "memory usage: 88.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df[\"pickup_datetime\"] = pd.to_datetime(df[\"pickup_datetime\"])\n",
    "df[\"dropoff_datetime\"] = pd.to_datetime(df[\"dropoff_datetime\"])\n",
    "\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bc330e52",
   "metadata": {},
   "source": [
    "### Форматирование данных"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "cd86e1d3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x720 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10, 10))\n",
    "sns.heatmap(df.isna())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f865fe05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1048575 entries, 0 to 8586\n",
      "Data columns (total 10 columns):\n",
      " #   Column              Non-Null Count    Dtype         \n",
      "---  ------              --------------    -----         \n",
      " 0   vendor_id           1048575 non-null  int64         \n",
      " 1   pickup_datetime     1048575 non-null  datetime64[ns]\n",
      " 2   dropoff_datetime    1048575 non-null  datetime64[ns]\n",
      " 3   passenger_count     1048575 non-null  int64         \n",
      " 4   pickup_longitude    1048575 non-null  float64       \n",
      " 5   pickup_latitude     1048575 non-null  float64       \n",
      " 6   dropoff_longitude   1048575 non-null  float64       \n",
      " 7   dropoff_latitude    1048575 non-null  float64       \n",
      " 8   store_and_fwd_flag  1048575 non-null  object        \n",
      " 9   trip_duration       1048575 non-null  int64         \n",
      "dtypes: datetime64[ns](2), float64(4), int64(3), object(1)\n",
      "memory usage: 88.0+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4a8f1885",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"trip_duration\"] = df[\"trip_duration\"].apply(lambda x : x / 60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "e5a2abff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        7.583333\n",
       "1       11.050000\n",
       "2       35.400000\n",
       "3        7.150000\n",
       "4        7.250000\n",
       "          ...    \n",
       "8582     3.450000\n",
       "8583    12.333333\n",
       "8584    10.083333\n",
       "8585     4.783333\n",
       "8586    19.483333\n",
       "Name: trip_duration, Length: 1048575, dtype: float64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"trip_duration\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "b917e119",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>vendor_id</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>trip_duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1.048575e+06</td>\n",
       "      <td>1.048575e+06</td>\n",
       "      <td>1.048575e+06</td>\n",
       "      <td>1.048575e+06</td>\n",
       "      <td>1.048575e+06</td>\n",
       "      <td>1.048575e+06</td>\n",
       "      <td>1.048575e+06</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>1.534503e+00</td>\n",
       "      <td>1.664382e+00</td>\n",
       "      <td>-7.397342e+01</td>\n",
       "      <td>4.075094e+01</td>\n",
       "      <td>-7.397336e+01</td>\n",
       "      <td>4.075183e+01</td>\n",
       "      <td>1.603575e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.988084e-01</td>\n",
       "      <td>1.314261e+00</td>\n",
       "      <td>4.280165e-02</td>\n",
       "      <td>3.381389e-02</td>\n",
       "      <td>4.274282e-02</td>\n",
       "      <td>3.645002e-02</td>\n",
       "      <td>9.755004e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>0.000000e+00</td>\n",
       "      <td>-7.854740e+01</td>\n",
       "      <td>3.435970e+01</td>\n",
       "      <td>-7.981798e+01</td>\n",
       "      <td>3.218114e+01</td>\n",
       "      <td>1.666667e-02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>-7.399186e+01</td>\n",
       "      <td>4.073738e+01</td>\n",
       "      <td>-7.399131e+01</td>\n",
       "      <td>4.073594e+01</td>\n",
       "      <td>6.616667e+00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2.000000e+00</td>\n",
       "      <td>1.000000e+00</td>\n",
       "      <td>-7.398174e+01</td>\n",
       "      <td>4.075415e+01</td>\n",
       "      <td>-7.397973e+01</td>\n",
       "      <td>4.075455e+01</td>\n",
       "      <td>1.103333e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>2.000000e+00</td>\n",
       "      <td>2.000000e+00</td>\n",
       "      <td>-7.396731e+01</td>\n",
       "      <td>4.076836e+01</td>\n",
       "      <td>-7.396301e+01</td>\n",
       "      <td>4.076984e+01</td>\n",
       "      <td>1.791667e+01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>2.000000e+00</td>\n",
       "      <td>9.000000e+00</td>\n",
       "      <td>-6.133553e+01</td>\n",
       "      <td>5.188108e+01</td>\n",
       "      <td>-6.133553e+01</td>\n",
       "      <td>4.391176e+01</td>\n",
       "      <td>5.877137e+04</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          vendor_id  passenger_count  pickup_longitude  pickup_latitude  \\\n",
       "count  1.048575e+06     1.048575e+06      1.048575e+06     1.048575e+06   \n",
       "mean   1.534503e+00     1.664382e+00     -7.397342e+01     4.075094e+01   \n",
       "std    4.988084e-01     1.314261e+00      4.280165e-02     3.381389e-02   \n",
       "min    1.000000e+00     0.000000e+00     -7.854740e+01     3.435970e+01   \n",
       "25%    1.000000e+00     1.000000e+00     -7.399186e+01     4.073738e+01   \n",
       "50%    2.000000e+00     1.000000e+00     -7.398174e+01     4.075415e+01   \n",
       "75%    2.000000e+00     2.000000e+00     -7.396731e+01     4.076836e+01   \n",
       "max    2.000000e+00     9.000000e+00     -6.133553e+01     5.188108e+01   \n",
       "\n",
       "       dropoff_longitude  dropoff_latitude  trip_duration  \n",
       "count       1.048575e+06      1.048575e+06   1.048575e+06  \n",
       "mean       -7.397336e+01      4.075183e+01   1.603575e+01  \n",
       "std         4.274282e-02      3.645002e-02   9.755004e+01  \n",
       "min        -7.981798e+01      3.218114e+01   1.666667e-02  \n",
       "25%        -7.399131e+01      4.073594e+01   6.616667e+00  \n",
       "50%        -7.397973e+01      4.075455e+01   1.103333e+01  \n",
       "75%        -7.396301e+01      4.076984e+01   1.791667e+01  \n",
       "max        -6.133553e+01      4.391176e+01   5.877137e+04  "
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "090e5aa2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='trip_duration'>"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "plt.figure(figsize = (5 , 5))\n",
    "sns.boxplot(df[\"trip_duration\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e5531825",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in range(90, 101):\n",
    "    qunt = df[\"trip_duration\"].quantile(i/100)\n",
    "    df_qunt = df[df[\"trip_duration\"] < qunt][\"trip_duration\"]\n",
    "    \n",
    "    sns.boxplot(df_qunt)\n",
    "    plt.title(i)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "9fa0e4a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "q_up = df[\"trip_duration\"].quantile(0.93)\n",
    "df = df[df[\"trip_duration\"] < q_up]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "aac4e0a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "N    970191\n",
       "Y      4929\n",
       "Name: store_and_fwd_flag, dtype: int64"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"store_and_fwd_flag\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "6788153e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    970191\n",
       "1      4929\n",
       "Name: store_and_fwd_flag, dtype: int64"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "d_tm = {\"N\" : 0, \"Y\" : 1}\n",
    "df[\"store_and_fwd_flag\"] = df[\"store_and_fwd_flag\"].map(d_tm)\n",
    "df[\"store_and_fwd_flag\"].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2792cad",
   "metadata": {},
   "source": [
    "## Форматирование погодных данных"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "c251844c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "date                   0\n",
       "maximum temperature    0\n",
       "minimum temperature    0\n",
       "average temperature    0\n",
       "precipitation          0\n",
       "snow fall              0\n",
       "snow depth             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weather.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "d38bf4b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['0.00' 'T' '1.80' '0.24' '0.05' '0.01' '2.31' '0.73' '0.53' '0.44' '1.01'\n",
      " '0.03' '0.30' '1.22' '0.02' '0.14' '0.11' '0.06' '0.29' '0.07' '0.04'\n",
      " '0.38' '0.16' '0.09' '0.47' '0.20' '0.61' '0.54' '0.25' '0.18' '1.65'\n",
      " '0.40' '0.91' '0.45' '0.22' '0.12' '0.83' '0' '0.49' '0.66' '0.08' '0.62'\n",
      " '0.35' '1' '1.09' '1.08' '0.15' '0.32' '0.82' '0.31' '0.5' '0.56' '0.68'\n",
      " '0.2' '0.4' '0.23' '0.55' '1.11' '1.41' '1.81' '2.2' '0.19' '0.39']\n",
      "----------\n",
      "['0.0' 'T' '0.4' '0.2' '27.3' '2.5' '0.1' '1.4' '0.5' '0' '2.8']\n",
      "----------\n",
      "['0' 'T' '6' '22' '19' '17' '9' '4' '2' '1']\n",
      "----------\n"
     ]
    }
   ],
   "source": [
    "for col in [\"precipitation\", \"snow fall\", \"snow depth\"]:\n",
    "    print(weather[col].unique())\n",
    "    print(\"-\" * 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "4e4fd6e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "for col in [\"precipitation\", \"snow fall\", \"snow depth\"]:\n",
    "    weather.loc[weather[col] == \"T\", col] = 0\n",
    "    weather[col] = weather[col].astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "bc014449",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>maximum temperature</th>\n",
       "      <th>minimum temperature</th>\n",
       "      <th>average temperature</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>snow fall</th>\n",
       "      <th>snow depth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>64.625683</td>\n",
       "      <td>49.806011</td>\n",
       "      <td>57.215847</td>\n",
       "      <td>0.115219</td>\n",
       "      <td>0.098361</td>\n",
       "      <td>0.275956</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>18.041787</td>\n",
       "      <td>16.570747</td>\n",
       "      <td>17.124760</td>\n",
       "      <td>0.309682</td>\n",
       "      <td>1.441631</td>\n",
       "      <td>1.928253</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>50.000000</td>\n",
       "      <td>37.250000</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>64.500000</td>\n",
       "      <td>48.000000</td>\n",
       "      <td>55.750000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>81.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>73.500000</td>\n",
       "      <td>0.040000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>96.000000</td>\n",
       "      <td>81.000000</td>\n",
       "      <td>88.500000</td>\n",
       "      <td>2.310000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>22.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       maximum temperature  minimum temperature  average temperature  \\\n",
       "count           366.000000           366.000000           366.000000   \n",
       "mean             64.625683            49.806011            57.215847   \n",
       "std              18.041787            16.570747            17.124760   \n",
       "min              15.000000            -1.000000             7.000000   \n",
       "25%              50.000000            37.250000            44.000000   \n",
       "50%              64.500000            48.000000            55.750000   \n",
       "75%              81.000000            65.000000            73.500000   \n",
       "max              96.000000            81.000000            88.500000   \n",
       "\n",
       "       precipitation   snow fall  snow depth  \n",
       "count     366.000000  366.000000  366.000000  \n",
       "mean        0.115219    0.098361    0.275956  \n",
       "std         0.309682    1.441631    1.928253  \n",
       "min         0.000000    0.000000    0.000000  \n",
       "25%         0.000000    0.000000    0.000000  \n",
       "50%         0.000000    0.000000    0.000000  \n",
       "75%         0.040000    0.000000    0.000000  \n",
       "max         2.310000   27.300000   22.000000  "
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weather.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "c31997f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "for temp in [\"maximum temperature\", \"minimum temperature\", \"average temperature\"]:\n",
    "    weather[temp] = weather[temp].apply(lambda x : (x - 32)/1.8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "d2b465b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>maximum temperature</th>\n",
       "      <th>minimum temperature</th>\n",
       "      <th>average temperature</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>snow fall</th>\n",
       "      <th>snow depth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "      <td>366.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>18.125379</td>\n",
       "      <td>9.892228</td>\n",
       "      <td>14.008804</td>\n",
       "      <td>0.115219</td>\n",
       "      <td>0.098361</td>\n",
       "      <td>0.275956</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>10.023215</td>\n",
       "      <td>9.205971</td>\n",
       "      <td>9.513755</td>\n",
       "      <td>0.309682</td>\n",
       "      <td>1.441631</td>\n",
       "      <td>1.928253</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-9.444444</td>\n",
       "      <td>-18.333333</td>\n",
       "      <td>-13.888889</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>10.000000</td>\n",
       "      <td>2.916667</td>\n",
       "      <td>6.666667</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>18.055556</td>\n",
       "      <td>8.888889</td>\n",
       "      <td>13.194444</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>27.222222</td>\n",
       "      <td>18.333333</td>\n",
       "      <td>23.055556</td>\n",
       "      <td>0.040000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>35.555556</td>\n",
       "      <td>27.222222</td>\n",
       "      <td>31.388889</td>\n",
       "      <td>2.310000</td>\n",
       "      <td>27.300000</td>\n",
       "      <td>22.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       maximum temperature  minimum temperature  average temperature  \\\n",
       "count           366.000000           366.000000           366.000000   \n",
       "mean             18.125379             9.892228            14.008804   \n",
       "std              10.023215             9.205971             9.513755   \n",
       "min              -9.444444           -18.333333           -13.888889   \n",
       "25%              10.000000             2.916667             6.666667   \n",
       "50%              18.055556             8.888889            13.194444   \n",
       "75%              27.222222            18.333333            23.055556   \n",
       "max              35.555556            27.222222            31.388889   \n",
       "\n",
       "       precipitation   snow fall  snow depth  \n",
       "count     366.000000  366.000000  366.000000  \n",
       "mean        0.115219    0.098361    0.275956  \n",
       "std         0.309682    1.441631    1.928253  \n",
       "min         0.000000    0.000000    0.000000  \n",
       "25%         0.000000    0.000000    0.000000  \n",
       "50%         0.000000    0.000000    0.000000  \n",
       "75%         0.040000    0.000000    0.000000  \n",
       "max         2.310000   27.300000   22.000000  "
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weather.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "5d35333b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>vendor_id</th>\n",
       "      <th>pickup_datetime</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>store_and_fwd_flag</th>\n",
       "      <th>trip_duration</th>\n",
       "      <th>maximum temperature</th>\n",
       "      <th>minimum temperature</th>\n",
       "      <th>average temperature</th>\n",
       "      <th>precipitation</th>\n",
       "      <th>snow fall</th>\n",
       "      <th>snow depth</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-14 17:24:55</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.982155</td>\n",
       "      <td>40.767937</td>\n",
       "      <td>-73.964630</td>\n",
       "      <td>40.765602</td>\n",
       "      <td>0</td>\n",
       "      <td>7.583333</td>\n",
       "      <td>10.555556</td>\n",
       "      <td>4.444444</td>\n",
       "      <td>7.5</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2016-03-14 14:05:39</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.975090</td>\n",
       "      <td>40.758766</td>\n",
       "      <td>-73.953201</td>\n",
       "      <td>40.765068</td>\n",
       "      <td>0</td>\n",
       "      <td>22.433333</td>\n",
       "      <td>10.555556</td>\n",
       "      <td>4.444444</td>\n",
       "      <td>7.5</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>2016-03-14 15:04:38</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.994484</td>\n",
       "      <td>40.745087</td>\n",
       "      <td>-73.998993</td>\n",
       "      <td>40.722710</td>\n",
       "      <td>0</td>\n",
       "      <td>11.583333</td>\n",
       "      <td>10.555556</td>\n",
       "      <td>4.444444</td>\n",
       "      <td>7.5</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-14 04:24:36</td>\n",
       "      <td>3</td>\n",
       "      <td>-73.944359</td>\n",
       "      <td>40.714489</td>\n",
       "      <td>-73.910530</td>\n",
       "      <td>40.709492</td>\n",
       "      <td>0</td>\n",
       "      <td>12.583333</td>\n",
       "      <td>10.555556</td>\n",
       "      <td>4.444444</td>\n",
       "      <td>7.5</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>2016-03-14 14:57:56</td>\n",
       "      <td>1</td>\n",
       "      <td>-73.952881</td>\n",
       "      <td>40.766468</td>\n",
       "      <td>-73.978630</td>\n",
       "      <td>40.761921</td>\n",
       "      <td>0</td>\n",
       "      <td>17.500000</td>\n",
       "      <td>10.555556</td>\n",
       "      <td>4.444444</td>\n",
       "      <td>7.5</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   vendor_id     pickup_datetime  passenger_count  pickup_longitude  \\\n",
       "0          2 2016-03-14 17:24:55                1        -73.982155   \n",
       "1          1 2016-03-14 14:05:39                1        -73.975090   \n",
       "2          1 2016-03-14 15:04:38                1        -73.994484   \n",
       "3          2 2016-03-14 04:24:36                3        -73.944359   \n",
       "4          2 2016-03-14 14:57:56                1        -73.952881   \n",
       "\n",
       "   pickup_latitude  dropoff_longitude  dropoff_latitude  store_and_fwd_flag  \\\n",
       "0        40.767937         -73.964630         40.765602                   0   \n",
       "1        40.758766         -73.953201         40.765068                   0   \n",
       "2        40.745087         -73.998993         40.722710                   0   \n",
       "3        40.714489         -73.910530         40.709492                   0   \n",
       "4        40.766468         -73.978630         40.761921                   0   \n",
       "\n",
       "   trip_duration  maximum temperature  minimum temperature  \\\n",
       "0       7.583333            10.555556             4.444444   \n",
       "1      22.433333            10.555556             4.444444   \n",
       "2      11.583333            10.555556             4.444444   \n",
       "3      12.583333            10.555556             4.444444   \n",
       "4      17.500000            10.555556             4.444444   \n",
       "\n",
       "   average temperature  precipitation  snow fall  snow depth  \n",
       "0                  7.5           0.29        0.0         0.0  \n",
       "1                  7.5           0.29        0.0         0.0  \n",
       "2                  7.5           0.29        0.0         0.0  \n",
       "3                  7.5           0.29        0.0         0.0  \n",
       "4                  7.5           0.29        0.0         0.0  "
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"date\"] = df[\"pickup_datetime\"].apply(lambda x : str(x.day) + \"-\" + str(x.month) + \"-\" + str(x.year))\n",
    "df = df.merge(weather, on = \"date\").drop([\"date\", \"dropoff_datetime\"], axis = 1)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66ef335b",
   "metadata": {},
   "source": [
    "# Сохранение данных и вывод о проделанной работе"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "693a4c48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Сохранение данных!\n",
      "Данные сохранены\n"
     ]
    }
   ],
   "source": [
    "print(\"Сохранение данных!\")\n",
    "df.to_csv(\"c1_result.csv\", index = False)\n",
    "print(\"Данные сохранены\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9d2c4453",
   "metadata": {},
   "source": [
    "### Вывод"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8818b6a2",
   "metadata": {},
   "source": [
    "- Обработаны пропуски во всех данных\n",
    "- Обработаны выбросы во всех данных\n",
    "- данные приведены к приемлемому формату\n",
    "- Объединены данные о всех поездаках и о погоде в том числе"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
