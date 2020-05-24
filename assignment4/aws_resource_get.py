import boto3
import argparse
import csv
import socket
import sys


field_names = ['ResourceArn', 'TagKey', 'TagValue']

def writeToCsv(writer, args, tag_list):
    for resource in tag_list:
        print("Extracting tags for resource: " +
              resource['ResourceARN'] + "...")
        for tag in resource['Tags']:
            row = dict(
                ResourceArn=resource['ResourceARN'], TagKey=tag['Key'], TagValue=tag['Value'])
            writer.writerow(row)

def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True,
                        help="Output CSV file (eg, /tmp/tagged-resources.csv)")
    return parser.parse_args()

def main():
    args = input_args()
    list = ['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'af-south-1', 'ap-east-1', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'eu-south-1', 'eu-west-3', 'eu-north-1', 'me-aouth-1', 'sa-east-1']
    for i in list:
        restag = boto3.client('resourcegroupstaggingapi', i)
        with open(args.output, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, quoting=csv.QUOTE_ALL,
                                    delimiter=',', dialect='excel', fieldnames=field_names)
            writer.writeheader()
            response = restag.get_resources(ResourcesPerPage=50)
            writeToCsv(writer, args, response['ResourceTagMappingList'])
            while 'PaginationToken' in response and response['PaginationToken']:
                token = response['PaginationToken']
                response = restag.get_resources(
                    ResourcesPerPage=50, PaginationToken=token)
                writeToCsv(writer, args, response['ResourceTagMappingList'])

if __name__ == '__main__':
    main()
