FROM bitnami/nginx:1.25.3-debian-11-r4

USER root
# Utwórz katalogi, jeśli nie istnieją
RUN mkdir -p /var/lib/apt/lists/partial

# Skopiuj pliki aplikacji Django do obrazu
COPY . /app

WORKDIR /app

# Zainstaluj zależności
RUN apt-get update && apt-get install -y python3-pip && pip3 install -r requirements.txt

# Uruchom Django w trybie produkcyjnym
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "GymWebsite.wsgi:application"]
