import os
import pysrt
from hanziconv import HanziConv

dir = os.listdir('./data/')
outfile = open('./pair.txt', 'a', encoding='utf-8')
output = ''

for file in dir:
    subs = pysrt.open('./data/' + file)
    print(file)
    point = 0
    while point < len(subs) - 1:
        print(str(point) + "/" + str(len(subs)))
        if (subs[point].end.minutes == subs[point + 1].end.minutes):  # in same minute
            # process - in subtitle
            if "-" in subs[point].text:
                result = ((subs[point].text).replace("-", '')).split(" ", 1)
                output += ("'" + result[0] + "'" + ',' + "'" + result[1] + "'" + '\n')
            elif "-" in subs[point + 1].text:
                result = ((subs[point + 1].text).replace("-", '')).split(" ", 1)
                output += ("'" + result[0] + "'" + ',' + "'" + result[1] + "'" + '\n')
                point += 1
            # normal
            elif ((subs[point + 1].end.seconds - subs[point].start.seconds) <= 1):
                if ("\n" not in subs[point].text and "\n" not in subs[point + 1].text):
                    output += ("'" + subs[point].text + "'" + ',' + "'" + subs[point + 1].text + "'" + '\n')
                    point += 1
        point += 1
    outfile.write(HanziConv.toTraditional(output))
