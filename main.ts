controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    info.changeScoreBy(1)
    info.startCountdown(1)
})
info.onCountdownEnd(function () {
    info.changeLifeBy(-1)
    music.play(music.stringPlayable("B A C5 G A F B D ", 120), music.PlaybackMode.InBackground)
})
info.onLifeZero(function () {
    music.stopAllSounds()
    game.setGameOverMessage(false, "Your Ass Exploded.")
    game.splash("AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA AAAAAaAaAaaAaAAaAaAAaAaA")
    game.gameOver(false)
    music.play(music.stringPlayable("F E F C D E D E ", 66), music.PlaybackMode.LoopingInBackground)
})
music.stopAllSounds()
music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.LoopingInBackground)
game.splash("SoftArcade Presents")
music.stopAllSounds()
game.splash("Fart Holding Game v3.1.1")
music.play(music.melodyPlayable(music.jumpUp), music.PlaybackMode.InBackground)
game.showLongText("A long time ago, Someone Held In A Fart.", DialogLayout.Bottom)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("FOR HIS ENTIRE LIFE! And He’s Still Living.", DialogLayout.Center)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("And That someone, Was You!", DialogLayout.Bottom)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("Yep!", DialogLayout.Bottom)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("You!", DialogLayout.Bottom)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("You Held In A Fart For Your ENTIRE Life!!", DialogLayout.Bottom)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("Well..", DialogLayout.Center)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("Your Job Is To Hold It In For Even LONGER!!", DialogLayout.Full)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("I Am Trusting You On This. Bye.", DialogLayout.Bottom)
music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
game.showLongText("Press B to Hold In Fart.", DialogLayout.Full)
game.showLongText("Hold In Fart Every Second.", DialogLayout.Full)
game.showLongText("You Have Five Lives. If You Lose One, Press B to continue.", DialogLayout.Full)
music.stopAllSounds()
scene.setBackgroundImage(assets.image`Zero`)
info.setLife(5)
info.setScore(0)
info.startCountdown(5)
music.play(music.stringPlayable("C5 A D F G E A E ", 200), music.PlaybackMode.LoopingInBackground)
