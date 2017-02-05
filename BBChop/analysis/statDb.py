#    Copyright 2008 Ealdwulf Wuffinga

#    This file is part of BBChop.
#
#    BBChop is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    BBChop is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with BBChop.  If not, see <http://www.gnu.org/licenses/>.

import dbm
import pickle

filename="data/statsdb"

global theDB


def open():
    global theDB
    theDB=dbm.open(filename,"w")
def create():
    global theDB
    theDB=dbm.open(filename,"c")



def close():
    theDB.close()

def add(key,value):
    theDB[pickle.dumps(key)]=pickle.dumps(value)

def get(key):
    return pickle.loads(theDB[pickle.dumps(key)])
def has_key(key):
    return pickle.dumps(key) in theDB

def iteritems():
    global theDB
    for (key,value) in theDB.items():
        yield (pickle.loads(key),pickle.loads(value))
