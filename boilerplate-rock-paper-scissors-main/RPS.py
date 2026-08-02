def player(prev_play, opponent_history=[], play_order={}):
    # Eğer ilk oyunsa, prev_play boş dönecektir. Bunu 'R' olarak varsayalım.
    if not prev_play:
        prev_play = 'R'
    
    # Rakibin hamlesini geçmişe ekliyoruz
    opponent_history.append(prev_play)

    # N-Gram derinliği: Son 5 hamlelik dizileri takip edeceğiz
    n = 5

    # Geçmiş yeterince dolduğunda örüntüleri (frekansları) kaydetmeye başla
    if len(opponent_history) >= n:
        last_n_moves = "".join(opponent_history[-n:])
        # Bu 5'li dizilimin kaç kez tekrar ettiğini sayıyoruz
        play_order[last_n_moves] = play_order.get(last_n_moves, 0) + 1

    prediction = 'S' # Yeterli veri yoksa varsayılan tahminimiz

    # Son 4 hamleyi alarak, 5. hamlenin ne olabileceğini tahmin et
    if len(opponent_history) >= (n - 1):
        last_m_moves = "".join(opponent_history[-(n - 1):])
        
        # Son 4 hamlenin sonuna R, P veya S geldiği ihtimalleri oluştur
        potential_plays = [
            last_m_moves + "R",
            last_m_moves + "P",
            last_m_moves + "S",
        ]

        # Bu ihtimallerden sözlüğümüzde kayıtlı olanları (daha önce oynanmışları) bul
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # Eğer daha önce oynanmış bir örüntü bulduysak, en çok oynananı tahmin olarak seç
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1]

    # Rakibin tahmin edilen hamlesini (prediction) yenecek olan ideal hamleyi dön
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]