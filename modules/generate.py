import time
import re
import os
import platform
import os.path
import configparser
import subprocess
if not os.path.exists("presets"):
    os.makedirs("presets")
if not os.path.exists("presets/dorktypes"):
    os.makedirs("presets/dorktypes")
if not os.path.exists("presets/keywords"):
    os.makedirs("presets/keywords")
if not os.path.exists("presets/keyword2s"):
    os.makedirs("presets/keyword2s")
if not os.path.exists("presets/pageparameters"):
    os.makedirs("presets/pageparameters")
if not os.path.exists("presets/pagetypes"):
    os.makedirs("presets/pagetypes")
if not os.path.exists("presets/domainextentions"):
    os.makedirs("presets/domainextentions")
if not os.path.exists("presets/searchfunctions"):
    os.makedirs("presets/searchfunctions")
def file_len(fname):
    with open(fname, errors="ignore") as f:
        for i, l in enumerate(f):
            pass
    return i + 1
if not os.path.isfile("presets/dorktypes/preset1.txt"):
    create = open("presets/dorktypes/preset1.txt","w+")
    create.write("(KW).(PT)?(PP)=\n(KW).(PT)?(PP)= site:(DE)\n(SF)\".(DE)\" + \"(KW)\"\n(SF)(KW).(PT)?(PP)=\n(SF)(KW).(PT)?(PP)= site:(DE)\n(SF)(PP)=(KW).(PT)? site:(DE)\n(SF)\"(KW)\" + \"(DE)\".(PT)?(PP)=\n.(PT)?(PP)= \"(KW)\"\n(PP)= \"(KW)\" + \".(DE)\"\n.(PT)? + \".(DE)\" = (KW)\n.(PT)?\"(KW)\" + \".(DE)\" (PP)=\n(SF)(PP)= \"(KW)\" + \".(DE)\n(PP)= (SF)\"(KW)\"\n.(PT)?(SF)\"(KW)\" (PP)=\n\".(DE)\" + \"(KW)\".(PT)?\n(SF)(PP)= + \"(KW)\".(PT)?\n(PP)= (KW).(PT)? (SF)(DE)\n(KW) (PP)= .(PT)?\n(PP)= (KW).(PT)?\n(PP)= .(PT)? (KW)\n.(PT)?(PP)= (KW)\n.(PT)? (KW) (PP)=\n(SF)(PP)= \"(KW)\".(PT)?\n\"(KW)\".(PT)? (SF)(PP)=\n.(PT)?(PP)= (SF)\"(KW)\"\n(SF)\"(KW)\".(PT)?(PP)=\n(SF)\"(KW)\" (PP)= .(PT)?\n(PP)= .(PT)? (SF)\"(KW)\"\n.(PT)?(PP)= (SF)\"(KW)\" + (DE)\n(SF)\"(KW)\" + (DE).(PT)?(PP)=\n(SF)\"(KW)\" + (DE) (PP)= .(PT)?\n(PP)= .(PT)? (SF)\"(KW)\" + (DE)\n.(PT)?(PP)= \"(KW)\" + (DE)\n.(PT)?(PP)= (DE) + \"(KW)\"\n\"(KW)\" + (DE).(PT)?(PP)=\n(DE) + \"(KW)\".(PT)?(PP)=\n\"(KW)\" + (DE) (PP)= .(PT)?\n(PP)= .(PT)? \"(KW)\" + (DE)\n(PP)= (DE) + \"(KW)\".(PT)?\n.(PT)? (DE) + \"(KW)\" (PP)=\n.(PT)? \"(KW)\" + (DE) (PP)=")
    create.close()
if not os.path.isfile("presets/dorktypes/preset2.txt"):
    create = open("presets/dorktypes/preset2.txt","w+")
    create.write(".(PT)?(PP)= \"(KW)\" / (DE)\n.(PT)?(PP)= (DE) / \"(KW)\"\n\"(KW)\" / (DE).(PT)?(PP)=\n(DE) / \"(KW)\".(PT)?(PP)=\n\"(KW)\" / (DE) (PP)= .(PT)?\n(PP)= (DE) / \"(KW)\".(PT)?\n.(PT)? (DE) / \"(KW)\" (PP)=\n.(PT)? \"(KW)\" / (DE) (PP)=\n(KW) / (PT)?(PP)= site:(DE)\n(KW) / (PT)= + site:(DE)")
    create.close()
if not os.path.isfile("presets/dorktypes/preset3.txt"):
    create = open("presets/dorktypes/preset3.txt","w+")
    create.write("\"(KW)\".(PT)?(PP)= \"(KW2)\"\n\"(KW2)\" + \"(KW)\".(PT)?(PP)=\n\"(KW)\" + \"(KW2)\".(PT)?(PP)=\n.(PT)?(PP)= (SF)\"(KW)\" + \"(KW2)\"\n.(PT)?(PP)= (SF)\"(KW2)\" + \"(KW)\"\n(PP)= .(PT)? (SF)\"(KW)\" + \"(KW2)\"\n(PP)= .(PT)? (SF)\"(KW2)\" + \"(KW)\"\n(SF)\"(KW2)\" + \"(KW)\" (PP)= \"(KW)\".(PT)?\n(SF)\"(KW)\" + \"(KW2)\" (PP)= \"(KW)\".(PT)?")
    create.close()
