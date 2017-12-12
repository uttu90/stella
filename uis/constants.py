
subcatchmentName = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T] = range(20)

landcoverName = [
    'hutan_primer',
    'Hutan_sekunder_kerapatan_tinggi',
    'hutan_sekunder_kerapatan_rendah',
    'lahan_basah',
    'AF_Kelapa',
    'AF_Coklat',
    'Kebun_campur',
    'Hutan_pinus',
    'Hutan_Jati',
    'Perkebunan_Kelapa',
    'Perkebunan_Coklat',
    'perkebunan_kelapa_sawit',
    'perkebunan_jambu_mete',
    'perkebunan_cengkeh',
    'belukar',
    'persawahan',
    'crop',
    'padang_rumput',
    'lahan_terbuka',
    'pemukiman',
]

[
    hutan_primer,
    Hutan_sekunder_kerapatan_tinggi,
    hutan_sekunder_kerapatan_rendah,
    lahan_basah,
    AF_Kelapa,
    AF_Coklat,
    Kebun_campur,
    Hutan_pinus,
    Hutan_Jati,
    Perkebunan_Kelapa,
    Perkebunan_Coklat,
    perkebunan_kelapa_sawit,
    perkebunan_jambu_mete,
    perkebunan_cengkeh,
    belukar,
    persawahan,
    crop,
    padang_rumput,
    lahan_terbuka,
    pemukiman
] = range(20)

[Start, Trans1, Trans2, End] = range(4)

[Inflowlake, obs_1, obs_2, obs_3, obs_4, obs_5, obs_6, obs_7] = range(8)
outputMapsSubcatchment = [
    'Landcover',
    'L_InFlowtoLake',
    'O_EvapoTransAcc',
    'O_PercAcc',
    'O_RainAcc',
    'O_SurfQFlowAcc',
    'O_BaseFlowAcc',
    'O_DeepInfAcc',
    'O_IntercAcc',
    'O_SoilQFlowAcc',
    'O_InfAcc',
    'D_GWaDisch',
    'D_SoilDischarge'
]

ouputTimeSeries = [
    'I_RFlowdata_mmday',
    'L_InFlowtoLake',
    'O_RainAcc',
    'O_IntercAcc',
    'O_EvapoTransAcc',
    'O_SurfQFlowAcc',
    'O_InfAcc',
    # 'O_RainAcc'
    'O_DeepInfAcc',
    'O_PercAcc',
    'O_BaseFlowAcc',
    'O_SoilQFlowAcc',
    'O_CumRain',
    'O_CumIntercepEvap',
    'O_CumEvapotrans',
    'O_CumSurfQFlow',
    'O_CumInfiltration',
    # 'O_CumRain'
    'O_CumPercolation',
    'O_CumDeepInfilt',
    'O_CumBaseFlow',
    'O_CumSoilQFlow',
    'L_HEPPWatUseFlow',
    'L_LakeVol',
    'L_HEPP_Kwh',
    'L_LakeLevel'
]

outputMap = [
    'O_EvapoTransAcc',
    'L_InFlowtoLake',
    'O_PercAcc',
    'O_RainAcc',
    'O_SurfQFlowAcc',
    'O_BaseFlowAcc',
    'O_DeepInfAcc',
    'O_IntercAcc',
    'O_SoilQFlowAcc',
    'O_InfAcc',
    'D_GWaDisch',
    'D_SoilDischarge',
]

subcatchmentTicks = range(0, 20)
landCoverTicks = range(0, 20)
