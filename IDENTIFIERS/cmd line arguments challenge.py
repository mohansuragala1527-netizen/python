# command line arguments - challenge
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--num1", type=int)
parser.add_argument("--num2", type=int)

args = parser.parse_args()

print("Sum =", args.num1 + args.num2)