if not os.path.isfile("presets/dorktypes/preset4.txt"):
    create = open("presets/dorktypes/preset4.txt","w+")
    create.write("\"(KW2)\" / \"(KW)\".(PT)?(PP)=\n\"(KW)\" / \"(KW2)\".(PT)?(PP)=\n(PP)= .(PT)? (SF)\"(KW)\" / \"(KW2)\"\n(PP)= .(PT)? (SF)\"(KW2)\" / \"(KW)\"\n.(PT)?(PP)= (SF)\"(KW)\" / \"(KW2)\"\n.(PT)?(PP)= (SF)\"(KW2)\" / \"(KW)\"\n(SF)\"(KW2)\" / \"(KW)\" (PP)= \"(KW)\".(PT)?\n(SF)\"(KW)\" / \"(KW2)\" (PP)= \"(KW)\".(PT)?")
    create.close()
if not os.path.isfile("presets/keywords/preset1.txt"):
    create = open("presets/keywords/preset1.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keywords/preset1.txt")
    create.close()
if not os.path.isfile("presets/keywords/preset2.txt"):
    create = open("presets/keywords/preset2.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keywords/preset2.txt")
    create.close()
if not os.path.isfile("presets/keywords/preset3.txt"):
    create = open("presets/keywords/preset3.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keywords/preset3.txt")
    create.close()
if not os.path.isfile("presets/keywords/preset4.txt"):
    create = open("presets/keywords/preset4.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keywords/preset4.txt")
    create.close()
if not os.path.isfile("presets/keyword2s/preset1.txt"):
    create = open("presets/keyword2s/preset1.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keyword2s/preset1.txt")
    create.close()
if not os.path.isfile("presets/keyword2s/preset2.txt"):
    create = open("presets/keyword2s/preset2.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keyword2s/preset2.txt")
    create.close()
if not os.path.isfile("presets/keyword2s/preset3.txt"):
    create = open("presets/keyword2s/preset3.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keyword2s/preset3.txt")
    create.close()
if not os.path.isfile("presets/keyword2s/preset4.txt"):
    create = open("presets/keyword2s/preset4.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/keyword2s/preset4.txt")
    create.close()
if not os.path.isfile("presets/pageparameters/preset1.txt"):
    create = open("presets/pageparameters/preset1.txt","w+")
    create.write("page_id\ncat\ncategory\nid\ncoID\navd\ninclude\nparam\npanel\nsec\nitem_id\nproduct_id\npurchase_id\nlogin_id\nuser_id\nregister\ngame_id\ntype\ntype_id\ngamer_id\nusername_id")
    create.close()
if not os.path.isfile("presets/pageparameters/preset2.txt"):
    create = open("presets/pageparameters/preset2.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/pageparameters/preset2.txt")
    create.close()
if not os.path.isfile("presets/pageparameters/preset3.txt"):
    create = open("presets/pageparameters/preset3.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/pageparameters/preset3.txt")
    create.close()
if not os.path.isfile("presets/pageparameters/preset4.txt"):
    create = open("presets/pageparameters/preset4.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/pageparameters/preset4.txt")
    create.close()
if not os.path.isfile("presets/pagetypes/preset1.txt"):
    create = open("presets/pagetypes/preset1.txt","w+")
    create.write("php\nphp4\nphp3\nasp\nhtml\njsp\naspx\ncgi\ncfm\nflv\npdf\njsf\nasinx\npsml\nraw\nfile\ntss\nblog\nhtm")
    create.close()
if not os.path.isfile("presets/pagetypes/preset2.txt"):
    create = open("presets/pagetypes/preset2.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/pagetypes/preset2.txt")
    create.close()
if not os.path.isfile("presets/pagetypes/preset3.txt"):
    create = open("presets/pagetypes/preset3.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/pagetypes/preset3.txt")
    create.close()
if not os.path.isfile("presets/pagetypes/preset4.txt"):
    create = open("presets/pagetypes/preset4.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/pagetypes/preset4.txt")
    create.close()
if not os.path.isfile("presets/domainextentions/preset1.txt"):
    create = open("presets/domainextentions/preset1.txt","w+")
    create.write("com\nnet\norg\nco\nus")
    create.close()
