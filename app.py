import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Block Blast",
    page_icon="🧩",
    layout="centered",
    initial_sidebar_state="collapsed",
)

GAME_FILE = Path(__file__).parent / "game.html"

st.markdown(
    """
    <style>
    .block-container {max-width: 760px; padding-top: 1.2rem; padding-bottom: 1rem;}
    header[data-testid="stHeader"] {background: transparent;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧩 Block Blast")
st.caption("Chọn khối, đặt lên bảng, xóa hàng hoặc cột và cố gắng đạt điểm cao!")

if not GAME_FILE.exists():
    st.error("Không tìm thấy game.html. Hãy đặt app.py và game.html trong cùng một thư mục.")
else:
    html = GAME_FILE.read_text(encoding="utf-8")
    components.html(html, height=850, scrolling=True)

st.caption("Game chạy trong khung trình duyệt bên trên. Kỷ lục được lưu trong trình duyệt bạn đang chơi.")

