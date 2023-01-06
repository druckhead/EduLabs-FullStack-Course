import os
from virustotal import VirusTotal
from exceptions import *
import argparse
import pickle

if __name__ == '__main__':
    # Create a parser
    parser = argparse.ArgumentParser(
        prog='VirusTotal Scanner',
        description='The program allows to check a URL with VirusTotal API',
        epilog='Text at bottom for help'
    )

    # Define arguments so it will know how to parse
    parser.add_argument('urls',
                        help='One or more URLs to scan. Separated by comma')
    
    parser.add_argument('-k', '--apikey',
                        action='store',
                        help="Optionaly add your own custom apikey")
    
    parser.add_argument('-s', '--scan',
                        action='store_true',
                        help="force new scan")
   
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='verbose help message')
   
    parser.add_argument('-d', "--days",
                        action='store',
                        type=int,
                        help="The amount of days to for the cache to persist",
                        default=180)
    
    parser.add_argument('-c', '--clear',
                        action="store_true",
                        help='Clear the cached links')
    
    parser.add_argument('-i',
                        action="store_true",
                        help="Prompt before removal")
    # end define args

    # Perform the parse
    args = parser.parse_args(["https://www.google.com"])
    
    print(f"urls={args.urls}", f"apikey={args.apikey}", f"scan={args.scan}", f"verbose={args.verbose}",
          f"days={args.days}", sep='\n')

    # look for pickle file
    if not os.path.exists(os.path.join(os.curdir, "files", "vt.pickle")):
        # check if the directory exists
        if not os.path.exists(os.path.join(os.curdir, "files")):
            # if not create it and init a VirusTotal obj
            os.mkdir(os.path.join(os.curdir, "files"))
            vt = VirusTotal()
    else:
        try:
            with open(os.path.join(os.curdir, "files", "vt.pickle"), 'rb') as pickeled_obj:
                # load the pickle obj
                vt = pickle.load(pickeled_obj)
        except FileNotFoundError as err:
            print(err)

    try:
        if args.scan is True:
            vt.scan_url(args.urls)
            vt.url_analysis(args.urls, days=args.days)
        else:
            try:
                vt.url_analysis(args.urls, days=args.days)
            except AnalysisExpired as exp:
                print(exp)
                vt.scan_url(args.urls)
                vt.url_analysis(args.urls, days=args.days)
            except BadRequest as err:
                print(err)
                vt.scan_url(args.urls)
                vt.url_analysis(args.urls)
    except BadRequest as badrequest:
        print(badrequest)
    finally:
        try:
            with open(os.path.join(os.curdir, "files", "vt.pickle"), 'wb') as writefile:
                pickle.dump(vt, writefile)
        except Exception as err:
            print(err)
