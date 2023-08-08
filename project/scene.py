from manim import *

# dizi-seri tanımı
class Dizi(Scene):
    def construct(self):
        dizi = MathTex("a_1", ",", "a_2", ",", "a_3", ",", "a_4", ",", "a_5", ",", "a_6", ",", "a_7", ",", "a_8", ",", "a_9", ",", "a_{10}")
        self.play(Write(dizi))
        self.wait()


class SerilerAnimasyon(Scene):
    def construct(self):
        title = Tex("Matematikte Seriler").scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Seri tanımı
        seri_tanim = Text("Bir seride, terimlerin toplamı alınır.").scale(0.8)
        self.play(FadeIn(seri_tanim))
        self.wait(2)
        self.play(FadeOut(seri_tanim))

        # Seri örneği
        seri_ornek = MathTex("1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\cdots").scale(1.2)
        self.play(Transform(seri_tanim, seri_ornek))
        self.wait(2)

        # Seri toplamı
        seri_toplam = MathTex("S = 1 + \\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\cdots").scale(1.2)
        toplam_aciklama = Text("Toplamı bulmak için limit alınır.").scale(0.8)
        self.play(FadeOut(seri_tanim), Transform(seri_ornek, seri_toplam), Write(toplam_aciklama))
        self.wait(2)

        # Limit ifadesi
        limit_ifadesi = MathTex("S = \\lim_{{n \\to \\infty}} \\sum_{{k=1}}^n \\frac{1}{2^k}").scale(1.2)
        self.play(Transform(seri_toplam, limit_ifadesi), FadeOut(toplam_aciklama))
        self.wait(2)

        self.play(FadeOut(title), FadeOut(seri_toplam))
        self.wait(1)
