from manim import *
class surd(Scene):
    def construct(self):
        t1 = Text('Solving Surd', font= 'monospace', font_size= 24)
        t2 = MathTex('\sqrt{12} + \sqrt{108} = \sqrt{x}').move_to(UP*2.5)
        
        self.play(
            Write(t1)
        )
        self.wait(2)
        self.play(
            FadeTransform(t1, t2)
        )
        
        t2copy = t2.copy()
        t3 = MathTex(r"\sqrt{4 \times 3} + \sqrt{36 \times 3} = \sqrt{x}").next_to(t2, DOWN * 0.9)
        
        self.play(
            ReplacementTransform(t2copy, t3), run_time = 0.5
        )
        
        t3copy = t3.copy()
        t4 = MathTex(r"\sqrt{4} \times \sqrt{3} + \sqrt{36} \times \sqrt{3} = \sqrt{x}").next_to(t3, DOWN * 0.9)
        
        self.play(
            ReplacementTransform(t3copy, t4), run_time = 0.5
        )
        
        
        t4copy = t4.copy()
        t5 = MathTex(r' 2\sqrt{3} + 6\sqrt{3} =\sqrt{x}').next_to(t4, DOWN * 0.9)
        
        self.play(
            ReplacementTransform(t4copy, t5), run_time = 0.5
        )
        
        
        t5copy = t5.copy()
        t6 = MathTex(r' (2+6)\sqrt{3}  =\sqrt{x}').next_to(t5, DOWN * 0.9)
        
        self.play(
            ReplacementTransform(t5copy, t6), run_time = 0.5
        )
        
        
        t6copy = t6.copy()
        t7 = MathTex(r' (8\sqrt{3})^{2}  =(\sqrt{x})^{2}').next_to(t6, DOWN * 0.9)
        
        self.play(
            ReplacementTransform(t6copy, t7), run_time = 0.5
        )
            
        
        t7copy = t7.copy()
        t8 = MathTex(r'64 \times 3 = x').next_to(t7, DOWN * 0.9)
        
        
        self.play(
            ReplacementTransform(t7copy, t8), run_time = 0.5
        )
            
        
        t8copy = t8.copy()
        t9 = MathTex(r'192 = x').next_to(t8, DOWN * 0.9)
        
        self.play(
            ReplacementTransform(t8copy, t9), run_time = 0.5
        )
            
        
        
        
    
        
        
        
        
        self.wait(2)