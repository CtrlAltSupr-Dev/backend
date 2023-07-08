from pprint import pprint

from params import *
from bc_parser import bc_search
from time import sleep
from schedule import process_schedule
import csv

procesed_initials = {}
procesed_nrcs = {}
new_sections = 0
new_courses = 0
all_courses = []


"""                all_courses[c["nrc"]] = ",".join([c["initials"],
                    c["name"],
                    c["school"],
                    c["area"],
                    c["section"],
                    c["nrc"],
                    c["teachers"],
                    c["format"],
                    c["campus"]"""

HEADER = ["Nombre", "Escuela", "Seccion", "NRC", "Profesores", "Formato", "Campus"]


def log_comb(comb):
    print("Current search: ", comb)


def process_courses(courses, period):
    global procesed_initials, procesed_nrcs
    global new_courses, new_sections
    global all_courses
    for c in courses:
        # Skip recently procesed sections
        if c["nrc"] in procesed_nrcs:
            continue

        # Mark as procesed inmediatly to avoid repeating errors
        procesed_nrcs[c["nrc"]] = True

        """
                        all_courses[c["nrc"]] = ",".join([c["initials"],
                    c["name"],
                    c["credits"],
                    c["school"],
                    c["area"],
                    c["category"],
                    c["section"],
                    c["nrc"],
                    c["teachers"],
                    c["format"],
                    c["campus"],
                    c["is_english"],
                    c["is_removable"],
                    c["is_special"],
                    c["available_quota"],
                    c["total_quota"]])
        
        """

        try:
            if c["initials"] not in procesed_initials:

                all_courses.append([str(x) for x in
                    [c["name"],
                    c["school"],
                    c["section"],
                    c["nrc"],
                    c["teachers"],
                    c["format"],
                    c["campus"]]])
                procesed_initials[c["initials"]] = True

        except Exception as err:
            print(c, err)


def scrap(current_comb = ""):

    if len(current_comb) >= 5:
        return

    characters = LETTERS if (len(current_comb) <= 2) else NUMBERS

    for letter in characters:
        comb = current_comb + letter
        if len(comb) == 1:
            log_comb(comb)
        courses = bc_search(comb, PERIOD)

        process_courses(courses, PERIOD)

        if len(courses) > 50:
            scrap(comb)


if __name__ == "__main__":
    scrap()
    with open("dump.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(HEADER)
        csvwriter.writerows(all_courses)

