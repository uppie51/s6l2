import numpy as np 
mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
print("1.Abbiamo la lista di liste.")
print("Che tipo di struttura dati o matematica potrebbe rappresentare?") 
print("una matrice in forma di lista di liste.")
print("Come facciamo per accedere ad un elemento in particolare?") 
indice_riga = 1 
indice_colonna = 2 
elemento = mat[indice_riga][indice_colonna]
print(f"Elemento nella riga {indice_riga} e colonna {indice_colonna} e: {elemento}") 
print("2.Trasformiamo la lista dell'esercizio precedente in un array NumPy.")
print("Come facciamo per accedere ai singoli elementi?") 
mat_np = np.array(mat)
print(mat_np)
elemento2 = mat_np[0, 4]
print(f"L elemento nella prima riga e quinta colonna e: {elemento2}") 
print("3.Abbiamo il seguente array NumPy.Lo ridimensioniamo mediante il metodo .reshape():") 
print("Quante dimensioni ha il nuovo array?Come facciamo per accedere ai singoli elementi?")  
linear_data = np.array([x for x in range(27)]) 
print(linear_data)
reshaped_data = linear_data.reshape((3, 3, 3)) 
x = len(reshaped_data) 
print(x)
print(reshaped_data) 
print("adesso reshaped_data ha tre dimensioni.")
elemento = reshaped_data[1, 2, 0]
print(elemento) 
print(f"L elemento nella seconda dimensione, terza riga, prima colonna e: {elemento}") 
print("4.In una catena di montaggio abbiamo una struttura metallica di 28.75 cm di lunghezza;")
print("per assicurarne la stabilita, e necessario inserire 15 rivetti, dei quali uno all inizio e uno alla fine, ") 
print("e tutti quanti separati dalla stessa distanza; come possiamo calcolare i punti esatti in cui inserire i rivetti tramite NumPy?") 
lunghezza = 28.75 
rivetti = 15 
spazio = lunghezza/(rivetti-1) 
print(spazio)
posizione = np.round(np.arange(0,lunghezza,spazio),2) 
print("Posizione dei rivetti:") 
print(posizione) 
print("5.Abbiamo la seguente matrice. Creiamo un ndarray con gli stessi valori.")
print("Ci sono due modalita: inizializzare un array e poi inserire i valori nelle posizioni adatte, oppure creare una lista di liste e poi effettuare un casting.")
mat = [[1, 1, 1, 1], [5, 1, 1, 1], [20, -4, 0, 42]]
print(mat)
np_array = np.array(mat) 
print(np_array) 
print("6.Creiamo il seguente ndarray.")
print("Per ogni valore, sottraiamo il minimo (2) e poi dividiamo il risultato per il massimo (42) meno il minimo.") 
ndarray = np.array([[10, 22, 21, 8, 9], [9, 42, 3, 18, 11], [5, 4, 30, 12, 29], [37, 31, 7, 2, 26], [8, 6, 4, 33, 15]]) 
print(ndarray) 
minimo = np.min(ndarray) 
massimo = np.max(ndarray)
ndarray_nuovo = (ndarray - minimo)/(massimo - minimo)
print(ndarray_nuovo)

