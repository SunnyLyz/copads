'''
Ragaraja Interpreter
Date created: 16th August 2012
Licence: Python Software Foundation License version 2

Ragaraja is a derivative and massive extension of Brainfuck. 
This work is influenced by a large number of Brainfuck 
derivatives, other esoteric programming languages, and even 
assembly languages. Probably the most critical difference 
between Ragaraja and other Brainfuck derivatives is the large 
number of commands / instructions - 1000 possible commands / 
instructions, inspired by Nandi (follower of Lord Shiva) who 
was supposed to be the first author of Kama Sutra and wrote it 
in 1000 chapters. 

Etymology: Ragaraja is the name of a Mahayana Buddhist deity 
from Esoteric traditions. The Chinese calls him �iran M�ngw�ng. 
Ragaraja is one of the Wisdom Kings (a group of Bodhisattvas) 
and represents the state at which sexual excitement or agitation 
can be channeled towards enlightenment and passionate love can 
become compassion for all living things. Hence, I name this 
compilation/derivative/extension of Brainfuck in 1000 
commands/instructions/opcode to signify the epitome, a 
channeling of raw urge to the love and compassion for and 
towards every being. May really be viewed as Brainfuck 
attaining enlightenment or Nirvana. Whoever that can 
remember all 1000 commands and use it, really deserves an award. 

The interpreter environment consists of the following elements:

1. Array/Tape: A circular tape initialized with 30 thousand cells 
each with zero. This can be visualized as a 30,000 cell register 
machine. The number of cells can increase or decrease during runtime.
2. Source: The program
3. Input List: A list of data given to the execution environment at 
initialization.
4. Output List: A list of output from the execution. This may also be 
used as a secondary tape. 

When the program terminates, all 4 elements are returned, and the 
interpreter terminates itself. 

Ref: http://esolangs.org/wiki/Ragaraja
'''
import random
import register_machine as r
from lc_bf import increment, decrement
from lc_bf import forward, backward
from lc_bf import call_out, accept_predefined
from lc_bf import cbf_start_loop, cbf_end_loop

def not_used(array, apointer, inputdata, output, source, spointer):
	'''
	'''
    return (array, apointer, inputdata, output, source, spointer)

