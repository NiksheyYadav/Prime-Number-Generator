# The GPLv3 License (GPLv3)

# Copyright © 2024 NiksheyYadav

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>



num = range(1,10000)


def is_prime(num):
    loc = num
    for i in range(2,loc):
        if loc%i == 0:
            return False
    return True
    
primes = filter(is_prime, num)
    
print(list(primes))