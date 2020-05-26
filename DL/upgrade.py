import os

acc = os.popen("cat /var/lib/jenkins/workspace/mlops_job1/accuracy.txt")
acc1 = acc.read()
print(acc1)
acc2 = acc1.rstrip()
print(acc2)
acc3 = float(acc2)


if acc3<80:
    x = os.popen("cat /var/lib/jenkins/workspace/mlops_job1/train.py | grep model.add | wc -l")
    x1 = x.read()
    x2 = x1.rstrip()
    x3 = int(x2)
    print(x3)
    if x3==2:
        y = 'model.add(Dense(units=32, activation=\"relu\"))'
    elif x3==3:
        y = 'model.add(Dense(units=16, activation=\"relu\"))'
    elif x3==4:
        y = 'model.add(Dense(units=8, activation=\"relu\"))'
    else:
        print("MAAF KARDO")
        exit()
    os.system("sed -i '/softmax/ i {}' /var/lib/jenkins/workspace/mlops_job1/train.py".format(y))
    os.system("curl -u admin:redhat http://192.168.99.102:8080/view/Ml%20+%20Jenkins/job/mlops_job2/build?token=trainjob")
    acc = os.popen("cat /var/lib/jenkins/workspace/mlops_job1/accuracy.txt")
    acc1 = acc.read()
    print(acc1)
    acc2 = acc1.rstrip()
    print(acc2)
    acc3 = float(acc2)
else:
    os.system("curl -u admin:redhat 192.168.99.102:8080/view/Ml%20+%20Jenkins/job/mlops_mail/build?token=mailing")
    print("ACCURACY ABOVE 80")

