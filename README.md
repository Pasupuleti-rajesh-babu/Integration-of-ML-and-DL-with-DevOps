# Integration of ML and DL with DevOps
<p>Firstly, I’m very glad for making out this project. After spending four complete days on this project finally I made it. In the process of doing this project, I’ve learned many new things and I explored so many great things in order to complete this project. And I’m very thankful to Mr. Vimal Daga sir for making me capable enough to make this project.

Well, now I’ll explain the project. Automation makes every large task in the simplest way. Now we’ll e doing automation of Machine learning.</p>

<h2>Problem Statement</h2>
<p>
  1. Create container image that’s has Python3 and Keras or NumPy installed using docker file

2. When we launch this image, it should automatically start to train the model in the container.

3. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins

4. Job1: Pull the Github repo automatically when some developers push the repo to Github.

5. Job2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the software required for the CNN processing).

6. Job3: Train your model and predict accuracy or metrics.

7. Job4: if metrics accuracy is less than 80%, then tweak the machine learning model architecture.

8. Job5: Retrain the model or notify that the best model is being created

9. Create One extra job job6 for monitor: If the container where the app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left
</p>


<h3>Machine learning Docker file<h3>

<img width= 600 src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wmOVHcLJ-hKtC4QLtmmBvA.png">

<h3>Deep learning Docker file</h3>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*iDdhb--OETzXWQDUjnntoQ.png">

<h4>Now you have to create docker image using the following</h4>
<p>
docker build -t ml:v1 . → for machine learning

</p>

<p>docker build -t dl:v1 . → for deep learning</p>

<p>After successful creation of two docker images and now creating the jobs with Jenkins</p>
<h3>Job1</h3>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*txufCImYE3X6BZbj4oienQ.png">
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5JPiySxFiAvlCQjXlJLVug.png">
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*EBb8wMBxS5Bvuchn0UGKMw.png">
<h3>job1 output</h3>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fzw3RlqpRucQ2bxQvTQuEA.png">
<h3>Job2</h3>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*3iPbvzQDp-iJGhbCw7zwIA.png">
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nx0fR5i1ZWl0Mw45s_uImg.png">
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*5IuLcJyHoPrTaQ2eq8ahqA.png">
<h3>job2 output:</h3>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*u5pEfoseVjMO71Z-n4AYHw.jpeg">
<p>once the task is done it will send the mail to client</p>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*h3ihvyLZTU0jNUB1qyaU4A.png">
<h3>Job3</h3>
<p>This job checks the accuracy of the model and if it is less than 85 tweaks the code a bit and asks Job 2 to retrain it.</p>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UctFv_BZekmn3lWoFA1lkg.png">
<h3>job3 output:</h3>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*slTQkIF62W3rh6Wv4proCg.jpeg">
<h3>Final Output</h3>
<p>we recevied accuracy to the mail</p>
<img width= 600 
src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*IFXPOiFNYJoTCI5wcfRcow.png">