ragaraja = {'000': forward,
			'001': not_used,
			'002': not_used,
			'003': not_used,
			'004': backward,
			'005': not_used,
			'006': not_used,
			'007': not_used,
			'008': increment,
			'009': not_used,
			'010': not_used,
			'011': decrement,
			'012': not_used,
			'013': not_used,
			'014': cbf_start_loop,
			'015': cbf_end_loop,
			'016': not_used,
			'017': not_used,
			'018': not_used,
			'019': not_used,
			'020': call_out,
			'021': not_used,
			'022': not_used,
			'023': not_used,
			'024': not_used,
			'025': not_used,
			'026': not_used,
			'027': not_used,
			'028': not_used,
			'029': not_used,
			'030': not_used,
			'031': not_used,
			'032': not_used,
			'033': not_used,
			'034': not_used,
			'035': not_used,
			'036': not_used,
			'037': not_used,
			'038': not_used,
			'039': not_used,
			'040': not_used,
			'041': not_used,
			'042': not_used,
			'043': not_used,
			'044': not_used,
			'045': not_used,
			'046': not_used,
			'047': not_used,
			'048': not_used,
			'049': not_used,
			'050': not_used,
			'051': not_used,
			'052': not_used,
			'053': not_used,
			'054': not_used,
			'055': not_used,
			'056': not_used,
			'057': not_used,
			'058': not_used,
			'059': not_used,
			'060': not_used,
			'061': not_used,
			'062': not_used,
			'063': accept_predefined,
			'064': not_used,
			'065': not_used,
			'066': not_used,
			'067': not_used,
			'068': not_used,
			'069': not_used,
			'070': not_used,
			'071': not_used,
			'072': not_used,
			'073': not_used,
			'074': not_used,
			'075': not_used,
			'076': not_used,
			'077': not_used,
			'078': not_used,
			'079': not_used,
			'080': not_used,
			'081': not_used,
			'082': not_used,
			'083': not_used,
			'084': not_used,
			'085': not_used,
			'086': not_used,
			'087': not_used,
			'088': not_used,
			'089': not_used,
			'090': not_used,
			'091': not_used,
			'092': not_used,
			'093': not_used,
			'094': not_used,
			'095': not_used,
			'096': not_used,
			'097': not_used,
			'098': not_used,
			'099': not_used,
			'100': not_used,
			'101': not_used,
			'102': not_used,
			'103': not_used,
			'104': not_used,
			'105': not_used,
			'106': not_used,
			'107': not_used,
			'108': not_used,
			'109': not_used,
			'110': not_used,
			'111': not_used,
			'112': not_used,
			'113': not_used,
			'114': not_used,
			'115': not_used,
			'116': not_used,
			'117': not_used,
			'118': not_used,
			'119': not_used,
			'120': not_used,
			'121': not_used,
			'122': not_used,
			'123': not_used,
			'124': not_used,
			'125': not_used,
			'126': not_used,
			'127': not_used,
			'128': not_used,
			'129': not_used,
			'130': not_used,
			'131': not_used,
			'132': not_used,
			'133': not_used,
			'134': not_used,
			'135': not_used,
			'136': not_used,
			'137': not_used,
			'138': not_used,
			'139': not_used,
			'140': not_used,
			'141': not_used,
			'142': not_used,
			'143': not_used,
			'144': not_used,
			'145': not_used,
			'146': not_used,
			'147': not_used,
			'148': not_used,
			'149': not_used,
			'150': not_used,
			'151': not_used,
			'152': not_used,
			'153': not_used,
			'154': not_used,
			'155': not_used,
			'156': not_used,
			'157': not_used,
			'158': not_used,
			'159': not_used,
			'160': not_used,
			'161': not_used,
			'162': not_used,
			'163': not_used,
			'164': not_used,
			'165': not_used,
			'166': not_used,
			'167': not_used,
			'168': not_used,
			'169': not_used,
			'170': not_used,
			'171': not_used,
			'172': not_used,
			'173': not_used,
			'174': not_used,
			'175': not_used,
			'176': not_used,
			'177': not_used,
			'178': not_used,
			'179': not_used,
			'180': not_used,
			'181': not_used,
			'182': not_used,
			'183': not_used,
			'184': not_used,
			'185': not_used,
			'186': not_used,
			'187': not_used,
			'188': not_used,
			'189': not_used,
			'190': not_used,
			'191': not_used,
			'192': not_used,
			'193': not_used,
			'194': not_used,
			'195': not_used,
			'196': not_used,
			'197': not_used,
			'198': not_used,
			'199': not_used,
			'200': not_used,
			'201': not_used,
			'202': not_used,
			'203': not_used,
			'204': not_used,
			'205': not_used,
			'206': not_used,
			'207': not_used,
			'208': not_used,
			'209': not_used,
			'210': not_used,
			'211': not_used,
			'212': not_used,
			'213': not_used,
			'214': not_used,
			'215': not_used,
			'216': not_used,
			'217': not_used,
			'218': not_used,
			'219': not_used,
			'220': not_used,
			'221': not_used,
			'222': not_used,
			'223': not_used,
			'224': not_used,
			'225': not_used,
			'226': not_used,
			'227': not_used,
			'228': not_used,
			'229': not_used,
			'230': not_used,
			'231': not_used,
			'232': not_used,
			'233': not_used,
			'234': not_used,
			'235': not_used,
			'236': not_used,
			'237': not_used,
			'238': not_used,
			'239': not_used,
			'240': not_used,
			'241': not_used,
			'242': not_used,
			'243': not_used,
			'244': not_used,
			'245': not_used,
			'246': not_used,
			'247': not_used,
			'248': not_used,
			'249': not_used,
			'250': not_used,
			'251': not_used,
			'252': not_used,
			'253': not_used,
			'254': not_used,
			'255': not_used,
			'256': not_used,
			'257': not_used,
			'258': not_used,
			'259': not_used,
			'260': not_used,
			'261': not_used,
			'262': not_used,
			'263': not_used,
			'264': not_used,
			'265': not_used,
			'266': not_used,
			'267': not_used,
			'268': not_used,
			'269': not_used,
			'270': not_used,
			'271': not_used,
			'272': not_used,
			'273': not_used,
			'274': not_used,
			'275': not_used,
			'276': not_used,
			'277': not_used,
			'278': not_used,
			'279': not_used,
			'280': not_used,
			'281': not_used,
			'282': not_used,
			'283': not_used,
			'284': not_used,
			'285': not_used,
			'286': not_used,
			'287': not_used,
			'288': not_used,
			'289': not_used,
			'290': not_used,
			'291': not_used,
			'292': not_used,
			'293': not_used,
			'294': not_used,
			'295': not_used,
			'296': not_used,
			'297': not_used,
			'298': not_used,
			'299': not_used,
			'300': not_used,
			'301': not_used,
			'302': not_used,
			'303': not_used,
			'304': not_used,
			'305': not_used,
			'306': not_used,
			'307': not_used,
			'308': not_used,
			'309': not_used,
			'310': not_used,
			'311': not_used,
			'312': not_used,
			'313': not_used,
			'314': not_used,
			'315': not_used,
			'316': not_used,
			'317': not_used,
			'318': not_used,
			'319': not_used,
			'320': not_used,
			'321': not_used,
			'322': not_used,
			'323': not_used,
			'324': not_used,
			'325': not_used,
			'326': not_used,
			'327': not_used,
			'328': not_used,
			'329': not_used,
			'330': not_used,
			'331': not_used,
			'332': not_used,
			'333': not_used,
			'334': not_used,
			'335': not_used,
			'336': not_used,
			'337': not_used,
			'338': not_used,
			'339': not_used,
			'340': not_used,
			'341': not_used,
			'342': not_used,
			'343': not_used,
			'344': not_used,
			'345': not_used,
			'346': not_used,
			'347': not_used,
			'348': not_used,
			'349': not_used,
			'350': not_used,
			'351': not_used,
			'352': not_used,
			'353': not_used,
			'354': not_used,
			'355': not_used,
			'356': not_used,
			'357': not_used,
			'358': not_used,
			'359': not_used,
			'360': not_used,
			'361': not_used,
			'362': not_used,
			'363': not_used,
			'364': not_used,
			'365': not_used,
			'366': not_used,
			'367': not_used,
			'368': not_used,
			'369': not_used,
			'370': not_used,
			'371': not_used,
			'372': not_used,
			'373': not_used,
			'374': not_used,
			'375': not_used,
			'376': not_used,
			'377': not_used,
			'378': not_used,
			'379': not_used,
			'380': not_used,
			'381': not_used,
			'382': not_used,
			'383': not_used,
			'384': not_used,
			'385': not_used,
			'386': not_used,
			'387': not_used,
			'388': not_used,
			'389': not_used,
			'390': not_used,
			'391': not_used,
			'392': not_used,
			'393': not_used,
			'394': not_used,
			'395': not_used,
			'396': not_used,
			'397': not_used,
			'398': not_used,
			'399': not_used,
			'400': not_used,
			'401': not_used,
			'402': not_used,
			'403': not_used,
			'404': not_used,
			'405': not_used,
			'406': not_used,
			'407': not_used,
			'408': not_used,
			'409': not_used,
			'410': not_used,
			'411': not_used,
			'412': not_used,
			'413': not_used,
			'414': not_used,
			'415': not_used,
			'416': not_used,
			'417': not_used,
			'418': not_used,
			'419': not_used,
			'420': not_used,
			'421': not_used,
			'422': not_used,
			'423': not_used,
			'424': not_used,
			'425': not_used,
			'426': not_used,
			'427': not_used,
			'428': not_used,
			'429': not_used,
			'430': not_used,
			'431': not_used,
			'432': not_used,
			'433': not_used,
			'434': not_used,
			'435': not_used,
			'436': not_used,
			'437': not_used,
			'438': not_used,
			'439': not_used,
			'440': not_used,
			'441': not_used,
			'442': not_used,
			'443': not_used,
			'444': not_used,
			'445': not_used,
			'446': not_used,
			'447': not_used,
			'448': not_used,
			'449': not_used,
			'450': not_used,
			'451': not_used,
			'452': not_used,
			'453': not_used,
			'454': not_used,
			'455': not_used,
			'456': not_used,
			'457': not_used,
			'458': not_used,
			'459': not_used,
			'460': not_used,
			'461': not_used,
			'462': not_used,
			'463': not_used,
			'464': not_used,
			'465': not_used,
			'466': not_used,
			'467': not_used,
			'468': not_used,
			'469': not_used,
			'470': not_used,
			'471': not_used,
			'472': not_used,
			'473': not_used,
			'474': not_used,
			'475': not_used,
			'476': not_used,
			'477': not_used,
			'478': not_used,
			'479': not_used,
			'480': not_used,
			'481': not_used,
			'482': not_used,
			'483': not_used,
			'484': not_used,
			'485': not_used,
			'486': not_used,
			'487': not_used,
			'488': not_used,
			'489': not_used,
			'490': not_used,
			'491': not_used,
			'492': not_used,
			'493': not_used,
			'494': not_used,
			'495': not_used,
			'496': not_used,
			'497': not_used,
			'498': not_used,
			'499': not_used,
			'500': not_used,
			'501': not_used,
			'502': not_used,
			'503': not_used,
			'504': not_used,
			'505': not_used,
			'506': not_used,
			'507': not_used,
			'508': not_used,
			'509': not_used,
			'510': not_used,
			'511': not_used,
			'512': not_used,
			'513': not_used,
			'514': not_used,
			'515': not_used,
			'516': not_used,
			'517': not_used,
			'518': not_used,
			'519': not_used,
			'520': not_used,
			'521': not_used,
			'522': not_used,
			'523': not_used,
			'524': not_used,
			'525': not_used,
			'526': not_used,
			'527': not_used,
			'528': not_used,
			'529': not_used,
			'530': not_used,
			'531': not_used,
			'532': not_used,
			'533': not_used,
			'534': not_used,
			'535': not_used,
			'536': not_used,
			'537': not_used,
			'538': not_used,
			'539': not_used,
			'540': not_used,
			'541': not_used,
			'542': not_used,
			'543': not_used,
			'544': not_used,
			'545': not_used,
			'546': not_used,
			'547': not_used,
			'548': not_used,
			'549': not_used,
			'550': not_used,
			'551': not_used,
			'552': not_used,
			'553': not_used,
			'554': not_used,
			'555': not_used,
			'556': not_used,
			'557': not_used,
			'558': not_used,
			'559': not_used,
			'560': not_used,
			'561': not_used,
			'562': not_used,
			'563': not_used,
			'564': not_used,
			'565': not_used,
			'566': not_used,
			'567': not_used,
			'568': not_used,
			'569': not_used,
			'570': not_used,
			'571': not_used,
			'572': not_used,
			'573': not_used,
			'574': not_used,
			'575': not_used,
			'576': not_used,
			'577': not_used,
			'578': not_used,
			'579': not_used,
			'580': not_used,
			'581': not_used,
			'582': not_used,
			'583': not_used,
			'584': not_used,
			'585': not_used,
			'586': not_used,
			'587': not_used,
			'588': not_used,
			'589': not_used,
			'590': not_used,
			'591': not_used,
			'592': not_used,
			'593': not_used,
			'594': not_used,
			'595': not_used,
			'596': not_used,
			'597': not_used,
			'598': not_used,
			'599': not_used,
			'600': not_used,
			'601': not_used,
			'602': not_used,
			'603': not_used,
			'604': not_used,
			'605': not_used,
			'606': not_used,
			'607': not_used,
			'608': not_used,
			'609': not_used,
			'610': not_used,
			'611': not_used,
			'612': not_used,
			'613': not_used,
			'614': not_used,
			'615': not_used,
			'616': not_used,
			'617': not_used,
			'618': not_used,
			'619': not_used,
			'620': not_used,
			'621': not_used,
			'622': not_used,
			'623': not_used,
			'624': not_used,
			'625': not_used,
			'626': not_used,
			'627': not_used,
			'628': not_used,
			'629': not_used,
			'630': not_used,
			'631': not_used,
			'632': not_used,
			'633': not_used,
			'634': not_used,
			'635': not_used,
			'636': not_used,
			'637': not_used,
			'638': not_used,
			'639': not_used,
			'640': not_used,
			'641': not_used,
			'642': not_used,
			'643': not_used,
			'644': not_used,
			'645': not_used,
			'646': not_used,
			'647': not_used,
			'648': not_used,
			'649': not_used,
			'650': not_used,
			'651': not_used,
			'652': not_used,
			'653': not_used,
			'654': not_used,
			'655': not_used,
			'656': not_used,
			'657': not_used,
			'658': not_used,
			'659': not_used,
			'660': not_used,
			'661': not_used,
			'662': not_used,
			'663': not_used,
			'664': not_used,
			'665': not_used,
			'666': not_used,
			'667': not_used,
			'668': not_used,
			'669': not_used,
			'670': not_used,
			'671': not_used,
			'672': not_used,
			'673': not_used,
			'674': not_used,
			'675': not_used,
			'676': not_used,
			'677': not_used,
			'678': not_used,
			'679': not_used,
			'680': not_used,
			'681': not_used,
			'682': not_used,
			'683': not_used,
			'684': not_used,
			'685': not_used,
			'686': not_used,
			'687': not_used,
			'688': not_used,
			'689': not_used,
			'690': not_used,
			'691': not_used,
			'692': not_used,
			'693': not_used,
			'694': not_used,
			'695': not_used,
			'696': not_used,
			'697': not_used,
			'698': not_used,
			'699': not_used,
			'700': not_used,
			'701': not_used,
			'702': not_used,
			'703': not_used,
			'704': not_used,
			'705': not_used,
			'706': not_used,
			'707': not_used,
			'708': not_used,
			'709': not_used,
			'710': not_used,
			'711': not_used,
			'712': not_used,
			'713': not_used,
			'714': not_used,
			'715': not_used,
			'716': not_used,
			'717': not_used,
			'718': not_used,
			'719': not_used,
			'720': not_used,
			'721': not_used,
			'722': not_used,
			'723': not_used,
			'724': not_used,
			'725': not_used,
			'726': not_used,
			'727': not_used,
			'728': not_used,
			'729': not_used,
			'730': not_used,
			'731': not_used,
			'732': not_used,
			'733': not_used,
			'734': not_used,
			'735': not_used,
			'736': not_used,
			'737': not_used,
			'738': not_used,
			'739': not_used,
			'740': not_used,
			'741': not_used,
			'742': not_used,
			'743': not_used,
			'744': not_used,
			'745': not_used,
			'746': not_used,
			'747': not_used,
			'748': not_used,
			'749': not_used,
			'750': not_used,
			'751': not_used,
			'752': not_used,
			'753': not_used,
			'754': not_used,
			'755': not_used,
			'756': not_used,
			'757': not_used,
			'758': not_used,
			'759': not_used,
			'760': not_used,
			'761': not_used,
			'762': not_used,
			'763': not_used,
			'764': not_used,
			'765': not_used,
			'766': not_used,
			'767': not_used,
			'768': not_used,
			'769': not_used,
			'770': not_used,
			'771': not_used,
			'772': not_used,
			'773': not_used,
			'774': not_used,
			'775': not_used,
			'776': not_used,
			'777': not_used,
			'778': not_used,
			'779': not_used,
			'780': not_used,
			'781': not_used,
			'782': not_used,
			'783': not_used,
			'784': not_used,
			'785': not_used,
			'786': not_used,
			'787': not_used,
			'788': not_used,
			'789': not_used,
			'790': not_used,
			'791': not_used,
			'792': not_used,
			'793': not_used,
			'794': not_used,
			'795': not_used,
			'796': not_used,
			'797': not_used,
			'798': not_used,
			'799': not_used,
			'800': not_used,
			'801': not_used,
			'802': not_used,
			'803': not_used,
			'804': not_used,
			'805': not_used,
			'806': not_used,
			'807': not_used,
			'808': not_used,
			'809': not_used,
			'810': not_used,
			'811': not_used,
			'812': not_used,
			'813': not_used,
			'814': not_used,
			'815': not_used,
			'816': not_used,
			'817': not_used,
			'818': not_used,
			'819': not_used,
			'820': not_used,
			'821': not_used,
			'822': not_used,
			'823': not_used,
			'824': not_used,
			'825': not_used,
			'826': not_used,
			'827': not_used,
			'828': not_used,
			'829': not_used,
			'830': not_used,
			'831': not_used,
			'832': not_used,
			'833': not_used,
			'834': not_used,
			'835': not_used,
			'836': not_used,
			'837': not_used,
			'838': not_used,
			'839': not_used,
			'840': not_used,
			'841': not_used,
			'842': not_used,
			'843': not_used,
			'844': not_used,
			'845': not_used,
			'846': not_used,
			'847': not_used,
			'848': not_used,
			'849': not_used,
			'850': not_used,
			'851': not_used,
			'852': not_used,
			'853': not_used,
			'854': not_used,
			'855': not_used,
			'856': not_used,
			'857': not_used,
			'858': not_used,
			'859': not_used,
			'860': not_used,
			'861': not_used,
			'862': not_used,
			'863': not_used,
			'864': not_used,
			'865': not_used,
			'866': not_used,
			'867': not_used,
			'868': not_used,
			'869': not_used,
			'870': not_used,
			'871': not_used,
			'872': not_used,
			'873': not_used,
			'874': not_used,
			'875': not_used,
			'876': not_used,
			'877': not_used,
			'878': not_used,
			'879': not_used,
			'880': not_used,
			'881': not_used,
			'882': not_used,
			'883': not_used,
			'884': not_used,
			'885': not_used,
			'886': not_used,
			'887': not_used,
			'888': not_used,
			'889': not_used,
			'890': not_used,
			'891': not_used,
			'892': not_used,
			'893': not_used,
			'894': not_used,
			'895': not_used,
			'896': not_used,
			'897': not_used,
			'898': not_used,
			'899': not_used,
			'900': not_used,
			'901': not_used,
			'902': not_used,
			'903': not_used,
			'904': not_used,
			'905': not_used,
			'906': not_used,
			'907': not_used,
			'908': not_used,
			'909': not_used,
			'910': not_used,
			'911': not_used,
			'912': not_used,
			'913': not_used,
			'914': not_used,
			'915': not_used,
			'916': not_used,
			'917': not_used,
			'918': not_used,
			'919': not_used,
			'920': not_used,
			'921': not_used,
			'922': not_used,
			'923': not_used,
			'924': not_used,
			'925': not_used,
			'926': not_used,
			'927': not_used,
			'928': not_used,
			'929': not_used,
			'930': not_used,
			'931': not_used,
			'932': not_used,
			'933': not_used,
			'934': not_used,
			'935': not_used,
			'936': not_used,
			'937': not_used,
			'938': not_used,
			'939': not_used,
			'940': not_used,
			'941': not_used,
			'942': not_used,
			'943': not_used,
			'944': not_used,
			'945': not_used,
			'946': not_used,
			'947': not_used,
			'948': not_used,
			'949': not_used,
			'950': not_used,
			'951': not_used,
			'952': not_used,
			'953': not_used,
			'954': not_used,
			'955': not_used,
			'956': not_used,
			'957': not_used,
			'958': not_used,
			'959': not_used,
			'960': not_used,
			'961': not_used,
			'962': not_used,
			'963': not_used,
			'964': not_used,
			'965': not_used,
			'966': not_used,
			'967': not_used,
			'968': not_used,
			'969': not_used,
			'970': not_used,
			'971': not_used,
			'972': not_used,
			'973': not_used,
			'974': not_used,
			'975': not_used,
			'976': not_used,
			'977': not_used,
			'978': not_used,
			'979': not_used,
			'980': not_used,
			'981': not_used,
			'982': not_used,
			'983': not_used,
			'984': not_used,
			'985': not_used,
			'986': not_used,
			'987': not_used,
			'988': not_used,
			'989': not_used,
			'990': not_used,
			'991': not_used,
			'992': not_used,
			'993': not_used,
			'994': not_used,
			'995': not_used,
			'996': not_used,
			'997': not_used,
			'998': not_used,
			'999': not_used
		   }
			
