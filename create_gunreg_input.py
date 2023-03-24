import random as r

names = """Willie Banks
Allen Cummings
Guadalupe Pierce
Gary Jackson
Kristopher Gonzales
Damon Weber
Meghan Rose
Robert Little
Angelica Jennings
Leah Burns
Felipe Sharp
Gregory Jacobs
Marjorie Simon
Maria Lindsey
Jeff Gardner
Tanya Wade
Walter Flowers
Jeremiah Pratt
Norma Tucker
Spencer Gray
Nora Chavez
Tracy Osborne
Marianne Farmer
Donnie Salazar
Terri Alvarez
Jacqueline Sims
Randall Vargas
Alex Mann
Michael Higgins
Christina Dennis
Carrie Coleman
Laurie Warren
Hilda Paul
Raymond Boyd
Jerome Sullivan
Lorraine Romero
Wayne Lowe
Woodrow Mcdonald
Winston Thompson
Clyde Adkins
Kristin Obrien
Alexander Willis
Cesar Ball
Wallace Houston
Bryant Black
Natasha Moreno
Leslie Cunningham
Rosie Reynolds
Sonya Castillo
Geoffrey Clayton
Irma Erickson
Leslie Lucas
Eula Austin
Alejandro Nash
Tomas Hines
Beulah Abbott
Tasha Warner
Jodi Adams
Joyce Rice
Miguel Phillips
Dorothy Phelps
Debbie Nguyen
Kelley Moody
Shannon Hicks
Josephine Collins
Pablo Manning
Marguerite Mccarthy
Mathew Welch
Florence Griffith
Hannah Walker
Paul Goodwin
Claire Price
Celia Buchanan
Penny Daniels
Emily Fernandez
Myron Sherman
Malcolm Hill
Sophie Sparks
Tricia Roberson
Shaun Saunders
Wilson Benson
Nathaniel Bennett
Freddie Nunez
Owen Sutton
Edmund Potter
Pearl Walton
Angela Sanders
Dan Carlson
Marty Gutierrez
Shelly Tran
Renee Hanson
Preston Dawson
Winifred Carpenter
Javier Harper
Ronnie Green
Carla Valdez
Saul Roy
Gene King
Eduardo Rivera
Moses Newman
Willie Banks
Allen Cummings
Guadalupe Pierce
Gary Jackson
Kristopher Gonzales
Damon Weber
Meghan Rose
Robert Little
Angelica Jennings
Leah Burns
Felipe Sharp
Gregory Jacobs
Marjorie Simon
Maria Lindsey
Jeff Gardner
Tanya Wade
Walter Flowers
Jeremiah Pratt
Norma Tucker
Spencer Gray
Nora Chavez
Tracy Osborne
Marianne Farmer
Donnie Salazar
Terri Alvarez
Jacqueline Sims
Randall Vargas
Alex Mann
Michael Higgins
Christina Dennis
Carrie Coleman
Laurie Warren
Hilda Paul
Raymond Boyd
Jerome Sullivan
Lorraine Romero
Wayne Lowe
Woodrow Mcdonald
Winston Thompson
Clyde Adkins
Kristin Obrien
Alexander Willis
Cesar Ball
Wallace Houston
Bryant Black
Natasha Moreno
Leslie Cunningham
Rosie Reynolds
Sonya Castillo
Geoffrey Clayton
Irma Erickson
Leslie Lucas
Eula Austin
Alejandro Nash
Tomas Hines
Beulah Abbott
Tasha Warner
Jodi Adams
Joyce Rice
Miguel Phillips
Dorothy Phelps
Debbie Nguyen
Kelley Moody
Shannon Hicks
Josephine Collins
Pablo Manning
Marguerite Mccarthy
Mathew Welch
Florence Griffith
Hannah Walker
Paul Goodwin
Claire Price
Celia Buchanan
Penny Daniels
Emily Fernandez
Myron Sherman
Malcolm Hill
Sophie Sparks
Tricia Roberson
Shaun Saunders
Wilson Benson
Nathaniel Bennett
Freddie Nunez
Owen Sutton
Edmund Potter
Pearl Walton
Angela Sanders
Dan Carlson
Marty Gutierrez
Shelly Tran
Renee Hanson
Preston Dawson
Winifred Carpenter
Javier Harper
Ronnie Green
Carla Valdez
Saul Roy
Gene King
Eduardo Rivera
Moses Newman""".split()

