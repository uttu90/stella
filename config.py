rainfallConfig = {
    'I_UseSpatVarRain?': 0,
    'I_RainMultiplier': 1,
    'I_RainCycle?': 0,
    'I_Rain_IntensMean': 10,
    'I_Rain_IntensCoefVar': 0.3,
    'I_Rain_GenSeed': 200
}

I_GWRelFracConst = 0.01
I_GWRelFracConst_ = 0
I_InitRelGW = 1
I_InitRelSoil = 1
I_DaminThisStream_ = 0
I_EvapotransMethod = 1
I_InterceptEffectonTransp = 0.1
I_MaxDynGWConst = 100
I_MaxInf = 700
I_MaxInfSSoil = 150
I_PercFracMultiplier = 0.05
I_PowerInfiltRed = 3.5
I_RiverflowDispersalFactor = 0.6
I_RoutVeloc_m_per_s = 0.55
I_SoilPropConst_ = 0
I_Tortuosity = 0.6
I_SoilSatMinFCConst = 100
I_SurfLossFrac = 0
L_LakeTranspMultiplier = 1
L_ResrDepth = 10000
I_AvailWaterConst = 0


# SUBCATCHMENT = 20
FOURYEARS = 1460
LANDCOVERTYPE = 20
# OBSPOINT = 8
MONTH = 12
dt = 1

LANDCOVER = {}
LANDCOVER["hutan_primer"] = 1
LANDCOVER["Hutan_sekunder_kerapatan_tinggi"] = 2
LANDCOVER["hutan_sekunder_kerapatan_rendah"] = 3
LANDCOVER["lahan_basah"] = 4
LANDCOVER["AF_Kelapa"] = 5
LANDCOVER["AF_Coklat"] = 6
LANDCOVER["Kebun_campur"] = 7
LANDCOVER["Hutan_pinus"] = 8
LANDCOVER["Hutan_Jati"] = 9
LANDCOVER["Perkebunan_Kelapa"] = 10
LANDCOVER["Perkebunan_Coklat"] = 11
LANDCOVER["perkebunan_kelapa_sawit"] = 12
LANDCOVER["perkebunan_jambu_mete"] = 13
LANDCOVER["perkebunan_cengkeh"] = 14
LANDCOVER["belukar"] = 15
LANDCOVER["persawahan"] = 16
LANDCOVER["crop"] = 17
LANDCOVER["padang_rumput"] = 18
LANDCOVER["lahan_terbuka"] = 19
LANDCOVER["pemukiman"] = 20

# A matrix with [Subcatchement, VegClass] will be a normal matrix
# A matrix with [VegClass, Subcatchement] will be a transpose matrix
# Subcatchement will role as a row
# VegClass will role as a column
# Add, Multiply, Divide w


YEARS = range(1975, 2001)
VEGCLASS = ['hutan_primer', 'Hutan_sekunder_kerapatan_tinggi', 'hutan_sekunder_kerapatan_rendah',
            'lahan_basah', 'AF_Kelapa', 'AF_Coklat', 'Kebun_campur', 'Hutan_pinus',
            'Hutan_Jati', 'Perkebunan_Kelapa', 'Perkebunan_Coklat', 'perkebunan_kelapa_sawit',
            'perkebunan_jambu_mete', 'perkebunan_cengkeh', 'belukar',
            'persawahan', 'crop', 'padang_rumput', 'lahan_terbuka', 'pemukiman']
SUBCATCHMENT = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T']
MEASUREPERIOD = range(1, 4)
OBSPOINT = ['Inflowlake', 'obs_1', 'obs_2', 'obs_3', 'obs_4', 'obs_5', 'obs_6', 'obs_7']
PATCH = range(1, 101)
INPUTDATAYEAR = ['Start', 'Trans1', 'Trans2', 'End']
LANDCOVERSUBCATCHM = [subcatch + vegclass for subcatch in SUBCATCHMENT for vegclass in VEGCLASS]
OBSPOINT1 = ['Outflow', 2, 3, 4, 5]
