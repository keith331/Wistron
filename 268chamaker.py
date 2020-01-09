import xml.etree.ElementTree as et
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter
from collections import defaultdict
import os
import glob

current_dir = os.path.dirname(os.path.abspath(__file__))
# data_dir = os.path.abspath(os.path.join(current_dir, os.path.join('..')))
data_dir = glob.glob('*.xml')
latest_file = max(data_dir, key=os.path.getctime)
print(latest_file)

# Defauls a dictionary as list type
newdata = defaultdict(list)

# Read xml file
xtree = et.parse(latest_file)
root = xtree.getroot()


# Initialize paramers for matplotlib

#  Show current file name on figure title
fig = plt.figure(figsize=(12,10),facecolor='#c9c9c9',num='File name :  %s' %latest_file)
plt.subplots_adjust(left=0.07,right=0.92,wspace=0.35)
def style(self):
    plt.grid(which='minor',linestyle='-',color='#b1b1b1', linewidth='1')
    plt.grid(which='major',linestyle='-',color='#666666', linewidth='1.2')
    plt.xticks(fontsize=11, weight='bold')
    plt.yticks(fontsize=10)
    plt.xlim(100,10000)
    plt.xscale('log',basex = 10)
    # plt.tick_params(axis='x', bottom=False, left=False, labelbottom=False)

# ==== change the x-axis of log plot appreance
    for axix in [self.xaxis, self.yaxis]:
        axix.set_major_formatter(ScalarFormatter())


result = []
lowlim = []
uplim = []
for elm in root:
    for lv2elm in elm:
        id = lv2elm.attrib.get('Name')
        newdata['id'].append(id)
        for lv3elm in lv2elm:

            for lv4elm in lv3elm:
                r = lv4elm.attrib.get('Result')
                result.append(r)
                l = lv4elm.attrib.get('LowerLimit')
                lowlim.append(l)
                u = lv4elm.attrib.get('UpperLimit')
                uplim.append(u)


result = [e for e in result if e != '']
'''
============
Sweep test method for QA268, Remove list[0] that unnecessary
If custom don't add something like valid driver (ADB), this
driver infomation won't display, thus no need adding 'result.pop(0)'
============
'''
result.pop(0)
result = list(map(float,result))
totalitems = len(result) // 45
lowlim = [e for e in lowlim if e != '']
lowlim = list(map(float,lowlim))
uplim = [e for e in uplim if e != '']
uplim = list(map(float,uplim))


# Catch x-axis for one time

i = 0
while i < 45:
    newdata['hz'].append(result[i])
    i += 3


