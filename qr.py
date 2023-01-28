import qrcode
from qrcode.image.styledpil import StyledPilImage

# from qrcode.image.styledpil import StyledPilImage


def save_qr(qr, source, colour="", with_image=True):
    kwargs = {
        "fill_color": "black",
        "back_color": "white",
    }
    if with_image:
        kwargs["embeded_image_path"] = f"site/fsob_logo{colour}.png"
    img = qr.make_image(image_factory=StyledPilImage, **kwargs)
    name = f"fsob_qr_{source}{colour}.png"
    img.save(f"site/{name}")
    return name


url_list = {
    "main": "https://futuresoundofbristol.com/",
    "cracked": "http://futuresoundofbristol.com/?utm_campaign=launch&utm_source=cracked&utm_medium=print",
    "b247": "http://futuresoundofbristol.com/?utm_campaign=launch&utm_source=b247&utm_medium=banner",
    "ooh": "http://futuresoundofbristol.com/?utm_campaign=launch&utm_source=ooh&utm_medium=print",
    "loud": "http://futuresoundofbristol.com/?utm_campaign=launch&utm_source=loud&utm_medium=print",
}

for source, url in url_list.items():
    qr = qrcode.QRCode(
        box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(url)

    save_qr(qr, source, colour="_colour", with_image=True)
    print(f"<h2>{source.title()}</h2>")
    print(f'<a href="{url}">', end="")
    print(f'<img src="{save_qr(qr, source)}" width="200"/>', end="")
    print("</a>")
    print(f'<a href="{url}">', end="")
    print(f'<img src="{save_qr(qr, source, colour="_colour")}" width="200"/>', end="")
    print("</a>")
    print(f'<a href="{url}">', end="")
    print(
        f'<img src="{save_qr(qr, source, colour="_colour_white")}" width="200"/>',
        end="",
    )
    print("</a>")
    print(f'<a href="{url}">', end="")
    print(
        f'<img src="{save_qr(qr, source, colour="_simple", with_image=False)}" width="200"/>',
        end="",
    )
    print("</a>")
