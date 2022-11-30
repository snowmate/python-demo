<p align="center">
    <img  width="20%" height="20%" src=/assets/logo.png>
</p>


# Snowmate - Python Demo
&nbsp;&nbsp;

Snowmate generates unit tests with inputs, mocks, and assertions based on your software's behavior. &nbsp;&nbsp;

This demo project will allow you to feel how Snowmate works, generate unit tests, and quickly execute them.
Snowmate can support any Python project and save a considerable amount of time on test authoring.

&nbsp;&nbsp;

### Installation

Clone this project and install the requirements.txt file

```shell
git clone https://github.com/snowmate/python-demo.git
cd python-demo
python3 -m pip install -r requirements.txt
```

&nbsp;&nbsp;


### Getting Started

1. Download Snowmate's VSCode extension / PyCharm plugin [here](download.snowmate.io).

2. A sign-in modal will pop up in your IDE after downloading. Use your email to sign in to Snowmate.
3. After signing in, open the `main.py` file, and a short onboarding process will start immediately.
4. After adding snowlib.start to your code [Onboarding step 4/4], execute the `main.py` file.
   Make sure to add snowlib.start in `main.py`, where this comment appears:

    ```python
    # Install, import, and add snowlib.start(...) here ---->
    ```

5. Execute the `main.py` file.
6. Wait a few seconds and... check out the tests Snowmate generated for you!


&nbsp;&nbsp;

#### On VSCode. click on the "Snow Snowmate tests" button to see the generated tests

![VSCode with Snowmate](/assets/VSCode.png?raw=true "")



#### On PyCharm, click on the Snowmate's dog logo to see the generated tests

![PyCharm with Snowmate](/assets/PyCharm.png?raw=true "")


&nbsp;&nbsp;

&nbsp;&nbsp;



### Support
Contact support any time at support@snowmate.io

### License
Apache 2.0