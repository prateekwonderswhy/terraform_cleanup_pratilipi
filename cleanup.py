import json
import boto3

client = boto3.client('autoscaling')

f = open('asg_names.json', 'r')

contents = f.read()

f.close()

data = json.loads(contents)

asg_names_list = data['asg_names']['value']

batch_job_asg_list = []

for i in range(len(asg_names_list)):
    if "batch-job" in asg_names_list[i]:
        batch_job_asg_list.append(asg_names_list[i])


for i in range(len(batch_job_asg_list)):
    print(batch_job_asg_list[i])



# for i in range(len(batch_job_asg_list)):
#     response = client.delete_auto_scaling_group(
#     AutoScalingGroupName= batch_job_asg_list[i],
#     ForceDelete=True
# )
