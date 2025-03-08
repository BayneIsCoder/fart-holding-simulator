def on_b_pressed():
    info.change_score_by(1)
    info.start_countdown(1)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_countdown_end():
    print("life lost")
    info.change_life_by(-1)
    print("now playing Life Lost")
    music.play(music.string_playable("B A C5 G A F B D ", 120),
        music.PlaybackMode.IN_BACKGROUND)
info.on_countdown_end(on_countdown_end)

def on_life_zero():
    music.stop_all_sounds()
    game.set_game_over_message(False, "Your Ass Exploded.")
    game.splash("AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA")
    print("player died")
    game.game_over(False)
    print("now playing You Lost!")
    music.play(music.string_playable("F E F C D E D E ", 66),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
info.on_life_zero(on_life_zero)

print("Game Booting..")
music.stop_all_sounds()
print("Game Booted!")
music.play(music.melody_playable(music.ba_ding),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
game.splash("SoftArcade Presents")
music.stop_all_sounds()
game.splash("Fart Holding Game v3.2.1")
music.play(music.melody_playable(music.jump_up),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("A long time ago, Someone Held In A Fart.",
    DialogLayout.BOTTOM)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("FOR HIS ENTIRE LIFE! And He’s Still Living.",
    DialogLayout.CENTER)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("And That someone, Was You!", DialogLayout.BOTTOM)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("Yep!", DialogLayout.BOTTOM)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("You!", DialogLayout.BOTTOM)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("You Held In A Fart For Your ENTIRE Life!!",
    DialogLayout.BOTTOM)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("Well..", DialogLayout.CENTER)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("Your Job Is To Hold It In For Even LONGER!!",
    DialogLayout.FULL)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("I Am Trusting You On This. Bye.", DialogLayout.BOTTOM)
music.play(music.melody_playable(music.pew_pew),
    music.PlaybackMode.IN_BACKGROUND)
game.show_long_text("Press B to Hold In Fart.", DialogLayout.FULL)
game.show_long_text("Hold In Fart Every Second.", DialogLayout.FULL)
game.show_long_text("You Have Five Lives. If You Lose One, Press B to continue.",
    DialogLayout.FULL)
music.stop_all_sounds()
print("game started!")
info.set_life(5)
info.set_score(0)
info.start_countdown(5)
music.play(music.string_playable("C5 A D F G E A E ", 200),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)