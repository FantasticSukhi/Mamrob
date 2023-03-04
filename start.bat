@echo off
TITLE Hotspot Robot
:: Enables virtual env mode and then starts Hotspot
env\scripts\activate.bat && py -m HotspotRobot
