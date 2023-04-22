import pyshark
import time
import csv
from mapping import printRecord
import boto3 
from botocore.exceptions import NoCredentialsError
from datetime import datetime 

ACCESS_KEY = 'xxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxx'


# define interface
f=open("abhi2.csv","a+",newline='')
fields = ["Src_IP","Src_City","Src_Latitude","Src_Longitude","Dst_IP","Dst_City","Dst_Latitude","Dst_Longitude"]
#add gere new column name
writer = csv.DictWriter(f, fieldnames=fields)

writer.writeheader()
f.close()
try:
    networkInterface = "enX0"


    # define capture object
    capture = pyshark.LiveCapture(interface=networkInterface, output_file="New.pcap")

    print("listening on %s" % networkInterface)
    for packet in capture.sniff_continuously():
        # adjusted output
    #        try:
        # get timestamp
        try:
            localtime = time.asctime(time.localtime(time.time()))

            # get packet content
            protocol = packet.transport_layer  # protocol type
            src_addr = packet.ip.src  # source address
            src_port = packet[protocol].srcport  # source port
            dst_addr = packet.ip.dst  # destination address
            dst_port = packet[protocol].dstport  # destination port

            # output packet info


            print("%s IP %s:%s <-> %s:%s (%s)" % (localtime, src_addr, src_port, dst_addr, dst_port, protocol))
            print("----------------More Info-----------------------")
            #print("%s %s"%(src_addr,dst_addr))
            print(packet)
            current = "Ahmedabad"
            f = open("abhi2.csv", "a+", newline='')
            writer = csv.DictWriter(f, fieldnames=fields)
            #print(src_addr,dst_addr)
            if '192.' not in src_addr:
                src_location = printRecord(src_addr)
            else:
                src_location={'city':current,
                    'latitude' : 23.022505,
                    'longitude' : 72.571365}
            if '192.' not in dst_addr:
                dst_location = printRecord(dst_addr)
            else:
                dst_location={'city':current,
                    'latitude' : 23.022505,
                    'longitude' : 72.571365}

            writer.writerow({"Src_IP": src_addr,"Src_City":src_location['city'] , "Src_Latitude": src_location['latitude'], "Src_Longitude": src_location['longitude'],
                             "Dst_IP": dst_addr,"Dst_City":dst_location['city'], "Dst_Latitude": dst_location['latitude'], "Dst_Longitude": dst_location['longitude']})
            #add new column dict here to save in csv
            f.close()


        except (AttributeError, RuntimeError, TypeError, NameError) as e:
        #     # ignore packets other than TCP, UDP and IPv4
            pass
except KeyboardInterrupt:
    inFile = open('abhi2.csv', 'r')

    outFile = open('IPlocation2.csv', 'w')

    listLines = []

    for line in inFile:

        if line in listLines:
            continue

        else:
            outFile.write(line)
            listLines.append(line)

    outFile.close()

    inFile.close()

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('IPlocation2.csv', 'network-romeel-security', 'IPLocation.csv')
uploaded2 = upload_to_aws('New.pcap', 'network-romeel-security', 'ANMA.pcap')
