# -*- coding:utf-8 -*-

import boto3
import json
import syslog_output

# get sts creadentials

def get_sts_credentials(role_arn):
	try:
		client = boto3.client('sts')
		res = client.assume_role(
	    	RoleArn=role_arn,
	    	RoleSessionName='test1',
#	   	Externalld=ext_id
        	)
		rt=res['Credentials']
	except Exception, e:
	  	msg=u'exception error' + str(e)
 	  	syslog_output.logging_msg(msg)
	  	rt=None
	return rt

#
if __name__ == '__main__':
   role_arn=u'arn:aws:iam::XXXXXXXXX:XXXXXXXX-role1'
   ext_id=u'test'
   res = get_sts_credentials(role_arn)
#print res

session=boto3.session.Session(region_name='ap-northeast-1',aws_access_key_id=res['AccessKeyId'],aws_secret_access_key=res['SecretAccessKey'],aws_session_token=res['SessionToken'])

s3=session.client('s3')
s3_res=s3.list_buckets()
#print s3_res

f = open('S3.txt', 'w')
f.write(str(s3_res))
f.close()

ec2 = session.client('ec2')
ec2_res = ec2.describe_instances()
#print ec2_res

f = open('EC2.txt', 'w')
f.write(str(ec2_res))
f.close()

trail=session.client('cloudtrail')
trail_res=trail.describe_trails()
#print trail_res

f = open('trail.txt', 'w')
f.write(str(trail_res))
f.close()

rds=session.client('rds')
rds_res=rds.describe_db_snapshots()
#print rds_res

f = open('rds.txt', 'w')
f.write(str(rds_res))
f.close()
