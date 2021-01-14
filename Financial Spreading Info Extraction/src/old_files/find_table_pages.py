# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 12:36:02 2020.

@author: rahul.gupta
"""

import os
import pdfplumber
import cv2
import numpy as np
import pandas as pd


def main(file_path):
    """."""
    with pdfplumber.open(file_path) as pdf:
        j = 0
        all_pages = []
        for pageX in pdf.pages:
            j += 1
            print('Page: ', j)
            table_flag = pageX.find_tables(table_settings={
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines"})
            if len(table_flag) > 0:
                if any([len(x.rows) > 3 for x in table_flag]):
                    all_pages.append(j)
                    continue
            pgBox = pageX.bbox
            pgLines = pageX.lines
            pgRects = pageX.rects
            pgChars = pageX.chars
            if 'Rotate' in pageX.page_obj.attrs.keys():
                if is_rotated(pageX.page_obj.attrs['Rotate'], pgChars):
                    wordL = pageX.extract_words(horizontal_ltr=False, vertical_ttb=False)
                    table_flag = get_tbl_from_words_rotates(wordL, pgBox, pgLines, pgRects)
                else:
                    wordL = pageX.extract_words()
                    table_flag = get_tbl_from_words(wordL, pgBox, pgLines, pgRects)
            else:
                wordL = pageX.extract_words()
                table_flag = get_tbl_from_words(wordL, pgBox, pgLines, pgRects)
            if len(table_flag) > 0:
                all_pages.append(j)

        return all_pages


def is_rotated(rotate_attr, pgChars):
    """."""
    if rotate_attr in [270, 90]:
        return True
    char_rot = []
    for x in pgChars:
        if x['text'] in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            char_rot.append(float(x['x1']) - float(x['x0']) > float(x['y1']) - float(x['y0']))
    return all(char_rot)


def get_tbl_from_words_rotates(wordL, pgBox, pgLines, pgRects):
    """."""
    line_list = max([pgLines, pgRects], key=lambda x: len(x))
    line_list = [l for l in line_list if not any((l['bottom']-l['top'] < 30, l['x1']-l['x0'] > 100))]
    if len(line_list) == 0:
        return []

    blank_image = ~np.zeros((int(pgBox[3]), int(pgBox[2]), 3), np.uint8)

    for i, z in enumerate(line_list):
        x1 = int(z['x0'])
        y1 = int(z['y0'])
        x2 = int(z['x1'])
        y2 = int(z['y1'])
        cv2.rectangle(blank_image, (x1, y2), (x2, y1), (255, 0, 0), 1)
    # cv2.imwrite('fxex.png', blank_image)

    linet = [(int(x['top']), int(x['bottom'])) for x in line_list]
    wordTL = [int(x['top']) for x in wordL]
    wordTL2 = [int(x['bottom']) for x in wordL]
    wordVL = [x for x in set(wordTL) if wordTL.count(x) > 3]
    wordVL2 = [x for x in set(wordTL2) if wordTL2.count(x) > 3]
    wordXL = [(int(x['x0']), int(x['x1']), int(x['top']),
               int(x['bottom']), x['text']) for x in wordL
              if int(x['top']) in wordVL or int(x['bottom']) in wordVL2]

    def topx(x, linet):
        """."""
        return [x[2] >= l[0] and x[3] <= l[1] for l in linet]
    wordXLs = [x for x in wordXL if any(topx(x, linet))]
    wordXld = pd.DataFrame(wordXLs)

    # --- Return if empty
    if wordXld.empty:
        return []
    # -------------------

    blank_image = cv2.flip(blank_image, 0)
    unqBots = sorted(list(set(wordXld[3])))
    newRects = []
    for ub in unqBots:
        t_df = wordXld[wordXld[3] == ub]
        t_df2 = t_df.sort_values(by=0)
        lz = [list(t_df2[1])[i+1]-list(t_df2[1])[i] < 20 for i in range(len(t_df2[1])-1)]
        cls_x = []
        x_x = []
        for i, x in enumerate(lz):
            if x:
                x_x.append(i)
            else:
                x_x.append(i)
                cls_x.append(x_x)
                x_x = []
        cls_x.append(x_x)
        for s_x in cls_x:
            if len(s_x) > 1:
                newRects.append({'x0': t_df2.iloc[min(s_x), 0],
                                 'x1': t_df2.iloc[max(s_x), 1],
                                 'y0': t_df2.iloc[0, 3],
                                 'y1': t_df2.iloc[0, 3]})
    unqBots = sorted(list(set(wordXld[2])))
    for ub in unqBots:
        t_df = wordXld[wordXld[2] == ub]
        t_df2 = t_df.sort_values(by=0)
        lz = [list(t_df2[0])[i+1]-list(t_df2[0])[i] < 20 for i in range(len(t_df2[0])-1)]
        cls_x = []
        x_x = []
        for i, x in enumerate(lz):
            if x:
                x_x.append(i)
            else:
                x_x.append(i)
                cls_x.append(x_x)
                x_x = []
        cls_x.append(x_x)
        for s_x in cls_x:
            if len(s_x) > 1:
                newRects.append({'x0': t_df2.iloc[min(s_x), 0],
                                 'x1': t_df2.iloc[max(s_x), 1],
                                 'y0': t_df2.iloc[0, 2],
                                 'y1': t_df2.iloc[0, 2]})

    for i, z in enumerate(newRects):
        x1 = int(z['x0'])
        y1 = int(z['y0'])
        x2 = int(z['x1'])
        y2 = int(z['y1'])
        cv2.rectangle(blank_image, (x1, y2), (x2, y1), (0, 0, 255), 1)
    # blank_image = cv2.flip(blank_image, 0)
    # cv2.imwrite('fxex.png', blank_image)
    xx_gray = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
    xx_gray = cv2.bitwise_not(xx_gray)
    xx_thresh = cv2.threshold(xx_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(xx_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # xx_imfX = xx_gray.copy()
    tb_nlist = []
    for idx, c in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)
        if w > 10 and h > 10:
            # cv2.rectangle(xx_imfX, (x, y), (x+w, y+h), 120, 3)
            tb_nlist.append(idx)
    # cv2.imwrite('xx_imfX.png', xx_imfX)
    return tb_nlist


def get_tbl_from_words(wordL, pgBox, pgLines, pgRects):
    """."""
    line_list = max([pgLines, pgRects], key=lambda x: len(x))
    line_list = [l for l in line_list if not any((l['x1']-l['x0'] < 30, l['bottom']-l['top'] > 100))]
    if len(line_list) == 0:
        return []
    blank_image = ~np.zeros((int(pgBox[3]), int(pgBox[2]), 3), np.uint8)

    # Printing lines or recs
    for i, z in enumerate(line_list):
        x1 = int(z['x0'])
        y1 = int(z['y0'])
        x2 = int(z['x1'])
        y2 = int(z['y1'])
        cv2.rectangle(blank_image, (x1, y2), (x2, y1), (255, 0, 0), 3)

    blank_image = cv2.flip(blank_image, 0)
    # plt.imshow(blank_image)

    # Printing Words
    linet = [(int(x['x0']), int(x['x1'])) for x in line_list]

    def topc(x):
        """."""
        return [x[0] >= l[0] and x[1] <= l[1] for l in linet]

    wordTL = [int(x['x0']) for x in wordL]
    wordTL2 = [int(x['x1']) for x in wordL]
    wordVL = [x for x in set(wordTL) if wordTL.count(x) > 3]
    wordVL2 = [x for x in set(wordTL2) if wordTL2.count(x) > 3]
    wordXL = [(int(x['x0']), int(x['x1']), int(x['top']),
               int(x['bottom']), x['text']) for x in wordL
              if int(x['x0']) in wordVL or int(x['x1']) in wordVL2]
    wordXLs = [x for x in wordXL if any(topc(x))]
    wordXld = pd.DataFrame(wordXLs)

    # --- Return if empty
    if wordXld.empty:
        return []
    # -------------------

    unqBots = sorted(list(set(wordXld[1])))
    newRects = []
    for ub in unqBots:
        t_df = wordXld[wordXld[1] == ub]
        t_df2 = t_df.sort_values(by=2)
        lz = [list(t_df2[2])[i+1]-list(t_df2[2])[i] < 20 for i in range(len(t_df2[2])-1)]
        cls_x = []
        x_x = []
        for i, x in enumerate(lz):
            if x:
                x_x.append(i)
            else:
                x_x.append(i)
                cls_x.append(x_x)
                x_x = []
        cls_x.append(x_x)
        for s_x in cls_x:
            if len(s_x) > 1:
                newRects.append({'x0': t_df2.iloc[0, 1],
                                 'x1': t_df2.iloc[0, 1],
                                 'y0': t_df2.iloc[min(s_x), 2],
                                 'y1': t_df2.iloc[max(s_x), 3]})
    unqBots = sorted(list(set(wordXld[0])))
    for ub in unqBots:
        t_df = wordXld[wordXld[0] == ub]
        t_df2 = t_df.sort_values(by=3)
        lz = [list(t_df2[3])[i+1]-list(t_df2[3])[i] < 20 for i in range(len(t_df2[3])-1)]
        cls_x = []
        x_x = []
        for i, x in enumerate(lz):
            if x:
                x_x.append(i)
            else:
                x_x.append(i)
                cls_x.append(x_x)
                x_x = []
        cls_x.append(x_x)
        for s_x in cls_x:
            if len(s_x) > 1:
                newRects.append({'x0': t_df2.iloc[0, 0],
                                 'x1': t_df2.iloc[0, 0],
                                 'y0': t_df2.iloc[min(s_x), 2],
                                 'y1': t_df2.iloc[max(s_x), 3]})
    # blank_image = np.zeros((int(pgBox[3]), int(pgBox[2]), 3), np.uint8)
    for i, z in enumerate(newRects):
        x1 = int(z['x0'])
        y1 = int(z['y0'])
        x2 = int(z['x1'])
        y2 = int(z['y1'])
        cv2.rectangle(blank_image, (x1, y2), (x2, y1), (0, 0, 255), 1)
    # blank_image = cv2.flip(blank_image, 0)
    # cv2.imwrite('fxex2.png', blank_image)
    # plt.imshow(blank_image)
    # -----------------------------------------------

    xx_gray = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
    xx_gray = cv2.bitwise_not(xx_gray)
    xx_thresh = cv2.threshold(xx_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(xx_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # xx_imfX = xx_gray.copy()
    tb_nlist = []
    for idx, c in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)
        if w > 10 and h > 10:
            # cv2.rectangle(xx_imfX, (x, y), (x+w, y+h), 120, 3)
            tb_nlist.append(idx)
    # plt.imshow(xx_imfX)
    
    # Work Around for files with small horizontal lines not captured
    if tb_nlist == []:
        long_lines_of_tables = [x for x in newRects if (x['y1'] - x['y0']) > 50]
        if len(long_lines_of_tables) > 4:
            tb_nlist = [1]
    return tb_nlist


def get_pages_with_tables(file_path):
    """Call this function to get pages with tables. Input is the full file path."""
    return main(file_path)