if not os.path.isfile("presets/domainextentions/preset2.txt"):
    create = open("presets/domainextentions/preset2.txt","w+")
    create.write("aaa\naarp\nabarth\nabb\nabbott\nabbvie\nabc\nabogado\nabudhabi\nacademy\naccenture\naccountant\naccountants\naco\nactive\nactor\nads\nadult\naeg\naero\naetna\nafl\nafrica\nagakhan\nagency\naig\naigo\nairbus\nairforce\nairtel\nakdn\nalfaromeo\nalibaba\nalipay\nallfinanz\nallstate\nally\nalsace\nalstom\namex\namica\namsterdam\nanalytics\nandroid\nanz\naol\napartments\napp\napple\naquarelle\narab\naramco\narchi\narmy\nart\narte\nasia\nassociates\nattorney\nauction\naudi\naudible\naudio\nauspost\nauthor\nauto\nautos\naws\naxa\nazure\nbaby\nbaidu\nbananarepublic\nband\nbank\nbar\nbarcelona\nbarclaycard\nbarclays\nbarefoot\nbargains\nbaseball\nbasketball\nbauhaus\nbayern\nbbc\nbbt\nbbva\nbcg\nbcn\nbeauty\nbeer\nbentley\nberlin\nbest\nbestbuy\nbet\nbharti\nbible\nbid\nbike\nbing\nbingo\nbio\nbiz\nblack\nblackfriday\nblanco\nblockbuster\nblog\nbloomberg\nblue\nbms\nbmw\nbnl\nbnpparibas\nboehringer\nbom\nbond\nboo\nbook\nbooking\nboots\nbosch\nbostik\nboston\nbot\nboutique\nbox\nbradesco\nbridgestone\nbroadway\nbroker\nbrother\nbrussels\nbudapest\nbugatti\nbuild\nbuilders\nbusiness\nbuy\nbuzz\nbzh\ncab\ncafe\ncal\ncall\ncalvinklein\ncam\ncamera\ncamp\ncancerresearch\ncanon\ncapetown\ncapital\ncapitalone\ncar\ncaravan\ncards\ncare\ncareer\ncareers\ncars\ncartier\ncasa\ncase\ncash\ncasino\ncat\ncatering\ncatholic\ncba\ncbn\ncbre\ncbs\ncenter\nceo\ncern\ncfa\ncfd\nchanel\nchannel\nchase\nchat\ncheap\nchintai\nchristmas\nchrome\nchrysler\nchurch\ncipriani\ncircle\ncisco\ncitadel\nciti\ncitic\ncity\nclaims\ncleaning\nclick\nclinic\nclinique\nclothing\ncloud\nclub\nclubmed\ncoach\ncodes\ncoffee\ncollege\ncologne\ncomcast\ncommbank\ncommunity\ncompany\ncompare\ncomputer\ncondos\nconstruction\nconsulting\ncontact\ncontractors\ncooking\ncool\ncoop\ncorsica\ncountry\ncoupon\ncoupons\ncourses\ncredit\ncreditcard\ncreditunion\ncricket\ncrown\ncrs\ncruise\ncruises\ncsc\ncuisinella\ncymru\ndabur\ndad\ndance\ndata\ndate\ndating\ndatsun\nday\ndeal\ndealer\ndeals\ndegree\ndelivery\ndell\ndeloitte\ndelta\ndemocrat\ndental\ndentist\ndesi\ndesign\ndev\ndhl\ndiamonds\ndiet\ndigital\ndirect\ndirectory\ndiscount\ndiscover\ndish\ndiy\ndnp\ndocs\ndoctor\ndodge\ndog\ndoha\ndomains\ndot\ndownload\ndrive\ndubai\nduck\ndunlop\ndupont\ndurban\ndvag\nearth\neat\neco\nedeka\neducation\nemail\nemerck\nenergy\nengineer\nengineering\nenterprises\nepost\nepson\nequipment\nericsson\nerni\nesq\nestate\nesurance\netisalat\neurovision\neus\nevents\neverbank\nexample\nexchange\nexpert\nexposed\nexpress\nextraspace\nfage\nfail\nfairwinds\nfaith\nfamily\nfan\nfans\nfarm\nfarmers\nfashion\nfast\nFedEx\nfeedback\nferrari\nferrero\nfiat\nfidelity\nfilm\nfinal\nfinance\nfinancial\nfire\nfirestone\nfirmdale\nfish\nfishing\nfit\nfitness\nflickr\nflights\nflir\nflorist\nflowers\nflsmidth\nfly\nfoo\nfood\nfoodnetwork\nfootball\nford\nforex\nforsale\nforum\nfoundation\nfox\nfree\nfresenius\nfrl\nfrogans\nfrontdoor\nfrontier\nfujitsu\nfujixerox\nfun\nfund\nfurniture\nfutbol\nfyi\ngal\ngallery\ngallo\ngallup\ngame\ngames\ngap\ngarden\ngbiz\ngea\ngent\ngenting\ngift\ngifts\ngives\ngiving\nglass\ngle\nglobal\nglobo\ngmail\ngmbh\ngmo\ngmx\ngodaddy\ngold\ngoldpoint\ngolf\ngoodyear\ngoogle\ngop\ngrainger\ngraphics\ngratis\ngreen\ngripe\ngrocery\ngroup\nguardian\ngucci\nguide\nguitars\nguru\nhair\nhamburg\nhangout\nhaus\nhbo\nhdfc\nhdfcbank\nhealth\nhealthcare\nhelp\nhelsinki\nhere\nhermes\nhiphop\nhisamitsu\nhitachi\nhiv\nhkt\nhockey\nholdings\nholiday\nhomegoods\nhomes\nhomesense\nhonda\nhoneywell\nhorse\nhospital\nhost\nhosting\nhot\nhoteles\nhotels\nhotmail\nhouse\nhow\nhsbc\nhtc\nhughes\nhyatt\nhyundai\nibm\nice\nieee\nifm\nikano\nimdb\nimmo\nimmobilien\nindustries\ninfiniti\ninfo\ning\nink\ninstitute\ninsurance\ninsure\nintel\ninternational\nintuit\ninvalid\ninvestments\nipiranga\nirish\niselect\nist\nistanbul\nitau\nitv\niveco\njaguar\njava\njcb\njcp\njeep\njetzt\njewelry\njobs\njoburg\njoy\njpmorgan\njuegos\njuniper\nkaufen\nkddi\nkerryhotels\nkerrylogistics\nkfh\nkia\nkim\nkinder\nkindle\nkitchen\nkiwi\nkoeln\nkomatsu\nkpmg\nkrd\nkred\nkuokgroup\nkyoto\nlacaixa\nladbrokes\nlamborghini\nlancaster\nlancia\nlancome\nland\nlandrover\nlanxess\nlasalle\nlat\nlatino\nlatrobe\nlaw\nlawyer\nlds\nlease\nlegal\nlego\nlexus\nlgbt\nliaison\nlidl\nlife\nlifeinsurance\nlifestyle\nlighting\nlike\nlilly\nlimited\nlimo\nlincoln\nlinde\nlink\nlipsy\nlive\nliving\nlixil\nloan\nloans\nlocal\nlocalhost\nlocker\nlocus\nlol\nlondon\nlotte\nlotto\nlove\nlpl\nlplfinancial\nltda\nlundbeck\nlupin\nluxe\nluxury\nmacys\nmadrid\nmaif\nmaison\nmakeup\nman\nmanagement\nmango\nmap\nmarket\nmarketing\nmarkets\nmarriott\nmaserati\nmattel\nmba\nmcd\nmcdonalds\nmckinsey\nmed\nmedia\nmeet\nmelbourne\nmeme\nmemorial\nmen\nmenu\nmeo\nmetlife\nmiami\nmicrosoft\nmini\nmint\nmit\nmitsubishi\nmlb\nmma\nmobi\nmobile\nmobily\nmoda\nmoe\nmoi\nmom\nmonash\nmoney\nmormon\nmortgage\nmoscow(ru)\nmoto\nmotorcycles\nmov\nmovie\nmovistar\nmsd\nmtn\nmtpc\nmtr\nmuseum\nmutual\nmutuelle\nnadex\nnagoya\nname\nnationwide\nnatura\nnavy\nnba\nnec\nnetflix\nnetwork\nneustar\nnew\nnewholland\nnews\nnexus\nnfl\nngo\nnhk\nnico\nnike\nnikon\nninja\nnissan\nnissay\nnokia\nnorton\nnow\nnra\nnrw\nntt\nnyc\nobi\nobserver\noff\noffice\nokinawa\nomega\none\nong\nonion\nonl\nonline\nooo\nopen\noracle\norange\norganic\norientexpress\norigins\nosaka\notsuka\novh\npage\npamperedchef\npanasonic\nparis\npartners\nparts\nparty\npassagens\npay\npccw\npet\npfizer\npharmacy\nphilips\nphone\nphoto\nphotography\nphotos\nphysio\npiaget\npics\npictet\npictures\npid\npin\nping\npink\npioneer\npizza\nplace\nplay\nplaystation\nplumbing\nplus\npohl\npoker\npolitie\nporn\npost\npraxi\npress\nprime\npro\nprod\nproductions\nprof\nprogressive\npromo\nproperties\nproperty\nprotection\npru\nprudential\npub\npwc\nqpon\nquebec\nquest\nqvc\nracing\nradio\nread\nrealestate\nrealtor\nrealty\nrecipes\nred\nredstone\nrehab\nreise\nreisen\nreit\nreliance\nren\nrent\nrentals\nrepair\nreport\nrepublican\nrest\nrestaurant\nreview\nreviews\nrexroth\nrich\nricoh\nrio\nrip\nrmit\nrocher\nrocks\nrodeo\nrogers\nroom\nrsvp\nrugby\nruhr\nrun\nrwe\nryukyu\nsaarland\nsafe\nsafety\nsakura\nsale\nsamsung\nsandvik\nsanofi\nsap\nsarl\nsave\nsaxo\nsbi\nsbs\nsca\nscb\nschaeffler\nschmidt\nscholarships\nschool\nschule\nschwarz\nscience\nscjohnson\nscor\nscot\nsearch\nseat\nsecure\nsecurity\nseek\nselect\nsener\nservices\nses\nseven\nsew\nsex\nsexy\nsfr\nshangrila\nsharp\nshaw\nshell\nshiksha\nshoes\nshop\nshopping\nshouji\nshow\nshowtime\nshriram\nsilk\nsina\nsingles\nsite\nski\nskin\nsky\nskype\nsling\nsmart\nsmile\nsncf\nsoccer\nsocial\nsoftbank\nsoftware\nsohu\nsolar\nsolutions\nsong\nSony\nsoy\nspace\nspiegel\nspot\nspreadbetting\nstada\nstaples\nstar\nstarhub\nstatebank\nstatefarm\nstatoil\nstc\nstcgroup\nstockholm\nstorage\nstore\nstream\nstudio\nstudy\nstyle\nsucks\nsupplies\nsupply\nsupport\nsurf\nsurgery\nsuzuki\nswatch\nswiftcover\nswiss\nsydney\nsymantec\nsystems\ntaipei\ntalk\ntaobao\ntarget\ntatamotors\ntatar\ntattoo\ntax\ntaxi\ntdk\nteam\ntech\ntechnology\ntel\ntelecity\ntelefonica\ntemasek\ntennis\ntest\nteva\ntheater\ntheatre\ntickets\ntienda\ntiffany\ntips\ntires\ntirol\ntjx\ntoday\ntokyo\ntools\ntop\ntoray\ntoshiba\ntotal\ntours\ntown\ntoyota\ntoys\ntrade\ntrading\ntraining\ntravel\ntravelchannel\ntravelers\ntrust\ntube\ntui\ntunes\ntushu\ntvs\nubs\nuconnect\nunicom\nuniversity\nuno\nuol\nups\nvacations\nvanguard\nvegas\nventures\nverisign\nversicherung\nvet\nviajes\nvideo\nvig\nviking\nvillas\nvip\nvirgin\nvisa\nvision\nvista\nvistaprint\nvivo\nvlaanderen\nvodka\nvolkswagen\nvolvo\nvote\nvoting\nvoto\nvoyage\nvuelos\nwales\nwalmart\nwalter\nwang\nwanggou\nwatch\nwatches\nweather\nweatherchannel\nwebcam\nweber\nwebsite\nwed\nwedding\nweibo\nweir\nwhoswho\nwien\nwiki\nwilliamhill\nwin\nwindows\nwine\nwinners\nwme\nwolterskluwer\nwoodside\nwork\nworks\nworld\nwow\nwtc\nwtf\nxbox\nxerox\nxfinity\nxihuan\nxperia\nxxx\nxyz\nyachts\nyahoo\nyamaxun\nyandex\nyodobashi\nyoga\nyokohama\nyou\nyoutube\nzappos\nzara\nzero\nzip\nzippo\nzone\nzuerich")
    create.close()
