from bs4 import BeautifulSoup
import urllib
import re
from time import sleep
from collections import Counter
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams['figure.figsize'] = (10.0, 8.0)