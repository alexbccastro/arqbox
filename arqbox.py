# Bibliotecas importadas
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk


# Janela Taxa de Ocupação
def taxa_ocupacao_window():
    # Cria a janela "Taxa de Ocupação"
    to_window = tk.Toplevel(root)
    to_window.title('ARQBOX - Taxa de Ocupação')
    to_window.geometry('+500+500')
    to_window.iconbitmap('arqbox_icon_545454_48px.ico')
    to_window.resizable(width=False, height=False)
    to_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    to_blank = Label(to_window, bg=main_bg)
    to_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a área da projeção da edificação
    lbl_area_edif = Label(to_window, text='Área da Projeção da Edificação (m²):', font=std_font, fg=main_txt, width=30)
    lbl_area_edif.grid(row=1, column=0, padx=15)
    lbl_area_edif['background'] = main_bg
    entry_area_edif = Entry(to_window, font=std_font, borderwidth=0, fg=main_txt, bg=entry_bg, width=30)
    entry_area_edif.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir a área da área do terreno
    lbl_area_terr = Label(to_window, text='Área do Terreno (m²):', font=std_font, fg=main_txt, width=30)
    lbl_area_terr.grid(row=2, column=0, padx=15, pady=5)
    lbl_area_terr['background'] = main_bg
    entry_area_terr = Entry(to_window, font=std_font, fg=main_txt, borderwidth=0, bg=entry_bg, width=30)
    entry_area_terr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados e resolução dos cálculos
    lbl_result = Label(to_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(to_window, font=std_font, fg=main_txt)

    # Cria a função que calcula a taxa de ocupação
    def calcular_taxa_ocupacao():
        to = (float(entry_area_edif.get()) / float(entry_area_terr.get())) * 100
        msg_result = f'Taxa de Ocupação: {to:.2f}%'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nTaxa de Ocupação = (Área da Projeção da Edificação/Área do ' \
                      f'Terreno)*100\nTaxa de Ocupação = ({entry_area_edif.get()}/{entry_area_terr.get()})*100'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(to_window, text='Calcular', font=std_font, fg=main_txt, activebackground=active_bg,
                      activeforeground=active_fg, borderwidth=0,
                      command=calcular_taxa_ocupacao, width=15)
    btn_calc.grid(row=3, column=0, padx=5, pady=15)
    btn_calc['background'] = '#EB4B98'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_area_edif.delete(0, 'end')
        entry_area_terr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(to_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, width=15, borderwidth=0, command=clean)
    btn_clean.grid(row=3, column=1, padx=5, pady=20)
    btn_clean['background'] = '#EB4B98'

    # Loop da janela
    to_window.mainloop()


# Janela Coeficiente de Aproveitamento
def coef_apr_window():
    # Cria a janela "Coeficiente de Aproveitamento"
    ca_window = tk.Toplevel(root)
    ca_window.title('ARQBOX - Coeficiente de Aproveitamento')
    ca_window.geometry('+500+500')
    ca_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ca_window.resizable(width=False, height=False)
    ca_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ca_blank = Label(ca_window, bg=main_bg)
    ca_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a área de todos os pavimentos
    lbl_area_pav = Label(ca_window, text='Área de Todos os Pavimentos (m²):', font=std_font, fg=main_txt, width=30)
    lbl_area_pav.grid(row=1, column=0, padx=15)
    lbl_area_pav['background'] = main_bg
    entry_area_pav = Entry(ca_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_area_pav.grid(row=1, column=1, padx=5)

    # Cria um label + entry para inserir a área da área do terreno
    lbl_area_terr = Label(ca_window, text='Área do Terreno (m²):', font=std_font, fg=main_txt, width=30)
    lbl_area_terr.grid(row=2, column=0, padx=15, pady=5)
    lbl_area_terr['background'] = main_bg
    entry_area_terr = Entry(ca_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_area_terr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados e resolução dos cálculos
    lbl_result = Label(ca_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ca_window, font=std_font, fg=main_txt)

    # Cria a função que calcula a coeficiente de aproveitamento
    def calcular_coef_apr():
        to = float(entry_area_pav.get()) / float(entry_area_terr.get())
        msg_result = f'Coeficiente de Aproveitamento: {to:.2f}'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nCoeficiente de Aproveitamento = Área dos Pavimentos/Área do Terreno' \
                      f'\nCoeficiente de Aproveitamento = {entry_area_pav.get()}/{entry_area_terr.get()}'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ca_window, text='Calcular', font=std_font, fg=main_txt, borderwidth=0, activeforeground=active_fg,
                      activebackground=active_bg, command=calcular_coef_apr, width=15)
    btn_calc.grid(row=3, column=0, padx=5, pady=15)
    btn_calc['background'] = '#9D52AA'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_area_pav.delete(0, 'end')
        entry_area_terr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ca_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=5, pady=20)
    btn_clean['background'] = '#9D52AA'

    # Loop da janela
    ca_window.mainloop()


