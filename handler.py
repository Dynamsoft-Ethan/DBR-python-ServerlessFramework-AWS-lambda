import json
from dbr import *
def hello(event, context):
    try:
        # Sets a directory path for saving the license cache.
        folder_path = "/tmp/my-folder"
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        BarcodeReader.set_license_cache_path(folder_path)

        # 1.Initialize license.
        # The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here is a free public trial license. Note that network connection is required for this license to work.
        # You can also request a 30-day trial license in the customer portal: https://www.dynamsoft.com/customer/license/trialLicense?product=dbr&utm_source=samples&package=python
        error = BarcodeReader.init_license("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9")
        
        if error[0] != EnumErrorCode.DBR_OK:
            return ("License error: "+ error[1])

        # 2.Create an instance of Barcode Reader.
        dbr = BarcodeReader()

        # Replace by your own image data
        barcode_base64_string = "R0lGODlhZABkAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAABkAGQAAAj/AAEIHEiwoMGD+xIqTEhwoUOFDR/ui8jwoMWLGDNilDhxIMeFFB2G1EiypEmBHEOm9Chx5MmXMFVCZPmxI8qWNG3G3Fjzo0uDIHfmlNlzJtCiOG9WPLpUaFClSJ8WjPrw51SjTrFSFYlwq1asVndK9Qp2aMaxSS+uhLoWgFSLb83ybNoWbtqiYbs2zctUZ129XNneLdvX7l7ARHUaDuy2J9+rh6FqRBu5MV3Car9Wfhy3sFzIfjEvfsxZ9OfOlkNvRvx5NOu5qhWfNu1Z8lnMqK3ibZ2TcuzJuGmnTux7cXHetUEDv1yzdNXZq20ndy34uXTQx69Tx05Vt2aft5l7/zXeHXrsv8nJVlb/2zx65b3L993qXfz7+uOFwsbPH7n+//1dl91wABaY3ncBEmjgggo2OOCAALIn4WDRpTbhhRhSKNt8GXaIIWnxeSiieiBWl6FYwm23XHsCIhhTbuFtmJl4CcK434spmldjjtOZZCN8LdIYIoszMkacfBYiuZt2gKH24ZBLJmldg+Std+GRzUHpImxOXqllliZWCR6TZFL5mpQynkSff11W6NuPK0bZpow/vsljkXIGZ6Wb38HJpoZ+hqljk2k5x9h9hApZZpSG2llhYgliSaeehxYa44OUIsqlpTeaGOhLmqL5qaNGLhgqozFKyiCkl3JapKqrCv/qaZ+uNkqrog7eWimYryZ63pa52gdorX9O2RamwhrrWKq+shokkXOKCWtJeU6pYrG7jklStaX2uOiw1raqbLjemimrqHdyW6eX50brn6RzsuesucGm+WW36EY1r7tlwpspiUMaWmK++H663bF3xtqvj7oOrDCQWSVL5MMrRtjwuxTPOqGYqGoM7Yi8+ksuwfiBPLK8viJr8skAczjur48yLDHHwJKa8bPxalhywjjOnHLNF2ds88+4Dr2pvvdK6x64BbdMcrNLv/weyh4rjTPTOSNdNdRXS+3qukX/O7Ka6QqnMs0xd7qt2UDvqS2KadO7o9uhViyzvc/aTS2l15ZqG+mZekM8MNgTA85suYQHnvjdfcuNcd73Lt514QtD7rHk9UL4eL0i4815wNgqruupbWeLtrZZT+p2nF87nXrjhE/tutiq1846y2TZurrhLuNrMd3A/n3z4dzhKvzwvfYu8ObIY6u55UIFBAA7"

        # 3.Decode barcodes from an base64 string data.
        results = dbr.decode_base64_string(barcode_base64_string)

        # 4.Output the barcode text.
        results_list=[]
        if results != None:
            i = 0
            for res in results:
                results_list.append(res.barcode_text)
                print("Barcode " + str(i) + ":" + res.barcode_text)
                i = i+1
            return results_list
        else:
            print("No data detected.")
            return "No data detected."
    except BarcodeReaderError as bre:
        print(bre)
        return bre.error_info
