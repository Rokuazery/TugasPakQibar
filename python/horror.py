import sys, time

def printTyping(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slowTyping(text):
    printTyping(text, delay=0.06)

def fastTyping(text):
    printTyping(text, delay=0.015)

def opening():
    slowTyping("Jam 5 sore di sekolah...")
    printTyping("Semua udah pulang, tinggal kamu yang masih di kelas.")
    slowTyping("Tiba-tiba lampu kedip-kedip...")
    fastTyping("dan kamu dengar suara samar-samar...")
    slowTyping("'Siapa yang makan ciki di sini??' 😨")

def encounter():
    printTyping("\nKamu nengok perlahan...")
    slowTyping("Ada sosok putih berdiri di pojokan kelas sambil bawa penghapus papan tulis.")
    fastTyping("Itu... Bu Susi?? Tapi... kok kakinya melayang 😭")
    
    printTyping("\nApa yang kamu lakukan?")
    printTyping("1. Lari secepatnya!")
    printTyping("2. Pura-pura jadi kursi.")
    printTyping("3. Nangis kejer sambil doa.")

    choice = input("> ")

    if choice == "1":
        fastTyping("\nKamu langsung sprint keluar kelas kayak Sonic 💨")
        slowTyping("Tapi tiba-tiba... BRAK!")
        fastTyping("Kamu pun kesandung terus meninggal dunia. 😭")
        printTyping("Tamat.")
        
    elif choice == "2":
        printTyping("\nKamu langsung jongkok, diem, pura-pura jadi kursi kayu.")
        slowTyping("Bu Susi jalan ke arahmu...")
        fastTyping("'Eh kursinya empuk banget ya...'")
        slowTyping("...Ternyata dia duduk di kamu. Kamu trauma seumur hidup 😭 Tamat.")
    elif choice == "3":
        printTyping("\nKamu nangis histeris sambil baca doa.")
        slowTyping("Kamu pun meninggal dunia dan bertemu Bu Susi di alam baka.")
        printTyping("Tamat.")
    else:
        slowTyping("\nKamu bengong gak milih apa-apa...")
        printTyping("Tiba-tiba Bu Susi ilang.")
        fastTyping("Tapi kamu sadar... HP kamu sekarang berubah jadi kapur tulis 😭 Tamat.")

def main():
    opening()
    encounter()

if __name__ == "__main__":
    main()
