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
import BBChop,pdb
c=[(4, 0), (3, 2), (1, 5), (1, 6), (0, 0)]
p=[1/5.0 for i in range(5)]
pdb.set_trace()
lp,fp = BBChop.probs(c,p)
