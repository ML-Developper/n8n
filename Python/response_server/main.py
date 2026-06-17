#
#
#
# import requests
# import time
# import threading
#
# # =========================
# # CONFIGURATION
# # =========================
# # zero erreur
# #url = "https://jsonplaceholder.typicode.com/posts/1"
# # erreurs
# #url = "https://api.github.com"
# # faild connection
# #url = "http://fake-server-123456.com"
#
#
# url = "http://localhost/page_server/"
#
#
#
#
#
# # Webhook n8n
# n8n_webhook = "https://jonna-nonadjustable-nichole.ngrok-free.dev/webhook-test/test-server"
#
# nombre_requetes = 20
# timeout = 5
#
# # =========================
# # VARIABLES
# # =========================
#
# success = 0
# fail = 0
# temps_reponse = []
#
# lock = threading.Lock()
#
# # =========================
# # TEST SERVEUR
# # =========================
#
# def tester_serveur():
#     global success, fail
#
#     try:
#         debut = time.time()
#
#         response = requests.get(url, timeout=timeout)
#
#         fin = time.time()
#
#         temps = fin - debut
#
#         with lock:
#             temps_reponse.append(temps)
#
#             if response.status_code == 200:
#                 success += 1
#                 print(f"✅ Serveur OK | {temps:.3f}s")
#
#             else:
#                 fail += 1
#                 print(f"❌ HTTP {response.status_code}")
#
#     except requests.exceptions.Timeout:
#         fail += 1
#         print("❌ Timeout")
#
#     except requests.exceptions.ConnectionError:
#         fail += 1
#         print("❌ Connexion refusée")
#
#     except Exception as e:
#         fail += 1
#         print(f"❌ Erreur : {e}")
#
# # =========================
# # EXECUTION
# # =========================
#
# print(f"\n🚀 Test de {url}\n")
#
# debut_total = time.time()
#
# threads = []
#
# for i in range(nombre_requetes):
#     t = threading.Thread(target=tester_serveur)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# fin_total = time.time()
#
# # =========================
# # ANALYSE
# # =========================
#
# temps_total = fin_total - debut_total
#
# taux_reussite = (success / nombre_requetes) * 100
#
# moyenne = 0
#
# if temps_reponse:
#     moyenne = sum(temps_reponse) / len(temps_reponse)
#
# rps = success / temps_total if temps_total > 0 else 0
#
# # =========================
# # MESSAGE FINAL
# # =========================
#
# if taux_reussite == 100:
#     etat = "Très stable"
#
# elif taux_reussite >= 80:
#     etat = "Stable"
#
# elif taux_reussite >= 50:
#     etat = "Instable"
#
# else:
#     etat = "Serveur faible"
#
# resultat = {
#     "serveur": url,
#     "success": success,
#     "fail": fail,
#     "taux_reussite": taux_reussite,
#     "temps_moyen": moyenne,
#     "capacite_rps": rps,
#     "etat": etat
# }
#
# print("\n📊 Résultat final :")
# print(resultat)
#
# # =========================
# # ENVOI VERS N8N
# # UNIQUEMENT SI ERREUR
# # =========================
#
# if fail > 0:
#
#     try:
#         response = requests.post(
#             n8n_webhook,
#             json=resultat
#         )
#
#         print("\n📡 Erreur détectée → Résultat envoyé à n8n")
#         print(f"Status webhook : {response.status_code}")
#
#     except Exception as e:
#         print(f"\n❌ Erreur envoi n8n : {e}")
#
# else:
#     print("\n✅ Aucun problème détecté → Pas d'envoi à n8n")

import requests
import time
import threading
import psutil
from datetime import datetime
import socket

# =========================
# CONFIGURATION TEST SERVEUR
# =========================

# zero erreur
# url = "https://jsonplaceholder.typicode.com/posts/1"

# erreurs
# url = "https://api.github.com"

# faild connection
# url = "http://fake-server-123456.com"

url = "http://localhost/page_server"

# webhook test serveur
n8n_webhook = "https://jonna-nonadjustable-nichole.ngrok-free.dev/webhook-test/test-server"

nombre_requetes = 20
timeout = 5

