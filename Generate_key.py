import pickle
from pathlib import Path
import streamlit_authenticator as sauth
Name=["Earth Enable"]
Username=["david"]
Password=["123"]
hashed_pass= sauth.Hasher(Password).generate()
file_path=Path(__file__).parent /"hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_pass,file)