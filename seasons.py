from datetime import date
import sys, inflect

p = inflect.engine()
def main():
    output = minutes()
    print(output,"minutes")

def ask_date():
        try:
            year, month, day = input("Date Of Birth:").split("-")
            return date(int(year), int(month), int(day))
        except ValueError:
            sys.exit("Invalid date")
def minutes():
     return p.number_to_words(((date.today() - ask_date()).days * 24 * 60), andword="")
if __name__ == "__main__":
    main()