import os

acc = os.popen("cat /var/lib/jenkins/workspace/j2/accuracy.txt")
acc1 = acc.read()
print(acc1)
acc2 = acc1.rstrip()
print(acc2)
acc3 = float(acc2)


if acc3<80:
    x = os.popen("cat /var/lib/jenkins/workspace/j2/train.py | grep model.add | wc -l")
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
    os.system("sed -i '/softmax/ i {}' /var/lib/jenkins/workspace/j2/train.py".format(y))
    os.system("curl -u root:1622@Psr http://192.168.55.107:8080/job/j2/build?token=rajesh")
    acc = os.popen("cat /var/lib/jenkins/workspace/j2/accuracy.txt")
    acc1 = acc.read()
    print(acc1)
    acc2 = acc1.rstrip()
    print(acc2)
    acc3 = float(acc2)
else:
    print("ACCURACY ABOVE 80")