# =========================
# CONFIGURATION PC STATUS
# =========================

WEBHOOK_URL = "https://jonna-nonadjustable-nichole.ngrok-free.dev/webhook-test/pc-status"

# =========================
# VARIABLES TEST SERVEUR
# =========================

success = 0
fail = 0
temps_reponse = []

lock = threading.Lock()

# =========================
# TEST SERVEUR
# =========================

def tester_serveur():
    global success, fail

    try:
        debut = time.time()

        response = requests.get(url, timeout=timeout)

        fin = time.time()

        temps = fin - debut

        with lock:
            temps_reponse.append(temps)

            if response.status_code == 200:
                success += 1
                print(f"✓ Serveur OK | {temps:.3f}s")

            else:
                fail += 1
                print(f"✗ HTTP {response.status_code}")

    except requests.exceptions.Timeout:
        fail += 1
        print("✗ Timeout")

    except requests.exceptions.ConnectionError:
        fail += 1
        print("✗ Connexion refusée")

    except Exception as e:
        fail += 1
        print(f"✗ Erreur : {e}")

# =========================
# LANCEMENT TEST SERVEUR
# =========================

def run_server_test():
    global success, fail, temps_reponse

    print(f"\n🚀 Test de {url}\n")

    debut_total = time.time()

    threads = []

    for i in range(nombre_requetes):
        t = threading.Thread(target=tester_serveur)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    fin_total = time.time()

    temps_total = fin_total - debut_total

    taux_reussite = (success / nombre_requetes) * 100

    moyenne = 0
    if temps_reponse:
        moyenne = sum(temps_reponse) / len(temps_reponse)

    rps = success / temps_total if temps_total > 0 else 0

    if taux_reussite == 100:
        etat = "Très stable"
    elif taux_reussite >= 80:
        etat = "Stable"
    elif taux_reussite >= 50:
        etat = "Instable"
    else:
        etat = "Serveur faible"

    resultat = {
        "serveur": url,
        "success": success,
        "fail": fail,
        "taux_reussite": taux_reussite,
        "temps_moyen": moyenne,
        "capacite_rps": rps,
        "etat": etat
    }

    print("\n📊 Résultat final :")
    print(resultat)

    if fail > 0:
        try:
            response = requests.post(
                n8n_webhook,
                json=resultat
            )

            print("\n⚠ Erreur détectée → résultat envoyé à n8n")
            print(f"Status webhook : {response.status_code}")

        except Exception as e:
            print(f"\n✗ Erreur envoi n8n : {e}")

    else:
        print("\n✓ Aucun problème détecté → pas d'envoi à n8n")

# =========================
# PC STATUS
# =========================

def zone(v, warn, danger):
    if v < warn:
        return "green"
    elif v < danger:
        return "orange"
    else:
        return "red"

def collect():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    temp = None

    if hasattr(psutil, "sensors_temperatures"):
        try:
            temps = psutil.sensors_temperatures()
            for v in temps.values():
                if v:
                    temp = v[0].current
                    break
        except:
            pass

    data = {
        "host": socket.gethostname(),
        "timestamp": datetime.now().isoformat(),

        "cpu": {
            "value": cpu,
            "zone": zone(cpu, 50, 80)
        },

        "ram": {
            "value": ram,
            "zone": zone(ram, 60, 80)
        },

        "disk": {
            "value": disk,
            "zone": zone(disk, 70, 90)
        },

        "temperature": {
            "value": temp,
            "zone": "green" if temp and temp < 60 else "orange" if temp and temp < 80 else "red"
        }
    }

    return data

def has_error(data):
    return any(
        data[k]["zone"] in ["orange", "red"]
        for k in ["cpu", "ram", "disk", "temperature"]
    )

def send(data):
    r = requests.post(WEBHOOK_URL, json=data, timeout=5)
    print("STATUS:", r.status_code)
    print("RESPONSE:", r.text)

def run_pc_monitor():
    data = collect()

    print("\n🖥 DATA COMPLETE:")
    print(data)

    if not has_error(data):
        print("✓ Tout est normal → rien envoyé")
        return

    print("⚠ Erreur détectée → envoi à n8n")
    send(data)

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    run_server_test()
    run_pc_monitor()