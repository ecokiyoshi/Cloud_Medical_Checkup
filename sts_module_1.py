# -*- coding:utf-8 -*-

import boto3
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
   role_arn=u'arn:aws:iam::XXXXXXXXX:role/XXXXXXX-role1'
   ext_id=u'test'
   res = get_sts_credentials(role_arn)
   print res

session=boto3.session.Session(region_name='ap-northeast-1',aws_access_key_id=res['AccessKeyId'],aws_secret_access_key=res['SecretAccessKey'],aws_session_token=res['SessionToken'])
s3=session.client('s3')
res=s3.list_buckets()
print res 

