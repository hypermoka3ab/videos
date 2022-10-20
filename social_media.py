from manim import *

class SocialMedia(Scene):
    def construct(self):
        facebook = SVGMobject(file_name="assets/svg/facebook.svg")
        reddit = SVGMobject(file_name="assets/svg/reddit.svg")
        instagram = SVGMobject(file_name="assets/svg/instagram.svg")
        discord = SVGMobject(file_name="assets/svg/discord.svg")

        logos = VGroup(
            facebook, instagram, discord
        ).scale(.5).arrange(RIGHT, buff=LARGE_BUFF)

        self.play(
            *[DrawBorderThenFill(mob) for mob in logos]
        )
        
        links = VGroup(
            facebook.copy(), Text("Hypermoka3ab"), 
            instagram.copy(), Text("@hyper_moka3ab"), 
            discord.copy(), Text("hypermoka3ab")
        ).arrange_in_grid(3, 2, cell_alignment=LEFT)

        self.wait()
        logos[0].target = links[0]
        logos[1].target = links[2]
        logos[2].target = links[4]
        self.play(
            *[
                MoveToTarget(mob) for mob in logos
            ],
            *[FadeIn(link, run_time=2) for link in links[1::2]]
        )
        self.wait()