if not os.path.isfile("presets/domainextentions/preset3.txt"):
    create = open("presets/domainextentions/preset3.txt","w+")
    create.write("ac\nad\nae\naf\nag\nai\nal\nam\nan\nao\naq\nar\narpa\nas\nat\nau\naw\nax\naz\nba\nbb\nbd\nbe\nbf\nbg\nbh\nbi\nbj\nbl\nbm\nbn\nbo\nbq\nbr\nbs\nbt\nbv\nbw\nby\nbz\nca\ncc\ncd\ncf\ncg\nch\nci\nck\ncl\ncm\ncn\nco\ncouk\ncom\ncomtr\ncr\ncu\ncv\ncw\ncx\ncy\ncz\nde\ndj\ndk\ndm\ndo\ndz\nec\nedu\nee\neg\neh\ner\nes\net\neu\nfi\nfj\nfk\nfm\nfo\nfr\nga\ngb\ngd\nge\ngf\ngg\ngh\ngi\ngl\ngm\ngn\ngov\ngp\ngq\ngr\ngs\ngt\ngu\ngw\ngy\nhk\nhm\nhn\nhr\nht\nhu\nid\nie\nil\nim\nin\nint\nio\niq\nir\nis\nit\nje\njm\njo\njp\nke\nkg\nkh\nki\nkm\nkn\nkp\nkr\nkw\nky\nkz\nla\nlb\nlc\nli\nlk\nlr\nls\nlt\nlu\nlv\nly\nma\nmc\nmd\nme\nmf\nmg\nmh\nmil\nmk\nml\nmm\nmn\nmo\nmp\nmq\nmr\nms\nmt\nmu\nmv\nmw\nmx\nmy\nmz\nna\nnc\nne\nnet\nnf\nng\nni\nnl\nno\nnp\nnr\nnu\nnz\nom\norg\npa\npe\npf\npg\nph\npk\npl\npm\npn\npr\nps\npt\npw\npy\nqa\nre\nro\nrs\nru\nrw\nsa\nsb\nsc\nsd\nse\nsg\nsh\nsi\nsj\nsk\nsl\nsm\nsn\nso\nsr\nss\nst\nsu\nsv\nsx\nsy\nsz\ntc\ntd\ntf\ntg\nth\ntj\ntk\ntl\ntm\ntn\nto\ntp\ntr\ntt\ntv\ntw\ntz\nua\nug\nuk\num\nus\nuy\nuz\nva\nvc\nve\nvg\nvi\nvn\nvu\nwf\nws\nye\nyt\nza\nzm\nzw\nru")
    create.close()
