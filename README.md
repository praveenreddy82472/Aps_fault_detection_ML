step:-1
pip install -r requirements.txt

step:-2
download your dataset : wget https://raw.githubusercontent.com/avnyadav/sensor-fault-detection/main/aps_failure_training



Git commands

If you are starting a project and you want to use git in your project

```
git init
```
Note: This is going to initalize git in your source code.

OR

You can clone exiting github repo

```
git clone <github_url>
```

Note: Clone/ Downlaod github repo in your system

Add your changes made in file to git stagging are

```
git add file_name
```

Note: You can given file_name to add specific file or use "." to add everything to staging are

Create commits

```
git commit -m "message"
```

```
git push origin main
```
Note: origin--> contains url to your github repo main--> is your branch name

To push your changes forcefully.

```
git push origin main -f
```

To pull changes from github repo

```
git pull origin main
```

Note: origin--> contains url to your github repo main--> is your branch name
