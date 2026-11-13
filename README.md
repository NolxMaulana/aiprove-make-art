# AIProve — Make Art: "The Agent Gazette"

Poster original untuk bounty `make-art-aiprove` (PosterJudge).
Bukan character sheet: ini satu poster utuh, dengan maskot sebagai satu elemen di dalamnya.

## Karya utama

- `poster.png` — 2400 × 3000 px, portrait, PNG. Karya utama untuk field `link` saat submit.
- `poster-square.png` — 2400 × 2400 px, varian persegi untuk feed/sosial, komposisi yang sama dipadatkan.
- `build_poster.py` — skrip pembuat poster (Python + Pillow, font sistem Liberation/DejaVu). Menjalankan ulang skrip menghasilkan ulang kedua PNG.

## Konsep

**"The Agent Gazette" — koran broadsheet yang isinya terminal.**

AIProve memberi wajah pada ide intinya: jangan percaya klaim, buktikan.
Poster ini memperlakukan AIProve seperti halaman depan koran serius,
lalu menaruh bukti itu di dalam jendela terminal, tempat agen benar-benar bekerja.

Headline-nya lugas dan bisa dibaca sekilas dari jauh:

> DON'T TAKE THEIR WORD FOR IT. / MAKE THEM PROVE IT.

Sub-headline: "The proof is the product." Lalu footer: "No hype, just proof."

## Elemen visual

- **Masthead broadsheet:** wordmark AIPROVE serif tebal hitam di atas garis merah,
  dengan eyebrow monospace "THE AGENT GAZETTE" dan aturan garis ganda khas koran.
  Kertas krem hangat, bingkai ganda hitam, tipografi serif/sans/mono yang tegas.
- **Jendela terminal:** panel gelap dengan tiga titik jendela, prompt
  `$ aiprove verify --agent`, lalu baris hasil `claim ... CHECKED`,
  `proof ... VALID`, `verdict ... PROVEN`, dan prompt penutup `$ prove it.`
  Ini sisi "terminal" dari brief: bukti bukan slogan, tapi keluaran yang bisa dibaca.
- **Maskot "Pru":** robot kecil original di dalam terminal, bukan maskot pinjaman.
  Kepala krem berbingkai hitam, antena merah, layar gelap dengan tanda centang hijau
  sebagai "mata", kursor, dan name tag merah PRU. Satu pose, satu peran:
  si pemeriksa bukti. Di poster ini ia elemen pendukung, bukan sheet karakter.
- **Tanda centang hijau besar** di sudut terminal: verdict visual yang langsung terbaca
  bahkan sebelum teksnya dibaca.
- **Tiga kolom koran** di bawah terminal — VERIFY / BUILD / EARN — masing-masing
  satu kalimat pendek, dipisah garis vertikal tipis seperti kolom koran.
- **"IN THIS ISSUE"** (hanya di poster utama): daftar isi tiga baris bernomor merah,
  menutup halaman seperti koran sungguhan dan mengisi komposisi portrait.
- **Palet tegas, sedikit warna:** krem kertas, hitam tinta, merah editorial,
  hijau verdict, plus aksen amber/cyan kecil di terminal. Tidak ada gradien
  mencolok, tidak ada teks kecil yang berantakan, tidak ada watermark pihak lain.

## Kenapa cocok dengan AIProve

- Brief-nya "beri AIProve wajah": wajah di sini adalah masthead koran
  ditambah satu maskot pemeriksa, bukan logo generik.
- Vibe broadsheet-meets-terminal diterjemahkan harfiah: struktur koran
  (masthead, headline, kolom, daftar isi) + isi terminal (prompt, verdict).
- Craft dinilai dari keterbacaan: semua teks berukuran besar, hierarki jelas
  (masthead → headline → terminal → kolom → footer), dan poster tetap terbaca
  saat diperkecil ke thumbnail.
- Tidak ada angka atau klaim yang tidak terverifikasi di dalam poster:
  tidak ada skor, peringkat, atau jumlah hadiah. Yang ada hanya janji
  yang bisa diuji: klaim dicek, bukti valid, verdict terbukti.

## Originalitas

Seluruh karya digambar dengan kode dari nol (Pillow, bentuk geometris dan teks),
tanpa foto, tanpa aset stok, tanpa meniru karya orang lain.
Font yang dipakai adalah font sistem open (Liberation, DejaVu).
Tidak ada token, kunci, alamat wallet, atau kode referral di file mana pun di sini.

## Link yang diusulkan untuk submit

Usulan field `link` (koordinator yang mengunggah ke GitHub):

- `https://github.com/NolxMaulana/aiprove-make-art/blob/main/poster.png`

Repo di atas belum dibuat oleh builder ini; koordinator perlu membuat repo
`aiprove-make-art` dan mengunggah `poster.png` ke branch `main` sebelum submit,
lalu verifikasi URL blob tersebut terbuka sebagai gambar.
Varian persegi bisa diunggah di repo yang sama sebagai `poster-square.png`.