if not os.path.isfile("presets/domainextentions/preset4.txt"):
    create = open("presets/domainextentions/preset4.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/domainextentions/preset4.txt")
    create.close()
if not os.path.isfile("presets/searchfunctions/preset1.txt"):
    create = open("presets/searchfunctions/preset1.txt","w+")
    create.write("inurl:\nintext:\nallintext:\nallintitle:\nsource:\nfiletype:\ninsubject:\nallinanchor:\nallinurl:\ncache:\ninanchor:\ninfo:\nintitle:\nlink:")
    create.close()
if not os.path.isfile("presets/searchfunctions/preset2.txt"):
    create = open("presets/searchfunctions/preset2.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/searchfunctions/preset2.txt")
    create.close()
if not os.path.isfile("presets/searchfunctions/preset3.txt"):
    create = open("presets/searchfunctions/preset3.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/searchfunctions/preset3.txt")
    create.close()
if not os.path.isfile("presets/searchfunctions/preset4.txt"):
    create = open("presets/searchfunctions/preset4.txt","w+")
    create.write("This preset is empty, you can edit this preset in presets/searchfunctions/preset4.txt")
    create.close()
empty = re.compile("This preset is empty")
print("Dorktypes:")
print("1. Preset1")
print("2. Preset2")
print("3. Preset3")
print("4. Preset4")
print("You can edit the presets in /presets/dorktypes/.")
selecting = 1
while selecting == 1:
    try:
        dorkselect = int(input("Select the dorktype preset you want to use:"))
    except:
        dorkselect = 404
    if dorkselect == 1:
        print("You selected dorktype preset 1.")
        selecteddorklist = "presets/dorktypes/preset1.txt"
        selecting = 2
    elif dorkselect == 2:
        print("You selected dorktype preset 2.")
        selecteddorklist = "presets/dorktypes/preset2.txt"
        selecting = 2
    elif dorkselect == 3:
        print("You selected dorktype preset 3.")
        selecteddorklist = "presets/dorktypes/preset3.txt"
        selecting = 2
    elif dorkselect == 4:
        print("You selected dorktype preset 4.")
        selecteddorklist = "presets/dorktypes/preset4.txt"
        selecting = 2
    else:
        print("You didn't select a valid option, please try again.")
    if selecting == 2:
        if not os.stat(selecteddorklist).st_size < 1:
            f = open(selecteddorklist)
            if not empty.match(f.read()):
                selecting = 0
                f.close()
            else:
                f.close()
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
        else:
            print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
            selecting = 1
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
has = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        if ('(kw)' in dorktype) or ('(KW)' in dorktype):
            has += 1
