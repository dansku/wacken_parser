# Wacken 2018 Parser

![Wacken Logo](wacken_logo.png)

Python script to parse the list of bands for the metal festival Wacken 2018 and output a json file with the listing.

Output example:

```
[  
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1262/",
      "baneName":"Amorphis",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_9zze9gxp7w_8b2e12276d.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1263/",
      "baneName":"Arch Enemy",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_n9e8tzubxm_0d6ffa6898.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1264/",
      "baneName":"Bannkreis",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_xxzaywdkx9_65bc20cdf4.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1265/",
      "baneName":"Belphegor",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_e8rd8fekps_1fd0b4da58.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1266/",
      "baneName":"Deserted Fear",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_2hqfryjxqt_1807fe2dfd.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1267/",
      "baneName":"Dirkschneider",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_krsi78a4tm_c7484689e0.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1268/",
      "baneName":"Doro",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_v49rriww3k_6cb4727e94.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1269/",
      "baneName":"Epica",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_srgi3n5wae_8e8328736a.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1270/",
      "baneName":"Firewind",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_jlxruguxd5_4175ec3474.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1271/",
      "baneName":"In Extremo",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_yl4a2iqrut_4d2dff38aa.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1272/",
      "baneName":"Knorkator",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_9xyruh9y9i_c9203bff1f.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1273/",
      "baneName":"Nightwish",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_9q7fdvcscw_3b41a7b8f1.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1274/",
      "baneName":"Running Wild",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_rrcpaj785h_40b40061b3.png"
   },
   {  
      "bandAddedOn":"06.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1275/",
      "baneName":"Sepultura",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_e9s9nfwpll_e6c4e26987.png"
   },
   {  
      "bandAddedOn":"07.08.2017",
      "bandUrl":"http://www.wacken.com/en/bands/bands-billing/bands-billing/1276/",
      "baneName":"Watain",
      "bandImage":"http://www.wacken.com/typo3temp/_processed_/csm_j72e6e4acb_d8bb2405ec.png"
   }
]
```