# The purpose of this project is to create a general template to morph projects into.
# Codes usually lie around in undisciplined forms and do not refer to a proper code base
# However, trying out new codes  usually requires figuring out format, and sometimes you 
# need to walk through the code to understand unclear parts, or simply for debugging
from Functions import numpyRun
def main( params,params_dict):
    NUM = numpyRun.calculatingBasicNumbers( params,params_dict)
    return NUM

if __name__ == "__main__":
    import argparse

    # Create the parser 
    parser = argparse.ArgumentParser(description="Process some integers.")

    # Add arguments
    parser.add_argument('integers', metavar='N', type=int, nargs='+',default=42,
    help='integers to be printed')
    parser.add_argument('--sum', type=int,  default=81, 
    help='the specific value of a sum')

    # Execute the parse_args() method
    args = parser.parse_args()
    params =[int(x) for x in   args.integers ]
    params_dict = {}
    params_dict['sum'] = int(    args.sum  )
    PL = main( params, params_dict)
    print(PL)