class TextAlign():
    LeftTop      = 0
    LeftCenter   = 1
    LeftBottom   = 2
    MiddleTop    = 3
    MiddleCenter = 4
    MiddleBottom = 5
    RightTop     = 6
    RightCenter  = 7
    RightBottom  = 8


class TextRender():
    def __init__(self, auto_wrap = False, antialias = True):
        self.auto_wrap = auto_wrap
        self.antialias = antialias

    def render(self, surface, font, text, rect, color, align = TextAlign.LeftTop):
        from pygame.surface import Surface
        from pygame.locals  import SRCALPHA, BLEND_RGBA_ADD
        
        text_surface = Surface((rect[2], rect[3]), SRCALPHA)
        line_height = font.get_linesize()
        wraped_text = ''

        # auto wrap
        for line in text.split('\n'):
            graph_info = font.metrics(line)
            width = 0
            for i in range(len(line)):
                if self.auto_wrap and width > 0 and (width + graph_info[i][1]) > rect[2]:
                    wraped_text += '\n'
                    width = 0
                wraped_text += line[i]
                width += graph_info[i][1]
            wraped_text += '\n'
        wraped_text = wraped_text[:-1]

        # process line text surfaces
        line_surfaces = []
        for line in wraped_text.split('\n'):
            line_surfaces.append(font.render(line, self.antialias, color))

        total_lines = len(line_surfaces)
        if   align % 3 == 1: # center
            oy = max(0, (rect[3] - (total_lines * line_height))/2.0)
        elif align % 3 == 2: # right
            oy = max(0, (rect[3] - (total_lines * line_height)))
        else:                # top
            oy = 0 

        lines = 0
        for ls in line_surfaces:
            if   align // 3 == 1: # center
                ox = max(0, (rect[2] - ls.get_width()) / 2)
            elif align // 3 == 2: # right
                ox = rect[2] - ls.get_width()
            else:                 # left
                ox = 0 

            text_surface.blit(ls, (
                ox, 
                lines * line_height + oy, 
                ls.get_width(), 
                ls.get_height(),
            ), special_flags=BLEND_RGBA_ADD) # select BLEND_RGBA_ADD to prevent antialias draw on surface without alpha 
            lines += 1

        surface.blit(text_surface, (rect[0], rect[1]))





        