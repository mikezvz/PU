# Dieses Spiel ist von mir, Mike Zogheib. In diesem Spiel geht einfach darum, Quiz Fragen zu beantworten. 
  #Es ist Simpel: Es gibt 5 Themenbereiche und zu jedem Themenbereich gibt es mindestens 20 Fragen. Für jede richtig beantwortete Frage kriegt man Punkte.  
    #Meistens ist es so, dass es eine Frage gibt und man kann aus 4 Antworten auswählen. 
    #In dem Fall muss man eine der Antwortmöglichkeiten 1:1 eintippen aber ohne Bindestrich. 
    #Manchmal muss man sie aber auch eintippen ohne verschiedene Antwortmöglichkeiten zur Verfügung gestellt zu bekommen, oder es ist eine Ja/Nein Frage.
     #Es kann auch sein, dass mehrere Antworten möglich sind für eine Frage. Dies wird dann aber angegeben. 
      #Es wird jeweils nicht gesagt, ob man eine Frage richtig beantwortet und es wird auch bis zum Ende eines Quizes kein Punktestand angezeigt. 
      #Am Ende eines Quizes kann man sich diese immer mit dem Befehl "Punktezahl anzeigen" sich anzeigen lassen.

PunktzahlSchulwissen = 0
PunktzahlFussball = 0
PunktzahlPolitik = 0
PunktzahlRechtundGesetz = 0
PunktzahlSchweizerBildung = 0
PunktzahlGesamt = 0 

Themenbereiche = ["Schulwissen", "Fussball", "Politik", "RechtundGesetz", "SchweizerBildung"]

