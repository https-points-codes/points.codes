IDNtechnician = input("Assigned Technician: ");IDNidn = input("Enter IDN: ");IDNlocation = "815 Kinoole St., Hilo, HI 96720  |   Open Sundays - Saturdays, 8:30 am - 4:30 pm";file = open("viewReport.html","a");file.write("\n")
file.write("\n");file.write(IDNidn);file.write(" = [\"");IDNname = input("Item name: ");IDNcondition = input("Item condition: ");IDNnotes = input("Item notes: ");IDNprocessor = input("Item processor: ");IDNram = input("Item RAM: ");IDNstorage = input("Item storage capacity: ");IDNdim = input("Item dimensions (x-axis x y-axis x z-axis): ");IDNyear = input("Current year (YYYY): ");IDNmonth = input("Current month (M e.g. 5): ");IDNday = input("Current day (D e.g. 3): ");IDNtime = input("Current time (12-24:m std format (e.g. 13:5): ");usd = input("USD: ");IDNposts = input("Is the item online? Y/N: ")
if IDNposts == "Y":
    file.write(posts)
    IDNtargets = input("CL-Craigslist? Y/N: ")
    if IDNtargets == "Y":
        IDN2 = "[POSTED-CL-$/"
        file.write(IDN2)
        file.write(IDNyear);file.write("/");file.write(IDNmonth);file.write("/");file.write(IDNday);file.write("\"],\"")
        IDN0 = [IDN2,usd,IDNname,IDNcondition,IDNnotes,IDNprocessor,IDNram,IDNstorage,IDNtechnician,IDNyear,IDNmonth,IDNday,IDNtime]
    else:
        IDN0 = [usd,IDNname,IDNcondition,IDNnotes,IDNprocessor,IDNram,IDNstorage,IDNtechnician,IDNyear,IDNmonth,IDNday,IDNtime]
