import streamlit as st


def apply_dashboard_theme() -> None:
    """Apply the dark blue dashboard styling."""

    st.markdown(
        """
        <style>

        :root {
            --blue: #2196f3;
            --blue-bright: #38bdf8;
            --blue-dark: #1565c0;

            --surface: #111a27;
            --surface-raised: #182334;
            --border: #26384f;
            --muted: #9aaabd;
        }

        /* =========================
           Main Application
           ========================= */

        .stApp {
            color: #f4f7fb;

            background:
                radial-gradient(
                    circle at 85% 0%,
                    rgba(33, 150, 243, 0.20),
                    transparent 32rem
                ),
                radial-gradient(
                    circle at 10% 100%,
                    rgba(21, 101, 192, 0.16),
                    transparent 28rem
                ),
                #080d14;
        }

        /* =========================
           Header
           ========================= */

        [data-testid="stHeader"] {
            background: transparent;
        }

        /* =========================
           Sidebar
           ========================= */

        [data-testid="stSidebar"] {
            background: linear-gradient(
                180deg,
                #0d1622 0%,
                #09111b 100%
            );

            border-right: 1px solid var(--border);
        }

        [data-testid="stSidebar"]
        [data-testid="stMarkdownContainer"] p,

        [data-testid="stSidebar"] label {
            color: #c9d5e3;
        }

        /* =========================
           Main Container
           ========================= */

        .block-container {
            max-width: 1180px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }

        /* =========================
           Hero Section
           ========================= */

        .rag-hero {
            position: relative;
            overflow: hidden;

            margin-bottom: 1.5rem;
            padding: 1.7rem 2rem;

            border: 1px solid #21466f;
            border-radius: 18px;

            background: linear-gradient(
                115deg,
                rgba(17, 39, 67, 0.96),
                rgba(12, 20, 32, 0.96)
            );

            box-shadow:
                0 18px 50px rgba(0, 0, 0, 0.30);
        }

        .rag-hero::after {
            content: "";

            position: absolute;

            width: 280px;
            height: 280px;

            right: -80px;
            top: -150px;

            border-radius: 50%;

            background: rgba(33, 150, 243, 0.20);

            filter: blur(20px);
        }

        .rag-eyebrow {
            margin-bottom: 0.45rem;

            color: var(--blue-bright);

            font-size: 0.76rem;
            font-weight: 800;

            letter-spacing: 0.16em;
            text-transform: uppercase;
        }

        .rag-title {
            margin: 0;

            color: #ffffff;

            font-size: clamp(
                2rem,
                4vw,
                3.25rem
            );

            font-weight: 850;

            letter-spacing: -0.045em;
            line-height: 1;
        }

        .rag-title span {
            color: var(--blue-bright);
        }

        .rag-subtitle {
            max-width: 690px;

            margin: 0.85rem 0 0;

            color: var(--muted);

            font-size: 1rem;
        }

        /* =========================
           File Uploader
           ========================= */

        [data-testid="stFileUploaderDropzone"] {
            border: 1px solid var(--border);
            border-radius: 14px;

            background: rgba(
                17,
                27,
                42,
                0.90
            );
        }

        [data-testid="stFileUploaderDropzone"] button {
            border-color: #246ca8;

            background: #122c47;

            color: #dff2ff;
        }

        /* =========================
           Chat Messages
           ========================= */

        [data-testid="stChatMessage"] {
            margin-bottom: 0.7rem;
            padding: 0.35rem 0.45rem;

            border: 1px solid var(--border);
            border-radius: 14px;

            background: rgba(
                17,
                27,
                42,
                0.90
            );
        }

        [data-testid="stChatMessage"]:has(
            [data-testid="chatAvatarIcon-assistant"]
        ) {
            border-left: 3px solid var(--blue);
        }

        /* =========================
           Alerts
           ========================= */

        div[data-testid="stAlert"] {
            border: 1px solid var(--border);
            border-radius: 14px;

            background: rgba(
                17,
                27,
                42,
                0.90
            );
        }

        /* =========================
           Primary Button
           ========================= */

        .stButton > button[kind="primary"] {
            border: 1px solid #38a9ff;

            background: linear-gradient(
                135deg,
                #2196f3,
                #1565c0
            );

            color: #ffffff;

            font-weight: 750;

            box-shadow:
                0 8px 24px
                rgba(33, 150, 243, 0.24);
        }

        .stButton > button[kind="primary"]:hover {
            border-color: #67c7ff;

            background: linear-gradient(
                135deg,
                #2aa4ff,
                #1976d2
            );
        }

        /* =========================
           Secondary Button
           ========================= */

        .stButton > button[kind="secondary"] {
            border-color: var(--border);

            background: var(--surface-raised);

            color: #dbe5f0;
        }

        /* =========================
           Chat Input
           ========================= */

        [data-testid="stChatInput"] {
            border: 1px solid #315579;

            border-radius: 14px;

            background: #111b2a;

            box-shadow:
                0 10px 35px
                rgba(0, 0, 0, 0.25);
        }

        [data-testid="stChatInput"]:focus-within {
            border-color: var(--blue);

            box-shadow:
                0 0 0 2px
                rgba(33, 150, 243, 0.14);
        }

        /* =========================
           Typography
           ========================= */

        h1,
        h2,
        h3 {
            letter-spacing: -0.025em;
        }

        a {
            color: var(--blue-bright) !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )