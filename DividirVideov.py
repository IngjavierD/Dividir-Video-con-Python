import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

class VideoFragmenterApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Fragmenter App")

        self.label = tk.Label(master, text="Seleccionar video:")
        self.label.pack()

        self.button = tk.Button(master, text="Seleccionar", command=self.select_file)
        self.button.pack()

        self.duration_label = tk.Label(master, text="Duración de fragmento (segundos):")
        self.duration_label.pack()

        self.duration_entry = tk.Entry(master)
        self.duration_entry.pack()

        self.fragment_button = tk.Button(master, text="Fragmentar Video", command=self.fragment_video)
        self.fragment_button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        self.input_video = file_path

    def fragment_video(self):
        duration = float(self.duration_entry.get())
        output_directory = os.path.dirname(self.input_video)

        video_fragmenter = VideoFragmenter()
        video_fragmenter.fragmentar_video(self.input_video, duration, output_directory)

class VideoFragmenter:
    @staticmethod
    def fragmentar_video(input_video, duracion_fragmento, output_directory):
        video = VideoFileClip(input_video)
        duracion_total = video.duration

        # Calcular el número de fragmentos
        num_fragmentos = int(duracion_total / duracion_fragmento) + 1

        for i in range(num_fragmentos):
            inicio = i * duracion_fragmento
            fin = min((i + 1) * duracion_fragmento, duracion_total)
            fragmento = video.subclip(inicio, fin)
            nombre_video = os.path.splitext(os.path.basename(input_video))[0]
            nombre_fragmento = f"{nombre_video}_{i + 1}.mp4"
            fragmento.write_videofile(os.path.join(output_directory, nombre_fragmento))

        video.close()

# Ejecutar la aplicación
root = tk.Tk()
app = VideoFragmenterApp(root)
root.mainloop()