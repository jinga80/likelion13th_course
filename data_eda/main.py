import myeda
import seaborn as sns

tips = sns.load_dataset("tips")

myeda.basicinfo(tips)