from PIL import Image

white_piece_names = ["B", "K", "N", "P", "Q", "R"]
black_piece_names = ["b", "k", "n", "p", "q", "r"]
for piece in white_piece_names:
    img = Image.open(f"./images/w{piece}.png")
    img = img.resize((90, 90))
    img.save(f"./images/w{piece}_new.png")
for piece in black_piece_names:
    img = Image.open(f"./images/b{piece.capitalize()}.png")
    img = img.resize((90, 90))
    img.save(f"./images/b{piece.capitalize()}_new.png")