if has >= 1:
    print("Keyword")
    print("1. Preset1")
    print("2. Preset2")
    print("3. Preset3")
    print("4. Preset4")
    print("You can edit the presets in /presets/keywords/.")
    selecting = 1
    while selecting == 1:
        try:
            keywordselect = int(input("Select the keyword preset you want to use:"))
        except:
            keywordselect = 404
        if keywordselect == 1:
            print("You selected keyword preset 1.")
            selectedkeywordlist = "presets/keywords/preset1.txt"
            selecting = 2
        elif keywordselect == 2:
            print("You selected keyword preset 2.")
            selectedkeywordlist = "presets/keywords/preset2.txt"
            selecting = 2
        elif keywordselect == 3:
            print("You selected keyword preset 3.")
            selectedkeywordlist = "presets/keywords/preset3.txt"
            selecting = 2
        elif keywordselect == 4:
            print("You selected keyword preset 4.")
            selectedkeywordlist = "presets/keywords/preset4.txt"
            selecting = 2
        else:
            print("You didn't select a valid option, please try again.")
        if selecting == 2:
            if not os.stat(selectedkeywordlist).st_size < 1:
                f = open(selectedkeywordlist)
                if not empty.match(f.read()):
                    selecting = 0
                    f.close()
                else:
                    f.close()
                    print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                    selecting = 1
            else:
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
else:
    selectedkeywordlist = "presets/keywords/preset1.txt"
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
has = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        if ('(kw2)' in dorktype) or ('(KW2)' in dorktype):
            has += 1
if has >= 1:
    print("Keyword2")
    print("1. Preset1")
    print("2. Preset2")
    print("3. Preset3")
    print("4. Preset4")
    print("You can edit the presets in /presets/keyword2s/.")
    selecting = 1
    while selecting == 1:
        try:
            keyword2select = int(input("Select the keyword2 preset you want to use:"))
        except:
            keyword2select = 404
        if keyword2select == 1:
            print("You selected keyword2 preset 1.")
            selectedkeyword2list = "presets/keyword2s/preset1.txt"
            selecting = 2
        elif keyword2select == 2:
            print("You selected keyword2 preset 2.")
            selectedkeyword2list = "presets/keyword2s/preset2.txt"
            selecting = 2
        elif keyword2select == 3:
            print("You selected keyword2 preset 3.")
            selectedkeyword2list = "presets/keyword2s/preset3.txt"
            selecting = 2
        elif keyword2select == 4:
            print("You selected keyword2 preset 4.")
            selectedkeyword2list = "presets/keyword2s/preset4.txt"
            selecting = 2
        else:
            print("You didn't select a valid option, please try again.")
        if selecting == 2:
            if not os.stat(selectedkeyword2list).st_size < 1:
                f = open(selectedkeyword2list)
                if not empty.match(f.read()):
                    selecting = 0
                    f.close()
                else:
                    f.close()
                    print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                    selecting = 1
            else:
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
else:
    selectedkeyword2list = "presets/keyword2s/preset1.txt"
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
has = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        if ('(pp)' in dorktype) or ('(PP)' in dorktype):
            has += 1
if has >= 1:
    print("Pageparameter")
    print("1. Preset1")
    print("2. Preset2")
    print("3. Preset3")
    print("4. Preset4")
    print("You can edit the presets in /presets/pageparameters/.")
    selecting = 1
    while selecting == 1:
        try:
            pageparameterselect = int(input("Select the pageparameter preset you want to use:"))
        except:
            pageparameterselect = 404
        if pageparameterselect == 1:
            print("You selected pageparameter preset 1.")
            selectedpageparameterlist = "presets/pageparameters/preset1.txt"
            selecting = 2
        elif pageparameterselect == 2:
            print("You selected pageparameter preset 2.")
            selectedpageparameterlist = "presets/pageparameters/preset2.txt"
            selecting = 2
        elif pageparameterselect == 3:
            print("You selected pageparameter preset 3.")
            selectedpageparameterlist = "presets/pageparameters/preset3.txt"
            selecting = 2
        elif pageparameterselect == 4:
            print("You selected pageparameter preset 4.")
            selectedpageparameterlist = "presets/pageparameters/preset4.txt"
            selecting = 2
        else:
            print("You didn't select a valid option, please try again.")
        if selecting == 2:
            if not os.stat(selectedpageparameterlist).st_size < 1:
                f = open(selectedpageparameterlist)
                if not empty.match(f.read()):
                    selecting = 0
                    f.close()
                else:
                    f.close()
                    print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                    selecting = 1
            else:
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
else:
    selectedpageparameterlist = "presets/pageparameters/preset1.txt"
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
has = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        if ('(pt)' in dorktype) or ('(PT)' in dorktype):
            has += 1
