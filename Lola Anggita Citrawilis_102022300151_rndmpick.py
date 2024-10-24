import random
import os

AGENT = {
    "Iso": {"type": "Duelist", "status": "idle"},
    "Jett": {"type": "Duelist", "status": "idle"},
    "Neon": {"type": "Duelist", "status": "idle"},
    "Phoenix": {"type": "Duelist", "status": "idle"},
    "Raze": {"type": "Duelist", "status": "idle"},
    "Reyna": {"type": "Duelist", "status": "idle"},
    "Yoru": {"type": "Duelist", "status": "idle"},
    "Breach": {"type": "Initiator", "status": "idle"},
    "Fade": {"type": "Initiator", "status": "idle"},
    "Gekko": {"type": "Initiator", "status": "idle"},
    "Kay/o": {"type": "Initiator", "status": "idle"},
    "Skye": {"type": "Initiator", "status": "idle"},
    "Sova": {"type": "Initiator", "status": "idle"},
    "Chamber": {"type": "Sentinel", "status": "idle"},
    "Cypher": {"type": "Sentinel", "status": "idle"},
    "Deadlock": {"type": "Sentinel", "status": "idle"},
    "Killjoy": {"type": "Sentinel", "status": "idle"},
    "Sage": {"type": "Sentinel", "status": "idle"},
    "Astra": {"type": "Controller", "status": "idle"},
    "Brimstone": {"type": "Controller", "status": "idle"},
    "Harbor": {"type": "Controller", "status": "idle"},
    "Omen": {"type": "Controller", "status": "idle"},
    "Viper": {"type": "Controller", "status": "idle"}
}


def Main():
    loop_abc = True
    while loop_abc:
        random_key = random.choice(list(AGENT.keys()))
        if AGENT[random_key]["type"] == "Duelist" and AGENT[random_key]["status"] == "idle":
            duelist = random_key
            AGENT[random_key]["status"] = "in use"
            break

    while loop_abc:
        random_key = random.choice(list(AGENT.keys()))
        if AGENT[random_key]["type"] == "Initiator" and AGENT[random_key]["status"] == "idle":
            initiator = random_key
            AGENT[random_key]["status"] = "in use"
            break

    while loop_abc:
        random_key = random.choice(list(AGENT.keys()))
        if AGENT[random_key]["type"] == "Controller" and AGENT[random_key]["status"] == "idle":
            controller = random_key
            AGENT[random_key]["status"] = "in use"
            break

    while loop_abc:
        random_key = random.choice(list(AGENT.keys()))
        if AGENT[random_key]["type"] == "Sentinel" and AGENT[random_key]["status"] == "idle":
            sentinel = random_key
            AGENT[random_key]["status"] = "in use"
            break

    while loop_abc:
        random_key = random.choice(list(AGENT.keys()))
        if AGENT[random_key]["status"] == "idle":
            fill = random_key
            AGENT[random_key]["status"] = "in use"
            break

    os.system('cls')
    print("========== Valorant Random Pick ==========")
    print("|| " + "Duelist".ljust(12) + ": " + str(duelist).ljust(22) + " ||")
    print("|| " + "Initiator".ljust(12) + ": " +
          str(initiator).ljust(22) + " ||")
    print("|| " + "Controller".ljust(12) + ": " +
          str(controller).ljust(22) + " ||")
    print("|| " + "Sentinel".ljust(12) + ": " + str(sentinel).ljust(22) + " ||")
    print("|| " + str(AGENT[random_key]["type"]
                      ).ljust(12) + ": " + str(fill).ljust(22) + " ||")
    print("==========================================")
    print("*Press Enter! to spin another picking")
    spin = input("")

    if spin == "":
        AGENT[duelist]["status"] = "idle"
        AGENT[initiator]["status"] = "idle"
        AGENT[controller]["status"] = "idle"
        AGENT[sentinel]["status"] = "idle"
        AGENT[fill]["status"] = "idle"
        Main()
    else:
        exit


Main()