for cycle in range(1,totalitems+1):

    if cycle == 1:
        spl = 1
        thd = 2
        id1 = newdata['id'][7]
        id2 = newdata['id'][8]
        while spl < 45:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3


        df1_fr = pd.DataFrame(columns = newdata['hz'],index = ['Uplim','Lowlim',id1])
        df1_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df1_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df1_fr.loc[id1] = newdata[id1]

        df1_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df1_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df1_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df1_thd.loc[id2] = newdata[id2]


    if cycle == 2:
        count = int(45)
        spl = 1 + count
        thd = 2 + count
        id1 = newdata['id'][7 + count]
        id2 = newdata['id'][8 + count]
        while spl < 45 + count:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3

        df2_fr = pd.DataFrame(columns = newdata['hz'],index = ['Uplim','Lowlim',id1])
        df2_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df2_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df2_fr.loc[id1] = newdata[id1]

        df2_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df2_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df2_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df2_thd.loc[id2] = newdata[id2]


    if cycle == 3:
        count = int(90)
        spl = 1 + count
        thd = 2 + count
        id1 = newdata['id'][7 + count]
        id2 = newdata['id'][8 + count]
        while spl < 45 + count:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3

        df3_fr = pd.DataFrame(columns = newdata['hz'],index = ['Uplim','Lowlim',id1])
        df3_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df3_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df3_fr.loc[id1] = newdata[id1]

        df3_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df3_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df3_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df3_thd.loc[id2] = newdata[id2]

    if cycle == 4:
        count = int(135)
        spl = 1 + count
        thd = 2 + count
        id1 = newdata['id'][7 + count]
        id2 = newdata['id'][8 + count]
        while spl < 45 + count:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3

        df4_fr = pd.DataFrame(columns = newdata['hz'],index = ['Uplim','Lowlim',id1])
        df4_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df4_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df4_fr.loc[id1] = newdata[id1]

        df4_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df4_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df4_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df4_thd.loc[id2] = newdata[id2]

    if cycle == 5:
        count = int(180)
        spl = 1 + count
        thd = 2 + count
        id1 = newdata['id'][7 + count]
        id2 = newdata['id'][8 + count]
        while spl < 45 + count:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3

        df5_fr = pd.DataFrame(columns = newdata['hz'],index = ['Uplim','Lowlim',id1])
        df5_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df5_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df5_fr.loc[id1] = newdata[id1]

        df5_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df5_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df5_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df5_thd.loc[id2] = newdata[id2]

    if cycle == 6:
        count = int(225)
        spl = 1 + count
        thd = 2 + count
        id1 = newdata['id'][7 + count]
        id2 = newdata['id'][8 + count]
        while spl < 45 + count:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3

        df6_fr = pd.DataFrame(columns = newdata['hz'],index = ['Uplim','Lowlim',id1])
        df6_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df6_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df6_fr.loc[id1] = newdata[id1]

        df6_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df6_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df6_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df6_thd.loc[id2] = newdata[id2]


    if cycle == 7:
        count = int(270)
        spl = 1 + count
        thd = 2 + count
        id1 = newdata['id'][7 + count]
        id2 = newdata['id'][8 + count]
        while spl < 45 + count:
            newdata[id1].append(result[spl])
            newdata['%s_lowlim' %id1].append(lowlim[spl])
            newdata['%s_uplim' %id1].append(uplim[spl])
            spl += 3

            newdata[id2].append(result[thd])
            newdata['%s_lowlim' %id2].append(lowlim[thd])
            newdata['%s_uplim' %id2].append(uplim[thd])
            thd += 3

        df7_fr = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id1])
        df7_fr.loc['Uplim'] = newdata['%s_uplim' %id1]
        df7_fr.loc['Lowlim'] = newdata['%s_lowlim' %id1]
        df7_fr.loc[id1] = newdata[id1]

        df7_thd = pd.DataFrame(columns = newdata['hz'], index = ['Uplim','Lowlim',id2])
        df7_thd.loc['Uplim'] = newdata['%s_uplim' %id2]
        df7_thd.loc['Lowlim'] = newdata['%s_lowlim' %id2]
        df7_thd.loc[id2] = newdata[id2]




