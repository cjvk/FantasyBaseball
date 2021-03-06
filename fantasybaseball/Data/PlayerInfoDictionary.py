from FantasyBaseball.Utils import *
DEBUG('./Data/URLDictionary.py')

"Stores urls for players"
# Alphabetize!
# 'A. Ramirez'     : 'http://sports.espn.go.com/mlb/players/stats?statsId=6014',
# 'B. Crosby'      : 'http://sports.espn.go.com/mlb/players/stats?statsId=7223',
# 'B. Roberts'     : 'http://sports.espn.go.com/mlb/players/stats?statsId=6741',
# 'D. Lee'         : 'http://sports.espn.go.com/mlb/players/stats?statsId=5775',
# 'J. Dye'         : 'http://sports.espn.go.com/mlb/players/stats?statsId=5610',
# 'J. Kendall'     : 'http://sports.espn.go.com/mlb/players/stats?statsId=5562',
# 'J. Kent'        : 'http://sports.espn.go.com/mlb/players/stats?statsId=4826',
# 'J. Mauer'       : 'http://sports.espn.go.com/mlb/players/stats?statsId=7062',
# 'J. Peralta'     : 'http://sports.espn.go.com/mlb/players/stats?statsId=7156',
# 'J. Posada'      : 'http://sports.espn.go.com/mlb/players/stats?statsId=5502',
# 'K. Griffey, Jr.': 'http://sports.espn.go.com/mlb/players/stats?statsId=4305',
# 'M. Ellis'       : 'http://sports.espn.go.com/mlb/players/stats?statsId=6899',
# 'V. Guerrero'    : 'http://sports.espn.go.com/mlb/players/stats?statsId=5737',
__hitters_ = {
    'A. Dunn'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4808', 'pos' : 'LF',},
    'A. Jones'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3520', 'pos' : 'CF',},
    'A. Pujols'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4574', 'pos' : '1B',},
    'A. Ramirez'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3853', 'pos' : '3B',},
    'A. Rodriguez'   : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3115', 'pos' : '3B',},
    'A. Rowand'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4745', 'pos' : 'CF',},
    'A. Soriano'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3993', 'pos' : 'LF',},
    'B. Abreu'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3537', 'pos' : 'RF',},
    'B. Crosby'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5770', 'pos' : 'SS',},
    'B. Giles'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3382', 'pos' : 'RF',},
    'B. Hawpe'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5955', 'pos' : 'RF',},
    'B. McCann'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6309', 'pos' : 'C',},
    'B. Roberts'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4773', 'pos' : '2B',},
    'B.J. Upton'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5970', 'pos' : 'CF',},
    'C. Beltran'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3971', 'pos' : 'CF',},
    'C. Crawford'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5035', 'pos' : 'LF',},
    'C. Figgins'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5302', 'pos' : '3B',},
    'C. Granderson'  : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6125', 'pos' : 'CF',},
    'C. Guillen'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3944', 'pos' : 'SS',},
    'C. Hart'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5973', 'pos' : 'RF',},
    'C. Jones'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3006', 'pos' : '3B',},
    'C. Lee'         : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4000', 'pos' : 'LF',},
    'C. Pena'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4594', 'pos' : '1B',},
    'C. Utley'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5383', 'pos' : '2B',},
    'D. Jeter'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3246', 'pos' : 'SS',},
    'D. Lee'         : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3614', 'pos' : '1B',},
    'D. Ortiz'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3748', 'pos' : 'DH',},
    'D. Pedroia'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6393', 'pos' : '2B',},
    'D. Wright'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6035', 'pos' : '3B',},
    'D. Young'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3538', 'pos' : '1B',},
    'E. Renteria'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3441', 'pos' : 'SS',},
    'F. Sanchez'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5315', 'pos' : '2B',},
    'G. Sizemore'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5882', 'pos' : 'CF',},
    'G. Atkins'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5507', 'pos' : '3B',},
    'H. Pence'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=28687', 'pos' : 'CF',},
    'H. Ramirez'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6195', 'pos' : 'SS',},
    'I. Suzuki'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4570', 'pos' : 'CF',},
    'J. Bay'         : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5496', 'pos' : 'LF',},
    'J. Carroll'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5349', 'pos' : '2B',},
    'J. Cust'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4609', 'pos' : 'DH',},
    'J. Dye'         : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3449', 'pos' : 'RF',},
    'J. Edmonds'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2993', 'pos' : 'CF',},
    'J. Giambi'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3226', 'pos' : 'DH',},
    'J. Kendall'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3401', 'pos' : 'C',},
    'J. Kent'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2668', 'pos' : '2B',},
    'J. Mauer'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5378', 'pos' : 'C',},
    'J. Peralta'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5527', 'pos' : 'SS',},
    'J. Posada'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3341', 'pos' : 'C',},
    'J. Reyes'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5411', 'pos' : 'SS',},
    'J. Rollins'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4258', 'pos' : 'SS',},
    'J. Thome'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2604', 'pos' : 'DH',},
    'J. Varitek'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3760', 'pos' : 'C',},
    'J. Vidro'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3666', 'pos' : 'DH',},
    'J.D. Drew'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3956', 'pos' : 'RF',},
    'K. Griffey, Jr.': {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2148', 'pos' : 'RF',},
    'K. Johnson'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6295', 'pos' : '2B',},
    'L. Berkman'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4118', 'pos' : '1B',},
    'L. Castillo'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3515', 'pos' : '2B',},
    'M. Alou'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2360', 'pos' : 'LF',},
    'M. Barrett'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3937', 'pos' : 'C',},
    'M. Bradley'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4245', 'pos' : 'LF',},
    'M. Cabrera'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5544', 'pos' : '3B',},
    'M. Ellis'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5086', 'pos' : '2B',},
    'M. Holliday'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5940', 'pos' : 'LF',},
    'M. Loretta'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3343', 'pos' : 'SS',},
    'M. Lowell'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3972', 'pos' : '3B',},
    'M. Murton'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6349', 'pos' : 'RF',},
    'M. Ordonez'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3728', 'pos' : 'RF',},
    'M. Ramirez'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2974', 'pos' : 'LF',},
    'M. Tejada'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3727', 'pos' : 'SS',},
    'M. Teixeira'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4937', 'pos' : '1B',},
    'M. Young'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4566', 'pos' : 'SS',},
    'O. Cabrera'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3739', 'pos' : 'SS',},
    'P. Burrell'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4214', 'pos' : 'LF',},
    'P. Fielder'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5915', 'pos' : '1B',},
    'P. Polanco'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3888', 'pos' : '2B',},
    'R. Cano'        : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6204', 'pos' : '2B',},
    'R. Durham'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3163', 'pos' : '2B',},
    'R. Howard'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6097', 'pos' : '1B',},
    'R. Martin'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6390', 'pos' : 'C',},
    'Re. Johnson'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5452', 'pos' : 'LF',},
    'T. Glaus'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3902', 'pos' : '3B',},
    'T. Helton'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3709', 'pos' : '1B',},
    'V. Guerrero'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3576', 'pos' : 'RF',},
    'V. Martinez'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5007', 'pos' : 'C',},
    'V. Wells'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4166', 'pos' : 'CF',},
    }
# 'B. Penny'      : 'http://sports.espn.go.com/mlb/players/stats?statsId=6276',
# 'F. Rodriguez'  : 'http://sports.espn.go.com/mlb/players/stats?statsId=7029',
# 'J. Blanton'    : 'http://sports.espn.go.com/mlb/players/stats?statsId=7461',
# 'J. Verlander'  : 'http://sports.espn.go.com/mlb/players/stats?statsId=7590',
# 'T. Hudson'     : 'http://sports.espn.go.com/mlb/players/stats?statsId=6245',
__pitchers_ = {
    'A. Pettitte'   : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3171', 'pos' : 'LSP',},
    'B. Penny'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4115', 'pos' : 'SP',},
    'B. Sheets'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4571', 'pos' : 'SP',},
    'B. Wagner'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3375', 'pos' : 'CL',},
    'B. Webb'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5455', 'pos' : 'SP',},
    'B. Zito'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4233', 'pos' : 'LSP',},
    'B.J. Ryan'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4133', 'pos' : 'CL',},
    'C. Carpenter'  : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3610', 'pos' : 'SP',},
    'C. Hamels'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6216', 'pos' : 'LSP',},
    'C. Young'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6073', 'pos' : 'SP',},
    'C. Zambrano'   : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4499', 'pos' : 'SP',},
    'C.C. Sabathia' : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4553', 'pos' : 'LSP',},
    'D. Haren'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5565', 'pos' : 'SP',},
    'D. Matsuzaka'  : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=28631', 'pos' : 'SP',},
    'D. Willis'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5470', 'pos' : 'LSP',},
    'E. Bedard'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5099', 'pos' : 'LSP',},
    'E. Gagne'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4181', 'pos' : 'CL',},
    'F. Hernandez'  : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6194', 'pos' : 'SP',},
    'F. Liriano'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6211', 'pos' : 'LSP',},
    'F. Rodriguez'  : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5357', 'pos' : 'CL',},
    'H. Street'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6175', 'pos' : 'CL',},
    'J. Beckett'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4242', 'pos' : 'SP',},
    'J. Blanton'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6132', 'pos' : 'SP',},
    'J. Guthrie'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5370', 'pos' : 'SP',},
    'J. Isringhausen':{'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3289', 'pos' : 'CL',},
    'J. Nathan'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4044', 'pos' : 'CL',},
    'J. Papelbon'   : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6373', 'pos' : 'CL',},
    'J. Peavy'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5019', 'pos' : 'SP',},
    'J. Santana'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4280', 'pos' : 'LSP',},
    'J. Smoltz'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2077', 'pos' : 'SP',},
    'J. Soria'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=28688', 'pos' : 'CL',},
    'J. Verlander'  : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6341', 'pos' : 'SP',},
    'J.J. Putz'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5640', 'pos' : 'CL',},
    'M. Buehrle'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4454', 'pos' : 'LSP',},
    'M. Cain'       : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6202', 'pos' : 'SP',},
    'M. Mussina'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2557', 'pos' : 'SP',},
    'M. Rivera'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3240', 'pos' : 'CL',},
    'P. Martinez'   : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2717', 'pos' : 'SP',},
    'R. Clemens'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=1427', 'pos' : 'SP',},
    'R. Halladay'   : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=3973', 'pos' : 'SP',},
    'R. Harden'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5588', 'pos' : 'SP',},
    'S. Kazmir'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=5917', 'pos' : 'LSP',},
    'T. Hoffman'    : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=2817', 'pos' : 'CL',},
    'T. Hudson'     : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=4084', 'pos' : 'SP',},
    'T. Saito'      : {'url' : 'http://sports.espn.go.com/mlb/players/stats?playerId=6498', 'pos' : 'CL',},
    }
#player_info = __hitters_
player_info = {}
player_info.update(__hitters_)
player_info.update(__pitchers_)

__hitting_stats_ = {'OBP' : {'type' : float , 'regex' : 'H.OBP' , 'ratio' : 'TPA' , } ,
                    'SLG' : {'type' : float , 'regex' : 'H.SLG' , 'ratio' : 'AB' , } ,
                    'TPA' : {'type' : int , 'regex' : 'H.TPA' , } ,
                    'AB'  : {'type' : int , 'regex' : 'H.AB' , } ,
                    }
__starter_stats_ = {'OBP' : {'type' : float , 'regex' : 'P.OBP' , 'ratio' : 'TBF' , } ,
                    'SLG' : {'type' : float , 'regex' : 'P.SLG' , 'ratio' : 'AB' , } ,
                    'TBF' : {'type' : int , 'regex' : 'P.TBF' , } ,
                    'BB' : {'type' : int , 'regex' : 'P.BB' , } ,
                    'AB' : {'type' : int , 'regex' : 'P.AB' , } ,
                    'SO' : {'type' : int , 'regex' : 'P.SO' , } ,
                    'IP' : {'type' : float , 'regex' : 'P.IP' , } , # remember '28.1' means 28 1/3
                    }
__closer_specific_stats_ = {'SV' : {'type' : int , 'regex' : 'P.SV' , } ,
                            'BLSV' : {'type' : int , 'regex' : 'P.BLSV' , } ,
                            'G' : {'type' : int , 'regex' : 'P.G' , } ,
                            }
__closer_stats_ = {}
__closer_stats_.update(__starter_stats_)
__closer_stats_.update(__closer_specific_stats_)
__closer_stats2_ = {'CL.OBP' : {'type' : float , 'regex' : 'P.OBP' , 'ratio' : 'CL.TBF' , } ,
                    'CL.SLG' : {'type' : float , 'regex' : 'P.SLG' , 'ratio' : 'CL.AB' , } ,
                    'CL.TBF' : {'type' : int , 'regex' : 'P.TBF' , } ,
                    'CL.BB' : {'type' : int , 'regex' : 'P.BB' , } ,
                    'CL.AB' : {'type' : int , 'regex' : 'P.AB' , } ,
                    'CL.SO' : {'type' : int , 'regex' : 'P.SO' , } ,
                    'CL.IP' : {'type' : float , 'regex' : 'P.IP' , } , # remember '28.1' means 28 1/3
                    'CL.SV' : {'type' : int , 'regex' : 'P.SV' , } ,
                    'CL.BLSV' : {'type' : int , 'regex' : 'P.BLSV' , } ,
                    'CL.G' : {'type' : int , 'regex' : 'P.G' , } ,
                    }

position_info = {'C'  : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 '1B' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 '2B' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 '3B' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 'SS' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 'LF' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 'CF' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 'RF' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 'SP' : {'stat_list' : __starter_stats_, 'category' : 'SP'},
                 'LSP': {'stat_list' : __starter_stats_, 'category' : 'SP'},
                 'CL' : {'stat_list' : __closer_stats_,  'category' : 'CL'},
                 'DH' : {'stat_list' : __hitting_stats_, 'category' : 'H'},
                 }

def get_stats_list(player_name):
    return position_info[player_info[player_name]['pos']]['stat_list']

def get_stat_description(stat_category, stat_name):
    if stat_category == 'H':
        dict = __hitting_stats_
    elif stat_category == 'SP':
        dict = __starter_stats_
    elif stat_category == 'CL':
        dict = __closer_stats_
    else:
        ERROR('get_stat_description: ' + stat_category + ' ' + stat_name)
        return {}
    if stat_name in dict:
        return dict[stat_name]
    else:
        ERROR('get_stat_description: ' + stat_category + ' ' + stat_name)
        return {}
    pass
