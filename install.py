import os
choice = input('[+] Kurmak için bas: (Y) Kaldırmak için (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 Loki.py')
    run('mkdir /usr/share/aut')
    run('cp Loki.py /usr/share/aut/Loki.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/Loki.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/Loki.py')
    print('''\n\n Tebrikler programı kurabildin \n from now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('[!] Kaldırıldı ')