def LCBF_to_Ragaraja(source):
	'''
	Converts Loose Circular Brainfuck source code to Ragaraja source code
	
	@param source: Loose Circular Brainfuck (LCBF) source code
	@type source: string
	@return: Ragaraja source code string
	'''
	converted = []
	for x in source:
		if x == '>': converted.append('000')
		elif x == '<': converted.append('004')
		elif x == '+': converted.append('008')
		elif x == '-': converted.append('011')
		elif x == '.': converted.append('020')
		elif x == ',': converted.append('063')
		elif x == '[': converted.append('014')
		elif x == ']': converted.append('015')
		else: converted.append('...')
	return converted
	
def nBF_to_Ragaraja(source):
	'''
	Converts NucleotideBF (nBF) source code to Ragaraja source code
	
	@param source: NucleotideBF (nBF) source code
	@type source: string
	@return: Ragaraja source code string
	'''
	converted = []
	for x in source:
		if x == 'G': converted.append('000')
		elif x == 'C': converted.append('004')
		elif x == 'A': converted.append('008')
		elif x == 'T': converted.append('011')
		elif x == '.': converted.append('020')
		elif x == 'R': converted.append('050')
		elif x == 'Y': converted.append('051')
		elif x == 'S': converted.append('052')
		elif x == 'W': converted.append('053')
		elif x == 'K': converted.append('054')
		elif x == 'M': converted.append('055')
		elif x == 'B': converted.append('056')
		elif x == 'D': converted.append('057')
		elif x == 'H': converted.append('058')
		elif x == 'V': converted.append('059')
		elif x == 'N': converted.append('060')
		else: converted.append('...')
	return converted
			
def interpreter(source, inputdata=[], array=None, size=30000):
	(array, apointer, inputdata, output, source, spointer) = \
		r.interpret(source, ragaraja, 3, inputdata, array, size)
	return (array, apointer, inputdata, output, source, spointer)
	
if __name__ == '__main__':
    print interpreter('000008008000000011011011004008', [], None, 30)