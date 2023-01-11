import string
import pyperclip
import sqlite3
import os
import random
from time import sleep


__version__ = "1.0.0"
__author__ = "Todo Lodo"


class Main:
    def __init__(self):
        self.chars = list(string.ascii_letters + string.digits + string.punctuation)

        dbFile = rf"{os.path.dirname(__file__) if __file__.endswith('.exe') else os.path.dirname(os.path.dirname(__file__))}\data\passwords.db"

        if not os.path.exists(rf"{os.path.dirname(__file__) if __file__.endswith('.exe') else os.path.dirname(os.path.dirname(__file__))}\data\passwords.db"):
            with open(dbFile, "x") as f:
                pass

        self.conn = sqlite3.connect(dbFile)
        self.curs = self.conn.cursor()

        self.curs.execute("create table if not exists passwords (reference char, username char, password char);")
        self.conn.commit()

        os.system("color")

        # • • •
        print("\n\x1b[1;35m• \x1b[1;32m• \x1b[1;31m•")

        # HEADER
        print("\n\x1b[1;34mPasswords\x1b[1;33m(\x1b[1;32m.py\x1b[1;33m/\x1b[1;31m.exe\x1b[1;33m) \x1b[1;34mconsole \x1b[1;32mscript\x1b[1;33m/\x1b[1;31mapplication\n"
              f"\x1b[0;33m ➝\x1b[1;33m version: \x1b[0;36m{__version__}\n"
              f"\x1b[0;33m ➝\x1b[1;33m author: \x1b[1;35mTodo Lodo\n"
              "\x1b[0;33m ➝\x1b[1;33m src:\x1b[3;36m https://github.com/TodoLodo/Passwords\x1b[0m")

        while True:
            try:
                # main-menu
                command = input("\n\x1b[0;33mChose option (main-menu):\n"
                                " \x1b[1;35m[\x1b[1;32m1\x1b[1;35m]\x1b[0m Generate password\n"
                                " \x1b[1;35m[\x1b[1;32m2\x1b[1;35m]\x1b[0m Store password\n"
                                " \x1b[1;35m[\x1b[1;32m3\x1b[1;35m]\x1b[0m Modify password\n"
                                " \x1b[1;35m[\x1b[1;32m4\x1b[1;35m]\x1b[0m Delete password\n"
                                " \x1b[1;35m[\x1b[1;32m5\x1b[1;35m]\x1b[0m Search password\n"
                                " \x1b[1;35m[\x1b[1;32m6\x1b[1;35m]\x1b[0m Show all passwords\n"
                                " \x1b[1;35m[\x1b[1;32m0\x1b[1;35m]\x1b[0m \x1b[31mExit\n"
                                "\n"
                                "\x1b[35m> \x1b[32m")

                if command == '1':
                    password, avgRep = self.genPass(int(input('\x1b[33mEnter password length: \x1b[1;32m')))
                    pyperclip.copy(password)
                    print(
                        f"\n\x1b[34mPassword {avgRep}% repetition (copied to clipboard!) \x1b[1;35m➝ \x1b[0m{password}")
                    command = input("\x1b[33mChose option:\n"
                                    " \x1b[1;35m[\x1b[1;32m1\x1b[1;35m]\x1b[0m Save password\n"
                                    " \x1b[1;35m[\x1b[1;32m2\x1b[1;35m]\x1b[0m Back to main-menu\n"
                                    " \x1b[1;35m[\x1b[1;32m0\x1b[1;35m]\x1b[0m \x1b[31mExit\n"
                                    "\n"
                                    "\x1b[1;35m> \x1b[1;32m")
                    if command == '1':
                        self.storePass(password)
                    elif command == '0':
                        self.Exit()
                    elif command != 2:
                        self.invalidOption(command)

                elif command == '2':
                    password = input("\x1b[33mEnter password to store: \x1b[1;32m")
                    self.storePass(password)

                elif command == '3':
                    self.modPass()

                elif command == '4':
                    self.delPass()

                elif command == '5':
                    self.search()

                elif command == '6':
                    self.showAllPass()

                elif command.lower() in ['ca', 'clearall']:
                    self.clearAll()

                elif command.lower() in ['i', 'info']:
                    self.info()

                elif command.lower() in ['0', 'exit']:
                    self.Exit()
                else:
                    self.invalidOption(command)

            except KeyboardInterrupt as e:
                print("\n\x1b[0;31mKeyboardInterrupt!")
                self.Exit(69)

    def genPass(self, length):
        charDic = {}
        probs = [1] * len(self.chars)
        password = ""
        avgRep = 0
        for i in range(length):
            char = random.choices(self.chars, weights=probs, k=1)[0]
            password += char
            probs[self.chars.index(char)] = 0
            if sum(probs) == 0:
                probs = [1] * len(self.chars)

            charDic[char] = charDic[char] + 1 if char in charDic else 1

            avgRep = sum((val if val > 1 else 0) / length for val in charDic.values()) * 100

        return password, avgRep

    def storePass(self, password):
        reference = input("\x1b[0;33mEnter reference (nickname): \x1b[1;32m")
        username = input("\x1b[0;33mEnter username: \x1b[1;32m")
        self.curs.execute(f"""insert into passwords (reference, username, password) values (?, ?, ?);""",
                          (reference, username, password))
        self.conn.commit()

        print("\x1b[1;34mPassword stored successfully!\x1b[0m")

    def modPass(self):
        count = self.curs.execute("select count(*) from passwords").fetchone()[0]

        if count:
            self.showAllPass()

            while True:
                command = input(
                    "\n\x1b[0;33mSelect index to modify or (\x1b[1;35m[\x1b[1;32m-1\x1b[1;35m]\x1b[0m Back to main-menu\x1b[0;33m, \x1b[1;35m[\x1b[1;32m0\x1b[1;35m]\x1b[0m \x1b[31mExit\x1b[0;33m): \x1b[1;32m")
                try:
                    if (r := int(command)) in range(1, count + 1):
                        data = self.curs.execute(f"SELECT *, rowid FROM passwords LIMIT 1 OFFSET {r-1}").fetchone()
                        oldRow = data[:-1]
                        rowid = data[-1]

                        reference = input("\x1b[0;33mEnter reference (leave space for same value): \x1b[1;32m")
                        username = input("\x1b[0;33mEnter username (leave space for same value): \x1b[1;32m")
                        password = input("\x1b[0;33mEnter password (leave space for same value): \x1b[1;32m")

                        newRow = (reference if reference != '' else oldRow[0], username if username != '' else oldRow[1],
                                  password if password != '' else oldRow[2])

                        data = [oldRow, newRow]

                        h0max = len("Instance")
                        h1max = len("Reference")
                        h2max = len("Username")
                        h3max = len("Password")
                        for row in data:
                            h1max = len(row[0]) if len(row[0]) > h1max else h1max
                            h2max = len(row[1]) if len(row[1]) > h2max else h2max
                            h3max = len(row[2]) if len(row[2]) > h3max else h3max

                        diff = [oldRow[0] == newRow[0], oldRow[1] == newRow[1], oldRow[2] == newRow[2]]

                        print(f"\n \x1b[1;34mInstance{' ' * (h0max - len('Instance'))} \x1b[1;35m| \x1b[1;34mReference{' ' * (h1max - len('Reference'))} \x1b[1;35m| \x1b[1;34mUsername{' ' * (h2max - len('Username'))} \x1b[1;35m| \x1b[1;34mPassword{' ' * (h3max - len('Password'))}")
                        print(f"\x1b[1;35m-{'-' * h0max}-+-{'-' * h1max}-+-{'-' * h2max}-+-{'-' * h3max}")
                        print(f" \x1b[0;30;43m{' Old' + ' ' * (h0max - len(' Old'))}\x1b[0m \x1b[1;35m| \x1b[{'0' if diff[0] else '0;33'}m{oldRow[0] + ' ' * (h1max - len(oldRow[0]))} \x1b[1;35m| \x1b[{'0' if diff[1] else '0;33'}m{oldRow[1] + ' ' * (h2max - len(oldRow[1]))} \x1b[1;35m| \x1b[{'0' if diff[2] else '0;33'}m{oldRow[2] + ' ' * (h3max - len(oldRow[2]))}")
                        print(
                            f" \x1b[0;30;42m{' New' + ' ' * (h0max - len(' New'))}\x1b[0m \x1b[1;35m| \x1b[{'0' if diff[0] else '1;32'}m{newRow[0] + ' ' * (h1max - len(newRow[0]))} \x1b[1;35m| \x1b[{'0' if diff[1] else '1;32'}m{newRow[1] + ' ' * (h2max - len(newRow[1]))} \x1b[1;35m| \x1b[{'0' if diff[2] else '1;32'}m{newRow[2] + ' ' * (h3max - len(newRow[2]))}")

                        command = input("\n\x1b[0;33mConfirm change?(y/N): \x1b[1;32m")
                        if command.lower() == 'y':
                            self.curs.execute(
                                f"update passwords set reference = {newRow[0]!r}, username = {newRow[1]!r}, password = {newRow[2]!r} where rowid = {rowid}")
                            self.conn.commit()
                            print("\n\x1b[1;34mPassword modified successfully!\x1b[0m")
                        break
                    elif command == '0':
                        self.Exit()
                    elif command == '-1':
                        break
                    else:
                        raise ValueError
                except ValueError:
                    self.invalidOption(command)
        else:
            print("\n\x1b[1;34mNo Records to Modify!")

    def delPass(self):
        count = self.curs.execute("select count(*) from passwords").fetchone()[0]

        if count:
            self.showAllPass()

            rowIndexes = []

            while True:
                command = input("\n\x1b[0;33mSelect indexes to delete separated by spaces or "
                                "(\x1b[1;35m[\x1b[1;32m-1\x1b[1;35m]\x1b[0m Back to main-menu\x1b[0;33m"
                                ", "
                                "\x1b[1;35m[\x1b[1;32m0\x1b[1;35m]\x1b[0m \x1b[31mExit\x1b[0;33m)"
                                ": \x1b[1;32m").split(" ")

                if len(command) == 1 and ('0' in command or '-1' in command):
                    if command[0] == '0':
                        self.Exit()
                    elif command[0] == '-1':
                        break

                elif len(command) > 0:
                    for val in command:
                        try:
                            if (i := int(val)) not in range(1, count + 1):
                                raise ValueError
                            elif i not in rowIndexes:
                                rowIndexes.append(i)
                        except ValueError:
                            self.invalidOption(val)

                    rowIndexes.sort()

                    h0max = len("#")
                    h1max = len("Reference")
                    h2max = len("Username")
                    h3max = len("Password")
                    data = self.curs.execute("select * from passwords").fetchall()

                    for i, row in enumerate(data):
                        h0max = len(str(i)) if len(str(i)) > h0max else h0max
                        h1max = len(row[0]) if len(row[0]) > h1max else h1max
                        h2max = len(row[1]) if len(row[1]) > h2max else h2max
                        h3max = len(row[2]) if len(row[2]) > h3max else h3max

                    print(
                        f"\n \x1b[1;32m#{' ' * (h0max - len('#'))} \x1b[1;35m| \x1b[1;34mReference{' ' * (h1max - len('Reference'))} \x1b[1;35m| \x1b[1;34mUsername{' ' * (h2max - len('Username'))} \x1b[1;35m| \x1b[1;34mPassword{' ' * (h3max - len('Password'))}")
                    print(f"\x1b[1;35m-{'-' * h0max}-+-{'-' * h1max}-+-{'-' * h2max}-+-{'-' * h3max}")

                    for i, row in enumerate(data):
                        print(
                            f" \x1b[{'1;32;41' if i in rowIndexes else '1;32'}m{str(i) + ' ' * (h0max - len(str(i)))}\x1b[0m \x1b[1;35m| \x1b[{'0;31' if i in rowIndexes else '0'}m{row[0] + ' ' * (h1max - len(row[0]))} \x1b[1;35m| \x1b[{'0;31' if i in rowIndexes else '0'}m{row[1] + ' ' * (h2max - len(row[1]))} \x1b[1;35m| \x1b[{'0;31' if i in rowIndexes else '0'}m{row[2] + ' ' * (h3max - len(row[2]))}")

                    command = input("\n\x1b[0;33mConfirm selection for deletion?(y/N): \x1b[1;32m")

                    if command.lower() == 'y':
                        for n, i in enumerate(rowIndexes):
                            i -= n
                            rowid = self.curs.execute(f"SELECT rowid FROM passwords LIMIT 1 OFFSET {i-1}").fetchone()[0]
                            self.curs.execute(f"delete from passwords where rowid = {rowid}")
                            self.conn.commit()

                        print("\n\x1b[1;34mPassword(s) deleted successfully!\x1b[0m")

                        break

                    elif (x := command.lower()) == 'n' or x == '':
                        rowIndexes = []

                    else:
                        self.invalidOption(command)

                elif len(command) == 0:
                    print(f"\x1b[31mChoice(s) can't be empty!\x1b[0m")

        else:
            print("\n\x1b[1;34mNo Records to Delete!")

    def search(self, key=None):
        count = self.curs.execute("select count(*) from passwords").fetchone()[0]

        if count:
            while key is None:
                key = input("\n\x1b[0;33mEnter keyword to search: \x1b[1;32m") if key is None else key
                key = None if not key else key
                if key is None:
                    print("\x1b[0;31mKeyword can't be Empty!")
            h0max = len("#")
            h1max = len("Reference")
            h2max = len("Username")
            h3max = len("Password")

            data = self.curs.execute("select * from passwords").fetchall()

            for i, row in enumerate(data):
                h1max = len(row[0]) if len(row[0]) > h1max else h1max
                h2max = len(row[1]) if len(row[1]) > h2max else h2max
                h3max = len(row[2]) if len(row[2]) > h3max else h3max

            print(f"\n \x1b[1;34m#{' ' * (h0max - len('#'))} \x1b[1;35m| \x1b[1;34mReference{' ' * (h1max - len('Reference'))} \x1b[1;35m| \x1b[1;34mUsername{' ' * (h2max - len('Username'))} \x1b[1;35m| \x1b[1;34mPassword{' ' * (h3max - len('Password'))}")
            print(f"\x1b[1;35m-{'-' * h0max}-+-{'-' * h1max}-+-{'-' * h2max}-+-{'-' * h3max}")

            for i, row in enumerate(data):
                if key in row[0].lower() or key in row[1].lower() or key in row[2].lower():
                    indexes = [[], [], []]
                    for ii, c in enumerate(row):
                        n = 0
                        sc = c.lower()
                        try:
                            while True:
                                _i = sc.index(key)
                                il = _i + len(key)
                                ia = _i
                                ila = il
                                if n:
                                    ia += indexes[ii][n - 1][1]
                                    ila += indexes[ii][n - 1][1]
                                indexes[ii].append((ia, ila))
                                sc = sc[il:]
                                n += 1
                        except ValueError:
                            pass

                    hmaxes = [h1max, h2max, h3max]
                    print(f" \x1b[1;32m{str(i) + ' ' * (h0max - len(str(i)))}", end="")
                    for _ie in range(len(indexes)):
                        print(" \x1b[1;35m|", end="")
                        ie = indexes[_ie]
                        if len(ie):
                            for _ien in range(len(ie)):
                                ien = ie[_ien]
                                if _ien == 0:
                                    print(f" \x1b[0m{row[_ie][:ien[0]]}\x1b[1;37;43m{row[_ie][ien[0]:ien[1]]}", end="\x1b[0m")
                                else:
                                    iep = ie[_ien-1]
                                    print(f"\x1b[0m{row[_ie][iep[1]:ien[0]]}\x1b[1;37;43m{row[_ie][ien[0]:ien[1]]}", end="\x1b[0m")
                                if _ien == len(ie)-1:
                                    print(f"\x1b[0m{row[_ie][ien[1]:]}{' '*(hmaxes[_ie]-len(row[_ie]))}", end="")
                        else:
                            print(f" \x1b[0m{row[_ie]}{' '*(hmaxes[_ie]-len(row[_ie]))}", end="")
                    print("")

        else:
            print("\n\x1b[1;34mNo Records to Search!")

    def showAllPass(self):
        h0max = len("#")
        h1max = len("Reference")
        h2max = len("Username")
        h3max = len("Password")

        data = self.curs.execute("select * from passwords").fetchall()
        for i, row in enumerate(data):
            h0max = len(str(i)) if len(str(i)) > h0max else h0max
            h1max = len(row[0]) if len(row[0]) > h1max else h1max
            h2max = len(row[1]) if len(row[1]) > h2max else h2max
            h3max = len(row[2]) if len(row[2]) > h3max else h3max

        # headers
        print(f" \x1b[1;32m#{' ' * (h0max - len('#'))} \x1b[1;35m|"
              f" \x1b[1;34mReference{' ' * (h1max - len('Reference'))} \x1b[1;35m|"
              f" \x1b[1;34mUsername{' ' * (h2max - len('Username'))} \x1b[1;35m|"
              f" \x1b[1;34mPassword{' ' * (h3max - len('Password'))}")
        # ---------------------------------+---------------------------------------+------------------------------------
        print(f"\x1b[1;35m-{'-' * h0max}-+-{'-' * h1max}-+-{'-' * h2max}-+-{'-' * h3max}-")
        # rows
        for i, row in enumerate(data):
            print(f" \x1b[1;32m{str(i) + ' ' * (h0max - len(str(i)))} \x1b[1;35m|"
                  f" \x1b[0m{row[0] + ' ' * (h1max - len(row[0]))} \x1b[1;35m|"
                  f" \x1b[0m{row[1] + ' ' * (h2max - len(row[1]))} \x1b[1;35m|"
                  f" \x1b[0m{row[2] + ' ' * (h3max - len(row[2]))}")

        # No Records
        if not self.curs.execute("select count(*) from passwords").fetchone()[0]:
            totLength = h0max+h1max+h2max+h3max+3
            halfLength = int(totLength/2)
            print(f"\x1b[0m {' '*halfLength}NO RECORDS{' '*(totLength-halfLength)} ")

    def clearAll(self, yes=False):
        if not yes:
            yes = True if input("\n\x1b[0;31mWARNING! This will delete all passwords, please CONFIRM? (y/N): \x1b[0;32m").lower() == 'y' else False

        if yes:
            self.curs.execute("delete from passwords")
            self.conn.commit()
            print("\n\x1b[1;34mPasswords deleted successfully!\x1b[0m")

    def info(self):
        s = f"Password script or application is based consoled based developed by {__author__} and current installed version is {__version__}"
        for c in s:
            print(c, end="")
            sleep(0.1)

    def Exit(self, e=0):
        print("\n\x1b[1;31m• \x1b[1;32m• \x1b[1;35m•\x1b[0m", end="\n")
        self.conn.close()
        exit(e)

    @staticmethod
    def invalidOption(option):
        print(f"\x1b[31mInvalid option!, {option}\x1b[0m")


if __name__ == "__main__":
    Main()
