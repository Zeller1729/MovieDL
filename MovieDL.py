from yt_dlp import YoutubeDL
import PySimpleGUI as sg

def video_DL(url,vname): 
    yt_opts=YoutubeDL({
        'format':'best',
        'outtmpl':vname
        })
    yt_opts .download([url])
        
if __name__=='__main__':   
    layout = [
            [sg.Text('動画のURL   '), sg.Input()],
            [sg.Text('保存する名前'), sg.Input()],
            [sg.Button('決定'), sg.Button('終了')]]

    window = sg.Window('動画ダウンローダー', layout)

    event, values = window.read()
    vname=values[1]+'.mp4'    
    window.close()
    
    if event == '決定':
        video_DL(values[0],vname)
        sg.PopupTimed('ダウンロードが終了しました。',title='ダウンロード完了')
    