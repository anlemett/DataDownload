#TMA_timezone = "Europe/Stockholm"

#airport_icao = "ESSA"

TMA_lon=[18.2130555555556, 18.5547222222222, 18.8469444444444, 19.3136111111111, 19.8280555555556, 19.2736111111111,
          18.9683333333333, 18.7547222222222, 18.5394444444444, 18.4572222222222, 17.9327777777778, 17.4569444444444,
          17.4077777777778, 17.2233333333333, 16.7077777777778, 16.2677777777778, 16.3183333333333, 16.4466666666667,
          17.5966666666667, 18.2130555555556];

TMA_lat=[60.2994444444444, 60.2661111111111, 59.8827777777778, 60.0352777777778, 59.6736111111111, 59.5994444444444,
          59.255, 59.0419444444444, 58.8325, 58.7525, 58.5830555555556, 58.6163888888889, 58.9661111111111,
          58.9786111111111, 59.0119444444444, 59.0494444444444, 59.3238888888889, 59.7494444444444, 60.2327777777778,
          60.2994444444444];

# Runway 01R
central_lat = 59.64
central_lon = 17.95

#central_lat = min(TMA_lat) + (max(TMA_lat)-min(TMA_lat))/2
#central_lon = min(TMA_lon) + (max(TMA_lon)-min(TMA_lon))/2

number_of_rwys = 4

# Runway 08/26
rwy1_lon=[17.9361345, 17.9791531944444];
rwy1_lat=[59.6584189166667, 59.6638971944444 ];

# Runway 01L/19R
rwy2_lon=[17.9132249722222, 17.9237679722222];
rwy2_lat=[59.637256, 59.6664016944444 ];

# Runway 01R/19L
rwy3_lon=[17.9507426111111, 17.9587480555556];
rwy3_lat=[59.6263963888889, 59.6484673055556];

# Bromma
rwy4_lon=[17.9296420277778, 17.9536581388889];
rwy4_lat=[59.3586702777778, 59.3500752777778];

ELTOK_lon = 16.6503
ELTOK_lat = 59.5861
HMR_lon = 18.3917
HMR_lat = 60.2794
XILAN_lon = 19.0761
XILAN_lat = 59.6594
NILUG_lon = 17.8847
NILUG_lat = 58.8158

# STARs
#ELTOK, SA865, ERK
ELTOK_STAR_1_lat = [ELTOK_lat, 59.51435, 59.53465]
ELTOK_STAR_1_lon = [ELTOK_lon, 17.39467, 18.20129]

#ELTOK, SA821, BALVI
ELTOK_STAR_2_lat = [ELTOK_lat, 59.50231, 59.4445]
ELTOK_STAR_2_lon = [ELTOK_lon, 17.15217, 17.3525]

#ELTOK, SA820, SA854, LNA
ELTOK_STAR_3_lat = [ELTOK_lat, 59.47262, 59.41472, 59.32203]
ELTOK_STAR_3_lon = [ELTOK_lon, 17.10353, 17.14413, 17.21301]


#HMR, SA541, ERK
HMR_STAR_1_lat = [HMR_lat, 60.05051, 59.53465]
HMR_STAR_1_lon = [HMR_lon, 18.21491, 18.20129]


#HMR, SA539, SA540, TEB
HMR_STAR_2_lat = [HMR_lat, 60.00597, 59.44522, 59.31541]
HMR_STAR_2_lon = [HMR_lon, 18.22111, 18.20523, 18.12119]


#NILUG, SA630, TEB
NILUG_STAR_1_lat = [NILUG_lat, 59.05516, 59.31541]
NILUG_STAR_1_lon = [NILUG_lon, 18.09073, 18.12119]


#NILUG, SA630, TEB, ERK
NILUG_STAR_2_lat = [NILUG_lat, 59.05516, 59.31541, 59.53465]
NILUG_STAR_2_lon = [NILUG_lon, 18.09073, 18.12119, 18.20129]


#XILAN, SA570, TEB
XILAN_STAR_1_lat = [XILAN_lat, 59.3616, 59.31541]
XILAN_STAR_1_lon = [XILAN_lon, 18.41423, 18.12119]


#XILAN, SA570, TEB, ERK
XILAN_STAR_2_lat = [XILAN_lat, 59.3616, 59.31541, 59.53465]
XILAN_STAR_2_lon = [XILAN_lon, 18.41423, 18.12119, 18.20129]
