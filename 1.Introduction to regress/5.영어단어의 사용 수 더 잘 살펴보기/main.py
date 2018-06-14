from scipy.stats import linregress
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#import elice_utils
import math
import operator
# from operator import itemgetter
# import ast

def main():    
    # 여기에 내용을 채우세요.
    words = read_data()
    words = sorted(words, key=lambda num: num[1], reverse = True) # words.txt 단어를 빈도수 순으로 정렬합니다.
    #print(words)
    
    X = list(range(1, len(words)+1))
    Y = [x[1] for x in words]
    
    # X, Y 리스트를 array로 변환한 후 각 원소 값에 log()를 적용합니다.
    X, Y = np.array(X), np.array(Y)  
    X, Y = np.log(X), np.log(Y)

    slope, intercept = do_linear_regression(X, Y)
    draw_chart(X, Y, slope, intercept)
    return slope, intercept

def read_data():
    # 여기에 내용을 채우세요.
    # words = []
    # X = []
    # Y = []
    # with open('words.txt') as file:
    #     for line in file:
    #         content = line.strip().split(',')
    #         #content = line.strip()
    #         words.append([content[0] ,int(content[1])])
    
    # words = sorted(words, key=itemgetter(1),reverse=True)
    # for i in range(len(words)):
    #     X.append(words[i][0])
    #     Y.append(words[i][1])
    # return (X,Y)

    words = []
    file = open("./words.txt", 'r')
    while True:
        line = file.readline()
        if not line:
            break
        word = line.split(',')[0]
        freq = line.split(',')[1]
        words.append([word, float(freq)])
    return words

def draw_chart(X, Y, slope, intercept):
    fig = plt.figure()
    
    # 여기에 내용을 채우세요.
    ax = fig.add_subplot(111)
    plt.scatter(X, Y)

    # 차트의 X, Y축 범위와 그래프를 설정합니다.
    min_X = min(X)
    max_X = max(X)
    min_Y = min_X * slope + intercept
    max_Y = max_X * slope + intercept
    plt.plot([min_X, max_X], [min_Y, max_Y], 
             color='red',
             linestyle='--',
             linewidth=3.0)
    
    # 기울과와 절편을 이용해 그래프를 차트에 입력합니다.
    ax.text(min_X, min_Y + 0.1, r'$y = %.2lfx + %.2lf$' % (slope, intercept), fontsize=15)
    
    plt.savefig('chart.png')
    elice_utils.send_image('chart.png')

def do_linear_regression(X, Y):
    # 여기에 내용을 채우세요.
    print(X)
    slope, intercept, r_value, p_value, std_err = linregress(X, Y)
    return (slope, intercept)

if __name__ == "__main__":
    main()