if has >= 1:
    print("Pagetype")
    print("1. Preset1")
    print("2. Preset2")
    print("3. Preset3")
    print("4. Preset4")
    print("You can edit the presets in /presets/pagetypes/.")
    selecting = 1
    while selecting == 1:
        try:
            pagetypeselect = int(input("Select the pagetype preset you want to use:"))
        except:
            pagetypeselect = 404
        if pagetypeselect == 1:
            print("You selected pagetype preset 1.")
            selectedpagetypelist = "presets/pagetypes/preset1.txt"
            selecting = 2
        elif pagetypeselect == 2:
            print("You selected pagetype preset 2.")
            selectedpagetypelist = "presets/pagetypes/preset2.txt"
            selecting = 2
        elif pagetypeselect == 3:
            print("You selected pagetype preset 3.")
            selectedpagetypelist = "presets/pagetypes/preset3.txt"
            selecting = 2
        elif pagetypeselect == 4:
            print("You selected pagetype preset 4.")
            selectedpagetypelist = "presets/pagetypes/preset4.txt"
            selecting = 2
        else:
            print("You didn't select a valid option, please try again.")
        if selecting == 2:
            if not os.stat(selectedpagetypelist).st_size < 1:
                f = open(selectedpagetypelist)
                if not empty.match(f.read()):
                    selecting = 0
                    f.close()
                else:
                    f.close()
                    print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                    selecting = 1
            else:
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
else:
    selectedpagetypelist = "presets/pagetypes/preset1.txt"
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
has = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        if ('(de)' in dorktype) or ('(DE)' in dorktype):
            has += 1
if has >= 1:
    print("Domainextention")
    print("1. Preset1")
    print("2. Preset2")
    print("3. Preset3")
    print("4. Preset4")
    print("You can edit the presets in /presets/domainextentions/.")
    selecting = 1
    while selecting == 1:
        try:
            domainextentionselect = int(input("Select the domainextention preset you want to use:"))
        except:
            domainextentionselect = 404
        if domainextentionselect == 1:
            print("You selected domainextention preset 1.")
            selecteddomainextentionlist = "presets/domainextentions/preset1.txt"
            selecting = 2
        elif domainextentionselect == 2:
            print("You selected domainextention preset 2.")
            selecteddomainextentionlist = "presets/domainextentions/preset2.txt"
            selecting = 2
        elif domainextentionselect == 3:
            print("You selected domainextention preset 3.")
            selecteddomainextentionlist = "presets/domainextentions/preset3.txt"
            selecting = 2
        elif domainextentionselect == 4:
            print("You selected domainextention preset 4.")
            selecteddomainextentionlist = "presets/domainextentions/preset4.txt"
            selecting = 2
        else:
            print("You didn't select a valid option, please try again.")
        if selecting == 2:
            if not os.stat(selecteddomainextentionlist).st_size < 1:
                f = open(selecteddomainextentionlist)
                if not empty.match(f.read()):
                    selecting = 0
                    f.close()
                else:
                    f.close()
                    print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                    selecting = 1
            else:
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
else:
    selecteddomainextentionlist = "presets/domainextentions/preset1.txt"
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
has = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        if ('(sf)' in dorktype) or ('(SF)' in dorktype):
            has += 1
if has >= 1:
    print("Searchfunction")
    print("1. Preset1")
    print("2. Preset2")
    print("3. Preset3")
    print("4. Preset4")
    print("You can edit the presets in /presets/searchfunctions/.")
    selecting = 1
    while selecting == 1:
        try:
            searchfunctionselect = int(input("Select the searchfunction preset you want to use:"))
        except:
            searchfunctionselect = 404
        if searchfunctionselect == 1:
            print("You selected searchfunction preset 1.")
            selectedsearchfunctionlist = "presets/searchfunctions/preset1.txt"
            selecting = 2
        elif searchfunctionselect == 2:
            print("You selected searchfunction preset 2.")
            selectedsearchfunctionlist = "presets/searchfunctions/preset2.txt"
            selecting = 2
        elif searchfunctionselect == 3:
            print("You selected searchfunction preset 3.")
            selectedsearchfunctionlist = "presets/searchfunctions/preset3.txt"
            selecting = 2
        elif searchfunctionselect == 4:
            print("You selected searchfunction preset 4.")
            selectedsearchfunctionlist = "presets/searchfunctions/preset4.txt"
            selecting = 2
        else:
            print("You didn't select a valid option, please try again.")
        if selecting == 2:
            if not os.stat(selectedsearchfunctionlist).st_size < 1:
                f = open(selectedsearchfunctionlist)
                if not empty.match(f.read()):
                    selecting = 0
                    f.close()
                else:
                    f.close()
                    print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                    selecting = 1
            else:
                print("The preset you selected is empty, please choose an other preset or change the content of the preset.")
                selecting = 1
else:
    selectedsearchfunctionlist = "presets/searchfunctions/preset1.txt"
if platform.system() == "Linux":
    clear = lambda: os.system('clear')
    clear()
if platform.system() == "Windows":
    clear = lambda: os.system('cls')
    clear()
totalcount = 0
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        currentcount = 1
        if ('(kw)' in dorktype) or ('(KW)' in dorktype):
            currentcount = currentcount * file_len(selectedkeywordlist)
        if ('(kw2)' in dorktype) or ('(KW2)' in dorktype):
            currentcount = currentcount * file_len(selectedkeyword2list)
        if ('(pp)' in dorktype) or ('(PP)' in dorktype):
            currentcount = currentcount * file_len(selectedpageparameterlist)
        if ('(pt)' in dorktype) or ('(PT)' in dorktype):
            currentcount = currentcount * file_len(selectedpagetypelist)
        if ('(de)' in dorktype) or ('(DE)' in dorktype):
            currentcount = currentcount * file_len(selecteddomainextentionlist)
        if ('(sf)' in dorktype) or ('(SF)' in dorktype):
            currentcount = currentcount * file_len(selectedsearchfunctionlist)
        totalcount = totalcount + currentcount