def Schulwissen():
    
    global PunktzahlGesamt 
    
    global PunktzahlSchulwissen
    
    PunktzahlSchulwissen = 0
    



    print ("1. Was ist die San Andreas Verwerfung?\n 4 Antwortmöglichkeiten:\n- Eine Verwerfung\n- Eine Plattengrenze\n- Eine Müllhalde\n- Eine Touristenattraktion")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Eine Plattengrenze":
        PunktzahlSchulwissen+=1
        
    print ("2. Vor was schützt die Ozonschicht?\n 4 Antwortmöglichkeiten:\n- Wärme der Sonne\n- Aliens\n- UV-Strahlen\n- Weltraumobjekte (Weltraumschrott, Asteroiden, etc.")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "UV-Strahlen":
        PunktzahlSchulwissen+=1
        
    print ("3. Was ist ein Tiefdruckgebiet?\n 4 Antwortmöglichkeiten:\n- Ein Gebiet mit niedrigem Luftdruck \n- Ein Gebiet, das weit unter dem Meeresspiegel ist\n- Ein Gebiet mit wenig Druck \n- Ein Gebiet mit wenig Menschen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Ein Gebiet mit niedrigem Luftdruck":
        PunktzahlSchulwissen+=1
    
    print ("4. Was ist ein Hochdruckgebiet?\n 4 Antwortmöglichkeiten:\n- Ein Gebiet mit hohen Luftdruck\n- Ein Gebiet, das weit über dem Meeresspiegel ist\n- Ein Gebiet mit hohem Luftdruck\n- Ein Gebiet mit wenig Menschen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Ein Gebiet mit hohem Luftdruck":
        PunktzahlSchulwissen+=1
    
    print ("5. Warum gibt es Sommer- und Winterzeit?\n 4 Antwortmöglichkeiten:\n- Wegen politischer Streitigkeiten\n- Damit Sommer und Winter unterschieden werden können\n- Weil die Tage im Sommer länger sind als im Winter\n- Weil es frueher eine Taktik war, damit Energie zu sparen und es wurde einfach nie abgeschafft")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Weil es frueher eine Taktik war, damit Energie zu sparen und es wurde einfach nie abgeschafft":
    
    print ("6. Wie wirkt sich der Treibhauseffekt hauptsächlich auf unser Klima aus?\n 4 Antwortmöglichkeiten:\n- Erderwaermung\n- Auf der Erde wird es immer kaelter\n- Schlechte Luft\n- Es gibt weltweit mehr Todesfaelle")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Erderwaermung":
        PunktzahlSchulwissen+=1
    
    print ("7. Wie entsteht Sand?\n 4 Antwortmöglichkeiten:\n- In den untersten Schichten der Erde entsteht er über Millionen Jahre hinweg\n- Der Wind schleift über Jahrtausende Steine ab\n- Im Meer gibt es einen Prozess namens Sandifizierung. Dieser geschieht durch Tiere\n- Man nimmt an, er wurde vor Zehntausenden von Jahren von Menschen erschaffen und verstreut, als ritueller Vorgang")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Der Wind schleift über Jahrtausende Steine ab":
        PunktzahlSchulwissen+=1
    
    print ("8. Warum gibt es das Schaltjahr?\n 4 Antwortmöglichkeiten:\n- Es war die Erfindung eines Mannes, mit dem Ziel, dass Arbeitnehmende weniger freie Tage pro Jahr haben\n- Weil ein Jahr nicht ganz 365 Tage hat. Alle 4 Jahre wird ein Tag hinzugefuegtgt, damit kein Tag verschenkt wird\n- Es ist ein religiöses Ritual\n- Nur in Frankreich gibt es dieses Jahr. Im Schaltjahr gibt es einen Tag, an dem Frankreich seine Erinnerungskultur pflegt")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Weil ein Jahr nicht ganz 365 Tage hat. Alle 4 Jahre wird ein Tag hinzugefuegt, damit kein Tag verschenkt wird":
        PunktzahlSchulwissen+=1
    
    print ("9. Um welche Uhrzeit steht die Sonne senkrecht über dem Äquator?\n 4 Antwortmöglichkeiten:\n- 15:30\n- 13:00\n- 13h00\n- 12:00")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "12:00":
        PunktzahlSchulwissen+=1
    
    print ("10. Die Erdachse ist schief, das weiss man. Wie schief ist sie wirklich?\n 4 Antwortmöglichkeiten:\n- 23,5 Grad\n- 40 Grad\n- 10 Grad\n- 86,5 Grad")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "23,5 Grad":
        PunktzahlSchulwissen+=1
    
    print ("11. Was ist der Unterschied zwischen Magma und Lava?\n 4 Antwortmöglichkeiten:\n- Es sind zwei komplett verschiedene Substanzen\n- Die eine Droge ist etwas stärker, die andere etwas milder\n- Sie unterscheiden sich nur in Farbe\n- Magma befindet sich im Erdinneren, Magma an der Erdoberflaeche")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Magma befindet sich im Erdinneren, Magma an der Erdoberflaeche":
        PunktzahlSchulwissen+=1
        
    print ("12. Mit Hilfe welcher Orte/Inseln könnte man sein Geburtstag zweimal am Tag feiern? Mehrere Antworten möglich.\n 4 Antwortmöglichkeiten:\n- Marianen, Karolinen\n- Gilbert-Inseln, Hawaii-Inseln\n- Sydney, Wellington\n- Peking, Tokyo")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Gilbert-Inseln, Hawaii-Inseln" or "Sydney, Wellington" in Eingabe:
        PunktzahlSchulwissen+=1

    print ("13. Was ist die Hauptstadt der Schweiz? \n 4 Antwortmöglichkeiten:\n- Zürich\n- Lausanne\n- Bern\n- Genf")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Bern":
        PunktzahlSchulwissen+=1
    
    print ("14. Was ist die Hauptstadt von Kenia?\n 4 Antwortmöglichkeiten:\n- Benicus\n- Nairobi\n- Assassaka\n- Accra")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Nairobi":
        PunktzahlSchulwissen+=1

    print ("15. Was ist die Hauptstadt von Thailand?\n 4 Antwortmöglichkeiten:\n- Bangkok\n- King Kong\n- Baht\n- Cumulus")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Bangkok":
        PunktzahlSchulwissen+=1
        
    print ("16. Welches ist der grösste Planet im Sonnensystem\n 4 Antwortmöglichkeiten:\n- Jupiter\n- Saturn\n- Erde\n- Uranus")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Jupiter":
        PunktzahlSchulwissen+=1

    print ("17. Welches ist das flächenmässig grösste Land der Welt?\n 4 Antwortmöglichkeiten:\n- China\n- Kanada\n- Grönland\n- Russland")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Russland":
        PunktzahlSchulwissen+=1
    
    print ("18. Welches ist der flächenmässig grösste Kontinent der Welt?\n 4 Antwortmöglichkeiten:\n- Australien\n- Nordamerika\n- Asien\n- Europa")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Asien":
        PunktzahlSchulwissen+=1
        
    print ("19. Welcher See ist grösser?\n 2 Antwortmöglichkeiten:\n- Bodensee \n- Victoria-See")
    Eingabe = input ("Tippen Sie den Namen von dem, der grösser ist 1:1 ein:")
    if Eingabe == "Victoria-See":
        PunktzahlSchulwissen+=1
        
    print ("20. Wie viele Halbkantone hat die Schweiz?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "6":
        PunktzahlSchulwissen+=1
    
    PunktzahlGesamt += PunktzahlSchulwissen
        
    Themenbereiche.remove ("Schulwissen")
    
    if Themenbereiche == False:
        print ("Herzlichen Glückwunsch, Sie sind am Ende des Quizes angelangt, Sie können stolz sein darauf!\n Sie zwei Möglichkeiten:\n Gesamter Punktestand ausgeben lassen\nProgrammbeenden")
        Eingabe = input("Wählen Sie eine Möglichkeit aus und tippen Sie diese 1:1 ein")
        if Eingabe == "Gesamter Punktestand ausgeben lassen":
            print (str(PunktzahlGesamt) + "/100")
        elif Eingabe == "Programmbeenden":
            quit()
        
    print ("Wollen Sie sich den Punktestand dieses Quizes anzeigen lassen oder den gesamten Punktestand?\nSie haben drei Möglichkeiten:\nGesamter Punktestand\nPunktestand Schulwissen\nNichts anzeigen")
    PunktestandJaNein = input("Wählen Sie aus einer der Optionen aus. Option bitte 1:1 abtippen")
    if PunktestandJaNein == "Gesamter Punktestand":
        print(str(PunktzahlGesamt) + "/100")
    elif PunktestandJaNein == "Punktestand Schulwissen":
        print (str(PunktzahlSchulwissen) + "/20")
    elif PunktestandJaNein == "Nichts anzeigen":
        pass
    
    print ("Mit welchem Themenbereich möchten Sie fortfahren?\n Diese Themenbereiche stehen Ihnen noch zur Verfügung:")
    print (Themenbereiche)
    
    Eingabe = input ("Wählen Sie einen Themenbereich aus und tippen Sie diesen 1:1 ein oder beenden Sie das Programm mit dem Befehl Programmbeenden")
    if Eingabe in Themenbereiche and Eingabe == "Fussball":
        Fussball()
    elif Eingabe in Themenbereiche and Eingabe == "Politik":
        Politik()
    elif Eingabe in Themenbereiche and Eingabe == "RechtundGesetz":
        RechtundGesetz()
    elif Eingabe in Themenbereiche and Eingabe == "SchweizerBildung":
        SchweizerBildung()
    elif Eingabe == "Programmbeenden":
        quit()
        
def Fussball ():
    
    global PunktzahlGesamt
    
    global PunktzahlFussball
    
    PunktzahlGesamt = 0 
    
    PunktzahlFussball = 0
    
    
    print ("1. Wo wurde Fussball erfunden?\n 4 Antwortmöglichkeiten:\n- England\n- Argentinien\n- Deutschland\n- Italien")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "England":
        PunktzahlFussball+=1
        
    print ("2. Wozu dient die Torlinientechnik?\n 4 Antwortmöglichkeiten:\n- Um zu erfassen, ob ein Ball wirklich drin ist im Tor\n- Sie ist für den Torwart gedacht, sodass er nie zu weit aus dem Tor geht\n- Sie ist für den Spieler gedacht, damit der nicht über die Torlinie rennt, sonst ist es ein Foul\n- Sie ist dafür gedacht, die Länge der Torlinie zu messen, damit die Linie nicht zu lang ist")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Um zu erfassen, ob ein Ball wirklich drin ist im Tor":
        PunktzahlFussball+=1
        
    print ("3. Wenn man einen Penalty schiesst, von welcher Distanz schiesst man dann?\n 4 Antwortmöglichkeiten:\n- 5m\n- 1km\n- 11m\n- 10m")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "11m":
        PunktzahlFussball+=1
        
    print ("4. Aus wie vielen Spielern besteht eine Fussballmannschaft, einschliesslich Torwart?\n 4 Antwortmöglichkeiten:\n- 10\n- 11\n- 15\n- 18")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "11":
        PunktzahlFussball+=1
        
    print ("5. Welches Land hat die erste Fussballweltmeisterschaft gewonnen?\n 4 Antwortmöglichkeiten:\n- Japan\n- Deutschland\n- Chile\n- Uruguay")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Uruguay":
        PunktzahlFussball+=1
        
    print ("6. Wann hat die Schweiz zum ersten Mal eine WM gewonnen?\n 4 Antwortmöglichkeiten:\n- Nie\n- 1965\n- 1962\n- 2002")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Nie":
        PunktzahlFussball+=1
        
    print ("7. Wann hat Italien zum ersten Mal eine WM gewonnen?\n 4 Antwortmöglichkeiten:\n- 1962\n- 1934\n- 1954\n- 1972")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "1934":
        PunktzahlFussball+=1
        
    print ("8. Wann hat Deutschland zum ersten Mal eine WM gewonnen?\n 4 Antwortmöglichkeiten:\n- 1942\n- 1950\n- 1954\n- 1968")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "1954":
        PunktzahlFussball+=1
        
    print ("9. Wer ist 2022 der Trainer der Schweizer Fussball-Nationalmannschaft\n 4 Antwortmöglichkeiten:\n- Joachim Löw\n- Ottmar Hitzfeld\n- Vladimir Petkovic\n- Murat Yakin")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Murat Yakin":
        PunktzahlFussball+=1
        
    print ("10. Wer ist der Gastgeber der WM 2022?\n 4 Antwortmöglichkeiten:\n- Kratar\n- Katar\n- Östreich\n- Grönland")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Katar":
        PunktzahlFussball+=1

    print ("11. War die Schweiz schon mal Gastgeber einer WM?")
    Eingabe = input ("Ja oder Nein:")
    if Eingabe == "Ja":
        PunktzahlFussball+=1
        
    print ("12. Welches der Länder ist nicht bei der Gruppenphase der WM 2022 dabei? Mehrere Antworten möglich.\n 4 Antwortmöglichkeiten:\n- Kambodscha\n- Italien\n- Senegal\n- Mexico")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Kambodscha" or "Italien":
        PunktzahlFussball+=1
        
    print ("13. Welcher der Spieler erlitt 2022 einen Herzstillstand in einem Spiel?\n 4 Antwortmöglichkeiten:\n- Christian Erikssen\n- Cristiano Ronaldo\n- Romelu Lukaka\n- Mohammed Saleh")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Christian Erikssen":
        PunktzahlFussball+=1

    print ("14. Wie es in Deutschland eine Bundesliga gibt, gibt es auch eine Fussballliga in der Schweiz. Wie heisst sie\n 4 Antwortmöglichkeiten:\n- Swiss League\n- Super League\n- Stars League\n- Cross League")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Super League":
        PunktzahlFussball+=1
        
    print ("15. Wer schoss das Siegestor für Deutschland im Finale der WM 2014?\n 4 Antwortmöglichkeiten:\n- Mario Goetze\n- Toni Kros\n- Manuel Neuerer\n- Götzüm Bondum")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Mario Goetze":
        PunktzahlFussball+=1
        
    print ("16. Welcher der Spieler ist aktuell nicht im Kader der Schweizer Nati?\n 4 Antwortmöglichkeiten:\n- Denis Zakaria\n- Xherdan Shaqiri\n- Ruben Vargas\n- Diablo Dias")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Diablo Dias":
        PunktzahlFussball+=1
        
    print ("17. Welcher Spieler ist aktuell Kapitän der Schweizer Nati")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Granit Xhaka":
        PunktzahlFussball+=1
        
        print ("18. Aus welchem Land kommt Xherdan Shaqiri?\n 4 Antwortmöglichkeiten:\n- Albanien\n- Kosovo\n- Montenegro\n- Serbien")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Kosovo":
        PunktzahlFussball+=1
        
    print ("19. Bei welcher Mannschaft hatte Ronaldo noch nie gespielt?\n 4 Antwortmöglichkeiten:\n- Real Madrid\n- Juventus\n- Liverpool\n- Benfica Lissabon")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Benfica Lissabon":
        PunktzahlFussball+=1
        
    print ("20. Aus welchem Land kommt Ronaldo?\n 4 Antwortmöglichkeiten:\n- Portugal\n- Brasilien\n- Chile\n- Spanien")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Portugal":
        PunktzahlFussball+=1
        
    PunktzahlGesamt+=PunktzahlFussball
        
    Themenbereiche.remove ("Fussball")
    
    if Themenbereiche == False:
        print ("Herzlichen Glückwunsch, Sie sind am Ende des Quizes angelangt, Sie können stolz sein darauf!\n Sie haben drei Möglichkeiten:\n Gesamter Punktestand ausgeben lassen\n Gesamter Punktestand grafisch ausgeben lassen\n Programmbeenden")
        Eingabe = input("Wählen Sie eine Möglichkeit aus und tippen Sie diese 1:1 ein")
        if Eingabe == "Gesamter Punktestand ausgeben lassen":
            print (str(PunktzahlGesamt) + "/100")
        elif Eingabe == "Programmbeenden":
            quit()
        
    print ("Wollen Sie sich den Punktestand dieses Quizes anzeigen lassen oder den gesamten Punktestand?\nSie haben drei Möglichkeiten:\nGesamter Punktestand\nPunktestand Fussball\nNichts anzeigen")
    PunktestandJaNein = input("Wählen Sie aus einer der Optionen aus. Option bitte 1:1 abtippen")
    if PunktestandJaNein == "Gesamter Punktestand":
        print(str(PunktzahlGesamt) + "/100")
    elif PunktestandJaNein == "Punktestand Fussball":
        print (str(PunktzahlFussball) + "/20")
    elif PunktestandJaNein == "Nichts anzeigen":
        pass
    
    print ("Mit welchem Themenbereich möchten Sie fortfahren?\n Diese Themenbereiche stehen Ihnen noch zur Verfügung:")
    print (Themenbereiche)
        
    Eingabe = input ("Wählen Sie einen Themenbereich aus und tippen Sie diesen 1:1 ein oder beenden Sie das Programm mit dem Befehl Programmbeenden")
    if Eingabe in Themenbereiche and Eingabe == "Schulwissen":
        Schulwissen()
    elif Eingabe in Themenbereiche and Eingabe == "Politik":
        Politik()
    elif Eingabe in Themenbereiche and Eingabe == "RechtundGesetz":
        RechtundGesetz()
    elif Eingabe in Themenbereiche and Eingabe == "SchweizerBildung":
        SchweizerBildung()
    elif Eingabe == "Programmbeenden":
        quit()
        
def Politik():
    
    global PunktzahlGesamt
    
    global PunktzahlPolitik
    
    PunktzahlPolitik = 0
    
    print ("1. Was für eine Staatsform hat die Schweiz aktuell\n 4 Antwortmöglichkeiten:\n- Monarchie\n- Diktatur\n- Demokratie\n- Kommunismus")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Demokratie":
        PunktzahlPolitik+=1
        
    print ("2. Was ist das Mindestalter in der Schweiz, um für Politiker, Initativen usw. abzustimmen?")
    Eingabe = input ("Tippen Sie die Zahl ein:")
    if Eingabe == "18":
        PunktzahlPolitik+=1
        
    print ("3. Welche Kriterien sind nötig, um politisch aktiv zu werden in der Schweiz? Mehrere Antworten möglich.\n 4 Antwortmöglichkeiten:\n- Volljaehrigkeit\n- keine geistige Behinderung\n- Ein breites, fundiertes Wissen ueber Politik\n- CH-Buerger")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Volljeahrigkeit" or "CH-Buerger" or "keine geistige Behinderung":
        PunktzahlPolitik+=1
        
    print ("4. Was ist das Ständemehr?\n 4 Antwortmöglichkeiten:\n- Bei einer Abstimmung reicht fuerr ein Ja nicht nur die Stimme der einzelnen, sondern jeder Kanton muss auch noch als Ganzes dafür abstimmen \n- Die Mehrheit des Ständerats stimmt für ein Ja ab, damit auch Politiker sich beteiligen können an Abstimmungen\n- Der Bundesrat stimmt mit ab, damit auch Politiker sich beteiligen können an Abstimmungen\n- Der Nationalrat stimmt mit ab, weil er gross ist")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Bei einer Abstimmung reicht fuer ein Ja nicht nur die Stimme der Einzelnen, sondern jeder Kanton muss auch noch als Ganzes dafür abstimmen":
        PunktzahlPolitik+=1
        
    print ("5. Reicht ein Ständemehr alleine aus?")
    Eingabe = input ("Tippen Sie Ja oder Nein 1:1 ein")
    if Eingabe == "Nein":
        PunktzahlPolitik+=1
        
    print ("6. Welche Priorität haben die Drei Gewalten in der Schweiz? Das Erste ist das Wichtigste.\n 4 Antwortmöglichkeiten:\n-Judikative, Legislative, Exekutive\n- Legislative, Exekutive, Judikative\n- Exekutive, Judikative, Legislative\n- Es gibt keine Antwort darauf")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Es gibt keine Antwort darauf":
        PunktzahlPolitik+=1
        
    print ("7. Zu welcher Gewalt gehört die Polizei?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Judikative":
        PunktzahlPolitik+=1
        
    print ("8. Wie viele Mitglieder hat der Bundesrat?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "7":
        PunktzahlPolitik+=1
       
    print ("9. Wann wurde er gegründet?\n 4 Antwortmöglichkeiten:\n- 1945\n- 1905\n- 1933\n- 1848")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "1848":
        PunktzahlPolitik+=1
        
    print ("10. Für welches Departement ist Alain Berset zuständig?\n 4 Antwortmöglichkeiten:\n- Eidgenoessisches Departement des Innern\n- Eidgenoessisches Justiz- und Polizeidepartement\n- Eidgenoessisches Finanzdepartement\n- Eidgenoessisches Departement für Umwelt, Verkehr, Energie und Kommunikation")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Eidgenoessisches Departement des Innern":
        PunktzahlPolitik+=1
        
    print ("11. Warum gibt es nicht einfach ein Mitglied im Bundesrat, sondern Mehrere?\n 4 Antwortmöglichkeiten:\n- Aus Spass\n- Zur Machtverteilung\n- Weil ein Bundesrat alleine zu viel zu tun hätte\n- Damit es weniger Mitglieder im National- und Ständerat gibt")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Zur Machtverteilung":
        PunktzahlPolitik+=1
        
    print ("12. Was ist das Parlament? Mehrere Antworten möglich.\n 4 Antwortmöglichkeiten:\n- National- und Staenderat\n- Bundesrat\n- Die Legislative\n- Die Vereinigung von Bundesrat, Staende- und Nationalrat")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "National- und Staenderat":
        PunktzahlPolitik+=1
        
    print ("13. Welches ist die grosse Kammer?\n 4 Antwortmöglichkeiten:\n- Ständerat\n- Bundesrat\n- Die Gerichte\n- Nationalrat")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Nationalrat":
        PunktzahlPolitik+=1
        
    print ("14. In welchem Rat sitzen mehr Mitglieder?\n 2 Antwortmöglichkeiten:\n- Ständerat\n- Nationalrat")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Nationalrat":
        PunktzahlPolitik+=1
        
    print ("15. Warum hat ein Kanton wie Zürich mehr Mitglieder im Nationalrat, wie z.B Appenzell-Innerhoden?\n 4 Antwortmöglichkeiten:\n- Wegen der Bevölkerungsdichte\n- Wegen der Einwohnerzahl\n- Das wurde halt einfach so bestimmt\n- Weil Appenzell-Innerhoden sich weigert, mehr Mitglieder reinzubringen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Wegen der Einwohnerzahl":
        PunktzahlPolitik+=1
        
    print ("16. Über welche Sache hat das Schweizer Volk nicht zu entscheiden?\n 4 Antwortmöglichkeiten:\n- Abstimmung von Initativen\n- Wahlen von Stände- und Nationalrat\n- Wahlen von Bundesrat\n- Was sie im Supermarkt kaufen möchten, wenn sie in einen gehen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Wahlen von Bundesrat":
        PunktzahlPolitik+=1
        
    print ("17. Ist die SVP im Parlament? Ja oder Nein.")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Ja":
        PunktzahlPolitik+=1
        
    print ("18. Welches ist das unterste Gericht der Schweiz?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Bezirksgericht":
        PunktzahlPolitik+=1
        
    print ("19. Die Europäische Union hat einen Europäischen Gerichtshof für etwas schwerere Verbrechen. Die Schweiz ist nicht in der EU und braucht aber auch ein höheres Gericht. Wie heisst dieses?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Bundesgericht":
        PunktzahlPolitik+=1
        
    print ("20. Wo liegt es?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein, nur Ort oder Stadt, also ohne in oder Sonstiges:")
    if Eingabe == "Lausanne":
        PunktzahlPolitik+=1
        
    Themenbereiche.remove ("Politik")
    
    if Themenbereiche == False:
        print ("Herzlichen Glückwunsch, Sie sind am Ende des Quizes angelangt, Sie können stolz sein darauf!\n Sie haben zwei Möglichkeiten:\n Gesamter Punktestand ausgeben lassen\nProgrammbeenden")
        Eingabe = input("Wählen Sie eine Möglichkeit aus und tippen Sie diese 1:1 ein")
        if Eingabe == "Gesamter Punktestand ausgeben lassen":
            print (str(PunktzahlGesamt) + "/100")
        elif Eingabe == "Programmbeenden":
            quit()
    
    PunktzahlGesamt += PunktzahlPolitik
        
    print ("Wollen Sie sich den Punktestand dieses Quizes anzeigen lassen oder den gesamten Punktestand?\nSie haben drei Möglichkeiten:\nGesamter Punktestand\nPunktestand Politik\nNichts anzeigen")
    PunktestandJaNein = input("Wählen Sie aus einer der Optionen aus. Option bitte 1:1 abtippen")
    if PunktestandJaNein == "Gesamter Punktestand":
        print(str(PunktzahlGesamt) + "/100")
    elif PunktestandJaNein == "Punktestand Politik":
        print (str(PunktzahlPolitik) + "/20")
    elif PunktestandJaNein == "Nichts anzeigen":
        pass
    
    print ("Mit welchem Themenbereich möchten Sie fortfahren?\n Diese Themenbereiche stehen Ihnen noch zur Verfügung:")
    print (Themenbereiche)
        
    Eingabe = input ("Wählen Sie einen Themenbereich aus und tippen Sie diesen 1:1 ein oder beenden Sie das Programm mit dem Befehl Programmbeenden")
    if Eingabe in Themenbereiche and Eingabe == "Fussball":
        Fussball()
    elif Eingabe in Themenbereiche and Eingabe == "Schulwissen":
        Schulwissen()
    elif Eingabe in Themenbereiche and Eingabe == "RechtundGesetz":
        RechtundGesetz()
    elif Eingabe in Themenbereiche and Eingabe == "SchweizerBildung":
        SchweizerBildung()
    elif Eingabe == "Programmbeenden":
        quit()


def RechtundGesetz():
    
    global PunktzahlGesamt
    
    global PunktzahlRechtundGesetz
    
    PunktzahlRechtundGesetz = 0
    
    print ("1. In der Schweiz gibt es viele Gesetzbücher. Welches ist kein Gesetzbuch?\n 4 Antwortmöglichkeiten:\n- USSR\n- StGB\n- ZGB\n- AHVG")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "USSR":
        PunktzahlRechtundGesetz+=1
        
    print ("2. Was ist Ausschreibung für MWSTG?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Mehrwertsteuergesetz":
        PunktzahlRechtundGesetz+=1
        
    print ("3. Welches Gesetzbuch regelt den Verkehr auf Strassen per Gesetz?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Strassenverkehrsgesetzbuch":
        PunktzahlRechtundGesetz+=1
        
    print ("4. Wer von denen nimmt in der Schweiz neue Gesetze an, arbeitet sie aus oder lehnt sie ab\n 4 Antwortmöglichkeiten:\n- Bundesrat\n- Bestimmte Politiker\n- Parlament\n- Bestimmte Parteien")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Parlament":
        PunktzahlRechtundGesetz+=1
        
    print ("5. Welches Gesetz gehört nicht zum StGB?\n 4 Antwortmöglichkeiten:\n- Wer einen Tierversuch durchfuehren will, benoetigt eine Bewilligung der zustaendigen kantonalen Behoerderde\n- Wer eine Ehe schliesst oder eine Partnerschaft eintragen laesst, obwohl er verheiratet ist oder in eingetragener Partnerschaft lebt, wer mit einer Person, die verheiratet ist oder in eingetragener Partnerschaft lebt, die Ehe schliesst oder die Partnerschaft eintragen laesst, wird mit einer Freiheitsstrafe von bis zu drei Jahren oder Geldstrafe bestraft\n- Wer jemanden eine fremde bewegliche Sache zur Aneignung wegnimmt, um sich oder einem anderen damit unrechtmaessig zu bereichern, wird mit Freiheitsstrafe bis zu fuenf Jahren oder Geldstrafe bestraft\n- Wer jemanden unrechtmaessig festnimmt oder gefangen haelt oder jemanden in anderer Weise unrechtmaessig die Freiheit entzieht, wer jemanden durch Gewalt, List oder Drohung entfuehrt, wird mit Freiheitsstrafe bis zu fuenf Jahren oder Geldstrafe bestraft")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Wer einen Tierversuch durchfuehren will, benoetigt eine Bewilligung der zustaendigen kantonalen Behoerde ":
        PunktzahlRechtundGesetz+=1
        
    print ("6. Welchem Gesetz unterliegt Kokain allgemein?\n 4 Antwortmöglichkeiten:\n- Kokaingesetz\n- Drogengesetz\n- Rauschmittelgesetz\n- Betaeubungsmittelgesetz")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Betaeubungsmittelgesetz":
        PunktzahlRechtundGesetz+=1

    print ("7. Welches Betäubungsmittel darf man in einer Menge von 10g oder weniger besitzen, ohne sich strafbar zu machen?\n 4 Antwortmöglichkeiten:\n- Cannabis\n- LSD\n- Snus\n- Mariuhana")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Cannabis":
        PunktzahlRechtundGesetz+=1 
        
    print ("8. Es gibt verschiedene Betäubungsmittel, die in der Schweiz verboten sind. Welches wird nicht als verboten beschrieben im Bundesgesetz über die Betäubungsmittel und die psychotropen Stoffe?\n 4 Antwortmöglichkeiten:\n- Cannabis\n- Rauchopium\n- LSD\n- Kokain")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Rauchopium":
        PunktzahlRechtundGesetz+=1
        
    print ("9. Kommen wir zur Gesetzgebung für Alkohol. Welches alkoholische Getränk fällt ab einem alkoholischen Prozentanteil von unter 18% nicht unter das Alkoholgesetz?\n 4 Antwortmöglichkeiten:\n- Bier\n- Wein\n- Alcopops\n- Spirituosen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Wein":
        PunktzahlRechtundGesetz+=1
        
    print ("10. Wein und Bier dürfen an ... -Jährige verkauft werden")
    Eingabe = input ("Tippen Sie die Zahl ein:")
    if Eingabe == "16":
        PunktzahlRechtundGesetz+=1
        
    print ("11. Spirituosen und Alcopops dürfen an ... -Jährige verkauft werden")
    Eingabe = input ("Tippen Sie die Zahl ein:")
    if Eingabe == "18":
        PunktzahlRechtundGesetz+=1
        
    print ("12. Für welches alkoholische Getränk ist Werbung im Radio und im Fernsehen verboten?\n 4 Antwortmöglichkeiten:\n- Wein\n- Alle Getraenke\n- Alcopops \n- Bier")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Alle Getraenke":
        PunktzahlRechtundGesetz+=1
        
    print ("13. Dürfen Privatpersonen Bier brauen? Ja oder Nein.")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Ja":
        PunktzahlRechtundGesetz+=1
        
    print ("14. Ab welchem Alter ist man stellungspflichtig, also ab welchem Alter muss man dem Militär beitreten?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "18":
        PunktzahlRechtundGesetz+=1

    print ("15. Beispielssituation: Ein Autofahrer fährt mit 140 km/h auf der Autobahn. Er überschreitet damit das Tempolimit von 120 km/h damit um 20 km/h. Welche Strafe ist möglich?\n 4 Antwortmöglichkeiten:\n- Mindestens 1 Monat Entzug\n- 3 tägige Gefängnisstrafe\n- Keine Strafe, es gibt nur eine Verwarnung\n- Fahrzeug wird weggenommen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Keine Strafe, es gibt nur eine Verwarnung":
        PunktzahlRechtundGesetz+=1
        
    print ("16. Beispielssituation: Max, 15 zwingt seinen Kollegen zu einer Handlung, die er gar nicht will. Er möchte seinen Kollegen dazu bringen, die Toiletten in der Schule verunreinigen. Welche Strafe ist dem Gesetz nach möglich?\n 4 Antwortmöglichkeiten:\n- Freiheitsstrafe\n- Geldbusse\n- Ärger\n- Schulverweis")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Geldbusse":
        PunktzahlRechtundGesetz+=1
        
    print ("17. Welche dieser Gesetze gibt es nicht?\n 4 Antwortmöglichkeiten:\n- Wer den Praesenzunterricht fuer mindestens 10 Tage nicht aktiv besucht und sich auch nicht abmeldet, der kann mit Bestaetigung der zustaendigen Schulverwaltung eine Geldstrafe von mindestens 300 Fr. erhalten.\n- Wer eine Behoerde, ein Mitglied einer Behoerde oder einen Beamten an einer Handlung hindert, die innerhalb ihrer Amtsbefugnisse liegt, wird mit Geldstrafe bis zu 30 Tagessaetzen bestraft.\n- Wer Tiere haelt oder betreut, muss sie angemessen naehren, pflegen, ihnen die für ihr Wohlergehen notwendige Beschaeftigung und Bewegungsfreiheit sowie soweit noetig Unterkunft gewaehren.\n- Wer den menschlichen Koerper oder dessen Teile gegen Entgelt oder einen anderen geldwerten Vorteil veraeussert oder erwirbt, wird mit einer Freiheitsstrafe oder einer Geldstrafe bestraft")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Wer den Praesenzunterricht fuer mindestens 10 Tage nicht aktiv besucht und sich auch nicht abmeldet, der kann mit Bestaetigung der zustaendigen Schulverwaltung eine Geldstrafe von mindestens 300 Fr. erhalten.":
        PunktzahlRechtundGesetz+=1
        
    print ("18. Welches Gesetzbuch oder welche Verfassung regelt die Grundrechte in der Schweiz?\n 4 Antwortmöglichkeiten:\n- Bundesgesetz über die Grundrechte\n- Eidgenössisches Einkommen über die Grundrechte\n- Bundesverfassung über die Grundrechte\n- Bundesverfassung der Schweizerischen Eidgenossenschaft")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Bundesverfassung der Schweizerischen Eidgenossenschaft":
        PunktzahlRechtundGesetz+=1
        
    print ("19. Welches Gesetz wurde 2022 nicht neu eingeführt/verschärft\n 4 Antwortmöglichkeiten:\n- Bestimmungen für besseren Schutz von Mensch und Umwelt\n- Strengere Import- und Exportbestimmungen für nicht EU-Waren\n- Unbürokratische Änderung des Geschlechtseintrags\n- Besserer Schutz vor häuslicher Gewalt und Stalking")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Strengere Import- und Exportbestimmungen für nicht EU-Waren":
        PunktzahlRechtundGesetz+=1
        
    print ("20. Welches Gesetz würdest du gerne neu einführen?")
    Eingabe = input ("Schreibe was du willst")
    PunktzahlRechtundGesetz+=1
    
    PunktzahlGesamt+=PunktzahlRechtundGesetz
    
    Themenbereiche.remove ("RechtundGesetz")
    
    if Themenbereiche == False:
        print ("Herzlichen Glückwunsch, Sie sind am Ende des Quizes angelangt, Sie können stolz sein darauf!\n Sie haben zwei Möglichkeiten:\n Gesamter Punktestand ausgeben lassen\nProgrammbeenden")
        Eingabe = input("Wählen Sie eine Möglichkeit aus und tippen Sie diese 1:1 ein")
        if Eingabe == "Gesamter Punktestand ausgeben lassen":
            print (str(PunktzahlGesamt) + "/100")
        elif Eingabe == "Programmbeenden":
            quit()
    
    print ("Wollen Sie sich den Punktestand dieses Quizes anzeigen lassen oder den gesamten Punktestand?\nSie haben drei Möglichkeiten:\nGesamter Punktestand\nPunktestand Recht und Gesetz\nNichts anzeigen")
    PunktestandJaNein = input("Wählen Sie aus einer der Optionen aus. Option bitte 1:1 abtippen")
    if PunktestandJaNein == "Gesamter Punktestand":
        print(str(PunktzahlGesamt) + "/100")
    elif PunktestandJaNein == "Punktestand Recht und Gesetz":
        print (str(PunktzahlRechtundGesetz) + "20")
    elif PunktestandJaNein == "Nichts anzeigen":
        pass
    
    print ("Mit welchem Themenbereich möchten Sie fortfahren?\n Diese Themenbereiche stehen Ihnen noch zur Verfügung:")
    print (Themenbereiche)
        
    Eingabe = input ("Wählen Sie einen Themenbereich aus und tippen Sie diesen 1:1 ein oder beenden Sie das Programm mit dem Befehl Programmbeenden")
    if Eingabe in Themenbereiche and Eingabe == "Fussball":
        Fussball()
    elif Eingabe in Themenbereiche and Eingabe == "Politik":
        Politik()
    elif Eingabe in Themenbereiche and Eingabe == "Schulwissen":
        Schulwissen()
    elif Eingabe in Themenbereiche and Eingabe == "SchweizerBildung":
        SchweizerBildung()
    elif Eingabe == "Programmbeenden":
        quit()
        

def SchweizerBildung():
    
    global PunktzahlGesamt
    
    global PunktzahlSchweizerBildung
    
    PunktzahlSchweizerBildung = 0
    
    print ("1. Erstmal grundsätzlich: Welches dieser Dinge muss man mindestens absolviert haben, um in die Berufswelt einzusteigen?\n 4 Antwortmöglichkeiten:\n- Lehre\n- Schule\n- Studium\n- Hochschule")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Schule":
        PunktzahlSchweizerBildung+=1

    print ("2. Welches dieser Angebote schliesst direkt an die obligatorische Schulzeit an? Mehrere Antworten möglich.\n 4 Antwortmöglichkeiten:\n- Mittelschule\n- Gymnasium\n- Lehre\n- Hochschule")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if "Lehre" or "Gymnasium" or "Mittelschule" in Eingabe:
        PunktzahlSchweizerBildung+=1
        
    print ("3. Welches ist keine Grundkompetenz für eine Berufslehre?\n 4 Antwortmöglichkeiten:\n- Gestalterische Faehigkeiten\n- Rechnen\n- Schreiben\n- Lesen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Gestalterische Faehigkeiten":
        PunktzahlSchweizerBildung+=1
        
    print ("4. Was ist keine grundlegende Anforderung für eine Berufslehre?\n 4 Antwortmöglichkeiten:\n- Pünktlichkeit\n- Sportlichkeit\n- Zuverlässigkeit\n- Kommunikations- und Teamfähigkeit")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Sportlichkeit":
        PunktzahlSchweizerBildung+=1
        
    print ("5. Was ist EFZ ausgeschrieben?\n 4 Antwortmöglichkeiten:\n- Eidgenoessisches Farmerzeugnis\n- éducation fédérale Zurich\n- Eidgenoessisches Faehigkeitszeugnis\n- Eidgenoessisches Fachhochschulen-Zeugnis")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Eidgenoessisches Faehigkeitszeugnis":
        PunktzahlSchweizerBildung+=1
        
    print ("6. Wie viele EFZ und EBA Berufe gibt es ungefähr?\n 4 Antwortmöglichkeiten:\n- 250\n- 400\n- 420\n- 120")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "250":
        PunktzahlSchweizerBildung+=1
        
    print ("7. Wie kann man in der Regel an einer Fachhochschule zugelassen werden?\n 4 Antwortmöglichkeiten:\n- Aufnahmeprüfung\n- IQ-Test\n- Projektabgabe\n- Berufsmaturitaet")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Berufsmaturitaet":
        PunktzahlSchweizerBildung+=1
        
    print ("8. Welches von denen ist ein Studiengebiet einer Fachhochschule?\n 4 Antwortmöglichkeiten:\n- Lebensmittelforschung\n- Technische Wissenschaften\n- Cyberwissenschaften\n- Justizmittel und Gesetze")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Technische Wissenschaften":
        PunktzahlSchweizerBildung+=1
        
    print ("9. Welche Typen von BMS gibt es?\n 4 Antwortmöglichkeiten:\n- BM Lite und BM Pro\n- BM und BM+\n- BM A und BM B\n- BM1 und BM2")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == " BM1 und BM2":
        PunktzahlSchweizerBildung+=1
        
    print ("10. Wie lange dauern BM1 und BM2?\n 4 Antwortmöglichkeiten:\n- Gleich lange\n- 3 Jahre und 4 Jahre \n- 4 Jahre und 3 Jahre\n- Gleich lange ist moeglich, aber BM2 kann auch nur 3 Jahre gehen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Gleich lange ist moeglich, aber BM2 kann auch nur 3 Jahre gehen":
        PunktzahlSchweizerBildung+=1
        
    print ("11. Was ist der Unterschied zwischen BM1 und BM2?\n 4 Antwortmöglichkeiten:\n- Waehrend der Lehre und nach der Lehre\n- BM1 mehr Praxisorientiert\n- BM2 teurer \n- BM1 ist nur fuer EFZ-Lehren und BM2 nur fuer EBA-Lehren")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Waehrend der Lehre und nach der Lehre":
        PunktzahlSchweizerBildung+=1
        
    print ("12. Was ist die Passarelle?\n 4 Antwortmöglichkeiten:\n- Ein Brueckenangebot\n- Die renommierteste Hochschule der Schweiz\n- Die Aufnahmepruefung für Universitaeten\n- Ein Unterstuetzungsangebot für Leute mit wenig Budget, die sich trotzdem Bildung leisten wollen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Die Aufnahmepruefung für Universitaeten":
        PunktzahlSchweizerBildung+=1
        
    print ("13. Was ermöglicht das Bestehen der Passarelle?\n 4 Antwortmöglichkeiten:\n- Zugang zur BMS\n- Zugang zu allen Studiengaengen der universitaeren Hochschulen der Schweiz sowie zu allen Studiengaengen der Paedagogischen Hochschulen\n- Lehrabschluss\n- Auslandsaufenthalt, Sprachaufenthalt")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Zugang zu allen Studiengaengen der universitaeren Hochschulen der Schweiz sowie zu allen Studiengaengen der Paedagogischen Hochschulen":
        PunktzahlSchweizerBildung+=1
        
    print ("14. Was sind die drei Maturitätstypen?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if "Gym" and "Beruf" and "Fach" in Eingabe:
        PunktzahlSchweizerBildung+=1
        
    print ("15. Was sind die drei Hochschultypen?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if "Universitaer" and "Paedagogischen" and "Fach" in Eingabe:
        PunktzahlSchweizerBildung+=1
        
    print ("16. Wie wird die Stufe der höheren Berufsbildung im Schweizer Bildungssystem noch genannt?")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Tertiaerstufe":
        PunktzahlSchweizerBildung+=1
        
    print ("17. Aus- und Weiterbildungen kosten Geld. Zwischen was wird bei den Kosten unterschieden\n 4 Antwortmöglichkeiten:\n- Ausbildungs- und Lebenskosten\n- Grundlegende Kosten und zusätzliche Kosten für Sachen, die man selber finanziert\n- Kosten für welche man nicht aufkommt und Kosten für welche man aufkommt\n- Kosten für Gegenstände/Materialien unter CHF 100.- und Kosten darüber")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Ausbildungs- und Lebenskosten":
        PunktzahlSchweizerBildung+=1

    print ("18. Für wen sind sogennante Brückenangebote gedacht?\n 4 Antwortmöglichkeiten:\n- Leute ohne Anschlussloesungsung\n- Leute die eine Weiterbildung anstreben\n- Leute die Bruecken ueberqueren moechten\n- Leute, die kein Geld haben, um sich eine Ausbildung zu finanzieren")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Leute ohne Anschlussloesung":
        PunktzahlSchweizerBildung+=1
        
    print ("19. Welche Wege gibt es für erwachsene Personen ohne EFZ oder EBA, trotzdem eine zu erlangen? Mehrere Antworten möglich.\n 4 Antwortmöglichkeiten:\n- Normale berufliche Grundbildung\n- Eine aehnliche Ausbildung zu EFZ und EBA absolvieren und dann auch ein EFZ oder EBA zu bekommen\n- Verkuerzte Berufslehre\n- Bei der Seite berufsberatung.ch einen Antrag stellen, um ein EFZ oder ein EBA zu bekommen")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Normale berufliche Grundbildung" or "Verkuerzte Berufslehre":
        PunktzahlSchweizerBildung+=1
        
    print ("20. Welchen Weg gibt es ein Doktorat zu erlangen?\n 4 Antwortmöglichkeiten:\n- Ein Forschungsprojekt betreiben und dokumentieren\n- Das Doktorat erkaufen\n- Einen Abschluss bei allen drei Hochschultypen haben\n- Nach einem Master- oder Bachelorstudium eine zusätzliche Prüfung ablegen ")
    Eingabe = input ("Tippen Sie die Antwort 1:1 ein:")
    if Eingabe == "Ein Forschungsprojekt betreiben und dokumentieren":
        PunktzahlSchweizerBildung+=1
        
    PunktzahlGesamt += PunktzahlSchweizerBildung    
        
    Themenbereiche.remove ("SchweizerBildung")
    
    if Themenbereiche == False:
        print ("Herzlichen Glückwunsch, Sie sind am Ende des Quizes angelangt, Sie können stolz sein darauf!\n Sie haben drei Möglichkeiten:\n Gesamter Punktestand ausgeben lassen\n Gesamter Punktestand grafisch ausgeben lassen\n Programmbeenden")
        Eingabe = input("Wählen Sie eine Möglichkeit aus und tippen Sie diese 1:1 ein")
        if Eingabe == "Gesamter Punktestand ausgeben lassen":
            print (str(PunktzahlGesamt) + "100")
        elif Eingabe == "Programmbeenden":
            quit()
        
    print ("Wollen Sie sich den Punktestand dieses Quizes anzeigen lassen oder den gesamten Punktestand?\nSie haben drei Möglichkeiten:\nGesamter Punktestand\nPunktestand Schulwissen\nNichts anzeigen")
    PunktestandJaNein = input("Wählen Sie aus einer der Optionen aus. Option bitte 1:1 abtippen")
    if PunktestandJaNein == "Gesamter Punktestand":
        print(str(PunktzahlGesamt) + "/100")
    elif PunktestandJaNein == "Punktestand Schulwissen":
        print (str(PunktzahlSchulwissen) + "/20")
    elif PunktestandJaNein == "Nichts anzeigen":
        quit()
    
    print ("Mit welchem Themenbereich möchten Sie fortfahren?\n Diese Themenbereiche stehen Ihnen noch zur Verfügung:")
    print (Themenbereiche)
        
        
    Eingabe == input ("Wählen Sie einen Themenbereich aus und tippen Sie diesen 1:1 ein oder beenden Sie das Programm mit dem Befehl Programmbeenden")
    if Eingabe in Themenbereiche and Eingabe == "Fussball":
        Fussball()
    elif Eingabe in Themenbereiche and Eingabe == "Politik":
        Politik()
    elif Eingabe in Themenbereiche and Eingabe == "RechtundGesetz":
        RechtundGesetz()
    elif Eingabe in Themenbereiche and Eingabe == "Schulwissen":
        Schulwissen()
    elif Eingabe == "Programmbeenden":
        quit()
    

print ("- Schulwissen\n- Fussball\n- Politik\n- Recht und Gesetz\n- Schweizer Bildung")
Themenbereich = input ("Wählen Sie aus einem Themenbereich aus, indem Sie diesen eintippen. Bitte eins zu eins, wie es steht")
if Themenbereich == "Schulwissen":
        Schulwissen()
elif Themenbereich == "Fussball":
        Fussball()
elif Themenbereich == "Politik":
        Politik()
elif Themenbereich == "Recht und Gesetz":
        RechtundGesetz()
elif Themenbereich == "Schweizer Bildung":
        SchweizerBildung()