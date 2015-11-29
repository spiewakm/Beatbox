# beatbox

Repozytorium `'beatbox'` zawiera następujące pliki oraz foldery:

* `beatbox.py`: główna aplikacja, która wykorzystuje ponadto poniższe moduły:

	* `read_song.py`: moduł do odczytywania definicji utworu, oraz kolejności tracków oraz sampli;

	* `create_song.py`: moduł do tworzenia demo, uwzględniając definicje utworu, w szczególności takie charakterystyki jak: bpm, attack, decay;

	* `save_song.py`: moduł do zapisu stworzonego wektora częstotliwości do pliku z rozszerzeniem .wav;

	* `nutes.py`: modul pomocniczy: generowanie nutek, podstawowa nutka oparta jest na funkcji $\sin$;

	* `instruments.py`: modul pomocniczy: generowanie dźwięków z dowolnego instrumentu, w poniższych utworach została wykorzystana kombinacja funckji $\sin$, ale można również użyć innych kształtów fali, np. fala piłokształtna.


Wykorzystując powyższe moduły, w szczególności główną aplikację beatbox.py
można wygenerować demo poniższych utworów:

  `mam_chusteczke/`

  `szla_dzieweczka/`

  `harry_potter/`

  `winter_is_coming/`


Każdy folder składa się:

  * `defs.txt`: definicja utworu, informacje na temat bpm, attack, decay;

	* `song.txt`: kolejność odtwarzania tracków;

	* `trackXY.txt`: kolejność odwarzania sampli (sample w tym samym wierszu odtwarzane są w tej samej chwili);

	* `sampleXY.wav/txt`: sample w formacie .wav lub .txt 
	  definicja instrumentu, kazdy plik sampleXY.txt powinien zawierać informacje na temat: 
	  
	     * "id" instrumentu, 
	  
	    * "fun" funkcji z której generujemy nutki dla wybranego instrumentu, 
	  
	    * "duration" czas trwania grania nutki, 
	  
	    * "vol" glosnosc nutek generowanych z wybranego instrumentu, 
	  
	    * "attack", 
	  
	    * "decay".


Utworzone demo można znaleźć w katalogu `/var/tmp/nazwa_utworu`, gdzie nazwa jest taka sama jak nazwa katalogu. Każde demo jest zapisywane w formacie .wav.

Istnieje możliwość stworzenia demo dla spakowanych folderów (format .zip).
