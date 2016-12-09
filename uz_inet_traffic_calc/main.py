"""

Calculates Internet Provider approx. traffic per day use
If you have unlim unlim then you don't need it

"""
import traceback
import sys

import requests
from pip import InsecureRequestWarning

from uz_inet_traffic_calc.providers.Sarkor import Sarkor


def main():
    """
    main function
    """

    provider = Sarkor()
    # login
    while not provider.login(input("login: "), input("password: ")):
        print("Login or password incorrect.")

    provider.set_values()

    provider.print()


if __name__ == "__main__":

    # noinspection PyBroadException
    try:
        main()
    except KeyboardInterrupt:
        print("\nExecuting SIGINT (Ctrl - C)\n")
        sys.exit(0)
    except:
        print(traceback.format_exc())

    input("Press Enter to exit...")