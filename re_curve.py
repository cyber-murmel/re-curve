#!/usr/bin/env python

# rekursive turtle program
# Autor: MarBle
# last change: 06.Sep.15

import turtle
import math
import argparse

#get Command Line Arguments
parser = argparse.ArgumentParser(description='Draw some nice recursive fractals. Createt by MarBle.')
parser.add_argument("-c", "--curve", type=str, default = "hilbert",  help='Name of curve')
parser.add_argument("-b", "--base" , type=int, default = 5     , help='Length of basic element')
parser.add_argument("-g", "--gens" , type=int, default = 5     , help='Number of generations')
parser.add_argument("-s", "--speed", type=int, default = 0     , help='Speed of turtle (1-10, 0=fastest)')
args = parser.parse_args()

#print Arguments
if args.curve != None: print 'Name of curve..............: '+args.curve
if args.base  != None: print 'Length of basic elements...: '+str(args.base)
if args.gens  != None: print 'Number of generations......: '+str(args.gens)
if args.speed != None: print 'Speed of Turtle............: '+str(args.speed)

#generate turle and screen
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(args.speed%10)
t.ht()
base = args.base
gens = args.gens


def dragon_start():
	t.pd()
	dragon(t, base, gens, 1)

def dragon(t, len, gen, dir):
	if gen == 0:
		t.fd(len)
	else:
		if dir == 1:
			dragon(t, len, gen-1, dir)
			t.lt(90)
			dragon(t, len, gen-1, -dir)
		else:
			dragon(t, len, gen-1, -dir)
			t.rt(90)
			dragon(t, len, gen-1, dir)


def vicsek_start():
	t.pd()
	for i in range(0,4):
		vicsek(t, base*2**gens, gens)
		t.lt(90)

def vicsek(t, len, gen):
	if gen == 0:
		for i in range(0,2):
			t.fd(len)
			t.lt(180)
	else:
		t.fd(len)
		t.rt(90)
		for i in range(0,3):
			vicsek(t, len/2, gen-1)
			t.lt(90)
		t.fd(len)
		t.lt(180)

def tsquare_start():
	t.pd()
	t.begin_fill()
	for i in range(0,4):
		tsquare(t, base*2**gens/2, gens)
		t.lt(90)
	t.end_fill()

def tsquare(t, len, gen):
	if gen == 0:
		for i in range(0,4):
			t.fd(len)
			t.lt(90)
	else:
		for i in range(0,2):
			t.fd(len)
			t.lt(90)
		for i in range(0,3):
			t.lt(90)
			tsquare(t, len/2, gen-1)
		t.lt(90)
		for i in range(0,2):
			t.fd(len)
			t.lt(90)


def sierpinski_arrowhead_start():
	t.goto(-base*2**gens, -base*2**gens*math.sqrt(3)/2)
	t.pd()
	sierpinski_arrowhead(t, base*2**gens, gens, 1)

def sierpinski_arrowhead(t, len, gen, dir):
	if gen == 0:
		t.lt(dir*60)
		t.fd(len)
		t.rt(dir*60)
		t.fd(len)
		t.rt(dir*60)
		t.fd(len)
		t.lt(dir*60)
	else:
		t.lt(dir*60)
		sierpinski_arrowhead(t, len/2, gen-1, -dir)
		t.rt(dir*60)
		sierpinski_arrowhead(t, len/2, gen-1, dir)
		t.rt(dir*60)
		sierpinski_arrowhead(t, len/2, gen-1, -dir)
		t.lt(dir*60)

def sierpinski_triangle_start():
	t.goto(-base*2**gens/2, -base*2**gens*math.sqrt(3)/4)
	t.pd()
	sierpinski_triangle(t, base*2**gens, gens)

def sierpinski_triangle(t, len, gen):
	if gen == 0:
		for i in range(0,3):
			t.fd(len)
			t.lt(120)
	else:
		for i in range(0,3):
			sierpinski_triangle(t, len/2, gen-1)
			t.pu()
			t.fd(len)
			t.lt(120)
			t.pd()