guns = """2mm Kolibri
Akdal Ghost TR01
ALFA Combat
ALFA Defender
AMT AutoMag II
AMT AutoMag III
AMT AutoMag IV
AMT AutoMag V
AMT Backup
AMT Hardballer
AMT Lightning pistol
AMT Skipper
Armatix iP1
Arsenal Firearms AF1 "Strike One"
Arsenal P-M02
Ashani
ASP pistol
Astra 400
Astra 600
Astra Model 900
Astra Model 903
Astra A-60
Astra A-80
Astra A-100
AutoMag (pistol)
Ballester-Molina
Bauer Automatic
Bayard 1908
Bechowiec-1
Beholla pistol
Benelli B76
Benelli MP 90S
Benelli MP 95E
Beretta M9
Beretta 21A Bobcat
Beretta 70
Beretta 87 Target
Beretta 90two
Beretta 92
Beretta 92G-SD/96G-SD
Beretta 93R
Beretta 418
Beretta 950
Beretta 3032 Tomcat
Beretta 8000
Beretta 9000
Beretta Cheetah
Beretta M1915
Beretta M1923
Beretta M1934
Beretta M1935
Beretta M1951
Beretta Nano
Beretta Pico
Beretta Px4 Storm
Beretta U22 Neos
Berloque pistol
Bersa 83
Bersa Thunder 9
Bersa Thunder 380
Bergmann-Bayard pistol
BFD 1911
Bren Ten
Browning BDA
Browning BDM
Browning Buck Mark
Browning Hi-Power
Brügger & Thomet MP9
Brügger & Thomet TP380
BUL Cherokee
BUL M-5
BUL Storm
Calico M950
Campo Giro
Caracal pistol
Pistola Aut. Celmi
Charola-Anitua
Claridge Hi-Tec/Goncz Pistol
Colt Commander
Colt Delta Elite
Colt M1911
Colt Model 1903 Pocket Hammer
Colt Model 1903 Pocket Hammerless
Colt Mustang
Colt Officer's ACP
Colt OHWS
Colt SCAMP
ČZ vz. 27
ČZ vz. 38
ČZ vz. 45
ČZ vz. 50 / ČZ vz. 70
CZ 52
ČZ vz. 75
ČZ vz. 82 / CZ 83
CZ 85
CZ 97B
Zastava CZ 99
ČZ vz. 100
ČZ vz. 110
ČZ vz. 2075 RAMI
Daewoo Precision Industries K5
Danuvia VD-01
Dan Wesson M1911 ACP pistol
Davis Warner Infallible
Deer gun
Desert Eagle
Dreyse M1907
FB P-64
FÉG 37M Pistol
FEG PA-63
Fort 12
Fort-17
FN Baby Browning
FN M1900
FN Model 1903
FN M1905
FN Model 1910
FN Grand Browning
FN Model 1922
FN Forty-Nine
FN Five-seven
FN FNP
FN FNS
FN FNX
FN HiPer
FP-45 Liberator
Frommer Stop
Gaztañaga Destroyer
Glisenti Model 1910
Glock 17
Glock 18
Glock 19
Glock 19X
Glock 20
Glock 21
Glock 22
Glock 23
Glock 24
Glock 25
Glock 26
Glock 27
Glock 28
Glock 29
Glock 30
Glock 31
Glock 32
Glock 33
Glock 34
Glock 35
Glock 36
Glock 37
Glock 38
Glock 39
GMC pistol
Grebey automatic pistol
Grand Power K100
GSh-18
Guncrafter Industries Model No. 1
Gyrojet
Hamada Type pistol
Harper's Ferry Model 1805
Heckler & Koch HK4
Heckler & Koch HK45
Heckler & Koch MK23
Heckler & Koch P7
Heckler & Koch P9
Heckler & Koch P11
Heckler & Koch P30
Heckler & Koch P2000
Heckler & Koch VP9
Heckler & Koch MP7
Heckler & Koch UCP
Heckler & Koch USP
Heckler & Koch VP70
Heizer Defense PKO-45
Hi-Point C-9
Hi-Point CF-380
Hi-Point Model JCP
Hi-Point Model JHP
High Standard .22 Pistol
High Standard HDM
Horhe (pistol)
Howdah pistol
HS2000
Inam
INDUMIL Córdova
Inglis Hi-Power
Intratec TEC-22
Jennings J-22
JO.LO.AR.
Jericho 941
Jieffeco Model 1911
Kahr K series
Kahr MK series
Kahr P series
Kahr PM series
Kel-Tec P-3AT
Kel-Tec P-11
Kel-Tec P-32
Kel-Tec PF-9
Kel-Tec PLR-16
Kel-Tec PMR-30
Kimber Aegis
Kimber Custom
Kimber Custom TLE II
Kimber Eclipse
Kimel AP-9
KIS (weapon)
Komodo Armament P1-95
Kongsberg Colt
Korovin pistol
Krag-Jørgensen pistol
KRISS KARD
Lahti L-35
Lancaster pistol
Langenhan pistol
Le Français (pistol)
Lercker pistol
Lewis Automatic Pistol
Liliput pistol
Llama M82
Lebedev pistol
Luger pistol
M15 pistol
MAB Model A
MAB Model D
MAB PA-15 pistol
MAC Mle 1950
MAC-10
MAC-11
MAG-95
The Makarov
Makarych
Mamba Pistol
Mars Automatic Pistol
Mauser C96
Mauser HSc
MGP-15 submachine gun
Minebea PM-9
Minebea P9
Mitchell Alpha .45
Mk 1 Underwater Defense Gun
Modèle 1935 pistol
MOLOT pistol
MP-443 Grach
MP-444
M.R. M1911
Musgrave Pistol
NAACO Brigadier
Nambu Type 94 pistol
North China Type 19 Handgun
Obregón pistol
Ortgies Semi-Automatic Pistol
OTs-02 Kiparis
OTs-23 Drotik
OTs-33 Pernach
Oznobischev 1925
P9RC
P-83 Wanad
PAMAS modèle G1
Pantax pistol
Para-Ordnance P14-45
Pardini GT9
Phoenix pistol
Pindad G2
Pindad P3
Pindad PS-01
Pistol Auto 9mm 1A
Pistol model 2000
Pistol Carpați Md. 1974
Pistola Herval
Pistole vz. 22
PL-15 Lebedev
PP-2000
Prilutsky M1914
PSM pistol
PSS Silent Pistol
PB (pistol)
P-96
PLK
QSW-06
QSZ-92
Reiger 1889
Remington 1911 R1
Remington Model 51
Remington R51
Remington Rider Single Shot Pistol
Remington XP-100
Remington Zig-Zag Derringer
Revol Arms DL45
Rock Island Armory 1911 series
Rohrbaugh R9
Roth Steyr M1907
Ruby pistol
Ruger Hawkeye
Ruger LCP
Ruger LC9
Ruger MP9
Ruger P85
Ruger P89
Ruger P90
Ruger P95
Ruger P97
Ruger P345
Ruger SR series
Ruger SR1911
Ruger-57
SAC-46
SAR 9
Sarsılmaz Kılınç 2000[1]
Sauer 38H
Savage Model 1907
Schulhof 1887
Schwarzlose Model 1898
Schönberger-Laumann 1892
Semmerling LM4
Semmerling XLM
SIG P210
SIG P220
SIG P239
SIG P226
SIG P250 DCc
SIG P227
SIG P228
SIG P229
SIG P230
Škorpion vz. 61
Smith & Wesson Model 39
Smith & Wesson Model 59
Smith & Wesson Model 422
Smith & Wesson Model 1006
Smith & Wesson Model 5906
Smith & Wesson M&P
Smith & Wesson SW1911
SP-21 Barak
SPP-1 underwater pistol
SR-1 Vektor
Star Firestar M43
Star Model 14
Star Model S
Star Ultrastar
Stechkin APS
Steyr GB
Steyr M
Steyr TMP
Steyr Mannlicher M1901
Steyr M1912
Strąpoć pistol
Sugiura pistol
Tanfoglio Force
Tanfoglio GT27
Tanfoglio T95
Taurus PT92
Taurus PT 24/7
Taurus Millennium series
Taurus PT1911
TEC-9
TP-82 Cosmonaut survival pistol
TT pistol
Trejo pistol
Type 80 (pistol)
Type 14 Nambu
Type 64 pistol
Type 64 (silenced pistol)
Type 77 pistol
UZI
Vektor CP1
Vektor SP1
Viper Jaws pistol
Vis pistol
Volkspistole
VPO-514
W+F Bern P43
W+F Bern P47
Walther CCP
Walther HP
Walther Model 9
Walther P5
Walther P22
Walther P38
Walther P88
Walther P99
Walther PDP
Walther PP
Walther PK380
Walther PPK
Walther PPQ
Walther PPS
Walther TPH
Webley Self-Loading Pistol
Welrod
Werder pistol model 1869
Whitney Wolverine
Wildey
WIST-94
Z84
Zafar
Zaragoza Corla
Zastava P25
Zastava M57
Zastava M70 (pistol)
Zastava M88
Zastava PPZ
Zigana (pistol)[2]
9A-91
AAC Honey Badger
AAI ACR
ArmaLite AR-15
ArmaLite AR-18
ArmaLite AR-100
ACR
ADS
AEK-971
AG-043
AO-63 assault rifle
Automatkarbin 5
AK-9
AK12/AK200AK15AK19AK201, AK202, AK204AK203AK205
AK-47
AK-63
AK-74
AK-100 rifle familyAK-101AK-102AK-103AK-104AK-105
AK-107
AKM
AMD-65
AMP-69
AN-94
AM17AMB17
AO-27 rifle
AO-35 assault rifle
AO-38 assault rifle
AS-44
APS-95
APS underwater rifle
AS Val
ASM-DT amphibious rifle
Barrett REC7Barrett M468
Beretta AR70/90
Beretta ARX160
BSA 28P
BR18
Bushmaster M4 Type Carbine
Chropi rifle
CEAM Modèle 1950
CETME Model L
Close Quarters Battle Receiver
Colt ACR
Diemaco C7Diemaco C8
Colt CM901
CZ 805 BREN/ CZ 805 BREN 2
ČZ 2000
Daewoo K1Daewoo K2
Dasan Machineries K16
Desert Tech MDR
Desarrollos Industriales Casanave SC-2005
Dlugov assault rifle
EM-2 rifle
Excalibur rifle
EMER K1
Fateh
FAMAS
FARA 83
FB Beryl
FB MSBS
FB Tantal
CAL
F2000
FNC
SCAR
FX-05 Xiuhcoatl
Galil Córdova
Grad AR
Grossfuss Sturmgewehr
G11
G36G36K
G41
HK33
HK36
HK416M27 Infantry Automatic Rifle
HK433
Type 20
Type 89
VHS
MD97
IA2
T4
Galil
Tavor TAR21
IWI Tavor X95
Ingram FBM
INSAS rifle[6]
Interdynamics MKS
IWI ACE
KH-2002 Khaybar
Kbkg wz. 1960
KORD 6P67
Komodo Armament D5
L64/65
SA80
Leader Dynamics Series T2 MK5
LR-300
LSAT rifle
LWRC M6
LWRC M4
Automatic AR15, M16 & M4 VariantsCAR-15 XM177M16M4/M4A1Colt Advanced Piston CarbineM4 Commando
MPT-55
Masaf rifle
M4-WAC-47
MK 556
Multi Caliber Individual Weapon System
Nesterov assault rifle
Norinco CQ
OTs-12 Tiss
OTs-14 Groza
Pindad SS1
Pindad SS2
Pistol Mitralieră model 1963/1965
Pușcă Automată model 1986
PVAR rifle
QBZ-95
QBZ-03
QTS-11
QBZ-191
Remington R4
Remington R5 RGP
Rk 62
Rk 95 TP
Robinson Armament XCR
RS556
SEAL Recon Rifle
S&T Daewoo K11
Sa vz. 58
SAR 80
SAR-21
SIG MCXSIG XM5 NGSW
SIG Sauer SIG516
SIG SG 530
SG540/SG543
SIG550SIG551
SOCIMI AR-831
Special Operations Assault Rifle
SR-3 Vikhr
SR-47
SR 88
Sterling SAR-87
Steyr AUG
Steyr ACR
Steyr STM 556
STV series rifle
STL-1A
Stoner 63
Sturmgewehr 44
StG 45(M)
T65 assault rifle
T86 assault rifle
T91 assault rifle
Thales NGSW
TKB-072
TKB-517
Type 56 assault rifle
Type 63 assault rifle
Type 81 assault rifle
Type 58 assault rifle
Type 88 assault rifleType 98 assault rifle
Norinco Type 86S
VAHAN
Valmet M76
Valmet M82
VB Berapi LP06
Vektor CR-21
Vektor R4
Vepr
Malyuk
W+F Stgw 70
W+F Stgw 71
Wieger StG-940
Wimmersperg Spz
XM8 rifle
XT-97 Assault Rifle
XM29 OICW
Zastava M21
Zastava M70
Zastava M80
Zastava M90
Apache revolver
Astra 680

Beaumont-Adams revolver
Beretta Laramie
Beretta Stampede
Bodeo Model 1889
Bossu Revolver
Charter Arms Bulldog
Chiappa Rhino
Collier flintlock revolver
Colombo-Ricci revolver
Colt 1851 Navy Revolver
Colt 1861 Navy Revolver
Colt Anaconda
Colt Army Model 1860
Colt Buntline
Colt Cobra
Colt Detective Special
Colt Diamondback
Colt Dragoon
Colt House Revolver
Colt Cloverleaf
Colt King Cobra
Colt M1877
Colt M1878
Colt M1889
Colt M1892
Colt Model 1905 Marine Corps
Colt Model 1849 Pocket Revolver
Colt Model 1855 Sidehammer Pocket Revolver
Colt Model 1862 Pocket Police
Colt Model 1871-72 Open Top
Colt New Line
Colt New Police Revolver
Colt New Service
Colt Open Top Pocket Model Revolver
Colt Official Police
Colt Paterson
Colt Police Positive
Colt Police Positive Special
Colt Python
Colt Trooper Mk. III
Colt Single Action Army
Colt Trooper
Colt Walker
Dan Wesson Model 715
Enfield Mk II
Enfield No. 2
FAMAE revolver
FN Barracuda
Freedom Arms Model 83 .500 WE
"Frontier Bulldog
(copy of Webley RIC)"
Galand Velo-dog
Garcia-Reynoso revolver
Gward revolver
IOF .22 revolver
JTL-E .500 S&W Magnum 12"
MP-412 REX
Kerr's Patent Revolver
Korth Combat
Type 26 revolver
Landstad revolver
Lefaucheux M1858
LeMat Revolver
M1879 Reichsrevolver
Gasser M1870
M1917 revolver
Magnum Research BFR
Manurhin MR 73
MAS 1873 revolver Chamelot-Delvigne
Mateba Autorevolver
Mauser Zig-Zag
MIL Thunder 5
Modèle 1892 revolver
Nagant M1895
Nagant wz. 30
New Nambu M60
NRP9 Police Revolver
OTs-01 Kobalt
OTs-20 Gnom
OTs-38 Stechkin silent revolver
Pfeifer Zeliska .600 Nitro Express revolver
Pindad R1
Medusa Model 47
Pirlot Frères Ordonnanzrevolver 1872
Rast & Gasser M1898
Remington Model 1858
Remington Model 1875
Remington Model 1890
M1879 and M1883 Reichsrevolver
Röhm RG-14
Rossi Model 971
RSh-12
Ruger Alaskan
Ruger Bearcat
Ruger Bisley
Ruger Blackhawk
Ruger GP100
Ruger LCR
Ruger Redhawk
Ruger Security Six
Ruger Single-Six
Ruger SP101
Ruger Super Redhawk
Ruger Vaquero
S333 Thunderstruck
Schmidt M1882
"Smith & Wesson Model 2
S&W .38 Single Action"
Smith & Wesson .38/44
Smith & Wesson Bodyguard
Smith & Wesson Centennial
Smith & Wesson Governor
Smith & Wesson Ladysmith (M-frame)
Smith & Wesson Model 1
Smith & Wesson Model 1 1/2
Smith & Wesson Model No. 2 Army
Smith & Wesson Model 3
Smith & Wesson Model 10
Smith & Wesson Model 12
Smith & Wesson Model 13
Smith & Wesson Model 14
Smith & Wesson Model 15
Smith & Wesson Model 17
Smith & Wesson Model 617
Smith & Wesson Model 19
Smith & Wesson Model 22
Smith & Wesson Model 27
Smith & Wesson Model 28
Smith & Wesson Model 29
Smith & Wesson Model 317 kit gun
Smith & Wesson Model 36
Smith & Wesson Model 327PD
Smith & Wesson Model 340PD
Smith & Wesson Model 460XVR
Smith & Wesson Model 500
Smith & Wesson Model 586
Smith & Wesson Model 57
Smith & Wesson Model 60
Smith & Wesson Model 64
Smith & Wesson Model 66
Smith & Wesson Model 67
Smith & Wesson Model 386
Smith & Wesson Model 625
Smith & Wesson Model 686
Smith & Wesson Safety Hammerless
Smith & Wesson Triple Lock
Starr revolver
Sterling Revolver
Swiss mini gun
"Taurus Judge
Taurus Public Defender"
Taurus Raging Judge
Taurus Model 605
Taurus Model 608
Taurus Model 617
Taurus Model 731
Taurus Model 82
Taurus Model 85
Tranter (revolver)
Udar revolver
Ultimate 500
Union Automatic Revolver
British Bull Dog revolver
Webley RIC
Webley Revolver
Webley-Fosbery Automatic Revolver

Zulaica Automatic Revolver
7,62 ITKK 31 VKT
AA-52
UP 7.62
HP 7.62
AEK-999
Agar gun
Ares Shrike 5.56
Bailey machine gun
Barnitzke machine gun
Beretta AS70/90
Berezin UB
Bergmann MG 15nA machine gun
Besa machine gun
Besal
Breda 30
Breda 38
Breda M37
Breda Mod. 5C
Breda-SAFAT machine gun
Bren light machine gun
Browning wz.1928
CETME Ameli
Charlton Automatic Rifle
Chauchat
STK 50MG
Ckm wz. 30
Colt Machine Gun
Colt Automatic Rifle
Daewoo K3
Darne machine gun
Degtyaryov machine gun
DShK
Dror light machine gun
DS-39
EMER-K1 LMG
EPK (Pyrkal) Machine gun
Fallschirmjager 42
Fiat-Revelli Modello 1914
Fiat-Revelli Modello 1935
Fittipaldi machine gun
FM 24/29 light machine gun
FN Minimi
FN BRG-15
FN MAG
Fokker-Leimberger
Furrer M25
Gatling gun
GAU-19
Gorgas machine gun
Heckler & Koch HK21HK25
Heckler & Koch MG4
Heckler & Koch MG5
HMG PK-16
Ho-103
"Hotchkiss M1909
Benét-Mercié"
Hotchkiss M1914 machine gun
Hotchkiss M1922 machine gun
Hotchkiss M1929 machine gun
Huot Automatic Rifle
IMI Negev
IP-2
In-Line
INSAS LMG
Kbkm wz. 2003
Kg m/40 light machine gun
Kk 62
Knight's Armament Company LMG
Kord machine gun
KPV heavy machine gun
Kulspruta m/39
Kulspruta m/42
L86 LSW
Lahti-Saloranta M/26
Lewis gun
LSAT light machine gun
M2 Browning
M27 IAR
M60
M73
M85
M134 Minigun
M240 Medium Machine Gun
M249 Machine Gun
M1895 Colt-Browning
M1917 Browning
M1918 Browning
M1919 Browning
M1921 Browning
M1926
M1941 Johnson
MAC-58
MAC 1931
MAC 1934
Madsen machine gun
Madsen-Saetter machine gun
Mark 48 machine gun
Maxim gun
Maxim-Tokarev
McCrudden light machine rifle
Mendoza C-1934
Mendoza RM2
MG 08
MG 11
MG 13
MG 15
MG 17 machine gun
MG 30
Maschinengewehr 34
MG 39 Rh
Maschinengewehr 42
Maschinengewehr 1945
Maschinengewehr 1951
MG 81
MG 131
Mini-SS
Nikonov machine gun
NSV machine gun
Parabellum MG 14
Perino Model 1908
Pindad SM-2
Pindad SM-3
Pindad SM-5
PKPKP Pecheneg
PM M1910
PMT-76
Puteaux APX Machine Gun
QBB-95
QJY-88
Rheinmetall MG 3
Rheinmetall MG 60
Rheinmetall RMG.50
Rolls-Royce Experimental Machine Gun
RPD
RPKRPK74
RPK16
RPL-20
S&T Motiv K12
Salvator-Dormus M1893
Schwarzlose MG M.07/12
SG-43 Goryunov
SIG MG 710-3
Sterling 7.62
St. Étienne Mle 1907
Stoner 63/63A Light Machine Gun
Sumitomo Type 62
Sumitomo Minimi
SureFire MGX
T24 machine gun
Taden gun
Type 1 heavy machine gun
Type 2 machine gun
Type 3 heavy machine gun
Type 11 light machine gun
Type 67 machine gun
Type 77 heavy machine gun
Type 80 machine gun
Type 81 squad machine gun
Type 85 heavy machine gun
Type 89 fixed aircraft machine gun
Type 89 machine gun flexible type
Type 90 machine gun
Type 92 machine gun
Type 92 heavy machine gun
Type 93 heavy machine gun
Type 96 light machine gun
Type 97 light machine gun
Type 97 aircraft machine gun
Type 99 light machine gun
UKM-2000
Ultimax 100
Uk vz. 59
Vektor SS-77
Vickers .50 machine gun
Vickers-Berthier
Vickers K machine gun (VGO)
Vickers machine gun
VMG 1927
W85 heavy machine gun
Weibel M/1932
XM133 Minigun
XM250 Next Generation Machine Gun
"XM312
(Cancelled project)[4]"
"XM806
(Cancelled project)"
Zastava M02 Coyote
Zastava M72
Zastava M77
Zastava M84
Zastava M87
ZB-50
ZB-60
ZB-53
ZB vz. 26
ZB vz. 30
Akdal MKA 1919
Armsel Striker
Atchisson Assault Shotgun
Baikal MP-153
Bandayevsky RB-12
Benelli M1
Benelli M3
Benelli M1014
Benelli Nova
Benelli Raffaello
Benelli Supernova
Benelli Vinci
Beretta 682
Beretta 1201FP
Beretta A303
Beretta AL391
Beretta DT-10
Beretta Silver Pigeon
Beretta Xtrema 2
Blaser F3
Browning Auto-5
Browning BSS
Browning Citori
Browning Double Automatic Shotgun
Browning Superposed
Ciener Ultimate Over/Under
Cooey 84
Cynergy Shotgun
ENARM Pentagun
Fabarm SDASS Tactical
FN SLP
FN TPS
FN SC-1
Franchi AL-48
Franchi Special Purpose Shotgun 12
Franchi SPAS-15
H&R Ultraslug Hunter
Hawk Industries Type 97
FABARM FP6
Heckler & Koch HK CAWS
High Standard Model 10
Ithaca 37
Ithaca Mag-10
KAC Masterkey
Kel-Tec KSG
KS-23
KUGS HD410
M26 Modular Accessory Shotgun System
M1216
MAG-7
Marlin Model 55
MAUL (shotgun)
Molot Bekas-M
Mossberg 500
Mossberg 590
Mossberg 930
MTs-255
NeoStead 2000
Norinco HP9-1
Pancor Jackhammer
Pindad SG-1
Remington Model 10
Remington Model 11
Remington Model 11-48
Remington Model 11-87
Remington Model 17
Remington Model 31
Remington Model 58
Remington Model 870
Remington Model 878
Remington Model 887
Remington Model 1100
Remington Model SP-10
Remington Spartan 100
Remington Spartan 310
Remington Spartan 453
RGA-86
RMB-93
Ruger Gold Label
Saiga-12
Sjögren shotgun
Snake Charmer
Stevens Model 520/620
Stoeger Coach Gun
Stoeger Condor
TOZ-106
TOZ-194
USAS-12
UTS-15
Valtro PM-5/PM-5-350
Vepr-12
Weatherby Orion
Weatherby SA-08
Winchester Model 20
Winchester Model 21
Winchester Model 37
Winchester Model 1200
Winchester Model 1887/1901
Winchester Model 1897
Winchester Model 1911
Winchester Model 1912
Accuracy International Arctic Warfare (L96A1)
Accuracy International Arctic Warfare Magnum
Accuracy International AW50
Accuracy International AS50
Accuracy International AX50
Anzio 20mm rifle
AR10T
Armalite AR-50
Barrett 50 Cal/M82/M107
Barrett M90
Barrett M95
Barrett M98B
Barrett M99
Barrett MRAD
Barrett XM109
Barrett XM500
Blaser 93 Tactical
Dragunov SVD
Dragunov SVU
DSR-1
GOL Sniper Magnum
G28M110A1 CSASS/M110E1
KSVK 12.7
Modular Sniper Rifle
M2010 Enhanced Sniper Rifle
M1903 Springfield
M1C/M1D Garand
Krag-Jørgensen
Karabiner 98k
Mosin-Nagant
M38 DMR
SVDK
Orsis T-5000
SV-98
VSS Vintorez
Savage 10FP
Savage 110 BA
VSK-94
SR-25
CheyTac Intervention
Tango 51
M110 Sniper Rifle
M21
M24
M25
M39 Enhanced DMR
MK 13
Mk 14 Enhanced Battle Rifle
Desert Tech SRS
FN Ballista
United States Marine Corps DMR
Squad Advanced Marksman Rifle
Brügger & Thomet APR308
Yirtiji 7.62
C14 Timberwolf
Diemaco C20 DMR
Crazy Horse rifle
RT-20
Cyclone
Steyr Scout
CZ 700
Bor rifle
IWI Dan
Denel NTW-20
D7CH
Rifle, No 4 (T)
ZVI Falcon
FN FNAR
FN Model 30-11
FN Special Police Rifle
FN Tactical Sport Rifle
FR F1
FN Model 30-11
FR F2 sniper rifle
Pattern 1914 Enfield
Gewehr 98
G3SG1
H-S Precision Pro Series 2000 HTR
Harris Gun Works M-96
Haskins Rifle
PSG1MSG90
Howa M1500
Istiglal Anti-Materiel Rifle
JS 7.62
Kalekalıp KNT-308
Kefefs
L42A1
Light Sniper Rifle
Longbow T-76
7.62 Tkiv 85
M40 rifle
M89SR
Mauser M59
Mauser M67
McMillan Tac-50
AMR-2
JNG-90
Alejandro Sniper Rifle
Azb DMR MK1
Blaser R93
Marine Scout Sniper Rifle
OSV-96
M82
Parker-Hale M85
PDSHP
PSR-90
Pindad SPR
PGM 338
PGM Hecate II
PGM Ultima Ratio
Puşca Semiautomată cu Lunetă
QBU-10
QBU-88
Remington SR-8
Robar RC-50
S&T Motiv K14
Sako TRG-42
C21 Sako TRG M10 Sniper Weapon System
Satevari MSWP
SC-76 Thunderbolt
SEAL Recon Rifle
Shaher
SIG550 Sniper
SIG Sauer SSG 2000
SIG Sauer SSG 3000
Siyavash
FN SCAR
Solothurn S-18/100
Steyr SSG 08
SSG 82
Steyr HS .50
Steyr SSG 69
Steyr IWS 2000
Lee-Enfield
K31
T-12
T93
Tabuk Sniper Rifle
Taher
TPG-1
Type 97 Sniper Rifle
Type 99 sniper rifle
Squad Designated Marksman Rifle
Snipex T-Rex
Snipex Alligator
Mk 12 Special Purpose Rifle
Våpensmia NM149
Vidhwansak
VSSK Vykhlop
Walther WA 2000
WKW Wilk
Yalguzag
Zastava M07
Zastava M12 Black Spear
Zastava M76
Zastava M91
Zastava M93 Black Arrow""".split('\n')

