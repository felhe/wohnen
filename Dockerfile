FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./wohnen.py", "inberlinwohnen", "--scrape", "--telegram", "--interval", "5" ]