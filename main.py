import pytube as pt
import streamlit as st
from PIL import Image
import urllib.request
import platform
import os

def download(yt,n,streams):
    video=streams.get_by_itag(n)
    operatingSys=platform.system()
    if operatingSys=='Linux':
        path="/home/"+os.environ.get('USER')+"/Downloads"
    elif operatingSys=='Windows':
        path=os.path.expanduser('~')+"\\Downloads"
    location=video.download(path)
    st.text('Your video will be downloaded to the location : '+path)


def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Youtube video downloader</h1>", unsafe_allow_html=True)
    url=st.text_input('Enter the link')

    if url=='':
        st.empty()
    elif url!='':
        yt=pt.YouTube(url=url)
        st.title(yt.title.split('|')[0])
        st.image(yt.thumbnail_url)
        streams=yt.streams.filter(file_extension='mp4',progressive=True)
        st.header('Select resolution')
        map={}
        for stream in streams:
            map[stream.resolution]=[stream.itag,stream.resolution,stream.mime_type]
        iter=map.__iter__()
        res=st.selectbox("",iter)
        if res!='':  
            dow=st.button('Download',on_click=download(yt,map[res][0],streams))  

if __name__=='__main__':
    main()