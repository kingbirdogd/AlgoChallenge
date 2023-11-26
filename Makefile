export PROJECT_HOME:=$(shell pwd|sed "s/\/$$//g;")
export SRC_DIR:=.
export INC_DIR:=.
include $(PROJECT_HOME)/common.mk
