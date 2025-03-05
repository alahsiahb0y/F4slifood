import streamlit as st
import time
import random
import base64


# Konfigurasi Halaman
st.set_page_config(page_title="F4SLI FOOD", page_icon="🍞", layout="wide")

def random_color():
    return f"rgba({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}, 1)"  # 0.5 untuk opacity
# Warna acak untuk background
background_color = random_color()

# CSS untuk lapisan background
st.markdown(
    f"""
    <style>
    .background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255, 255, 255, 0.8); /*ALTERNATIVE = rgba(255, 228, 125, 0.8) */
        z-index: 0; /* Letakkan di belakang konten lainnya */
    }}
    </style>
    <div class="background"></div>
    """,
    unsafe_allow_html=True
)

# Gaya CSS untuk background dan transparansi elemen
def set_background():
    page_bg = f'''
    <style>
        .stApp {{
            background: url('https://1.bp.blogspot.com/-fcJsCuIqaKk/TqEE2-3Mb8I/AAAAAAAAACA/Vbf7LXWMawo/s1600/IMG_1851.JPG') no-repeat center center fixed;
            background-size: cover;
        }}

        .container {{
            position: relative;
            z-index: 0;
            text-align: center;
        }}
    </style>
    <div class="overlay"></div>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)

set_background()

if "page" not in st.session_state:
    st.session_state.page = "tampilan_awal"

def navigate_to(page):
    st.session_state.page = page

def home():
    # Header Logo
    st.markdown(
        """
        <style>
                                        /*Button sebelum hover*/
        .stButton > button {
            background-color: #cc660099 !important; /* Warna latar belakang default */
            color: #ffffff !important;             /* Warna teks default */
            font-weight: bold ;
            font-size: 10px ;
            cursor: pointer;
            height: 60px ;
            padding: 20px ;
            transition: background-color 0.2s, color 0.2s; /* Efek transisi */
        }

                                     /* Gaya tombol saat hover */
        .stButton > button:hover {
            background-color: transparent !important;  /* Warna latar belakang saat hover */
            color: #cc660099 !important;          /* Warna teks saat hover */
            border: 3px solid #cc660099 !important;
            height: 60px !important;
            }
        
        .stImage img {
            width: 500px !important;
            display: block;
            margin: auto;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("LOGO66.png")
        st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("🍞 Deskripsi Menu 🍞", use_container_width=True):
        navigate_to("descr")
    if st.button("💰 Pesan Menu 💰", use_container_width=True):
        navigate_to("order")

if st.session_state.page == 'tampilan_awal':
    home()

elif st.session_state.page == 'descr':


    st.markdown(
        """
        <style>
                                        /*Button sebelum hover*/
        .stButton > button {
            background-color: #cc660099 ; /* Warna latar belakang default */
            color: #ffffff ;             /* Warna teks default */
            font-weight: bold !important;
            font-size: 100px !important;
            cursor: pointer;
            height: 60px !important;
            padding: 20px !important;
            transition: background-color 0.2s, color 0.2s; /* Efek transisi */
        }

                                     /* Gaya tombol saat hover */
        .stButton > button:hover {
            background-color: transparent !important;  /* Warna latar belakang saat hover */
            color: #cc660099 !important;          /* Warna teks saat hover */
            border: 3px solid #cc660099 !important;
            height: 60px !important;
            }
        </style>
        """,
        unsafe_allow_html=True)
    
    # Fungsi untuk mengonversi gambar ke base64
    def encode_image(image_path):
        try:
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")
        except FileNotFoundError:
            return ""  # Mengembalikan string kosong jika gambar tidak ditemukan

    # Daftar item (nama, gambar)
    items = [
        {"name": "Roti Phobia", "image": "LOGO66.png"},
        {"name": "Roti Cinnamon", "image": "LOGO66.png"},
        {"name": "Roti Pizza", "image": "LOGO66.png"},
        {"name": "Roti Sosis", "image": "LOGO66.png"},
        {"name": "Roti Garlic", "image": "LOGO66.png"},
        {"name": "Roti Coklat Almond", "image": "LOGO66.png"},
        {"name": "Kue Nies Bro", "image": "LOGO66.png"}
    ]
    # Header halaman
    st.markdown(
        "<div style='text-align: center; color: #cc6600; font-size: 50px; font-weight: bold;'>Halaman Deskripsi Menu<br><br></div>",
        unsafe_allow_html=True
    )

    cols = st.columns(3)  # Membuat 3 kolom

    for index, item in enumerate(items):
        col = cols[index % 3]  # Menentukan kolom berdasarkan index
        with col:
            if st.button(f"Lihat {item['name']}", key=f"{item['name']}_{index}", use_container_width=True):
                st.session_state.selected_item = item["name"]
                navigate_to("detail")
            item["image_base64"] = encode_image(item["image"])
    # Menampilkan item dalam 3 kolom
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    # cols = st.columns(3)
    # for i, item in enumerate(items):
    #     with cols[i % 3]:  # Memastikan elemen ditampilkan dalam kolom yang sesuai
    #         st.markdown(
    #             f"""
    #             <div style="background-color:#CC6009; padding:15px; border-radius:10px; text-align:center;">
    #                 <img src="data:image/png;base64,{item['image_base64']}" width="100%" style="border-radius:10px;">
    #                 <p style="color:white; font-size:20px; margin:5px 0;">{item['name']}</p>
    #             </div>
    #             """,
    #             unsafe_allow_html=True
    #         )
    #         if st.button(f"Lihat {item['name']}", key=item["name"], use_container_width=True):
    #             navigate_to("detail")
    if st.button("🏠 Kembali Ke Halaman Utama 🏠", use_container_width=True):
            navigate_to("tampilan_awal")













elif st.session_state.page == 'order':
    st.markdown("<h1 style='text-align: center; color: #cc6600;'>Pesan Menu Andalan Kamu !!!</h1>", unsafe_allow_html=True)
    st.markdown("""
    <style>
        .stButton > button {
            background-color: #cc660099 ; /* Warna latar belakang default */
            color: #ffffff ;             /* Warna teks default */
            font-weight: bold !important;
            font-size: 100px !important;
            cursor: pointer;
            height: 60px !important;
            padding: 20px !important;
            transition: background-color 0.2s, color 0.2s; /* Efek transisi */
        }

                                    /* Gaya tombol saat hover */
        .stButton > button:hover {
            background-color: transparent !important;  /* Warna latar belakang saat hover */
            color: #cc660099 !important;          /* Warna teks saat hover */
            border: 3px solid #cc660099 !important;
            height: 60px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    if 'cart' not in st.session_state:
        st.session_state.cart = {}
    if 'show_qris' not in st.session_state:
        st.session_state.show_qris = False

    # Fungsi untuk mengonversi gambar ke base64
    def encode_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    # Daftar item (nama, harga, gambar)
    items = [
        {"name": "Roti Phobia", "price": 5000, "image": "LOGO66.png"},
        {"name": "Roti Cinnamon", "price": 7000, "image": "LOGO66.png"},
        {"name": "Roti Garlic", "price": 6000, "image": "LOGO66.png"},
        {"name": "Roti Sosis", "price": 8000, "image": "LOGO66.png"},
        {"name": "Roti Pisang", "price": 7500, "image": "LOGO66.png"},
        {"name": "Brownies Milo", "price": 90000, "image": "LOGO66.png"}
    ]

    # Mengonversi gambar ke base64
    for item in items:
        item["image_base64"] = encode_image(item["image"])

    def tambah_item(item_name, price):
        if item_name in st.session_state.cart:
            st.session_state.cart[item_name]['count'] += 1
        else:
            st.session_state.cart[item_name] = {'count': 1, 'price': price}

    def lanjutkan_pembayaran():
        st.session_state.show_qris = True

    def kembali_ke_home():
        st.session_state.page = "home"
        st.session_state.show_qris = False
        st.session_state.cart = {}

    # Tombol Home
    if st.button("Home", use_container_width=True):
        kembali_ke_home()

    # Menampilkan item dalam 3 kolom
    cols = st.columns(3)
    for i, item in enumerate(items):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div style="background-color:#CC6009; padding:15px; border-radius:10px; text-align:center;">
                    <img src="data:image/jpg;base64,{item['image_base64']}" width="100px" style="border-radius:10px;">
                    <p style="color:white; font-size:20px; margin:5px 0;">{item['name']}</p>
                    <p style="color:white; font-size:18px; margin:0;">Rp {item['price']},-</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"+ ADD {item['name']}", use_container_width=True):
                tambah_item(item['name'], item['price'])

    # Menampilkan total harga jika ada item yang ditambahkan
    total_harga = sum(v['count'] * v['price'] for v in st.session_state.cart.values())
    if total_harga > 0:
        with st.container():
            st.markdown(
                f"""
                <div style="background-color:#cc6600; padding:15px; border-radius:10px; text-align:center; margin-top:10px;">
                    <p style="color:white; font-size:18px; margin:0;">Total: Rp {total_harga},-</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("Lanjutkan Ke Pembayaran", use_container_width=True):
                lanjutkan_pembayaran()

    # Menampilkan halaman QRIS jika tombol ditekan
    if st.session_state.show_qris:
        st.image("LOGO66.png", use_container_width=True)

    if st.button("Kembali Ke Halaman Utama", use_container_width=True):
        navigate_to("tampilan_awal")











if st.session_state.page == "detail":
    if st.session_state.selected_item:
        st.markdown(
            """
            <style>
                                            /*Button sebelum hover*/
            .stButton > button {
                background-color: #cc660099 !important; /* Warna latar belakang default */
                color: #ffffff !important;             /* Warna teks default */
                font-weight: bold ;
                font-size: 10px ;
                cursor: pointer;
                height: 60px ;
                padding: 20px ;
                transition: background-color 0.2s, color 0.2s; /* Efek transisi */
            }

                                        /* Gaya tombol saat hover */
            .stButton > button:hover {
                background-color: transparent !important;  /* Warna latar belakang saat hover */
                color: #cc660099 !important;          /* Warna teks saat hover */
                border: 3px solid #cc660099 !important;
                height: 60px !important;
                }
            </style>
            """, unsafe_allow_html=True
        )    
        st.markdown(f"""
        <h1 style='text-align: center; color: #cc6600;'>
            Deskripsi {st.session_state.selected_item} 
        </h1>
        """, unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🥖 Lihat Menu Yang Lain 🥖", use_container_width=True):
        navigate_to("descr")

    if st.button("🏠 Kembali Ke Halaman Utama 🏠", use_container_width=True):
        navigate_to("tampilan_awal")




# # Inisialisasi session state jika belum ada
# if "page" not in st.session_state:
#     st.session_state.page = "home"

# def navigate_to(page):
#     st.session_state.page = page
#     st.rerun()
   

#     # Menampilkan logo di tengah
#     # st.markdown('<div class="image-container">', unsafe_allow_html=True)
#     col1, col2, col3 = st.columns(3)
#     with col2:
#         st.image("LOGO66.png", use_container_width=True)
#     st.markdown("<br>", unsafe_allow_html=True)

#     # Pilihan Menu
#     st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    
#     if st.button("Lihat Deskripsi Menu", key="desc_menu", use_container_width=True):
#         navigate_to("deskripsi")
        
#     elif st.button("Pesan Menu", key="order_menu", use_container_width=True):
#         st.session_state.page = "pesan"
#         st.rerun()  # **Rerun untuk menerapkan perubahan langsung**
    
#     st.markdown("</div>", unsafe_allow_html=True)

# if st.session_state.page == "home":
#     home()

# elif st.session_state.page == "deskripsi":



















# elif st.session_state.page == "pesan":