print("Generating " + str(totalcount) + " dorks.")
startt = time.time()
kwps = open("keyword_processing.txt","w+")
print("Processing keywords")
with open(selecteddorklist, 'r', encoding="ISO-8859-1", errors="ignore") as dorktypes:
    for dorktype in dorktypes:
        dorktype = dorktype.rstrip('\n')
        if ('(kw)' in dorktype) or ('(KW)' in dorktype):
            with open(selectedkeywordlist, 'r', encoding="ISO-8859-1", errors="ignore") as keywords:
                for keyword in keywords:
                    keyword = keyword.rstrip('\n')
                    kwps.write(re.sub(r'(?i)\(kw\)', keyword, dorktype + "\n"))
        else:
            kwps.write(dorktype + "\n")
kwps.close()
kw2ps = open("keyword2_processing.txt","w+")
print("Processing keyword2s")
with open("keyword_processing.txt", 'r', encoding="ISO-8859-1", errors="ignore") as kwps:
    with open(selectedkeyword2list, 'r', encoding="ISO-8859-1", errors="ignore") as keyword2s:
        for kwp in kwps:
            kwp = kwp.rstrip('\n')
            if ('(kw2)' in kwp) or ('(KW2)' in kwp):
                keyword2s.seek(0)
                for keyword2 in keyword2s:
                    keyword2 = keyword2.rstrip('\n')
                    kw2ps.write(re.sub(r'(?i)\(kw2\)', keyword2, kwp + "\n"))
            else:
                kw2ps.write(kwp + "\n")
kw2ps.close()
os.remove("keyword_processing.txt")
ppps = open("pageparameter_processing.txt","w+")
print("Processing pageparameters")
with open("keyword2_processing.txt", 'r', encoding="ISO-8859-1", errors="ignore") as kw2ps:
    with open(selectedpageparameterlist, 'r', encoding="ISO-8859-1", errors="ignore") as pageparameters:
        for kw2p in kw2ps:
            kw2p = kw2p.rstrip('\n')
            if ('(pp)' in kw2p) or ('(PP)' in kw2p):
                pageparameters.seek(0)
                for pageparameter in pageparameters:
                    pageparameter = pageparameter.rstrip('\n')
                    ppps.write(re.sub(r'(?i)\(pp\)', pageparameter, kw2p + "\n"))
            else:
                ppps.write(kw2p + "\n")
ppps.close()
os.remove("keyword2_processing.txt")
ptps = open("pagetype_processing.txt","w+")
print("Processing pagetypes")
with open("pageparameter_processing.txt", 'r', encoding="ISO-8859-1", errors="ignore") as ppps:
    with open(selectedpagetypelist, 'r', encoding="ISO-8859-1", errors="ignore") as pagetypes:
        for ppp in ppps:
            ppp = ppp.rstrip('\n')
            if ('(pt)' in ppp) or ('(PT)' in ppp):
                pagetypes.seek(0)
                for pagetype in pagetypes:
                    pagetype = pagetype.rstrip('\n')
                    ptps.write(re.sub(r'(?i)\(pt\)', pagetype, ppp + "\n"))
            else:
                ptps.write(ppp + "\n")
ptps.close()
os.remove("pageparameter_processing.txt")
deps = open("domainextention_processing.txt","w+")
print("Processing domainextentions")
with open("pagetype_processing.txt", 'r', encoding="ISO-8859-1", errors="ignore") as ptps:
    with open(selecteddomainextentionlist, 'r', encoding="ISO-8859-1", errors="ignore") as domainextentions:
        for ptp in ptps:
            ptp = ptp.rstrip('\n')
            if ('(de)' in ptp) or ('(DE)' in ptp):
                domainextentions.seek(0)
                for domainextention in domainextentions:
                    domainextention = domainextention.rstrip('\n')
                    deps.write(re.sub(r'(?i)\(de\)', domainextention, ptp + "\n"))
            else:
                deps.write(ptp + "\n")
deps.close()
os.remove("pagetype_processing.txt")
sfps = open("searchfunction_processing.txt","w+")
print("Processing searchfunctions")
with open("domainextention_processing.txt", 'r', encoding="ISO-8859-1", errors="ignore") as deps:
    with open(selectedsearchfunctionlist, 'r', encoding="ISO-8859-1", errors="ignore") as searchfunctions:
        for dep in deps:
            dep = dep.rstrip('\n')
            if ('(sf)' in dep) or ('(SF)' in dep):
                searchfunctions.seek(0)
                for searchfunction in searchfunctions:
                    searchfunction = searchfunction.rstrip('\n')
                    sfps.write(re.sub(r'(?i)\(sf\)', searchfunction, dep + "\n"))
            else:
                sfps.write(dep + "\n")
sfps.close()
os.remove("domainextention_processing.txt")
finding = 1
fnum = 1
while finding == 1:
    if os.path.isfile("output_" + str(fnum) + ".txt"):
        fnum += 1
    else:
        os.rename("searchfunction_processing.txt", "output_" + str(fnum) + ".txt")
        finding = 0
print("Done generating")
print("It took " + str(round(time.time() - startt)) + " seconds to generate.")
input("Press enter to continue...")
if platform.system() == "Linux":
    p = subprocess.call(["python3", "start.py"])
if platform.system() == "Windows":
    p = subprocess.call(["python", "start.py"])
