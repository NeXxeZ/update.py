#! /usr/bin/python3

import os


def main():
    pasw = passHere
    os.system(""
              "echo {0} | sudo -S apt-get update && "
              "sudo apt-get upgrade -y && "
              "sudo apt-get dist-upgrade -y && "
              "sudo apt-get autoremove -y && "
              "sudo apt-get clean".format(pasw))


if __name__ == '__main__':
    main()
