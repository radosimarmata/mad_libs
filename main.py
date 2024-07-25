import random

def get_input(prompt):
  return input(prompt)

def create_story(template, placeholders):
  return template.format(*[get_input(f"Masukkan {placeholder}: ") for placeholder in placeholders])

def main():
  stories = [
    ("Pada suatu hari, seorang {0} bernama {1} pergi ke hutan {2}. Di sana, dia menemukan {3} yang {4}. Dengan segera, dia {5}.",
      ["profesi", "nama", "tempat", "benda", "kata sifat", "kata kerja"]),
    ("Pada hari pertama sekolah, {0} merasa sangat {1}. Guru yang bernama {2} meminta semua murid untuk membawa {3}. Ketika tiba giliran {0}, dia malah membawa {4}.",
      ["nama", "kata sifat", "nama guru", "benda", "benda aneh"]),
    ("Astronot {0} sedang bersiap untuk perjalanan ke planet {1}. Di dalam pesawat luar angkasa, dia menemukan {2} yang {3}. Dengan cepat, dia {4} untuk menyelesaikan masalah.",
      ["nama", "nama planet", "benda", "kata sifat", "kata kerja"]),
    ("Hari ini adalah ulang tahun {0}. Dia merayakannya di {1} dengan tema {2}. Semua orang membawa {3} sebagai hadiah, dan mereka bermain {4} bersama-sama.",
      ["nama", "tempat", "tema pesta", "benda", "permainan"]),
    ("Kapal pesiar {0} berlayar menuju {1}. Tiba-tiba, kapten {2} melihat seekor {3} terjebak di {4}. Dia memutuskan untuk {5} untuk menyelamatkan hewan tersebut.",
      ["nama kapal", "tempat", "nama kapten", "hewan", "benda", "kata kerja"]),
    ("{0} dan temannya {1} mengunjungi museum {2}. Mereka melihat pameran tentang {3} dan menemukan artefak {4} yang sangat {5}. Mereka kemudian {6} di dalam museum.",
      ["nama", "nama teman", "nama museum", "tema pameran", "benda", "kata sifat", "kata kerja"]),
    ("Pada musim panas, {0} pergi ke pantai {1} untuk berlibur. Di sana, dia bermain {2} dan menemukan {3} yang terdampar di pantai. Dia pun {4} dengan gembira.",
      ["nama", "nama pantai", "olahraga air", "benda", "kata kerja"]),
    ("Di laboratorium {0}, ilmuwan {1} sedang melakukan eksperimen dengan {2}. Tiba-tiba, terjadi ledakan yang menghasilkan {3} yang {4}. Dia dengan cepat {5} untuk menyelamatkan hasil penelitiannya.",
      ["nama laboratorium", "nama ilmuwan", "bahan kimia", "benda", "kata sifat", "kata kerja"]),
    ("{0} dan keluarganya mengunjungi taman hiburan {1}. Mereka menaiki wahana {2} dan makan {3} yang sangat {4}. Akhirnya, mereka pulang dengan membawa {5} sebagai kenang-kenangan.",
      ["nama", "nama taman", "nama wahana", "makanan", "kata sifat", "benda"]),
    ("Pada hari kompetisi olahraga, {0} bersiap untuk bertanding di cabang {1}. Dia merasa sangat {2} karena lawannya adalah juara bertahan. Dengan semangat, dia {3} dan akhirnya {4}.",
        ["nama", "cabang olahraga", "kata sifat", "kata kerja", "hasil pertandingan"])
  ]

  print("Selamat datang di permainan Mad Libs!")
  print("Pilih cerita yang ingin Anda mainkan:")

  for i, (story, _) in enumerate(stories):
    print(f"{i + 1}. Cerita {i + 1}")

  choice = int(get_input("Masukkan nomor cerita yang Anda pilih: ")) - 1

  template, placeholders = stories[choice]
  story = create_story(template, placeholders)
  
  print("\nBerikut adalah cerita Mad Libs Anda:\n")
  print(story)

if __name__ == "__main__":
  main()
