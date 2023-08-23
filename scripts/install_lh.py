import sys
import argparse
from datetime import datetime


parser=argparse.ArgumentParser()

parser.add_argument('--apikey', help='IBM Cloud API Key',required=True)
parser.add_argument('--region', help='Region of cluster',required=True)
parser.add_argument('--cluster', help='name of the cluster',required=True)

# Read supplied arguments
args    =   parser.parse_args()

api_key             =   args.apikey
region              =   args.region
cluster             =   args.cluster
 
# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)
 
# # Arguments passed
# print("\nName of Python script:", sys.argv[0])
 
# print("\nArguments passed:", end = " ")
# for i in range(1, n):
#     print(sys.argv[i], end = " ")
     
# # Addition of numbers
# Sum = 0
# # Using argparse module
# for i in range(1, n):
#     Sum += int(sys.argv[i])

print("\n Successfully executed the script. ")
     
print("\n api_key:", api_key)
print("\n region:", region)
print("\n cluster:", cluster)