ax1 = plt.subplot(7,2,1,facecolor='#efefef')
# plt.ylim(70,130)
style(ax1)
plt.title(df1_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
ax1.plot(newdata['hz'],df1_fr.iloc[0,:], color='red', linestyle='-.')
ax1.plot(newdata['hz'],df1_fr.iloc[1,:], color='red', linestyle='-.')
ax1.plot(newdata['hz'],df1_fr.iloc[2,:], linewidth=2)


ax1a = plt.subplot(7,2,2,facecolor='#f2f2f2')
# plt.ylim(70,130)
style(ax1a)
plt.title(df1_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
ax1a.plot(newdata['hz'],df1_thd.iloc[0,:], color='red', linestyle='-.')
ax1a.plot(newdata['hz'],df1_thd.iloc[1,:], color='red', linestyle='-.')
ax1a.plot(newdata['hz'],df1_thd.iloc[2,:], linewidth=2)

print(df1_fr, df1_thd)



if 'df2_fr' and 'df2_thd' in locals():


    ax2 = plt.subplot(7,2,3,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax2)
    plt.title(df2_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax2.plot(newdata['hz'],df2_fr.iloc[0,:], color='red', linestyle='-.')
    ax2.plot(newdata['hz'],df2_fr.iloc[1,:], color='red', linestyle='-.')
    ax2.plot(newdata['hz'],df2_fr.iloc[2,:], linewidth=2)



    ax2a = plt.subplot(7,2,4,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax2a)
    plt.title(df2_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax2a.plot(newdata['hz'],df2_thd.iloc[0,:], color='red', linestyle='-.')
    ax2a.plot(newdata['hz'],df2_thd.iloc[1,:], color='red', linestyle='-.')
    ax2a.plot(newdata['hz'],df2_thd.iloc[2,:], linewidth=2)




if 'df3_fr' and 'df3_thd' in locals():

    ax3 = plt.subplot(7,2,5,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax3)
    plt.title(df3_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax3.plot(newdata['hz'],df3_fr.iloc[0,:], color='red', linestyle='-.')
    ax3.plot(newdata['hz'],df3_fr.iloc[1,:], color='red', linestyle='-.')
    ax3.plot(newdata['hz'],df3_fr.iloc[2,:], linewidth=2)


    ax3a = plt.subplot(7,2,6,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax3a)
    plt.title(df3_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax3a.plot(newdata['hz'],df3_thd.iloc[0,:], color='red', linestyle='-.')
    ax3a.plot(newdata['hz'],df3_thd.iloc[1,:], color='red', linestyle='-.')
    ax3a.plot(newdata['hz'],df3_thd.iloc[2,:], linewidth=2)

if 'df4_fr' and 'df4_thd' in locals():

    ax4 = plt.subplot(7,2,7,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax4)
    plt.title(df4_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax4.plot(newdata['hz'],df4_fr.iloc[0,:], color='red', linestyle='-.')
    ax4.plot(newdata['hz'],df4_fr.iloc[1,:], color='red', linestyle='-.')
    ax4.plot(newdata['hz'],df4_fr.iloc[2,:], linewidth=2)

    ax4a = plt.subplot(7,2,8,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax4a)
    plt.title(df4_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax4a.plot(newdata['hz'],df4_thd.iloc[0,:], color='red', linestyle='-.')
    ax4a.plot(newdata['hz'],df4_thd.iloc[1,:], color='red', linestyle='-.')
    ax4a.plot(newdata['hz'],df4_thd.iloc[2,:], linewidth=2)

if 'df5_fr' and 'df5_thd' in locals():

    ax5 = plt.subplot(7,2,9,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax5)
    plt.title(df5_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax5.plot(newdata['hz'],df5_fr.iloc[0,:], color='red', linestyle='-.')
    ax5.plot(newdata['hz'],df5_fr.iloc[1,:], color='red', linestyle='-.')
    ax5.plot(newdata['hz'],df5_fr.iloc[2,:], linewidth=2)

    ax5a = plt.subplot(7,2,10,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax5a)
    plt.title(df5_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax5a.plot(newdata['hz'],df5_thd.iloc[0,:], color='red', linestyle='-.')
    ax5a.plot(newdata['hz'],df5_thd.iloc[1,:], color='red', linestyle='-.')
    ax5a.plot(newdata['hz'],df5_thd.iloc[2,:], linewidth=2)

if 'df6_fr' and 'df6_thd' in locals():

    ax6 = plt.subplot(7,2,11,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax6)
    plt.title(df6_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax6.plot(newdata['hz'],df6_fr.iloc[0,:], color='red', linestyle='-.')
    ax6.plot(newdata['hz'],df6_fr.iloc[1,:], color='red', linestyle='-.')
    ax6.plot(newdata['hz'],df6_fr.iloc[2,:], linewidth=2)

    ax6a = plt.subplot(7,2,12,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax6a)
    plt.title(df6_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax6a.plot(newdata['hz'],df6_thd.iloc[0,:], color='red', linestyle='-.')
    ax6a.plot(newdata['hz'],df6_thd.iloc[1,:], color='red', linestyle='-.')
    ax6a.plot(newdata['hz'],df6_thd.iloc[2,:], linewidth=2)



    # NOTE: The original 'THD' data was shown before 'SPL'
if 'df7_fr' and 'df7_thd' in locals():


    ax7 = plt.subplot(7,2,14,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax7)
    plt.title(df7_fr.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax7.plot(newdata['hz'],df7_fr.iloc[0,:], color='red', linestyle='-.')
    ax7.plot(newdata['hz'],df7_fr.iloc[1,:], color='red', linestyle='-.')
    ax7.plot(newdata['hz'],df7_fr.iloc[2,:], linewidth=2)


    ax7a = plt.subplot(7,2,13,facecolor='#f2f2f2')
    # plt.ylim(70,130)
    style(ax7a)
    plt.title(df7_thd.index[2],loc='left', weight='bold',backgroundcolor= '#6A9F3D')
    ax7a.plot(newdata['hz'],df7_thd.iloc[0,:], color='red', linestyle='-.')
    ax7a.plot(newdata['hz'],df7_thd.iloc[1,:], color='red', linestyle='-.')
    ax7a.plot(newdata['hz'],df7_thd.iloc[2,:], linewidth=2)




fig.tight_layout(h_pad=0.1)
plt.show()
