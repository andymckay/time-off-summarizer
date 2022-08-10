Summarizes a "My Org's Time Off" report from Workday into something I can grok. Download the output from workday into a `.xlsx` file.

To install dependencies:

```pip3 install -r requirements.txt```

Once you've got a downloaded file:

```bash
python3 summary.py path-to-your-downloaded.xlsx
|Name                   |Days off|
----------------------------------
|Jill                   |12.0    |
|Bob                    |3.0     |
```
