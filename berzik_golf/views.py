from django.shortcuts import render
from sphero import Sphero
import random
import time
import json
import threading
# Create your views here.
from django.http import HttpResponse
from berzik.settings import SP as s

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def connect_sphero():
	s = Sphero("/dev/tty.Sphero-GPR-AMP-SPP")
	s.connect()
	return s

def get_modulated_duration(speed):
	"""
	600 - 6000
	"""
	return 1+ int(float(speed))/800

def get_modulated_direction(x,z):
	"""
	0-360
	"""
	temp = 1

def roll_ball(speed,s):
	e = get_modulated_duration(speed)
	direction = random.randint(0,359)
	print direction
	direction = 0
	direction = 0
	s.roll(0xFF,direction)
	time.sleep(e)
	s.stop()

def move(request):
	sp_val = request.GET
	speed = sp_val["speed"]

	x = sp_val["x"]
	y = sp_val["y"]
	z = sp_val["z"]
	print x,y,z,speed
	"""
	try:
		s = connect_sphero()
	except Exception:
		return HttpResponse(json.dumps({"status":"failed"}))
	"""
	rr = random.randint(0,255)
	#s.set_rotation_rate(rr)
	#s.set_heading(0)
	if int(float(speed))>1000:
		download_thread = threading.Thread(target=roll_ball, args=[speed,s])
		download_thread.start()
	return HttpResponse(json.dumps({"status":"success"}))

def update_beacon(request):
	dis = request.GET["distance"]
	"""
	45 - 80
	"""
	distance = 25
	try:
		distance = int(float(dis)) - 55
	except:
		distance = 25

	distance = max(0,min(distance,255))
	r = distance * 11
	g = 255 - r

	print r,g,255
	download_thread = threading.Thread(target=set_up, args=[r,g,0])
	download_thread.start()
	return HttpResponse(json.dumps({"status":"success"}))


def set_up(r,g,b):
	s.set_rgb(r,g,0,True)


def set_ee(direction):
	s.set_heading(int(direction))


def update_direction(request):
	direction = request.GET["direction"]
	download_thread = threading.Thread(target=set_ee, args=[direction])
	download_thread.start()
	return HttpResponse(json.dumps({"status":"success"}))