def rand_phone_number():
    phone_number = "("
    for i in range(11):
        if i == 3:
            phone_number += ")"
        if i == 6:
            phone_number += "-"
        phone_number += str(r.randint(0, 9))
    
    return phone_number

# queries = ["sg", "sl", "i ", "d "]

query_count = int(input())

county_count = 10

highest_unused_serial_number = 0

f = open("input.txt", 'w')

f.write(str(county_count)+"\n")

query_info_list = []

for i in range(query_count):
    f.write("i \n")
    county_idx = str(r.randint(0, county_count-1))+"\n"
    f.write(county_idx)
    first_name = names[r.randint(0, len(names)-1)]+"\n"
    f.write(first_name)
    last_name = names[r.randint(0, len(names)-1)]+"\n"
    f.write(last_name)
    reg_num = str(r.randint(0, 10000))+"\n"
    f.write(reg_num)
    phone_num = rand_phone_number() + "\n"
    f.write(phone_num)
    serial_num = str(highest_unused_serial_number)+"\n"
    highest_unused_serial_number += 1
    f.write(serial_num)
    gun_model = guns[r.randint(0, len(guns)-1)]+"\n"
    f.write(gun_model)
    query_info_list.append([county_idx, first_name, last_name, str(reg_num), phone_num, serial_num, gun_model])