file.write(usd);file.write("\",\"");file.write(IDNname);file.write("\",\"");file.write(IDNcondition);file.write("\",\"");file.write(IDNnotes);file.write("\",\"");file.write(IDNprocessor);file.write("\",\"");file.write(IDNram);file.write("\",\"");file.write(IDNstorage);file.write("\",\"");file.write("\"Technician: ");file.write(IDNtechnician);file.write("\",\"");file.write(IDNlocation);file.write("\",\"");file.write(IDNmonth);file.write("-");file.write(IDNday);file.write("-");file.write(IDNday);file.write("-");file.write(IDNyear);file.write(" ");file.write(IDNtime);file.write("\"]")
IDN0098 = ["Dell Latitude","Works","Errors:1","Diagnostic error at bootup for power level","Sell now","password:alpine","Security Questions:Answers: Hilo","Technician: Gabriel", "11-5-2022 15:1"]
IDN0099 = ["[POSTED-CL-$/2022/11/11]","$210","HP ProBook", "Works","Sell now","15 in x 10 in x 0.75 in","Intel i5","8GB RAM","500GB SSD","Technician: Gabriel","11-5-2022 15:1"]
IDN0100 = ["Dell Latitude","Admin-Password-Locked BIOS","Disconnected ribbon","Need to temporarily disconnect BIOS Jumper to bypass security lock", "No CD drive","No HDD","Technician: Gabriel","11-5-2022 15:1"]
IDN0101 = ["HP ProBook", "Blinking light, doesn't power on","No battery","No HDD","No RAM","Left click button doesn't work","Technician: Gabriel","11-7-2022 10:21"]
IDN0102 = ["Dell (Silver)","Broken","Doesn't power on","No HDD or RAM","Technician: Gabriel","11-5-2022 15:1"]
IDN0103 = ["Dell ElitBook","Broken","Technician: Gabriel","11-5-2022 15:1"]
IDN0104 = ["[POSTED-CL-$/2022/11/11]","$160","Lenovo ThinkPad","Works","13.5 in x 9 in x 1.5 in","Password: alpine","Intel i5","4GB RAM","111GB SSD","Technician: Gabriel","11-7-2022 8:1"]
IDN0105 = ["[POSTED-CL-$/2022/11/11]","$60","HP (Purple)","Works","Keyboard does not work, requires external keyboard","A6 Vision AMD","80GB HDD","4GB RAM","Technician: Gabriel","11-7-2022 9:1"]
IDN0106 = ["Dell Inspiron 15","Stuck at windows configuration, reboots without powershell", "Errors: 2", "Error: Repeating sound alert at startup","Error: Unable to gauge power level","Technician: Gabriel","11-7-2022 11:7"]
IDN0107 = ["HP ProBook","Doesn't power on","Technician: Gabriel","11-7-2022 11:6"]
IDN0108 = ["Dell Latitude E5510","Powered on to BIOS error","Errors: 2","Fan malfunction Error code #M1001","Technician: Gabriel","11-7-2022 11:38"]
IDN0109 = ["HP Laptop (Silver)","Works","No battery","Needs to be plugged in","AMD Ryzen 3 2200u","Radeon Vega Mobile Graphics 2.50 GHzAMD","8GB RAM","500 GB HDD","Technician: Gabriel","11-7-2022 11:57"]
IDN0110 = ["HP ProBook","Works","Sell now","Intel i5","500gb HDD","8GB RAM","Technician: Gabriel","11-7-2022 11:58"]
IDN0111 = ["[POSTED-CL-$/2022/11/11]","$140","HP ProBook","Intel i5","8GB RAM","500GB SSD",",15 in x 10 in x 0.75","Keyboard doesn't work","Need to use external keyboard","Technician: Gabriel","11-7-2022 12:11"]
IDN0112 = ["Toshiba (silver)","i7","Doesn't power on","Technician: Gabriel","11-7-2022 13:14"]
IDN0113 = ["HP ProBook","Doesn't power on, blinking light","No HDD","No battery","No RAM","Technician: Gabriel","11-7-2022 12:20"]
IDN0114 = ["HP ProBook","Doesn't power on, blinking light","No HDD","No battery","No RAM","Technician: Gabriel","11-7-2022 12:24"]
IDN0115 = ["HP Envy","Works","Damaged screen-frame @ corner, screen still works","'W' Key doesn't work, needs external keyboard for full keyboard","i5","8GB RAM","700GB HDD","Technician: Gabriel","11-7-2022 13:19"]
IDN0116 = ["[POSTED-CL-$/2022/11/9]","Asus K501L","Works","Sell now","$180","Intel i5","8GB RAM","118GB SSD","15.5 in x 10 in x 0.5 in","Technician: Gabriel","11-7-2022 13:39"]
IDN0117 = ["Lenovo Thinkpad","Broken, no HDD connect, snapped wires","Technician: Gabriel","11-7-2022 14:30"]
IDN0118 = ["[POSTED-CL-$/2022/11/9]","$190","Acer Aspire E 15","Works","Sell now","Password: aloha","15 in x 10 in x 1 in","Intel i3","4gb RAM","1000GB HDD","Technician: Gabriel","11-7-2022 15:6"]
IDN0119 = ["[POSTED-CL-$/2022/11/9]","$200","Dell Latitude E7440","Works","Sell now","Intel i5","4GB RAM","500GB HD","12.75 in x 9 in x 0.5 in","Technician: Gabriel","11-7-2022 16:28"]
IDN0120 = ["[POSTED-CL-$/2022/11/11]","HP TPN-C126","80","Dead battery, needs to be plugged in","Keyboard doesn't work, needs external keyboard","AMD A12-9700P Radeaon R7, 10 Compute Cores 4C+6G 2.50 GHz","6gb RAM","930GB SSD","15 in x 10 in x 0.75 in","Technician: Gabriel","11-7-2022 16:54"]
IDN0130 = ["[POSTED-CL-$/2022/11/9]","$150","Dell Latitude 3570","Works","Sell now","Intel i3","4GB RAM","500Gb HDD","15 in x 10 in x 0.75 in","Technician: Gabriel","11-9-2022 8:31"]
IDN0131 = ["HP ProBook","Doesn't turn on, blinking light","Technician: Gabriel","11-9-2022 10:28"]
IDN0132 = ["HP Mini 311-1037NR","Doesn't power on","Technician: Gabriel","11-9-2022 10:29"]
IDN0133 = ["HP TPN-W129","Works","Lid damaged, still attached","Bad battery, needs to be plugged in","17in","Intel i3","6GB RAM","1T HDD","Technician: Gabriel","11-9-2022 14:13"]
IDN0134 = ["Lenovo S415 Powers on then shuts down, no screen activity"]
IDN0135 = ["Vaio VGN-SR590 Doesn't power on 11-9"]
IDN0136 = ["Vaio PCG-4126L Doesn't power on 11-9"]
IDN0137 = ["Dell Latitude 3450 Doesnt power on 11-11"]
IDN0138 = ["[POSTED-CL-$/2022/11/11]","$25","Dell Inspiron 3120","14.75 in x 9.5 in x 1 in","No battery; needs to be plugged in","Left click doesn't work very well, external mouse required","Very tricky keyboard, especially J key, which must be pressed hard at times to stop ghosting; external keyboard required","Intel i3","4GB RAM","500GB SSD","Technician: Gabriel","11-11-2022 11:50"]
IDN0139 = ["$40","Chromebook","Works","Bad battery, needs to be plugged in","Turns off as guest when using HDMI","Guest Use only or Add Google User","Needs Chrome OS reset to clear preexisting users"]
IDN0140 = ["HP TPN-C125","Doesn't power on"]
IDN0141 = ["$25","HP Pavillion","Works","Bad keyboard, bad mouse; need  to use external peripherals; the O-key ghosts sometimes","HDMI doesn't work","Bad battery; needs to be plugged in","6GB RAM","AMD A8-6410 APU w/ AMD Radeon R5 Gphx","Technician: Gabriel","11-11-2022 15:24"]
IDN0142 = ["[POSTED-CL-$/2022/11/11]","$140","Lenovo ThinkPad","Works","13.5 in x 9 in x 1.5 in","Password: alpine","Intel i5","2GB RAM","111GB SSD","Technician: Gabriel","11-11-2022 16:6"]
IDN0143 = ["[POSTED-CL-$/2022/11/11]","$125","Lenovo ThinkPad","Works","Bad battery; needs to be plugged in","13.5 in x 9 in x 1.5 in","Intel i5","2GB RAM","148GB SSD","Technician: Gabriel","11-11-2022 16:6"]
IDNd001 = ["AOC LCD Monitor 24 in","24 in","HDMI", "$45", "Technician: Gabriel","11-9-2022 12:5"]
IDNd002 = ["Dell Monitor 19 in", "$30", "Technician: Gabriel","11-9-2022 12:5"]
IDNd003 = ["Dell Monitor 24 in", "$40", "Technician: Gabriel","11-9-2022 12:5"]
IDNd004 = ["Dell Monitor 19 in", "$30", "Technician: Gabriel","11-9-2022 12:5"]
IDNd005 = ["Dell Monitor 17 in", "$20", "Technician: Gabriel","11-9-2022 12:5"]
IDNc001 = ["Samsung 32 in HDTV","$150"]
IDNc002 = ["$40","TCL ROKU HDTV 32 in", "Three very light stripes across screen","Works","Technician: Gabriel", "11-11-22 11:28"]
IDNp001 = ["Samsung Galaxy S", "$8"]
IDNp002 = ["Samsung Galaxy J3 V Verizon", "Factory data reset 11:38","Technician: Gabriel", "$15"]
IDN0139 = ["815 Kinoole St., Hilo, HI 96720 |   Open Sundays - Saturdays, 8:30 am - 4:30 pm","$150","Dell Optiplex 790","Good","Reserved for Fernando 808-557-9823 (1 week hold; expires 11-19-2022; wanted duo core instead if possible)","Intel i5","8GB","700GB","Technician: Gabriel","11-13-13-2022 8:20"]
IDN0140 = ["815 Kinoole St., Hilo, HI 96720  |   Open Sundays - Saturdays, 8:30 am - 4:30 pm","$150","Dell Optiplex 790","Good","Reserved for Fernando 808-557-9823 (1 week hold; expires 11-199-2022; wanted duo core instead if possible)","Intel i5","8GB","700GB","Gabriel","11-13-13-2022 8:20"]
IDN0141 = ["815 Kinoole St., Hilo, HI 96720  |   Open Sundays - Saturdays, 8:30 am - 4:30 pm","Dell Inspiron Tower","Works but freezes periodically","not for sale","Intel i5","","1TB","Gabriel","7-11-7-11-7-2022 8:1"]
IDN0142 = ["815 Kinoole St., Hilo, HI 96720  |   Open Sundays - Saturdays, 8:30 am - 4:30 pm","$100","Lenovo ThinkCentre","Good","Windows 7 installed; reserved for a repair job Lynold Acasio 896-3230","Intel i3","4GB","500GB","Technician: Gabriel","11-13-13-2022 9:46"]
folio = open("viewReport.py","a");folio.write("\nreport = [\"");folio.write(usd);folio.write("\",\"");folio.write("Technician: ");folio.write(IDNname);folio.write("\",\"");folio.write(IDNcondition);folio.write("\",\"");folio.write(IDNnotes);folio.write("\",\"");folio.write(IDNprocessor);folio.write("\",\"");folio.write(IDNram);folio.write("\",\"");folio.write(IDNstorage);folio.write("\",\"");folio.write(IDNtechnician);folio.write("\",\"");folio.write(IDNmonth);folio.write("-");folio.write(IDNday);folio.write("-");folio.write(IDNday);folio.write("-");folio.write(IDNyear);folio.write(" ");folio.write(IDNtime);folio.write("\"]");folio.write("\nprint(report)\n")
folio.close()
file.close()

