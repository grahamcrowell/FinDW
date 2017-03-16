import datetime
from enum import Enum
import pandas as pd
import numpy as np
import pandas_datareader.data as web

symbols = ['ADP','ADPI','ADPT','ADS','ADSK','ADTN','ADUS','ADVN','ADVS','AE','AEA','AEC','AEE','AEHR','AEIS','AEL','AEN','AEO','AEP','AEPI','AERG','AERO','AERT','AES','AET','AETI','AEY','AEZ','AF','AFAM','AFCE','AFFM','AFFX','AFFY','AFG','AFL','AFOP','AFP','AFSI','AGAM','AGCO','AGEN','AGII','AGL','AGM','AGN','AGNC','AGO','AGP','AGX','AGYS','AHC','AHCI','AHD','AHGP','AHII','AHL','AHPI','AHR','AHS','AHT','AI','AIG','AIM','AIMC','AIN','AIPC','AIQ','AIR','AIRM','AIRN','AIRT','AIRV','AIS','AIT','AIV','AIZ','AJG','AKAM','AKNS','AKR','AKRX','AKS','ALAN','ALB','ALC','ALCO','ALDA','ALE','ALEX','ALG','ALGN','ALGT','ALJ','ALK','ALKS','ALL','ALLP','ALNC','ALNY','ALOG','ALOT','ALOY','ALSE','ALSK','ALTH','ALTI','ALTR','ALTU','ALX','ALXA','ALXN','ALY','AM','AMAC','AMAG','AMAR','AMAT','AMB','AMCC','AMCS','AMD','AME','AMED','AMFI','AMG','AMGN','AMIC','AMIE','AMIN','AMKR','AMLJ','AMLN','AMMD','AMN','AMNB','AMOT','AMP','AMPH','AMPL','AMR','AMRB','AMRI','AMS','AMSC','AMSF','AMSG','AMSW','AMT','AMTD','AMTY','AMWD','AMZN','AN','ANAD','ANAT','ANCI','ANCX','ANDE','ANDR','ANDS','ANEN','ANF','ANGN','ANGO','ANH','ANIK','ANLY','ANN','ANR','ANSS','ANSV','ANSW','ANTF','ANTP','ANV','ANX','AOI','AOL','AON','AONE','AOS','AP','APA','APAB','APAC','APAG','APC','APD','APEI','APFC','APH','API','APKT','APL','APOG','APOL','APP','APPA','APPY','APSG','APU','APY','ARAY','ARB','ARBA','ARBX','ARCI','ARD','ARDN','ARE','AREX','ARG','ARGN','ARI','ARIA','ARII','ARJ','ARKR','ARL','ARLP','ARM','ARNA','ARO','AROW','ARP','ARQL','ARRS','ARRY','ARSD','ARST','ART','ARTG','ARTN','ARTW','ARTX','ARUN','ARW','ARWD','ARWR','ARYX','ASB','ASBC','ASCA','ASCM','ASEI','ASF','ASFI','ASFN','ASGN','ASGR','ASH','ASI','ASPS','ASRV','ASTC','ASTE','ASTI','ASTM','ASUR','ASYS','ASYT','ATAC','ATC','ATCO','ATEA','ATEC','ATGN','ATHN','ATHR','ATI','ATK','ATLO','ATLS','ATMI','ATML','ATNI','ATO','ATPG','ATR','ATRC','ATRI','ATRM','ATRN','ATRO','ATSG','ATSI','ATU','ATVI','ATW','ATX','AURD','AUTH','AUXL','AVA','AVAV','AVB','AVCA','AVD','AVID','AVII','AVNR','AVNW','AVP','AVR','AVSR','AVT','AVTR','AVX','AVXT','AVY','AVZA','AWBC','AWH','AWI','AWK','AWR','AWRE','AWX','AXAS','AXE','AXK','AXL','AXP','AXR','AXS','AXSI','AXST','AXTI','AYE','AYI','AYR','AZO','AZZ','B','BA','BABY','BAC','BAGL','BAMM','BANF','BANR','BARE','BARI','BAS','BAX','BAYN','BBBB','BBBY','BBEP','BBG','BBGI','BBI','BBND','BBNK','BBOX','BBSI','BBT','BBW','BBX','BBY','BC','BCO','BCON','BCPC','BCR','BCRX','BCSI','BCST','BDC','BDCO','BDGE','BDK','BDN','BDR','BDSI','BDX','BEAT','BEAV','BEBE','BEC','BECN','BEE','BELF','BEN','BERK','BEXP','BEZ','BF','BFED','BFIN','BFLY','BFNB','BFRM','BFS','BFSB','BG','BGC','BGCP','BGFV','BGG','BGH','BGP','BGS','BHB','BHE','BHI','BHIP','BHLB','BHS','BID','BIDZ','BIG','BIIB','BIO','BIOC','BIOD','BIOF','BIOS','BIP','BITS','BJ','BJCT','BJRI','BJS','BK','BKC','BKD','BKE','BKH','BKI','BKMU','BKR','BKRS','BKS','BKUN','BKYF','BLC','BLD','BLDR','BLFS','BLGM','BLK','BLKB','BLL','BLSW','BLT','BLTI','BLUD','BMC','BMI','BMR','BMRC','BMRN','BMS','BMTC','BMTI','BMY','BNCL','BNCN','BNE','BNHN','BNI','BNVI','BNX','BOBE','BOFI','BOFL','BOH','BOKF','BOLT','BONT','BOOM','BOOT','BPAX','BPFH','BPI','BPL','BPO','BPOP','BPSG','BPT','BPUR','BPZ','BR','BRC','BRCD','BRCM','BRE','BRID','BRK','BRKL','BRKR','BRKS','BRLI','BRN','BRNC','BRO','BRS','BRT','BRY','BSDM','BSET','BSMD','BSQR','BSRR','BSTC','BSX','BTFG','BTH','BTIM','BTN','BTU','BTUI','BUCY','BUKS','BUSE','BVSN','BVX','BW','BWA','BWIN','BWLD','BWP','BWS','BWTR','BWY','BX','BXC','BXG','BXP','BXS','BYD','BYI','BZ','BZH','C','CA','CAB','CAC','CACB','CACC','CACH','CACI','CADE','CADX','CAFI','CAG','CAH','CAKE','CAL','CALC','CALD','CALM','CALP','CAM','CAMH','CAMP','CAP','CAPS','CAR','CAS','CASB','CASC','CASH','CASM','CASS','CASY','CAT','CATM','CATO','CATY','CAVM','CAW','CB','CBAN','CBB','CBBO','CBC','CBEY','CBG','CBIN','CBK','CBKN','CBL','CBLI','CBM','CBMC','CBMX','CBNJ','CBNK','CBON','CBOU','CBR','CBRL','CBRX','CBS','CBSH','CBST','CBT','CBTE','CBU','CBZ','CCBG','CCC','CCE','CCEL','CCF','CCI','CCIX','CCK','CCL','CCMP','CCNE','CCO','CCOI','CCRN','CCRT','CCUR','CDE','CDI','CDNS','CDR','CDTI','CDZI','CE','CEC','CECE','CECO','CEDC','CEG','CELG','CELL','CEMJQ','CENT','CENX','CEPH','CERN','CERS','CEVA','CF','CFBK','CFFC','CFFI','CFFN','CFI','CFL','CFN','CFNB','CFNL','CFR','CFS','CFW','CFX','CGI','CGNX','CGX','CHB','CHCI','CHCO','CHD','CHDN','CHDX','CHE','CHEV','CHFC','CHG','CHH','CHK','CHKE','CHMP','CHP','CHRD','CHRS','CHRW','CHS','CHSI','CHTP','CHTT','CHUX','CHYR','CI','CIA','CICI','CIDM','CIE','CIEN','CIGX','CIM','CINF','CIR','CITP','CITZ','CIX','CJBK','CKEC','CKH','CKP','CKR','CKXE','CL','CLC','CLCT','CLD','CLDA','CLDX','CLF','CLFC','CLFD','CLH','CLI','CLMS']

def make_data_frame(symbols, symbol_count=50):
    start = datetime.datetime(1990,1,1)
    end = datetime.datetime(2017,1,1)
    joined = None
    for symbol in symbols:
        try:
            temp_full_df = web.DataReader(symbol,'yahoo',start,end)
            temp_df = pd.DataFrame({'Date':list(temp_full_df.index), symbol:temp_full_df['Open']})
            print('loading {} ({} symbols left)'.format(symbol, symbol_count))
            if joined is None:
                # first loop iteration
                joined = temp_df
            else:
                joined = pd.merge(joined,temp_df,how='outer',on='Date')
                joined.index = joined['Date']
            symbol_count-=1
            if symbol_count == 0:
                break
        except:
            print('\t{} is has no price data'.format(symbol))
    joined.drop('Date',axis=1,inplace=True)
    return joined

joined = make_data_frame(symbols, 500)
joined.info(memory_usage='deep')


##################################################
# RESULTS:
##################################################
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 7016 entries, 1990-01-02 to 1996-12-25
# Columns: 500 entries, ADP to CFNB
# dtypes: float64(500)
# memory usage: 26.8 MB