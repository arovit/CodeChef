#!/usr/bin/python

import sys
import math

def quad(min, mid, max, cor_list):
    before = 0
    after = 0
    for i in cor_list:
        if i > mid:
           after = after + 1
	elif i == mid:
	   pass
        else:
           before = before + 1
    if after > before: 
        return range(mid, max+1)
    return range(min, mid+1)

def distance(a, b):
    var = ((a[0] - b[0])*(a[0] - b[0])) + ((a[1] - b[1])*(a[1] - b[1]))
    dt = math.sqrt(var)
    return dt

def sum_distance(x, y):
    global c_distance 
    if c_distance.get((x,y), None):
        return c_distance.get((x,y))
    sum_d = 0
    for point in points:
        sum_d = sum_d + distance((x,y), point)
    c_distance[(x,y)] = sum_d  
    return sum_d

def ternarySearch_x(f, l, r, y, absolutePrecision=3):
    #left and right are the current bounds; the minimum is between them
    if (r - l) < absolutePrecision:
        return (l + r)/2
    m1 = l + (r-l)/3
    m2 = r - (r-l)/3
    if f(m1, y) < f(m2, y):
        return ternarySearch_x(f, l, m2, y, absolutePrecision)
    elif f(m1, y) > f(m2, y):
        return ternarySearch_x(f, m1, r, y, absolutePrecision)
    else:
	return ternarySearch_x(f, m1, m2, y, absolutePrecision)

def arraySearch(index, array):
    return sum_distance(array[index][0], array[index][1])

def prepare_minpoint_quad():
    a = lambda x: x[0]
    b = lambda x: x[1]
    x_cor = map(a, points)
    y_cor = map(b, points)
    min_x_cor = min(x_cor)
    max_x_cor = max(x_cor)
    min_y_cor = min(y_cor)
    max_y_cor = max(y_cor)
    #x_list = quad(min(x_cor), int((min_x_cor + max_x_cor / 2 ), max_x_cor, x_cor)
    #y_list = quad(min(y_cor), int((min_y_cor + max_y_cor / 2 ), max_y_cor, y_cor)
    dis = []
    for y in range(min_y_cor ,max_y_cor):
        dis.append((ternarySearch_x(sum_distance, min_x_cor, max_x_cor, y),y))
    index = ternarySearch_x(arraySearch, 0, len(dis)-1, dis)
    d = sum_distance(dis[index][0], dis[index][1])
    print "%.6f"%d 

def take_input(n_point):
    global points
    points = []
    for i in range(0,n_point):
         points.append(map(int, raw_input().split()))
    prepare_minpoint_quad()

while True:
    global c_distance 
    c_distance = {}
    n_point = input()
    if not n_point:
        sys.exit(0) 
    take_input(n_point)
