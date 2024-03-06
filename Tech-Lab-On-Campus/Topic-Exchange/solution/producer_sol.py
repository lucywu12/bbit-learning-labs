import sys
import pika
import os
import producer_interface

class mqProducer(producer_interface):
    def __init__(self, exchange_name)