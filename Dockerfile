From FROM python:3.8.5-slim-buster

RUN apt update && apt upgrade -y && \
    apt-get install --no-install-recommends -y \
    aria2\
    debian-keyring \
    debian-archive-keyring \
    bash \
    bzip2 \
    curl \
    figlet \
    fonts-liberation \
    git \
    gnupg \
    util-linux \
    libappindicator3-1 \
    libffi-dev \
    libjpeg-dev \
    libjpeg62-turbo-dev \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libwebp-dev \
    linux-headers-amd64 \
    musl-dev \
    musl \
    neofetch \
    php-pgsql \
    python3-lxml \
    postgresql \
    postgresql-client \
    python3-psycopg2 \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libxss1 \
    python3-pip \
    python3-requests \
    python3-sqlalchemy \
    python3-tz \
    python3-aiohttp \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    libreadline-dev \
    libyaml-dev \
    gcc \
    sqlite3 \
    libsqlite3-dev \
    sudo \
    zlib1g \
    ffmpeg \
    libssl-dev \
    libgconf-2-4 \
    libxi6 \
    xvfb \
    unzip \
    libopus0 \
    libopus-dev \
    xdg-utils \
    && rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp
    
#clonning repo
RUN git clone https://github.com/wolfgangindia/wolfuserbot.git /root/userbot
#working directory
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH
CMD ["python3","-m","userbot"]