for query_info in query_info_list:
    # UPDATE
    # f.write("d \n")
    # for info in query_info:
    #     f.write(info)
    
    # SEARCH GLOBAL
    # f.write("sg\n")
    # f.write(query_info[5])
    
    # SEARCH LOCAL
    # f.write("sl\n")
    # f.write(query_info[0])
    # f.write(query_info[5])
    pass

# UPDATE
# i_or_d = r.randint(0, 1)
# if i_or_d == 0:
#     query = query_info_list[r.randint(0, query_count-1)]
#     f.write("d \n")
#     for i in range(7):
#         f.write(query[i])
# else:
#     f.write("i \n")
#     county_idx = str(r.randint(0, county_count-1))+"\n"
#     f.write(county_idx)
#     first_name = names[r.randint(0, len(names)-1)]+"\n"
#     f.write(first_name)
#     last_name = names[r.randint(0, len(names)-1)]+"\n"
#     f.write(last_name)
#     reg_num = str(r.randint(0, 10000))+"\n"
#     f.write(reg_num)
#     phone_num = rand_phone_number() + "\n"
#     f.write(phone_num)
#     serial_num = str(highest_unused_serial_number)+"\n"
#     highest_unused_serial_number += 1
#     f.write(serial_num)
#     gun_model = guns[r.randint(0, len(guns)-1)]+"\n"
#     f.write(gun_model)

# SEARCH GLOBAL
f.write("sg\n")
serial_num = query_info_list[0][5] # r.randint(0, query_count-1)][5]
f.write(serial_num)

# SEARCH LOCAL
# f.write("sl\n")
# query_idx = r.randint(0, query_count-1)
# county_idx = query_info_list[query_idx][0]
# serial_num = query_info_list[query_idx][5]
# f.write(county_idx)
# f.write(serial_num)
        
f.write('q')

f.close()
    
    