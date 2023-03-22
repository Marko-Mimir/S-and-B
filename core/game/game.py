import importlib

class game:
    def __init__(self, render, delta):
        self.render = render
        self.delta = delta
        self.active_scenes = []
        self.texts = []
        self.obj = []
        self.up = []
        self.main()

    def clean(self):
        for x in self.obj:
            self.render.obj = self.render.obj.remove(x)
            if self.render.obj is None:
                self.render.obj = []
        for x in self.texts:
            self.render.texts = self.render.texts.remove((x, x.last[0], x.last[1]))
            if self.render.texts is None:
                self.render.texts = []
        for x in self.up:
            self.delta.run_on_tick = self.delta.run_on_tick.remove(x)
            if self.delta.run_on_tick is None:
                self.delta.run_on_tick = []
        self.up = []
        self.texts = []
        self.obj = []
    #DO NOT USE, FOR EXAMPLE USE ONLY. WILL BREAK GAME ALSO IS OUTDATED SEE SCREEN.py DON'T DELETE WILL BRAKE ANYWAYS

    def main(self):
        self.add_new_scene("core.game.screens.mainmenu", "mainMenu")
    #INIT ONLY

    def add_new_scene(self, module_name, class_name):
        scene = importlib.import_module(module_name)

        class_ = getattr(scene, class_name)
        print("Adding scene: ", class_name)
        self.active_scenes.append(class_(self.render, self.delta, self))


    def clear_all_scenes(self):
        for x in self.active_scenes:
            x.clean()
        print("Deleting every scene.")
        self.active_scenes = []

    def clear_one_scene(self, sceneName):
        for x in self.active_scenes:
            if x.name == sceneName:
                x.clean()
                print("Deleting scene: ", sceneName)
                self.active_scenes.pop(self.active_scenes.index(x))
                break