def sierpinski_carpet_start():
	t.goto(-base*3**gens/2, -base*3**gens/2)
	t.pd()
	sierpinski_carpet(t, base*3**gens, gens)

def sierpinski_carpet(t, len, gen):
	if gen == 0:
		for i in range(0,4):
			t.fd(len)
			t.lt(90)
	else:
		for i in range(0,4):
			sierpinski_carpet(t, len/3, gen-1)
			t.fd(len/3)
			sierpinski_carpet(t, len/3, gen-1)
			t.fd(2*len/3)
			t.lt(90)

def pythagoras_start():
	t.goto(-base*math.sqrt(2)**gens/2, -base*2*math.sqrt(2)**gens)
	t.pd()
	t.begin_fill()
	pythagoras(t, base*math.sqrt(2)**gens, gens)
	t.end_fill()

def pythagoras(t, len, gen):
	if gen == 0:
		for i in range(0,4):
			t.fd(len)
			t.lt(90)
	else:
		t.lt(90)
		t.fd(len)
		t.rt(45)
		pythagoras(t, len/math.sqrt(2), gen-1)
		t.rt(45)
		t.fd(len)
		t.lt(135)
		t.fd(len/math.sqrt(2))
		t.rt(180)
		pythagoras(t, len/math.sqrt(2), gen-1)
		t.fd(len/math.sqrt(2))
		t.rt(45)
		t.fd(len)
		t.rt(90)
		t.fd(len)
		t.rt(180)
		

def marble_start():
	t.goto(-base*2**gens+base/2, -base*2**gens*math.sqrt(3)/2+base*math.sqrt(3)/4)
	t.pd()
	marble(t, base, gens, 1)

def marble(t, len, gen, dir):
	t.lt(dir*60)
	if gen == 0:
		t.fd(len)
		t.rt(dir*120)
		t.fd(len)
	else:
		marble(t, len, gen-1, -dir)
		t.fd(len)
		t.rt(dir*60)
		marble(t, len, gen-1, dir)
		t.rt(dir*60)
		t.fd(len)
		marble(t, len, gen-1, -dir)
	t.lt(dir*60)

def hilbert_start():
	t.goto(-base*2**gens+base/2, -base*2**gens+base/2)
	t.pd()
	hilbert(t, base, gens, 1)

def hilbert(t, len, gen, dir):
	t.lt(dir*90)
	if gen == 0:
		t.fd(len)
		t.rt(dir*90)
		t.fd(len)
		t.rt(dir*90)
		t.fd(len)
	else:
		hilbert(t, len, gen-1, -dir)
		t.fd(len)
		t.rt(dir*90)
		hilbert(t, len, gen-1, dir)
		t.fd(len)
		hilbert(t, len, gen-1, dir)
		t.rt(dir*90)
		t.fd(len)
		hilbert(t, len, gen-1, -dir)
	t.lt(dir*90)

def koch_start():
	t.goto(-base*3**gens/2,0)
	t.pd()
	koch(t, base*3**gens, gens)

def koch(t, len, gen):
	if gen == 0:
		t.fd(len)
	else:
		koch(t, len/3, gen-1)
		t.lt(60)
		koch(t, len/3, gen-1)
		t.rt(120)
		koch(t, len/3, gen-1)
		t.lt(60)
		koch(t, len/3, gen-1)

t.pu()
switcher={
	'marble'	: marble_start,
	'hilbert'	: hilbert_start,
	'koch'		: koch_start,
	'pythagoras': pythagoras_start,
	'carpet'	: sierpinski_carpet_start,
	'triangle'	: sierpinski_triangle_start,
	'arrowhead'	: sierpinski_arrowhead_start,
	'tsquare'	: tsquare_start,
	'vicsek'	: vicsek_start,
	'dragon'	: dragon_start
}
func = switcher.get(args.curve)
func()
turtle.exitonclick()