# Janela Taxa de Permeabilidade
def taxa_perm_window():
    # Cria a janela "Taxa de Ocupação"
    tp_window = tk.Toplevel(root)
    tp_window.title('ARQBOX - Taxa de Permeabilidade')
    tp_window.geometry('+500+500')
    tp_window.iconbitmap('arqbox_icon_545454_48px.ico')
    tp_window.resizable(width=False, height=False)
    tp_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    tp_blank = Label(tp_window, bg=main_bg)
    tp_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a área permeável
    lbl_area_perm = Label(tp_window, text='Área Permeável (m²):', font=std_font, fg=main_txt, width=30)
    lbl_area_perm.grid(row=1, column=0, padx=15)
    lbl_area_perm['background'] = main_bg
    entry_area_perm = Entry(tp_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_area_perm.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir a área da área do terreno
    lbl_area_terr = Label(tp_window, text='Área do Terreno (m²):', font=std_font, fg=main_txt, width=30)
    lbl_area_terr.grid(row=2, column=0, padx=15, pady=5)
    lbl_area_terr['background'] = main_bg
    entry_area_terr = Entry(tp_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_area_terr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados e resolução dos cálculos
    lbl_result = Label(tp_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(tp_window, font=std_font, fg=main_txt)

    # Cria a função que calcula a taxa de permeabilidade
    def calcular_taxa_permeabilidade():
        tp = (float(entry_area_perm.get()) / float(entry_area_terr.get())) * 100
        msg_result = f'Taxa de Permeabilidade: {tp:.2f}%'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nTaxa de Permeabilidade = (Área Permeável/Área do Terreno)x100' \
                      f'\nTaxa de Permeabilidade = ({entry_area_perm.get()}/{entry_area_terr.get()})x100'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(tp_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_taxa_permeabilidade, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=15)
    btn_calc['background'] = '#5158BB'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_area_perm.delete(0, 'end')
        entry_area_terr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(tp_window, text='Limpar', font=std_font, fg=main_txt, borderwidth=0, width=15,
                       activebackground=active_bg, activeforeground=active_fg, command=clean)
    btn_clean.grid(row=3, column=1, padx=15, pady=20)
    btn_clean['background'] = '#5158BB'

    # Loop da janela
    tp_window.mainloop()


# Janela Rampa (Comprimento)
def rampa_compr():
    # Cria a janela "Rampa (Comprimento)"
    rc_window = tk.Toplevel(root)
    rc_window.title('ARQBOX - Rampa (Comprimento)')
    rc_window.geometry('+500+500')
    rc_window.iconbitmap('arqbox_icon_545454_48px.ico')
    rc_window.resizable(width=False, height=False)
    rc_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    rc_blank = Label(rc_window, bg=main_bg)
    rc_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a altura da rampa
    lbl_rampa_altura = Label(rc_window, text='Altura da Rampa (m):', font=std_font, fg=main_txt, width=30)
    lbl_rampa_altura.grid(row=1, column=0, padx=15)
    lbl_rampa_altura['background'] = main_bg
    entry_rampa_altura = Entry(rc_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_rampa_altura.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir a inclinação da rampa
    lbl_rampa_incl = Label(rc_window, text='Inclinação da Rampa (%):', font=std_font, fg=main_txt, width=30)
    lbl_rampa_incl.grid(row=2, column=0, padx=15, pady=5)
    lbl_rampa_incl['background'] = main_bg
    entry_rampa_incl = Entry(rc_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_rampa_incl.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados, resolução dos cálculos e alertas
    lbl_result = Label(rc_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(rc_window, font=std_font, fg=main_txt)
    lbl_alert = Label(rc_window, font=std_font, fg='red')
    lbl_compr = Label(rc_window, font=std_font, fg='red')

    # Cria a função que calcula o comprimento da rampa
    def calcular_compr_rampa():
        rc = (100*float(entry_rampa_altura.get())) / float(entry_rampa_incl.get())
        msg_result = f'Comprimento da Rampa: {rc:.2f} m'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nComprimento de Rampa = (100xAltura da Rampa)/Inclinação da Rampa' \
                      f'\nComprimento de Rampa = (100x{entry_rampa_altura.get()})/{entry_rampa_incl.get()}'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

        # Cria uma mensagem de alerta caso a inclinação seja maior que 8.33%
        if float(entry_rampa_incl.get()) > 8.33:
            msg_alert = '[AVISO]: O valor de inclinação de rampa fornecido é superior ao estipulado\npela NBR 9050.' \
                        'Se você estiver calculando um comprimento de rampa\na ser projetada, ' \
                        'recomenda-se usar uma inclinação inferior a 8.33%.'
            lbl_alert.config(text=msg_alert)
            lbl_alert.grid(row=6, column=0, padx=5, pady=15, columnspan=2)
            lbl_alert['background'] = main_bg

        # Cria uma mensagem de alerta caso o comprimento de rampa seja maior que 50 metros
        if rc > 50:
            msg_compr = '[AVISO]: O comprimento de rampa calculado possui mais de 50 metros. Pela norma\nNBR 9050 ' \
                        ', a rampa deve ter um patamar, de 1.20m de largura, a cada\n50m de comprimento ' \
                        'de rampa.'
            lbl_compr.config(text=msg_compr)
            lbl_compr.grid(row=7, column=0, padx=15, pady=15, columnspan=2)
            lbl_compr['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(rc_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_compr_rampa, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=20)
    btn_calc['background'] = '#EB4B98'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_rampa_altura.delete(0, 'end')
        entry_rampa_incl.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()
        lbl_alert.config(text='')
        lbl_alert.grid_forget()
        lbl_compr.config(text='')
        lbl_compr.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(rc_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=5, pady=15)
    btn_clean['background'] = '#EB4B98'

    # Loop da janela
    rc_window.mainloop()


# Janela Rampa (Inclinação)
def rampa_incl():
    # Cria a janela "Rampa (Inclinação)"
    ri_window = tk.Toplevel(root)
    ri_window.title('ARQBOX - Rampa (Inclinação)')
    ri_window.geometry('+500+500')
    ri_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ri_window.resizable(width=False, height=False)
    ri_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ri_blank = Label(ri_window, bg=main_bg)
    ri_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a altura da rampa
    lbl_rampa_altura = Label(ri_window, text='Altura da Rampa (m):', font=std_font, fg=main_txt, width=30)
    lbl_rampa_altura.grid(row=1, column=0, padx=15)
    lbl_rampa_altura['background'] = main_bg
    entry_rampa_altura = Entry(ri_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_rampa_altura.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir o comprimento da rampa
    lbl_rampa_compr = Label(ri_window, text='Comprimento da Rampa (m):', font=std_font, fg=main_txt, width=30)
    lbl_rampa_compr.grid(row=2, column=0, padx=15, pady=5)
    lbl_rampa_compr['background'] = main_bg
    entry_rampa_compr = Entry(ri_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_rampa_compr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados, resolução dos cálculos e alerta
    lbl_result = Label(ri_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ri_window, font=std_font, fg=main_txt)
    lbl_alert = Label(ri_window, font=std_font, fg='red')

    # Cria a função que calcula a inclinação de rampa
    def calcular_incl_rampa():
        ri = (float(entry_rampa_altura.get()) / float(entry_rampa_compr.get())) * 100
        msg_result = f'Inclinação da Rampa: {ri:.2f} %'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nInclinação de Rampa = (Altura da Rampa / Comprimento da Rampa)x100' \
                      f'\nInclinação de Rampa = ({entry_rampa_altura.get()}/{entry_rampa_compr.get()})x100'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

        sugest_compr = (100 * float(entry_rampa_altura.get())) / 8.33
        sugest_alt = (8.33 * float(entry_rampa_compr.get())) / 100

        # Cria um alerta caso a inclinação da rampa seja maior que 8.33%
        if ri > 8.34:
            msg_alert = f'[AVISO]: A inclinação de rampa calculada é superior ao\nestipulado pela NBR 9050 ' \
                              f'Redomenda-se, portanto, os\ndevidos ajustes de dimensões.\n\nCaso deseje manter a ' \
                              f'altura da rampa em {entry_rampa_altura.get()} m,\nrecomenda-se um comprimento de ' \
                              f'rampa de {sugest_compr:.2f} m.\n\nCaso deseje manter o comprimento de rampa de ' \
                              f'{entry_rampa_compr.get()} m,\nrecomenda-se uma altura de rampa de {sugest_alt:.2f} m.'
            lbl_alert.config(text=msg_alert)
            lbl_alert.grid(row=6, column=0, padx=15, pady=15, columnspan=2)
            lbl_alert['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ri_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_incl_rampa, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=5)
    btn_calc['background'] = '#9D52AA'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_rampa_altura.delete(0, 'end')
        entry_rampa_compr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()
        lbl_alert.config(text='')
        lbl_alert.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ri_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=15, pady=20)
    btn_clean['background'] = '#9D52AA'

    # Loop da janela
    ri_window.mainloop()


# Janela Rampa (Altura)
def rampa_alt():
    # Cria a janela "Rampa (Altura)"
    ra_window = tk.Toplevel(root)
    ra_window.title('ARQBOX - Rampa (Altura)')
    ra_window.geometry('+500+500')
    ra_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ra_window.resizable(width=False, height=False)
    ra_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ra_blank = Label(ra_window, bg=main_bg)
    ra_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a inclinação de rampa
    lbl_rampa_incl = Label(ra_window, text='Inclinação da Rampa (%):', font=std_font, fg=main_txt, width=30)
    lbl_rampa_incl.grid(row=1, column=0, padx=15)
    lbl_rampa_incl['background'] = main_bg
    entry_rampa_incl = Entry(ra_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_rampa_incl.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir o comprimento de rampa
    lbl_rampa_compr = Label(ra_window, text='Comprimento da Rampa (m):', font=std_font, fg=main_txt, width=30)
    lbl_rampa_compr.grid(row=2, column=0, padx=15, pady=5)
    lbl_rampa_compr['background'] = main_bg
    entry_rampa_compr = Entry(ra_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_rampa_compr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados, resolução dos cálculos e alerta
    lbl_result = Label(ra_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ra_window, font=std_font, fg=main_txt)
    lbl_alert = Label(ra_window, font=std_font, fg='red')

    # Cria a função que calcula a altura da rampa
    def calcular_altura_rampa():
        ra = (float(entry_rampa_incl.get()) * float(entry_rampa_compr.get())) / 100
        msg_result = f'Altura da Rampa: {ra:.2f} m'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nAltura da Rampa = (Inclinação da Rampa x Comprimento da Rampa) / 100' \
                      f'\nAltura da Rampa = ({entry_rampa_incl.get()}x{entry_rampa_compr.get()}) / 100)'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

        # Cria um alerta caso a inclinação de rampa seja maior que 8,33%
        if float(entry_rampa_incl.get()) > 8.33:
            msg_alert = '[AVISO]: O valor de inclinação de rampa fornecido é superior ao estipulado\npela NBR 9050.' \
                        'Portanto, se você estiver calculando um comprimento de\nrampa a ser projetada, ' \
                        'recomenda-se usar uma inclinação inferior a 8.33%.'
            lbl_alert.config(text=msg_alert)
            lbl_alert.grid(row=6, column=0, padx=5, pady=15, columnspan=2)
            lbl_alert['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ra_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_altura_rampa, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=5)
    btn_calc['background'] = '#5158BB'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_rampa_incl.delete(0, 'end')
        entry_rampa_compr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ra_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=15, pady=20)
    btn_clean['background'] = '#5158BB'

    # Loop da janela
    ra_window.mainloop()


# Janela Telhado (Inclinação)
def telha_incl():
    # Cria a janela "Telhado (Inclinação)"
    ti_window = tk.Toplevel(root)
    ti_window.title('ARQBOX - Telhado (Inclinação)')
    ti_window.geometry('+500+500')
    ti_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ti_window.resizable(width=False, height=False)
    ti_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ti_blank = Label(ti_window, bg=main_bg)
    ti_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a altura da cumeeira
    lbl_telha_alt = Label(ti_window, text='Altura da Cumeeira (m):', font=std_font, fg=main_txt, width=30)
    lbl_telha_alt.grid(row=1, column=0, padx=15)
    lbl_telha_alt['background'] = main_bg
    entry_telha_alt = Entry(ti_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_telha_alt.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir o comprimento de telhado
    lbl_telha_compr = Label(ti_window, text='Comprimento do Telhado (m):', font=std_font, fg=main_txt, width=30)
    lbl_telha_compr.grid(row=2, column=0, padx=15, pady=5)
    lbl_telha_compr['background'] = main_bg
    entry_telha_compr = Entry(ti_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_telha_compr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados e resolução dos cálculos
    lbl_result = Label(ti_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ti_window, font=std_font, fg=main_txt)

    # Cria a função que calcula a altura do telhado
    def calcular_altura_telha():
        ti = (float(entry_telha_alt.get()) / float(entry_telha_compr.get())) * 100
        msg_result = f'Inclinação do Telhado: {ti:.2f} %'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nInclinação do Telhado = (Altura da Cumeeira / Comprimento do ' \
                      f'Telhado)/100\nInclinação do Telhado = ({entry_telha_alt.get()}/{entry_telha_compr.get()}x100)'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ti_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_altura_telha, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=15)
    btn_calc['background'] = '#EB4B98'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_telha_alt.delete(0, 'end')
        entry_telha_compr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ti_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=15, pady=20)
    btn_clean['background'] = '#EB4B98'

    # Loop da janela
    ti_window.mainloop()


# Janela Telhado (Altura da Cumeeira)
def telha_alt():
    # Cria a janela "Telhado (Altura da Cumeeira)"
    ta_window = tk.Toplevel(root)
    ta_window.title('ARQBOX - Telhado (Altura da Cumeeira)')
    ta_window.geometry('+500+500')
    ta_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ta_window.resizable(width=False, height=False)
    ta_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ta_blank = Label(ta_window, bg=main_bg)
    ta_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a inclinação
    lbl_telha_incl = Label(ta_window, text='Inclinação do Telhado (%):', font=std_font, fg=main_txt, width=30)
    lbl_telha_incl.grid(row=1, column=0, padx=15)
    lbl_telha_incl['background'] = main_bg
    entry_telha_incl = Entry(ta_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_telha_incl.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir o comprimento do telhado
    lbl_telha_compr = Label(ta_window, text='Comprimento do Telhado (m):', font=std_font, fg=main_txt, width=30)
    lbl_telha_compr.grid(row=2, column=0, padx=15, pady=5)
    lbl_telha_compr['background'] = main_bg
    entry_telha_compr = Entry(ta_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_telha_compr.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados e resolução dos cálculos
    lbl_result = Label(ta_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ta_window, font=std_font, fg=main_txt)

    # Cria a função que calcula a coeficiente de aproveitamento
    def calcular_altura_telha():
        ta = (float(entry_telha_incl.get()) * float(entry_telha_compr.get())) / 100
        msg_result = f'Altura da cumeeira: {ta:.2f} m'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nAltura da Cumeeira = (Inclinação do Telhado x Comprimento do ' \
                      f'Telhado)/100\nAltura da Cumeeira = ({entry_telha_incl.get()}x{entry_telha_compr.get()})/100)'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ta_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_altura_telha, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=15)
    btn_calc['background'] = '#9D52AA'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_telha_incl.delete(0, 'end')
        entry_telha_compr.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ta_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=5, pady=20)
    btn_clean['background'] = '#9D52AA'

    # Loop da janela
    ta_window.mainloop()


# Janela Telhado (Tipo de Telha)
def telha_tipo():
    # Cria a janela "Tipo de Telha"
    tt_window = tk.Toplevel(root)
    tt_window.title('ARQBOX - Telhado (Tipo de Telha)')
    tt_window.geometry('+500+500')
    tt_window.iconbitmap('arqbox_icon_545454_48px.ico')
    tt_window.resizable(width=False, height=False)
    tt_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    tt_blank = Label(tt_window, bg=main_bg)
    tt_blank.grid(row=0, column=0)

    # Cria uma lista de inclinações
    slope_list = ['Menor que 5%', '5%', '10%', '15%', '20%', '25%', '30%', '35%', '40%', '45%']
    selected = tk.StringVar()
    slope_text = Label(tt_window, text='Selecione a inclinação desejada:', bg=main_bg, font=std_font, fg=main_txt,
                       width=30)
    slope_text.grid(row=1, column=0, padx=15)

    # Cria o estilo do combobox
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", background=entry_bg, fieldbackground=entry_bg, foreground=main_txt,
                    bordercolor=entry_bg, arrowcolor=main_txt, selectforeground=main_txt, insertbackground='red',
                    TCombobox_dropdown={"background": "red"})

    # Cria um combobox da inclinação da telha
    slope_combobox = ttk.Combobox(tt_window, textvariable=selected, values=slope_list, width=30)
    slope_combobox.grid(row=1, column=1, padx=15)

    # Cria um label para os resultados e alerta
    lbl_result = Label(tt_window, font=std_font, fg=main_txt)
    lbl_alert = Label(tt_window, font=std_font, fg='red')

    # Cria a função que exibe as telhas sugerida
    def plot_selected():
        if selected.get() == 'Menor que 5%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nLaje'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '5%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha de alumínio'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '10%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha de fibrocimento\nTelha de ' \
                         f'cimento\nTelha de PVC'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '15%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha metálica\nTelha de zinco' \
                         f'\nTelha plástica ondulada'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '20%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha colonial'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '25%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha colonial\nTelha de vidro'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '30%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha cerâmica tradicional\n' \
                         f'Telha portuguesa\nTelha romana\nTelha americana\nTelha de vidro\nTelha de concreto'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '35%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha cerâmica tradicional\n' \
                         f'Telha portuguesa\nTelha romana\nTelha francesa\nTelha de concreto'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '40%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha romana\nTelha de concreto'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        if selected.get() == '45%':
            msg_result = f'Telha sugerida para a inclinação de {selected.get()}:\n\nTelha romana\nTelha de concreto'
            lbl_result.config(text=msg_result)
            lbl_result.grid(row=3, column=0, padx=15, pady=5, columnspan=2)
            lbl_result['background'] = main_bg

        # Cria um alerta sobre as inclinações
        msg_alert = f'[AVISO]: A inclinação de cada tipo de telha pode mudar de acordo com\nmarcas e fornecedores. ' \
                    f'Aconselha-se uma pequisa de mercado para obter\nespecificações técnicas mais precisas e seguras.'
        lbl_alert.config(text=msg_alert, fg='red')
        lbl_alert.grid(row=4, column=0, padx=5, pady=15, columnspan=2)
        lbl_alert['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(tt_window, text='Consultar', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=plot_selected, width=15)
    btn_calc.grid(row=2, column=0, padx=15, pady=15)
    btn_calc['background'] = '#5158BB'

    # Cria a função que limpa os resultados da janela
    def clean():
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_alert.config(text='')
        lbl_alert.grid_forget()
        selected.set('')

    # Cria um botão para limpar o cálculo
    btn_clean = Button(tt_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=2, column=1, padx=15, pady=20)
    btn_clean['background'] = '#5158BB'

    # Loop da janela
    tt_window.mainloop()


# Janela Escada (Altura do Espelho)
def escada_esp():
    # Cria a janela "Escada (Altura do Espelho)"
    ee_window = tk.Toplevel(root)
    ee_window.title('ARQBOX - Escada (Altura do Espelho)')
    ee_window.geometry('+500+500')
    ee_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ee_window.resizable(width=False, height=False)
    ee_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ee_blank = Label(ee_window, bg=main_bg)
    ee_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir o tamanho do piso
    lbl_piso = Label(ee_window, text='Tamanho do Piso (m):', font=std_font, fg=main_txt, width=30)
    lbl_piso.grid(row=1, column=0, padx=15)
    lbl_piso['background'] = main_bg
    entry_piso = Entry(ee_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_piso.grid(row=1, column=1, padx=15)

    # Cria um label para os resultados e resolução dos cálculos
    lbl_result = Label(ee_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ee_window, font=std_font, fg=main_txt)
    lbl_alert = Label(ee_window, font=std_font, fg='red')

    # Cria a função que calcula a altura do espelho
    def calcular_alt_espelho():
        ee = (0.64 - float(entry_piso.get())) / 2
        msg_result = f'Tamanho do Espelho: {ee:.2f} m'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nTamanho do Espelho = 2 x E + P = 0.64\nTamanho do Espelho = 2 x E = ' \
                      f'0.64 - P\nTamanho do Espelho = (64 - P)/2\nTamanho do Espelho = (64 - {entry_piso.get()})/2'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

        # Cria um alerta caso o piso seja menor que 0,28 m ou maior que 0,32 m
        if float(entry_piso.get()) < 0.28 or float(entry_piso.get()) > 0.32:
            msg_alert = f'[AVISO]: A altura do espelho calculada e/ou o tamanho do piso\nutilizado estão ' \
                        f'incorretos aos valores estipulados pelas normas\nbrasileiras. Redomenda-se os devidos ' \
                        f'ajustes de dimensões.\n\nA altura do espelho deve ser entre 0.16m e 0.18m,\ne o tamanho do ' \
                        f'piso deve ser entre 0.28m e 0.32m.'
            lbl_alert.config(text=msg_alert)
            lbl_alert.grid(row=6, column=0, padx=15, pady=15, columnspan=2)
            lbl_alert['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ee_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_alt_espelho, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=15)
    btn_calc['background'] = '#EB4B98'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_piso.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()
        lbl_alert.config(text='')
        lbl_alert.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ee_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=15, pady=20)
    btn_clean['background'] = '#EB4B98'

    # Loop da janela
    ee_window.mainloop()


# Janela Escada (Número de Pisos e Espelhos)
def escada_num():
    # Cria a janela "Escada (Número de Pisos e Espelhos)"
    ep_window = tk.Toplevel(root)
    ep_window.title('ARQBOX - Escada (Nº de Pisos e Espelhos)')
    ep_window.geometry('+500+500')
    ep_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ep_window.resizable(width=False, height=False)
    ep_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ep_blank = Label(ep_window, bg=main_bg)
    ep_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a altura do pé esquerdo
    lbl_pe = Label(ep_window, text='Pé Esquerdo (m):', font=std_font, fg=main_txt, width=30)
    lbl_pe.grid(row=1, column=0, padx=15)
    lbl_pe['background'] = main_bg
    entry_pe = Entry(ep_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_pe.grid(row=1, column=1, padx=15)

    # Cria um label + entry para inserir a altura do espelho
    lbl_riser = Label(ep_window, text='Altura do Espelho (m):', font=std_font, fg=main_txt)
    lbl_riser.grid(row=2, column=0, padx=15, pady=5)
    lbl_riser['background'] = main_bg
    entry_riser = Entry(ep_window, font=std_font, borderwidth=0, bg=entry_bg, fg=main_txt, width=30)
    entry_riser.grid(row=2, column=1, padx=15)

    # Cria um label para os resultados, resolução dos cálculos e alerta
    lbl_result = Label(ep_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ep_window, font=std_font, fg=main_txt)
    lbl_alert = Label(ep_window, font=std_font, fg='red')

    # Cria a função que calcula o número de espelhos e pisos
    def calcular_num_esp_pisos():
        num_esp = float(entry_pe.get())/float(entry_riser.get())
        num_pisos = float(num_esp)-1

        msg_result = f'Número de espelhos: {num_esp:.0f}\nNúmero de Pisos: {num_pisos:.0f}'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=4, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nNúmero de Espelhos = Altura do Pé Esquerdo / Altura do Espelho\n' \
                      f'Número de Espelhos = {entry_pe.get()}/{entry_riser.get()}\nNúmero de Pisos = Número ' \
                      f'de Espelhos -1\nNúmero de Pisos = {num_esp:.0f}-1'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=5, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

        # Cria um alerta caso a altura do espelho seja menor que 0,16 m ou maior que 0,18 m
        if float(entry_riser.get()) < 0.16 or float(entry_riser.get()) > 0.18:
            msg_alert = f'[AVISO]: O parâmetro de altura de espelho utilizado está em\ndesacordo com a NBR 9050.' \
                        f'Portanto, a altura do espelho deve\nser entre 0.16m e 0.18m'
            lbl_alert.config(text=msg_alert)
            lbl_alert.grid(row=6, column=0, padx=15, pady=15, columnspan=2)
            lbl_alert['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ep_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_num_esp_pisos, width=15)
    btn_calc.grid(row=3, column=0, padx=15, pady=15)
    btn_calc['background'] = '#9D52AA'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_pe.delete(0, 'end')
        entry_riser.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()
        lbl_alert.config(text='')
        lbl_alert.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ep_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=3, column=1, padx=5, pady=20)
    btn_clean['background'] = '#9D52AA'

    # Loop da janela
    ep_window.mainloop()


# Janela Escada (Altura)
def escada_alt():
    # Cria a janela "Escada (Altura)"
    ea_window = tk.Toplevel(root)
    ea_window.title('ARQBOX - Escada (Altura)')
    ea_window.geometry('+500+500')
    ea_window.iconbitmap('arqbox_icon_545454_48px.ico')
    ea_window.resizable(width=False, height=False)
    ea_window['background'] = main_bg

    # Cria um label vazio para dar espaço
    ea_blank = Label(ea_window, bg=main_bg)
    ea_blank.grid(row=0, column=0)

    # Cria um label + entry para inserir a altura do espelho
    lbl_riser = Label(ea_window, text='Altura do Espelho (m):', font=std_font, fg=main_txt, width=30)
    lbl_riser.grid(row=2, column=0, padx=15)
    lbl_riser['background'] = main_bg
    entry_riser = Entry(ea_window, font=std_font, borderwidth=0, fg=main_txt, bg=entry_bg, width=30)
    entry_riser.grid(row=2, column=1, padx=15)

    # Cria um label + entry para inserir o número de degraus
    lbl_steps = Label(ea_window, text='Número de Degraus:', font=std_font, fg=main_txt, width=30)
    lbl_steps.grid(row=3, column=0, padx=15, pady=5)
    lbl_steps['background'] = main_bg
    entry_steps = Entry(ea_window, font=std_font, borderwidth=0, fg=main_txt, bg=entry_bg, width=30)
    entry_steps.grid(row=3, column=1, padx=15)

    # Cria um label para os resultados, resolução dos cálculos e alerta
    lbl_result = Label(ea_window, font=std_font, fg=main_txt)
    lbl_resolut = Label(ea_window, font=std_font, fg=main_txt)
    lbl_alert = Label(ea_window, font=std_font, fg='red')

    # Cria a função que calcula a altura da escada
    def calcular_compr_alt_escada():
        ea = float(entry_riser.get()) * float(entry_steps.get())

        msg_result = f'Altura da Escada: {ea:.2f}m'
        lbl_result.config(text=msg_result)
        lbl_result.grid(row=5, column=0, padx=15, pady=5, columnspan=2)
        lbl_result['background'] = main_bg

        msg_resolut = f'Resolução do Cálculo:\nAltura da Escada = Altura do Espelho x Número de Degraus\n' \
                      f'Altura da Escada = {entry_riser.get()}x{entry_steps.get()}'
        lbl_resolut.config(text=msg_resolut)
        lbl_resolut.grid(row=6, column=0, padx=15, pady=15, columnspan=2)
        lbl_resolut['background'] = main_bg

        # Cria um alerta se a altura do espelho for menor que 0,16 m ou maior que 0,18 m
        if float(entry_riser.get()) < 0.16 or float(entry_riser.get()) > 0.18:
            msg_alert = f'[AVISO]: A altura do espelho utilizada não está de acordo com os valores\nestipulados ' \
                        f'pela NBR 9050. A altura do espelho deve ser entre\n0.16m e 0.18m.'
            lbl_alert.config(text=msg_alert)
            lbl_alert.grid(row=7, column=0, padx=15, pady=15, columnspan=2)
            lbl_alert['background'] = main_bg

    # Cria um botão para iniciar o cálculo
    btn_calc = Button(ea_window, text='Calcular', font=std_font, fg=main_txt, activeforeground=active_fg,
                      activebackground=active_bg, borderwidth=0, command=calcular_compr_alt_escada, width=15)
    btn_calc.grid(row=4, column=0, padx=15, pady=15)
    btn_calc['background'] = '#5158BB'

    # Cria a função que limpa os resultados da janela
    def clean():
        entry_riser.delete(0, 'end')
        entry_steps.delete(0, 'end')
        lbl_result.config(text='')
        lbl_result.grid_forget()
        lbl_resolut.config(text='')
        lbl_resolut.grid_forget()

    # Cria um botão para limpar o cálculo
    btn_clean = Button(ea_window, text='Limpar', font=std_font, fg=main_txt, activeforeground=active_fg,
                       activebackground=active_bg, borderwidth=0, width=15, command=clean)
    btn_clean.grid(row=4, column=1, padx=15, pady=20)
    btn_clean['background'] = '#5158BB'

    # Loop da janela
    ea_window.mainloop()


# Janela Sobre o ARQBOX
def about_arqbox():
    # Cria a janela "Sobre o ARQBOX"
    about_window = tk.Toplevel(root)
    about_window.title('Sobre o ARQBOX')
    about_window.geometry('+1100+500')
    about_window.iconbitmap("arqbox_icon_545454_48px.ico")
    about_window.resizable(width=False, height=False)
    about_window['background'] = main_bg

    # Cria uma imagem para ser exibida na tela
    ab_logo = tk.PhotoImage(file='arqbox_icon_2e2e2e_100px.png')

    # Cria um label para exibir a imagem
    ab_logo_label = Label(about_window, image=ab_logo, borderwidth=0)
    ab_logo_label.grid(row=0, column=0, padx=15)

    # Cria um label para exibir os créditos do programa
    credit = Label(about_window, text=f'ARQBOX: Calculadora de Arquitetura\n\nVersão 1.0\nProgramação: Alexandre '
                                      f'Augusto Bezerra da Cunha Castro\nData: Abril | 2023', font=std_font, anchor='w',
                   justify='left', fg=main_txt)
    credit.grid(row=0, column=1, padx=15, pady=25)
    credit['background'] = main_bg

    # Loop da janela
    about_window.mainloop()


# Janela Glossário
def glossary_window():
    # Cria a janela "Glossário"
    gl_window = tk.Toplevel(root)
    gl_window.title('ARQBOX 1.0 - Glossário')
    gl_window.geometry('+400+300')
    gl_window.resizable(width=False, height=False)
    gl_window.iconbitmap('arqbox_icon_545454_48px.ico')
    gl_window['background'] = main_bg

    # Cria uma imagem para ser exibida na tela
    ab_logo = tk.PhotoImage(file='arqbox_icon_2e2e2e_glossary.png')

    # Cria um label para exibir a imagem
    ab_logo_label = Label(gl_window, image=ab_logo, borderwidth=0)
    ab_logo_label.grid(row=0, column=0, padx=15, pady=15, sticky='w')

    # Cria um label para exibir o glossário
    lbl_glossary = Label(gl_window, text='Coeficiente de Aproveitamento (CA): Indica a proporção da área do\nterreno '
                                         'ou lote que pode ser construída, consdierando a área de todos os pavimentos;'
                                         '\n\nCumeeira: elemento arquitetônico respondável pela junção das águas de\n'
                                         'um telhado;\n\nEspelho: é a superfície vertical de um degrau;\n\nInclinação '
                                         'de Rampa: é a posição oblíqua entre altura e comprimento de uma\nrampa, '
                                         'expresso em valor percentual (%);\n\nInclinação de Telhado: é a posição '
                                         'oblíqua entre a altura da cumeeira e o\ncomprimento do telhado, expresso em '
                                         'valor percentual (%);\n\nPé Esquerdo: distância do piso de um pavimento para '
                                         'o piso de outro pavimento;\n\nPiso: é a superfície horizontal de um degrau;'
                                         '\n\nTaxa de Ocupação (TO): é o percentual de um terreno ou lote que\nestá '
                                         'ocupado pela projeção de uma área edificada;\n\nTaxa de Permeabilidade (TP): '
                                         'é o percentual do lote que deve permanecer sem\nedificações e com piso '
                                         'permeável.',
                         font='Arial 10 bold', fg=main_txt, anchor='w', justify='left')
    lbl_glossary.grid(row=1, column=0, padx=15, pady=15)
    lbl_glossary['background'] = main_bg

    # Loop da janela
    gl_window.mainloop()


# Janela inicial

# Define as cores utilizadas na interface
main_bg = '#2e2e2e'  # Cor de fundo principal
active_bg = '#ffffff'  # Cor de fundo ativo
active_bg2 = '#545454'  # Cor de fundo ativo secundário
active_fg = '#2e2e2e'  # Cor do texto ativo
active_fg2 = '#ffffff'  # Cor do texto ativo secundário
entry_bg = '#545454'  # Cor de fundo da entrada de texto
main_txt = '#ffffff'  # Cor do texto principal

# Cria a janela principal
root = tk.Tk()
root.title('ARQBOX: Calculadora de Arquitetura - Versão 1.0')
root.geometry('+400+300')
root.resizable(width=False, height=False)
root.wm_iconbitmap('arqbox_icon_545454_48px.ico')
root['background'] = main_bg

# Define as fontes utilizadas na interface
title_font = font.Font(family='Arial', size=12, weight='bold')
std_font = font.Font(family='Arial', size=10, weight='bold')

# Cria um label vazio para dar espaço entre os botões e a imagem
lbl_blank = Label(root)
lbl_blank.grid(row=0, column=0, pady=10)
lbl_blank['background'] = main_bg

# Cria uma imagem para o logotipo da calculadora
logo = tk.PhotoImage(file='arqbox_logo_txt_2e2e2e_100px.png')

# Cria um label para exibir a imagem do logotipo
logo_label = Label(root, image=logo, borderwidth=0, anchor='center', justify='center')
logo_label.grid(row=1, column=1, columnspan=1)

# Cria um botão para acessar a função "Sobre o ARQBOX"
btn_about = Button(root, text='Sobre o ARQBOX', font=std_font, fg='#545454', borderwidth=0, width=20,
                   activebackground=active_bg2, activeforeground=active_fg2, command=about_arqbox)
btn_about.grid(row=1, column=2)
btn_about['background'] = '#eee5e9'

# Cria um botão para acessar a função "Glossário"
btn_glossary = Button(root, text='Glossário', font=std_font, fg='#545454', borderwidth=0, width=20,
                      activebackground=active_bg2, activeforeground=active_fg2, command=glossary_window)
btn_glossary.grid(row=2, column=2)
btn_glossary['background'] = '#eee5e9'

# Cria um label para exibir o título da seção de cálculo
lbl_opcoes = Label(root, text='Escolha o índice que deseja calcular:', font=title_font, fg=main_txt)
lbl_opcoes.grid(row=3, column=1, padx=10, pady=10, columnspan=1)
lbl_opcoes['background'] = main_bg

# Cria um botão para acessar a função "Taxa de Ocupação"
btn_taxa_ocupacao = Button(root, text='Taxa de\nOcupação', font=std_font, fg=main_txt, borderwidth=0, width=20,
                           activebackground=active_bg, activeforeground=active_fg, command=taxa_ocupacao_window)
btn_taxa_ocupacao.grid(row=4, column=0, padx=65, pady=15)
btn_taxa_ocupacao['background'] = '#EB4B98'

# Cria um botão para acessar a função "Coeficiente de Aproveitamento"
btn_coef_aprov = Button(root, text='Coeficiente de\nAproveitamento', font=std_font, fg=main_txt, borderwidth=0,
                        width=20, activebackground=active_bg, activeforeground=active_fg, command=coef_apr_window)
btn_coef_aprov.grid(row=4, column=1, padx=65, pady=15)
btn_coef_aprov['background'] = '#9D52AA'

# Cria um botão para acessar a função "Taxa de Permeabilidade"
btn_taxa_perm = Button(root, text='Taxa de\nPermeabilidade', font=std_font, fg=main_txt, borderwidth=0, width=20,
                       activebackground=active_bg, activeforeground=active_fg, command=taxa_perm_window)
btn_taxa_perm.grid(row=4, column=2, padx=70, pady=15)
btn_taxa_perm['background'] = '#5158BB'

# Cria um botão para acessar a função "Comprimento de Rampa"
btn_rampa_compr = Button(root, text='Rampa\n(Comprimento)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                         activebackground=active_bg, activeforeground=active_fg, command=rampa_compr)
btn_rampa_compr.grid(row=5, column=0, padx=5, pady=15)
btn_rampa_compr['background'] = '#EB4B98'

# Cria um botão para acessar a função "Inclinação de Rampa"
btn_rampa_incl = Button(root, text='Rampa\n(Inclinação)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                        activebackground=active_bg, activeforeground=active_fg, command=rampa_incl)
btn_rampa_incl.grid(row=5, column=1, padx=5, pady=15)
btn_rampa_incl['background'] = '#9D52AA'

# Cria um botão para acessar a função "Altura de Rampa"
btn_rampa_alt = Button(root, text='Rampa\n(Altura)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                       activebackground=active_bg, activeforeground=active_fg, command=rampa_alt)
btn_rampa_alt.grid(row=5, column=2, padx=70, pady=15)
btn_rampa_alt['background'] = '#5158BB'

# Cria um botão para acessar a função "Inclinação de Telhado"
btn_telha_incl = Button(root, text='Telhado\n(Inclinação)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                        activebackground=active_bg, activeforeground=active_fg, command=telha_incl)
btn_telha_incl.grid(row=6, column=0, padx=5, pady=15)
btn_telha_incl['background'] = '#EB4B98'

# Cria um botão para acessar a função "Altura da Cumeeira"
btn_telha_alt = Button(root, text='Telhado\n(Altura da Cumeeira)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                       activebackground=active_bg, activeforeground=active_fg, command=telha_alt)
btn_telha_alt.grid(row=6, column=1, padx=5, pady=15)
btn_telha_alt['background'] = '#9D52AA'

# Cria um botão para acessar a função "Tipo de Telha"
btn_telha_tipo = Button(root, text='Telhado\n(Tipo de Telha)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                        activebackground=active_bg, activeforeground=active_fg, command=telha_tipo)
btn_telha_tipo.grid(row=6, column=2, padx=70, pady=15)
btn_telha_tipo['background'] = '#5158BB'

# Cria um botão para acessar a função "Altura do Espelho"
btn_esc_esp = Button(root, text='Escada\n(Altura do Espelho)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                     activebackground=active_bg, activeforeground=active_fg, command=escada_esp)
btn_esc_esp.grid(row=7, column=0, padx=5, pady=15)
btn_esc_esp['background'] = '#EB4B98'

# Cria um botão para acessar a função "Número de Pisos e Espelhos"
btn_esc_alt = Button(root, text='Escada\n(Nº de Pisos e Espelhos)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                     activebackground=active_bg, activeforeground=active_fg, command=escada_num)
btn_esc_alt.grid(row=7, column=1, padx=5, pady=15)
btn_esc_alt['background'] = '#9D52AA'

# Cria um botão para acessar a função "Altura da Escada"
btn_esc_alt = Button(root, text='Escada\n(Altura)', font=std_font, fg=main_txt, borderwidth=0, width=20,
                     activebackground=active_bg, activeforeground=active_fg, command=escada_alt)
btn_esc_alt.grid(row=7, column=2, padx=70, pady=15)
btn_esc_alt['background'] = '#5158BB'

# Cria um label vazio para dar espaço
lbl_blank = Label(root)
lbl_blank.grid(row=10, column=0)
lbl_blank['background'] = main_bg

# Loop da janela
root.mainloop()
